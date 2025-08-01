# Generated from: f25fec57-98f3-4544-8bef-1c29fce4f714.json
# Description: This process outlines the establishment of an urban vertical farm designed to optimize limited city space for sustainable agriculture. It involves selecting appropriate building infrastructure, integrating hydroponic systems, installing automated climate controls, and implementing AI-driven crop monitoring. The process also includes securing permits, sourcing organic nutrients, establishing waste recycling protocols, training staff on specialized equipment, and coordinating supply chain logistics for distribution. This atypical yet realistic workflow addresses complex challenges of urban farming scalability and environmental impact, ensuring efficient production of fresh produce within metropolitan areas while minimizing resource consumption and maximizing yield through technology integration and operational synergies.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Survey = Transition(label='Site Survey')
Permit_Filing = Transition(label='Permit Filing')
Structure_Design = Transition(label='Structure Design')
System_Install = Transition(label='System Install')
Hydroponic_Setup = Transition(label='Hydroponic Setup')
Climate_Config = Transition(label='Climate Config')
AI_Integration = Transition(label='AI Integration')
Nutrient_Sourcing = Transition(label='Nutrient Sourcing')
Waste_Planning = Transition(label='Waste Planning')
Staff_Training = Transition(label='Staff Training')
Crop_Seeding = Transition(label='Crop Seeding')
Growth_Monitoring = Transition(label='Growth Monitoring')
Quality_Testing = Transition(label='Quality Testing')
Harvest_Scheduling = Transition(label='Harvest Scheduling')
Distribution_Plan = Transition(label='Distribution Plan')
Data_Analysis = Transition(label='Data Analysis')

# Build partial orders for main phases

# Phase 1: Site Survey and Permit Filing (Permit Filing after Site Survey)
phase1 = StrictPartialOrder(nodes=[Site_Survey, Permit_Filing])
phase1.order.add_edge(Site_Survey, Permit_Filing)

# Phase 2: Design infrastructure and install systems/tools
# Structure Design -> System Install -> Hydroponic Setup -> Climate Config -> AI Integration
phase2 = StrictPartialOrder(nodes=[Structure_Design, System_Install, Hydroponic_Setup, Climate_Config, AI_Integration])
phase2.order.add_edge(Structure_Design, System_Install)
phase2.order.add_edge(System_Install, Hydroponic_Setup)
phase2.order.add_edge(Hydroponic_Setup, Climate_Config)
phase2.order.add_edge(Climate_Config, AI_Integration)

# Phase 3: Resource provision & planning (some activities concurrent)
# Nutrient Sourcing, Waste Planning, Staff Training can overlap
resourcing = StrictPartialOrder(nodes=[Nutrient_Sourcing, Waste_Planning, Staff_Training])
# No order edges: concurrent

# Phase 4: Production activities in order:
# Crop Seeding -> Growth Monitoring -> Quality Testing -> Harvest Scheduling
production = StrictPartialOrder(nodes=[Crop_Seeding, Growth_Monitoring, Quality_Testing, Harvest_Scheduling])
production.order.add_edge(Crop_Seeding, Growth_Monitoring)
production.order.add_edge(Growth_Monitoring, Quality_Testing)
production.order.add_edge(Quality_Testing, Harvest_Scheduling)

# Phase 5: Distribution planning and Data analysis can occur concurrently after production
distribution_analysis = StrictPartialOrder(nodes=[Distribution_Plan, Data_Analysis])
# no order edges, concurrent

# Compose the entire process as partial order, linking phases:
# phase1 --> phase2 --> resourcing & production --> distribution_analysis
# With resourcing concurrent with production, but both after phase2

root = StrictPartialOrder(
    nodes=[phase1, phase2, resourcing, production, distribution_analysis]
)

# Order edges connecting phases
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, resourcing)
root.order.add_edge(phase2, production)
root.order.add_edge(production, distribution_analysis)
root.order.add_edge(resourcing, distribution_analysis)