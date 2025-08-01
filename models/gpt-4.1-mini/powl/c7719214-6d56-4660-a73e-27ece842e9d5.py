# Generated from: c7719214-6d56-4660-a73e-27ece842e9d5.json
# Description: This process outlines the intricate supply chain management for artisan cheese production, starting from sourcing rare milk varieties from micro-farms, monitoring seasonal animal diets, coordinating fermentation timing, to ensuring optimal aging conditions in climate-controlled caves. It integrates quality checks, custom packaging, and niche market distribution through boutique retailers and specialty food events. Each step involves close collaboration with local farmers, microbiologists, logistics experts, and marketing teams to maintain authentic flavor profiles while adapting to fluctuating demand and regulatory requirements. The process balances tradition with innovation, emphasizing traceability and sustainability at every stage, guaranteeing a product that meets exacting standards and satisfies discerning consumers in a competitive gourmet market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Milk_Sourcing = Transition(label='Milk Sourcing')
Diet_Monitoring = Transition(label='Diet Monitoring')
Culture_Selection = Transition(label='Culture Selection')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Draining = Transition(label='Whey Draining')
Mold_Inoculate = Transition(label='Mold Inoculate')
Press_Forming = Transition(label='Press Forming')
Salt_Application = Transition(label='Salt Application')
Aging_Setup = Transition(label='Aging Setup')
Humidity_Control = Transition(label='Humidity Control')
Flavor_Testing = Transition(label='Flavor Testing')
Packaging_Design = Transition(label='Packaging Design')
Order_Processing = Transition(label='Order Processing')
Retail_Delivery = Transition(label='Retail Delivery')
Event_Coordination = Transition(label='Event Coordination')
Feedback_Review = Transition(label='Feedback Review')

# Stage 1: Milk sourcing and diet monitoring in parallel but both precede culture selection
po1 = StrictPartialOrder(
    nodes=[Milk_Sourcing, Diet_Monitoring, Culture_Selection]
)
po1.order.add_edge(Milk_Sourcing, Culture_Selection)
po1.order.add_edge(Diet_Monitoring, Culture_Selection)

# Stage 2: Pasteurize milk then cut curd and drain whey sequentially
po2 = StrictPartialOrder(
    nodes=[Milk_Pasteurize, Curd_Cutting, Whey_Draining]
)
po2.order.add_edge(Milk_Pasteurize, Curd_Cutting)
po2.order.add_edge(Curd_Cutting, Whey_Draining)

# Stage 3: Mold inoculation, press forming and salt application sequentially
po3 = StrictPartialOrder(
    nodes=[Mold_Inoculate, Press_Forming, Salt_Application]
)
po3.order.add_edge(Mold_Inoculate, Press_Forming)
po3.order.add_edge(Press_Forming, Salt_Application)

# Stage 4: Aging setup precedes humidity control and then flavor testing
po4 = StrictPartialOrder(
    nodes=[Aging_Setup, Humidity_Control, Flavor_Testing]
)
po4.order.add_edge(Aging_Setup, Humidity_Control)
po4.order.add_edge(Humidity_Control, Flavor_Testing)

# Stage 5: Packaging design then order processing
po5 = StrictPartialOrder(
    nodes=[Packaging_Design, Order_Processing]
)
po5.order.add_edge(Packaging_Design, Order_Processing)

# Stage 6: Retail delivery and event coordination happen in parallel after order processing
po6 = StrictPartialOrder(
    nodes=[Retail_Delivery, Event_Coordination, Feedback_Review]
)
po6.order.add_edge(Retail_Delivery, Feedback_Review)
po6.order.add_edge(Event_Coordination, Feedback_Review)

# Combine the stages into a partial order reflecting the process flow
root = StrictPartialOrder(
    nodes=[po1, po2, po3, po4, po5, po6]
)
# Order dependencies among stages:

# Stage 1 -> Stage 2 and Stage 3 (Fermentation timing coordination after culture selection)
root.order.add_edge(po1, po2)
root.order.add_edge(po1, po3)

# Stage 2 and Stage 3 both precede Stage 4 (Aging setup depends on previous steps)
root.order.add_edge(po2, po4)
root.order.add_edge(po3, po4)

# Stage 4 precedes packaging and order processing (Stage 5)
root.order.add_edge(po4, po5)

# Packaging and order processing precede delivery and event coordination (Stage 6)
root.order.add_edge(po5, po6)