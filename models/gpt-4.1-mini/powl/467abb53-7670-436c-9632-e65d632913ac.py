# Generated from: 467abb53-7670-436c-9632-e65d632913ac.json
# Description: This process involves the complex orchestration of urban vertical farm development, integrating architectural design, environmental control systems, and agricultural science to optimize crop yield in constrained city spaces. It starts with site assessment and feasibility analysis, followed by modular farm design and structural adaptation to existing buildings. Subsequently, it includes installing hydroponic and aeroponic systems, integrating IoT sensors for real-time monitoring, and implementing automated nutrient delivery and climate regulation. The process also covers workforce training, supply chain coordination for seed and resource procurement, and establishing waste recycling protocols. Continuous data collection and AI-driven crop management optimize growth cycles, while marketing strategies are aligned to promote locally grown produce. This atypical business process blends technology, sustainability, and urban planning to revolutionize food production in metropolitan areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Assess = Transition(label='Site Assess')
Feasibility_Eval = Transition(label='Feasibility Eval')
Modular_Design = Transition(label='Modular Design')
Structure_Adapt = Transition(label='Structure Adapt')
System_Install = Transition(label='System Install')
Sensor_Deploy = Transition(label='Sensor Deploy')
Nutrient_Setup = Transition(label='Nutrient Setup')
Climate_Control = Transition(label='Climate Control')
Worker_Train = Transition(label='Worker Train')
Seed_Procure = Transition(label='Seed Procure')
Resource_Manage = Transition(label='Resource Manage')
Waste_Recycle = Transition(label='Waste Recycle')
Data_Collect = Transition(label='Data Collect')
AI_Optimize = Transition(label='AI Optimize')
Market_Launch = Transition(label='Market Launch')
Supply_Sync = Transition(label='Supply Sync')

# Step 1: site assessment and feasibility evaluation (serial)
step1 = StrictPartialOrder(nodes=[Site_Assess, Feasibility_Eval])
step1.order.add_edge(Site_Assess, Feasibility_Eval)

# Step 2: modular design and structural adaptation (serial)
step2 = StrictPartialOrder(nodes=[Modular_Design, Structure_Adapt])
step2.order.add_edge(Modular_Design, Structure_Adapt)

# Step 3: installing hydroponic and aeroponic systems modeled as System Install (single activity)
# No explicit separation, so just System_Install

# Step 4 & 5: sensor deploy, nutrient setup, climate control (serial)
step4_5 = StrictPartialOrder(nodes=[Sensor_Deploy, Nutrient_Setup, Climate_Control])
step4_5.order.add_edge(Sensor_Deploy, Nutrient_Setup)
step4_5.order.add_edge(Nutrient_Setup, Climate_Control)

# Step 6: workforce training (single)
# Step 7: supply chain coordination for seed and resource procurement modeled as supply sync, seed procure, resource manage
supply_chain = StrictPartialOrder(nodes=[Supply_Sync, Seed_Procure, Resource_Manage])
supply_chain.order.add_edge(Supply_Sync, Seed_Procure)
supply_chain.order.add_edge(Seed_Procure, Resource_Manage)

# Step 8: waste recycling (single)

# Step 9: continuous data collection and AI-driven crop management (serial)
data_ai = StrictPartialOrder(nodes=[Data_Collect, AI_Optimize])
data_ai.order.add_edge(Data_Collect, AI_Optimize)

# Step 10: marketing strategies aligned to promote produce (single)

# Now combine the above steps in the natural process order inferred from description:

# Overall order:
# Step1 --> Step2 --> System_Install --> step4_5 --> Worker_Train
#            --> supply_chain and Waste_Recycle concurrent after step4_5 and Worker_Train
# data_ai and Market_Launch concurrent after above
# So we compose partial orders to represent concurrency and order

# Construct partial order of initial steps with proper order

initial_steps = StrictPartialOrder(nodes=[step1, step2])
initial_steps.order.add_edge(step1, step2)

# Then step2 before System_Install

s1 = StrictPartialOrder(nodes=[initial_steps, System_Install])
s1.order.add_edge(initial_steps, System_Install)

# Then step4_5 after System_Install

s2 = StrictPartialOrder(nodes=[s1, step4_5])
s2.order.add_edge(s1, step4_5)

# Worker_Train after step4_5

s3 = StrictPartialOrder(nodes=[s2, Worker_Train])
s3.order.add_edge(s2, Worker_Train)

# supply_chain and Waste_Recycle concurrent, both after Worker_Train (and step4_5)

# Create supply_chain and Waste_Recycle in a partial order, no order between them, both after s3

post_train = StrictPartialOrder(nodes=[s3, supply_chain, Waste_Recycle])
post_train.order.add_edge(s3, supply_chain)
post_train.order.add_edge(s3, Waste_Recycle)

# data_ai and Market_Launch concurrent after supply_chain and Waste_Recycle

post_supply_waste = StrictPartialOrder(nodes=[post_train, data_ai, Market_Launch])
post_supply_waste.order.add_edge(post_train, data_ai)
post_supply_waste.order.add_edge(post_train, Market_Launch)

# Final root

root = post_supply_waste