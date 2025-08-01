# Generated from: 5d0b7a16-926f-48ce-b2df-0a87ce204be0.json
# Description: This process outlines the establishment of a fully automated urban vertical farm specializing in exotic microgreens and rare herbs. It involves site assessment, modular system design, automated nutrient calibration, climate optimization using AI, pest bio-control integration, and continuous yield monitoring. The process further incorporates local community engagement for education, waste recycling through composting, and real-time market demand analysis to adjust crop cycles dynamically. It ensures sustainable resource use, minimal carbon footprint, and high-quality organic produce delivery within urban environments through advanced logistics and smart packaging solutions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_survey     = Transition(label="Site Survey")
modular_design  = Transition(label="Modular Design")
system_assembly = Transition(label="System Assembly")
sensor_install  = Transition(label="Sensor Install")
nutrient_setup  = Transition(label="Nutrient Setup")
climate_tune    = Transition(label="Climate Tune")
pest_control    = Transition(label="Pest Control")
seed_selection  = Transition(label="Seed Selection")
planting_cycle  = Transition(label="Planting Cycle")
growth_monitor  = Transition(label="Growth Monitor")
waste_cycle     = Transition(label="Waste Cycle")
market_scan     = Transition(label="Market Scan")
demand_adjust   = Transition(label="Demand Adjust")
harvest_prep    = Transition(label="Harvest Prep")
packaging_ops   = Transition(label="Packaging Ops")
delivery_plan   = Transition(label="Delivery Plan")
community_meet  = Transition(label="Community Meet")

# Build the loop body: Growth Monitor -> Waste Cycle -> Market Scan -> Demand Adjust
body = StrictPartialOrder(nodes=[growth_monitor, waste_cycle, market_scan, demand_adjust])
body.order.add_edge(growth_monitor, waste_cycle)
body.order.add_edge(waste_cycle, market_scan)
body.order.add_edge(market_scan, demand_adjust)

# Build the LOOP: Planting Cycle, then repeat the body + Planting Cycle
loop = OperatorPOWL(operator=Operator.LOOP, children=[planting_cycle, body])

# Build the main partial order
root = StrictPartialOrder(
    nodes=[
        site_survey,
        modular_design,
        system_assembly,
        sensor_install,
        nutrient_setup,
        climate_tune,
        pest_control,
        seed_selection,
        loop,
        harvest_prep,
        packaging_ops,
        delivery_plan,
        community_meet
    ]
)

# Define the main control-flow edges
root.order.add_edge(site_survey, modular_design)
root.order.add_edge(modular_design, system_assembly)
root.order.add_edge(system_assembly, sensor_install)
root.order.add_edge(sensor_install, nutrient_setup)
root.order.add_edge(nutrient_setup, climate_tune)
root.order.add_edge(climate_tune, pest_control)
root.order.add_edge(pest_control, seed_selection)
root.order.add_edge(seed_selection, loop)
root.order.add_edge(loop, harvest_prep)
root.order.add_edge(harvest_prep, packaging_ops)
root.order.add_edge(packaging_ops, delivery_plan)

# Community engagement can happen in parallel after system assembly
root.order.add_edge(system_assembly, community_meet)