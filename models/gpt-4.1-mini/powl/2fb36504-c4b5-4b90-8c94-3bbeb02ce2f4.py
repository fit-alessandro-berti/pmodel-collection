# Generated from: 2fb36504-c4b5-4b90-8c94-3bbeb02ce2f4.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farming facility within a repurposed industrial building. It involves assessing structural integrity, selecting suitable crops, designing multi-tier hydroponic systems, integrating IoT sensors for climate control, sourcing sustainable materials, setting up automated nutrient delivery, implementing renewable energy solutions, training staff on specialized farming techniques, establishing supply chain logistics for perishable goods, ensuring compliance with local agricultural and safety regulations, and launching a community engagement program to promote urban agriculture awareness. The process requires coordination among architects, agronomists, engineers, and marketing teams to create a resilient, efficient, and scalable urban farm that addresses food security in densely populated areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Structural_Check = Transition(label='Structural Check')
Crop_Select = Transition(label='Crop Select')
System_Design = Transition(label='System Design')
IoT_Setup = Transition(label='IoT Setup')
Material_Sourcing = Transition(label='Material Sourcing')
Nutrient_Plan = Transition(label='Nutrient Plan')
Energy_Install = Transition(label='Energy Install')
Staff_Training = Transition(label='Staff Training')
Logistics_Plan = Transition(label='Logistics Plan')
Regulation_Audit = Transition(label='Regulation Audit')
Community_Outreach = Transition(label='Community Outreach')
Quality_Testing = Transition(label='Quality Testing')
Market_Launch = Transition(label='Market Launch')
Feedback_Loop = Transition(label='Feedback Loop')

# Feedback_Loop will form a loop with Quality_Testing
loop = OperatorPOWL(operator=Operator.LOOP, children=[Quality_Testing, Feedback_Loop])

# StrictPartialOrder of the main process:
# Steps modeled in a partial order, reflecting the description:

# 1) Initial assessments:
# Site Survey --> Structural Check --> Crop Select
# 2) Design and setup:
# Crop Select --> System Design --> IoT Setup
# 3) Procurement and setup:
# IoT Setup --> Material Sourcing --> Nutrient Plan --> Energy Install
# 4) Training staff:
# Energy Install --> Staff Training
# 5) Planning logistics and compliance:
# Staff Training --> Logistics Plan --> Regulation Audit
# 6) Community engagement and launch:
# Regulation Audit --> Community Outreach --> Market Launch
# 7) Quality testing and feedback loop on product/process quality
# Market Launch --> loop (Quality Testing + Feedback Loop)

nodes = [Site_Survey, Structural_Check, Crop_Select, System_Design, IoT_Setup, Material_Sourcing,
         Nutrient_Plan, Energy_Install, Staff_Training, Logistics_Plan, Regulation_Audit,
         Community_Outreach, Market_Launch, loop]

root = StrictPartialOrder(nodes=nodes)
root.order.add_edge(Site_Survey, Structural_Check)
root.order.add_edge(Structural_Check, Crop_Select)
root.order.add_edge(Crop_Select, System_Design)
root.order.add_edge(System_Design, IoT_Setup)
root.order.add_edge(IoT_Setup, Material_Sourcing)
root.order.add_edge(Material_Sourcing, Nutrient_Plan)
root.order.add_edge(Nutrient_Plan, Energy_Install)
root.order.add_edge(Energy_Install, Staff_Training)
root.order.add_edge(Staff_Training, Logistics_Plan)
root.order.add_edge(Logistics_Plan, Regulation_Audit)
root.order.add_edge(Regulation_Audit, Community_Outreach)
root.order.add_edge(Community_Outreach, Market_Launch)
root.order.add_edge(Market_Launch, loop)