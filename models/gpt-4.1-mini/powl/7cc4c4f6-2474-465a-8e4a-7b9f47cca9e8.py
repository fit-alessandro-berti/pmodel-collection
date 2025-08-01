# Generated from: 7cc4c4f6-2474-465a-8e4a-7b9f47cca9e8.json
# Description: This process outlines the complex operational workflow of an urban vertical farming facility integrating automated environmental controls, real-time data analytics, and multi-crop management to maximize yield. The cycle begins with seed selection and preparation, followed by nutrient solution formulation tailored to each crop. Automated seeding and planting occur next, supported by environmental monitoring that adjusts lighting, humidity, and temperature dynamically. Growth phases are tracked via sensor arrays and AI-driven health assessments, triggering targeted interventions such as pest control or nutrient adjustments. Harvesting is scheduled based on optimal maturity indices and coordinated with packaging and cold storage systems. Waste recycling and water reclamation subsystems ensure sustainability. Finally, data is archived for continuous improvement and market forecasting, completing a closed-loop, tech-enabled agricultural ecosystem uncommon in traditional farming yet realistic for modern urban food production.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
Seed_Prep = Transition(label='Seed Prep')
Nutrient_Mix = Transition(label='Nutrient Mix')
Automated_Plant = Transition(label='Automated Plant')

Env_Monitor = Transition(label='Env Monitor')
Light_Adjust = Transition(label='Light Adjust')
Humidity_Control = Transition(label='Humidity Control')
Temp_Regulate = Transition(label='Temp Regulate')

Growth_Track = Transition(label='Growth Track')
Health_Assess = Transition(label='Health Assess')

Pest_Control = Transition(label='Pest Control')
Nutrient_Boost = Transition(label='Nutrient Boost')

Harvest_Plan = Transition(label='Harvest Plan')
Packaging_Prep = Transition(label='Packaging Prep')
Cold_Storage = Transition(label='Cold Storage')

Waste_Recycle = Transition(label='Waste Recycle')
Water_Reclaim = Transition(label='Water Reclaim')

Data_Archive = Transition(label='Data Archive')
Market_Forecast = Transition(label='Market Forecast')

# Environmental controls partial order (concurrent and partially ordered adjustments after Env Monitor)
env_controls = StrictPartialOrder(nodes=[Light_Adjust, Humidity_Control, Temp_Regulate])
env_controls.order.add_edge(Light_Adjust, Humidity_Control)    # Adjust lighting before humidity control
env_controls.order.add_edge(Humidity_Control, Temp_Regulate)  # Then humidity before temperature

# Interventions choice: either Pest_Control or Nutrient_Boost or none (skip)
from pm4py.objects.powl.obj import SilentTransition
skip = SilentTransition()
intervention_choice = OperatorPOWL(operator=Operator.XOR, children=[Pest_Control, Nutrient_Boost, skip])

# Growth tracking partial order: Growth_Track before Health_Assess
growth_tracking = StrictPartialOrder(nodes=[Growth_Track, Health_Assess])
growth_tracking.order.add_edge(Growth_Track, Health_Assess)

# Interventions loop: after growth tracking & health assess, optionally loop interventions + growth tracking again
# So, loop node with:
# A = growth_tracking + health_assess
# B = intervention_choice
# But growth_tracking is two activities with order, so we need to combine growth_tracking and health_assess as one node? 
# Instead, compose a partial order inside the loop to represent (Growth_Track -> Health_Assess)
loop_body = StrictPartialOrder(nodes=[Growth_Track, Health_Assess])
loop_body.order.add_edge(Growth_Track, Health_Assess)
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, intervention_choice])

# Harvesting sequence (Harvest_Plan -> Packaging_Prep -> Cold_Storage)
harvest_seq = StrictPartialOrder(nodes=[Harvest_Plan, Packaging_Prep, Cold_Storage])
harvest_seq.order.add_edge(Harvest_Plan, Packaging_Prep)
harvest_seq.order.add_edge(Packaging_Prep, Cold_Storage)

# Sustainability partial order (Waste_Recycle and Water_Reclaim concurrent)
sustainability = StrictPartialOrder(nodes=[Waste_Recycle, Water_Reclaim])

# Final archiving partial order: Data_Archive -> Market_Forecast
archiving = StrictPartialOrder(nodes=[Data_Archive, Market_Forecast])
archiving.order.add_edge(Data_Archive, Market_Forecast)

# Now top level partial order:
# Seed_Prep -> Nutrient_Mix -> Automated_Plant -> Env_Monitor -> env_controls partial order
# env_controls -> loop (growth tracking + interventions)
# loop -> harvest_seq
# harvest_seq -> sustainability
# sustainability -> archiving

# Compose the top-level partial order nodes
nodes = [
    Seed_Prep,
    Nutrient_Mix,
    Automated_Plant,
    Env_Monitor,
    env_controls,
    loop,
    harvest_seq,
    sustainability,
    archiving
]
root = StrictPartialOrder(nodes=nodes)

# Add edges to encode the described ordering
root.order.add_edge(Seed_Prep, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Automated_Plant)
root.order.add_edge(Automated_Plant, Env_Monitor)
root.order.add_edge(Env_Monitor, env_controls)
root.order.add_edge(env_controls, loop)
root.order.add_edge(loop, harvest_seq)
root.order.add_edge(harvest_seq, sustainability)
root.order.add_edge(sustainability, archiving)