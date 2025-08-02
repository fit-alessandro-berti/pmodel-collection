# Generated from: 08ff2518-c8ad-42d1-8acb-afc41547497a.json
# Description: This process outlines the intricate steps involved in establishing an urban vertical farm within a densely populated city environment. It includes site analysis, regulatory compliance, modular system design, climate control calibration, nutrient cycling optimization, and community integration. The process requires coordination among agronomists, engineers, local authorities, and marketing teams to ensure sustainability, crop yield maximization, and economic viability while minimizing environmental impact in constrained urban spaces. It culminates in continuous monitoring and adaptive management to respond to urban challenges such as pollution, limited sunlight, and water reuse.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Site_Survey    = Transition(label='Site Survey')
Permit_Filing  = Transition(label='Permit Filing')
Module_Design  = Transition(label='Module Design')
Sensor_Setup   = Transition(label='Sensor Setup')
Climate_Adjust = Transition(label='Climate Adjust')
Water_Cycle    = Transition(label='Water Cycle')
Nutrient_Prep  = Transition(label='Nutrient Prep')
Seed_Sowing    = Transition(label='Seed Sowing')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control   = Transition(label='Pest Control')
Harvest_Plan   = Transition(label='Harvest Plan')
Market_Study   = Transition(label='Market Study')
Community_Meet = Transition(label='Community Meet')
Waste_Reuse    = Transition(label='Waste Reuse')
Data_Review    = Transition(label='Data Review')
Yield_Audit    = Transition(label='Yield Audit')
Feedback_Loop  = Transition(label='Feedback Loop')

# Step 1: Regulatory & Site Preparation partial order
# Site Survey -> Permit Filing
regulatory_preparation = StrictPartialOrder(
    nodes=[Site_Survey, Permit_Filing]
)
regulatory_preparation.order.add_edge(Site_Survey, Permit_Filing)

# Step 2: Modular Design and Sensor Setup
module_and_sensor = StrictPartialOrder(
    nodes=[Module_Design, Sensor_Setup]
)
# No order between them (concurrent)

# Step 3: Climate and nutrient control partial order:
# Climate Adjust -> (Water Cycle and Nutrient Prep) concurrent
climate_and_nutrient = StrictPartialOrder(
    nodes=[Climate_Adjust, Water_Cycle, Nutrient_Prep]
)
climate_and_nutrient.order.add_edge(Climate_Adjust, Water_Cycle)
climate_and_nutrient.order.add_edge(Climate_Adjust, Nutrient_Prep)
# Water Cycle and Nutrient Prep concurrent

# Step 4: Planting and Monitoring partial order
# Seed Sowing -> Growth Monitor -> Pest Control
plant_cycle = StrictPartialOrder(
    nodes=[Seed_Sowing, Growth_Monitor, Pest_Control]
)
plant_cycle.order.add_edge(Seed_Sowing, Growth_Monitor)
plant_cycle.order.add_edge(Growth_Monitor, Pest_Control)

# Step 5: Harvest Planning and Market Study concurrent
harvest_and_market = StrictPartialOrder(
    nodes=[Harvest_Plan, Market_Study]
)
# concurrent

# Step 6: Community Meeting and Waste Reuse concurrent
community_and_waste = StrictPartialOrder(
    nodes=[Community_Meet, Waste_Reuse]
)
# concurrent

# Step 7: Monitoring and Adaptive Management loop
# Data Review -> Yield Audit -> Feedback Loop repeats (loop)
monitoring_loop_body = StrictPartialOrder(
    nodes=[Data_Review, Yield_Audit]
)
monitoring_loop_body.order.add_edge(Data_Review, Yield_Audit)

monitoring_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitoring_loop_body, Feedback_Loop]
)

# Compose the overall main partial order with edges to reflect coordination flow.

# Overall order structure:
# regulatory_preparation -> module_and_sensor -> climate_and_nutrient -> plant_cycle
# plant_cycle -> harvest_and_market
# harvest_and_market -> community_and_waste
# community_and_waste -> monitoring_loop

root = StrictPartialOrder(
    nodes=[
        regulatory_preparation,
        module_and_sensor,
        climate_and_nutrient,
        plant_cycle,
        harvest_and_market,
        community_and_waste,
        monitoring_loop
    ]
)

root.order.add_edge(regulatory_preparation, module_and_sensor)
root.order.add_edge(module_and_sensor, climate_and_nutrient)
root.order.add_edge(climate_and_nutrient, plant_cycle)
root.order.add_edge(plant_cycle, harvest_and_market)
root.order.add_edge(harvest_and_market, community_and_waste)
root.order.add_edge(community_and_waste, monitoring_loop)