# Generated from: 2975a843-6c5b-4be2-9e86-eb8f39c8e600.json
# Description: This process involves the establishment and operationalization of an urban vertical farming system within a densely populated city environment. It begins with site selection based on environmental assessments and zoning regulations, proceeds through modular infrastructure assembly, and integrates IoT sensor deployment for real-time monitoring. Nutrient solution preparation and seed germination are carefully coordinated with automated lighting and climate controls to optimize plant growth cycles. The process further includes pest management via biological controls, waste recycling for sustainability, and periodic data analysis to refine growth algorithms. Harvesting is synchronized with distribution logistics to ensure freshness, while customer feedback loops inform continuous improvement of crop varieties and system efficiency. Overall, the process emphasizes sustainability, technology integration, and urban resource optimization to deliver fresh produce with minimal environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Site_Select = Transition(label='Site Select')
Env_Assess = Transition(label='Env Assess')
Zoning_Check = Transition(label='Zoning Check')
Modular_Build = Transition(label='Modular Build')
Sensor_Deploy = Transition(label='Sensor Deploy')
Nutrient_Prep = Transition(label='Nutrient Prep')
Seed_Germinate = Transition(label='Seed Germinate')
Light_Control = Transition(label='Light Control')
Climate_Adjust = Transition(label='Climate Adjust')
Pest_Manage = Transition(label='Pest Manage')
Waste_Recycle = Transition(label='Waste Recycle')
Data_Analyze = Transition(label='Data Analyze')
Harvest_Sync = Transition(label='Harvest Sync')
Logistics_Plan = Transition(label='Logistics Plan')
Feedback_Loop = Transition(label='Feedback Loop')

# Site selection sequence: Site Select -> Env Assess -> Zoning Check
site_selection = StrictPartialOrder(nodes=[Site_Select, Env_Assess, Zoning_Check])
site_selection.order.add_edge(Site_Select, Env_Assess)
site_selection.order.add_edge(Env_Assess, Zoning_Check)

# Infrastructure and sensor deployment: Modular Build -> Sensor Deploy
infra_sensor = StrictPartialOrder(nodes=[Modular_Build, Sensor_Deploy])
infra_sensor.order.add_edge(Modular_Build, Sensor_Deploy)

# Nutrient prep and seed germination coordinated with lighting and climate:
# Nutrient Prep and Seed Germinate are concurrent -> both precede Light Control and Climate Adjust running concurrently
nutrient_seed = StrictPartialOrder(nodes=[Nutrient_Prep, Seed_Germinate, Light_Control, Climate_Adjust])
nutrient_seed.order.add_edge(Nutrient_Prep, Light_Control)
nutrient_seed.order.add_edge(Nutrient_Prep, Climate_Adjust)
nutrient_seed.order.add_edge(Seed_Germinate, Light_Control)
nutrient_seed.order.add_edge(Seed_Germinate, Climate_Adjust)

# Pest management and waste recycling concurrent but after environment/infrastructure, and before data analyze
pest_waste = StrictPartialOrder(nodes=[Pest_Manage, Waste_Recycle])

# Data analyze after pest and waste
data = StrictPartialOrder(nodes=[Data_Analyze])
# data analyze depends on completion of pest and waste - this will be added later at full PO

# Harvest sync and logistics plan sequential
harvest_logistics = StrictPartialOrder(nodes=[Harvest_Sync, Logistics_Plan])
harvest_logistics.order.add_edge(Harvest_Sync, Logistics_Plan)

# Feedback loop after logistics and data analyze
feedback = StrictPartialOrder(nodes=[Feedback_Loop])

# Combine pest_waste and data analyze (data analyze after both)
pest_waste_data = StrictPartialOrder(
    nodes=[Pest_Manage, Waste_Recycle, Data_Analyze])
pest_waste_data.order.add_edge(Pest_Manage, Data_Analyze)
pest_waste_data.order.add_edge(Waste_Recycle, Data_Analyze)

# Combine harvesting/logistics and feedback loop
harvest_feedback = StrictPartialOrder(nodes=[Harvest_Sync, Logistics_Plan, Feedback_Loop])
harvest_feedback.order.add_edge(Harvest_Sync, Logistics_Plan)
harvest_feedback.order.add_edge(Logistics_Plan, Feedback_Loop)

# Now build full model with all parts in a partial order:

# Nodes: site_selection, infra_sensor, nutrient_seed, pest_waste_data, harvest_feedback

root = StrictPartialOrder(
    nodes=[site_selection, infra_sensor, nutrient_seed, pest_waste_data, harvest_feedback])

# Add edges for control flow
# site_selection before infra_sensor and nutrient_seed
root.order.add_edge(site_selection, infra_sensor)
root.order.add_edge(site_selection, nutrient_seed)

# infra_sensor and nutrient_seed before pest_waste_data
root.order.add_edge(infra_sensor, pest_waste_data)
root.order.add_edge(nutrient_seed, pest_waste_data)

# pest_waste_data before harvest_feedback
root.order.add_edge(pest_waste_data, harvest_feedback)