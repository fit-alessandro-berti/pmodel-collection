# Generated from: 175cacaa-1d8a-4b0a-aa71-94e96309fc0d.json
# Description: This process details the establishment of a vertical farming operation within an urban environment, combining advanced hydroponics and IoT-driven monitoring systems. It involves site acquisition, environmental assessment, modular farm design, automated nutrient delivery setup, climate control calibration, crop scheduling, continuous data analysis, pest management integration, and sustainable waste recycling, aiming to optimize food production in limited spaces while minimizing environmental impact and maximizing yield through innovative technology and strategic urban planning.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activity transitions
site_survey    = Transition(label='Site Survey')
permit_filing  = Transition(label='Permit Filing')
design_layout  = Transition(label='Design Layout')
module_assembly = Transition(label='Module Assembly')
sensor_install = Transition(label='Sensor Install')
water_setup    = Transition(label='Water Setup')
nutrient_mix   = Transition(label='Nutrient Mix')
climate_config = Transition(label='Climate Config')
crop_planting  = Transition(label='Crop Planting')
data_sync      = Transition(label='Data Sync')
pest_control   = Transition(label='Pest Control')
growth_monitor = Transition(label='Growth Monitor')
harvest_prep   = Transition(label='Harvest Prep')
waste_sorting  = Transition(label='Waste Sorting')
yield_analysis = Transition(label='Yield Analysis')
market_sync    = Transition(label='Market Sync')

# After 'Design Layout' these setup tasks can run in parallel
setup_concurrent = StrictPartialOrder(
    nodes=[
        module_assembly,
        sensor_install,
        water_setup,
        nutrient_mix,
        climate_config
    ]
)
# No edges added => fully concurrent

# Define the pest-management & growth-monitoring sequence
pest_growth_PO = StrictPartialOrder(
    nodes=[pest_control, growth_monitor]
)
pest_growth_PO.order.add_edge(pest_control, growth_monitor)

# Loop for continuous monitoring: Data Sync then (Pest Control -> Growth Monitor) repeatedly
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[data_sync, pest_growth_PO]
)

# Build the root partial order
root = StrictPartialOrder(
    nodes=[
        site_survey,
        permit_filing,
        design_layout,
        setup_concurrent,
        crop_planting,
        monitor_loop,
        harvest_prep,
        waste_sorting,
        yield_analysis,
        market_sync
    ]
)

# Add the control-flow dependencies
root.order.add_edge(site_survey, permit_filing)
root.order.add_edge(permit_filing, design_layout)
root.order.add_edge(design_layout, setup_concurrent)
root.order.add_edge(setup_concurrent, crop_planting)
root.order.add_edge(crop_planting, monitor_loop)
root.order.add_edge(monitor_loop, harvest_prep)
root.order.add_edge(harvest_prep, waste_sorting)
root.order.add_edge(waste_sorting, yield_analysis)
root.order.add_edge(yield_analysis, market_sync)