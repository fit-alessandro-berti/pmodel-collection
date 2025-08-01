# Generated from: 3528ffb9-d79b-40cd-bc2e-05f412707f8b.json
# Description: This process outlines the complex integration of vertical farming systems within urban environments. It involves site analysis, modular design adaptation, multi-layer crop scheduling, automated nutrient delivery, environmental monitoring, community engagement, and logistics coordination. The process addresses challenges like limited space, energy optimization, and real-time data integration to maximize yield while minimizing resource consumption. Additionally, it incorporates IoT device calibration, waste recycling loops, and dynamic market demand adjustments, ensuring sustainable urban agriculture that seamlessly blends technology, ecology, and social factors for efficient food production in dense metropolitan areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey    = Transition(label='Site Survey')
design_adapt   = Transition(label='Design Adapt')
module_build   = Transition(label='Module Build')
crop_plan      = Transition(label='Crop Plan')
seed_prep      = Transition(label='Seed Prep')
planting       = Transition(label='Planting')
nutrient_mix   = Transition(label='Nutrient Mix')
sensor_setup   = Transition(label='Sensor Setup')
climate_control= Transition(label='Climate Control')
data_sync      = Transition(label='Data Sync')
growth_check   = Transition(label='Growth Check')
pest_monitor   = Transition(label='Pest Monitor')
waste_cycle    = Transition(label='Waste Cycle')
harvest        = Transition(label='Harvest')
market_sync    = Transition(label='Market Sync')
community_meet = Transition(label='Community Meet')
energy_audit   = Transition(label='Energy Audit')

# A silent skip for choices
skip = SilentTransition()

# 1) Planning sub‐process: Crop Plan -> Seed Prep -> Planting
planning_PO = StrictPartialOrder(nodes=[crop_plan, seed_prep, planting])
planning_PO.order.add_edge(crop_plan, seed_prep)
planning_PO.order.add_edge(seed_prep, planting)

# 2) Monitoring & Pest check loop:
#    Body A = Growth Check -> Pest Monitor
bodyA = StrictPartialOrder(nodes=[growth_check, pest_monitor])
bodyA.order.add_edge(growth_check, pest_monitor)
#    B = Waste Cycle (recycling loop)
loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[bodyA, waste_cycle])

# 3) Dynamic market adjustment: XOR(Market Sync, skip)
market_choice = OperatorPOWL(operator=Operator.XOR, children=[market_sync, skip])

# 4) Assemble the top‐level partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_adapt,
    module_build,
    planning_PO,
    nutrient_mix,
    sensor_setup,
    climate_control,
    data_sync,
    loop_monitor,
    harvest,
    market_choice,
    community_meet,
    energy_audit
])

# Define the control‐flow dependencies
# Initial analysis & design chain
root.order.add_edge(site_survey, design_adapt)
root.order.add_edge(design_adapt, module_build)

# After modules are built, start planning
root.order.add_edge(module_build, planning_PO)

# After planning completes, proceed to nutrient mix
root.order.add_edge(planning_PO, nutrient_mix)

# Hardware & IoT setup in parallel after module build
root.order.add_edge(module_build, sensor_setup)
root.order.add_edge(module_build, climate_control)
root.order.add_edge(module_build, data_sync)

# All prepare tasks must finish before entering monitoring loop
root.order.add_edge(nutrient_mix, loop_monitor)
root.order.add_edge(sensor_setup, loop_monitor)
root.order.add_edge(climate_control, loop_monitor)
root.order.add_edge(data_sync, loop_monitor)

# After the monitoring/waste‐recycle loop, go to harvest
root.order.add_edge(loop_monitor, harvest)

# Harvest → Market adjustment → Community engagement → Energy audit
root.order.add_edge(harvest, market_choice)
root.order.add_edge(market_choice, community_meet)
root.order.add_edge(community_meet, energy_audit)