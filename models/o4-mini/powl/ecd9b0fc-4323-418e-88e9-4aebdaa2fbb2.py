# Generated from: ecd9b0fc-4323-418e-88e9-4aebdaa2fbb2.json
# Description: This process involves establishing a multi-layer vertical farm within an urban environment to optimize space and maximize crop yield. It begins with site evaluation and structural analysis, followed by the installation of hydroponic systems and LED grow lights. Environmental controls like humidity, temperature, and CO2 levels are calibrated precisely. Seeds are selected based on local demand and growth cycles. Automated nutrient delivery and water recycling systems are integrated to minimize waste. Continuous monitoring through IoT sensors ensures optimal plant health, while periodic pest management using biological agents preserves organic standards. Harvest scheduling and packaging are coordinated to meet rapid urban distribution channels, ensuring fresh produce delivery within hours of picking. Finally, data analytics refine future crop selections and operational efficiency, supporting sustainability and profitability goals in a constrained urban footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
structure_check  = Transition(label='Structure Check')
hydroponic_install = Transition(label='Hydroponic Install')
lighting_setup   = Transition(label='Lighting Setup')
climate_control  = Transition(label='Climate Control')
seed_selection   = Transition(label='Seed Selection')
nutrient_mix     = Transition(label='Nutrient Mix')
water_recycling  = Transition(label='Water Recycling')
sensor_deploy    = Transition(label='Sensor Deploy')
growth_monitor   = Transition(label='Growth Monitor')
pest_control     = Transition(label='Pest Control')
harvest_plan     = Transition(label='Harvest Plan')
packaging_prep   = Transition(label='Packaging Prep')
delivery_route   = Transition(label='Delivery Route')
data_analysis    = Transition(label='Data Analysis')
yield_forecast   = Transition(label='Yield Forecast')

# Define loop for continuous monitoring (Growth Monitor then optionally Pest Control)
monitoring_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitor, pest_control]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, structure_check, hydroponic_install, lighting_setup,
    climate_control, seed_selection, nutrient_mix, water_recycling,
    sensor_deploy, monitoring_loop, harvest_plan, packaging_prep,
    delivery_route, data_analysis, yield_forecast
])

# Sequence: Site Survey -> Structure Check -> Installations -> Setup -> Calibration
root.order.add_edge(site_survey, structure_check)
root.order.add_edge(structure_check, hydroponic_install)
root.order.add_edge(hydroponic_install, lighting_setup)
root.order.add_edge(lighting_setup, climate_control)

# After climate control: select seeds and deploy sensors
root.order.add_edge(climate_control, seed_selection)
root.order.add_edge(climate_control, sensor_deploy)

# After seed selection: mix nutrients and recycle water
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(seed_selection, water_recycling)

# Before starting monitoring loop: sensors deployed, nutrient and water systems ready
root.order.add_edge(sensor_deploy, monitoring_loop)
root.order.add_edge(nutrient_mix, monitoring_loop)
root.order.add_edge(water_recycling, monitoring_loop)

# After monitoring loop completes: harvest, packaging, delivery, analysis, forecasting
root.order.add_edge(monitoring_loop, harvest_plan)
root.order.add_edge(harvest_plan, packaging_prep)
root.order.add_edge(packaging_prep, delivery_route)
root.order.add_edge(delivery_route, data_analysis)
root.order.add_edge(data_analysis, yield_forecast)