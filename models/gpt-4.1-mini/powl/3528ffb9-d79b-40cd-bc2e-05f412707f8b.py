# Generated from: 3528ffb9-d79b-40cd-bc2e-05f412707f8b.json
# Description: This process outlines the complex integration of vertical farming systems within urban environments. It involves site analysis, modular design adaptation, multi-layer crop scheduling, automated nutrient delivery, environmental monitoring, community engagement, and logistics coordination. The process addresses challenges like limited space, energy optimization, and real-time data integration to maximize yield while minimizing resource consumption. Additionally, it incorporates IoT device calibration, waste recycling loops, and dynamic market demand adjustments, ensuring sustainable urban agriculture that seamlessly blends technology, ecology, and social factors for efficient food production in dense metropolitan areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Site_Survey = Transition(label='Site Survey')
Design_Adapt = Transition(label='Design Adapt')
Module_Build = Transition(label='Module Build')
Crop_Plan = Transition(label='Crop Plan')
Seed_Prep = Transition(label='Seed Prep')
Planting = Transition(label='Planting')
Nutrient_Mix = Transition(label='Nutrient Mix')
Sensor_Setup = Transition(label='Sensor Setup')
Climate_Control = Transition(label='Climate Control')
Data_Sync = Transition(label='Data Sync')
Growth_Check = Transition(label='Growth Check')
Pest_Monitor = Transition(label='Pest Monitor')
Waste_Cycle = Transition(label='Waste Cycle')
Harvest = Transition(label='Harvest')
Market_Sync = Transition(label='Market Sync')
Community_Meet = Transition(label='Community Meet')
Energy_Audit = Transition(label='Energy Audit')

# Waste recycling loop: Waste_Cycle repeated with Planting (replant/recycle)
waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[Planting, Waste_Cycle])

# Growth monitoring with Pest monitoring in partial order to run concurrent with Growth_Check
growth_monitoring = StrictPartialOrder(
    nodes=[Growth_Check, Pest_Monitor]
)
# no edges means concurrent

# Automated nutrient delivery sequence: Nutrient_Mix -> Sensor_Setup -> Climate_Control
nutrient_sequence = StrictPartialOrder(
    nodes=[Nutrient_Mix, Sensor_Setup, Climate_Control]
)
nutrient_sequence.order.add_edge(Nutrient_Mix, Sensor_Setup)
nutrient_sequence.order.add_edge(Sensor_Setup, Climate_Control)

# Multi-layer crop scheduling & seed preparation before Planting
crop_sequence = StrictPartialOrder(
    nodes=[Crop_Plan, Seed_Prep]
)
crop_sequence.order.add_edge(Crop_Plan, Seed_Prep)

# Community engagement and Energy auditing concurrent
community_energy = StrictPartialOrder(
    nodes=[Community_Meet, Energy_Audit]
)
# no edges means concurrent

# Market sync runs after Harvest
market_after_harvest = StrictPartialOrder(
    nodes=[Harvest, Market_Sync]
)
market_after_harvest.order.add_edge(Harvest, Market_Sync)

# Site survey precedes design adapt which precedes module build
design_module = StrictPartialOrder(
    nodes=[Site_Survey, Design_Adapt, Module_Build]
)
design_module.order.add_edge(Site_Survey, Design_Adapt)
design_module.order.add_edge(Design_Adapt, Module_Build)

# Data Sync occurs after Climate Control and concurrent with Growth monitoring & Pest
# Combine Climate Control, growth_monitoring, Data_Sync in partial order
data_and_monitoring = StrictPartialOrder(
    nodes=[Climate_Control, growth_monitoring, Data_Sync]
)
data_and_monitoring.order.add_edge(Climate_Control, Data_Sync)
# growth_monitoring concurrent with Data_Sync and Climate_Control (no edge to it)

# Overall crop cycle: crop_sequence -> planting and waste_loop (planting + waste loop) -> harvest + monitoring + nutrient_sequence
# Combine crop_sequence -> waste_loop (waste loop incorporates Planting)
crop_and_planting = StrictPartialOrder(
    nodes=[crop_sequence, waste_loop]
)
crop_and_planting.order.add_edge(crop_sequence, waste_loop)

# Combine nutrient_sequence before data_and_monitoring
nutrient_before_data = StrictPartialOrder(
    nodes=[nutrient_sequence, data_and_monitoring]
)
nutrient_before_data.order.add_edge(nutrient_sequence, data_and_monitoring)

# Combine all main flows:
# design_module -> crop_and_planting -> nutrient_before_data -> harvest_and_market & community_energy
harvest_and_market = market_after_harvest
main_post_planting = StrictPartialOrder(
    nodes=[nutrient_before_data, harvest_and_market, community_energy, growth_monitoring]
)
# Nutrient/data flows before harvest_and_market and community_energy and growth_monitoring
main_post_planting.order.add_edge(nutrient_before_data, harvest_and_market)
main_post_planting.order.add_edge(nutrient_before_data, community_energy)
main_post_planting.order.add_edge(nutrient_before_data, growth_monitoring)

overall_process = StrictPartialOrder(
    nodes=[design_module, crop_and_planting, main_post_planting]
)
overall_process.order.add_edge(design_module, crop_and_planting)
overall_process.order.add_edge(crop_and_planting, main_post_planting)

root = overall_process