# Generated from: 99342759-50ea-442e-bb5d-87e7e5178f70.json
# Description: This process details the intricate steps involved in sourcing, producing, aging, packaging, and distributing small-batch artisan cheese. It begins with selecting rare milk varieties from niche farms, followed by precise fermentation and curdling techniques unique to each cheese type. The aging process involves controlled environments tailored for texture and flavor development. Quality control includes microscopic bacterial analysis and sensory evaluation. Packaging uses biodegradable materials with embedded freshness sensors. Distribution prioritizes temperature-controlled logistics and direct relationships with specialty retailers and exclusive restaurants, ensuring optimal product integrity and customer satisfaction throughout the supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Milk_Sourcing = Transition(label='Milk Sourcing')
Milk_Testing = Transition(label='Milk Testing')
Culture_Prep = Transition(label='Culture Prep')
Curd_Formation = Transition(label='Curd Formation')
Whey_Removal = Transition(label='Whey Removal')
Pressing_Cheese = Transition(label='Pressing Cheese')
Salt_Application = Transition(label='Salt Application')
Aging_Setup = Transition(label='Aging Setup')
Microbial_Check = Transition(label='Microbial Check')
Sensory_Test = Transition(label='Sensory Test')
Packaging_Prep = Transition(label='Packaging Prep')
Sensor_Embed = Transition(label='Sensor Embed')
Label_Printing = Transition(label='Label Printing')
Storage_Monitor = Transition(label='Storage Monitor')
Logistics_Plan = Transition(label='Logistics Plan')
Retail_Delivery = Transition(label='Retail Delivery')
Customer_Feedback = Transition(label='Customer Feedback')

# Defining partial order for Milk Sourcing and Testing phases
milk_po = StrictPartialOrder(nodes=[Milk_Sourcing, Milk_Testing])
milk_po.order.add_edge(Milk_Sourcing, Milk_Testing)

# Cheese production: Culture Prep -> Curd Formation -> Whey Removal -> Pressing Cheese -> Salt Application
prod_po = StrictPartialOrder(
    nodes=[Culture_Prep, Curd_Formation, Whey_Removal, Pressing_Cheese, Salt_Application]
)
prod_po.order.add_edge(Culture_Prep, Curd_Formation)
prod_po.order.add_edge(Curd_Formation, Whey_Removal)
prod_po.order.add_edge(Whey_Removal, Pressing_Cheese)
prod_po.order.add_edge(Pressing_Cheese, Salt_Application)

# Aging: Aging Setup followed by Microbial Check and Sensory Test (these two concurrent)
aging_po = StrictPartialOrder(nodes=[Aging_Setup, Microbial_Check, Sensory_Test])
aging_po.order.add_edge(Aging_Setup, Microbial_Check)
aging_po.order.add_edge(Aging_Setup, Sensory_Test)

# Packaging: Packaging Prep -> Sensor Embed -> Label Printing
packaging_po = StrictPartialOrder(nodes=[Packaging_Prep, Sensor_Embed, Label_Printing])
packaging_po.order.add_edge(Packaging_Prep, Sensor_Embed)
packaging_po.order.add_edge(Sensor_Embed, Label_Printing)

# Distribution: Storage Monitor -> Logistics Plan -> Retail Delivery
distribution_po = StrictPartialOrder(nodes=[Storage_Monitor, Logistics_Plan, Retail_Delivery])
distribution_po.order.add_edge(Storage_Monitor, Logistics_Plan)
distribution_po.order.add_edge(Logistics_Plan, Retail_Delivery)

# Final: Customer Feedback after Retail Delivery
final_po = StrictPartialOrder(nodes=[Retail_Delivery, Customer_Feedback])
final_po.order.add_edge(Retail_Delivery, Customer_Feedback)

# Combine these partial orders in a global PO with proper order edges
# The global sequence:
# milk_po -> prod_po -> aging_po -> packaging_po -> distribution_po -> final_po

root = StrictPartialOrder(
    nodes=[milk_po, prod_po, aging_po, packaging_po, distribution_po, final_po]
)
root.order.add_edge(milk_po, prod_po)
root.order.add_edge(prod_po, aging_po)
root.order.add_edge(aging_po, packaging_po)
root.order.add_edge(packaging_po, distribution_po)
root.order.add_edge(distribution_po, final_po)