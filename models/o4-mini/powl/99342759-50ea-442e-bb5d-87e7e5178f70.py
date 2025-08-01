# Generated from: 99342759-50ea-442e-bb5d-87e7e5178f70.json
# Description: This process details the intricate steps involved in sourcing, producing, aging, packaging, and distributing small-batch artisan cheese. It begins with selecting rare milk varieties from niche farms, followed by precise fermentation and curdling techniques unique to each cheese type. The aging process involves controlled environments tailored for texture and flavor development. Quality control includes microscopic bacterial analysis and sensory evaluation. Packaging uses biodegradable materials with embedded freshness sensors. Distribution prioritizes temperature-controlled logistics and direct relationships with specialty retailers and exclusive restaurants, ensuring optimal product integrity and customer satisfaction throughout the supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
milk_sourcing    = Transition(label='Milk Sourcing')
milk_testing     = Transition(label='Milk Testing')
culture_prep     = Transition(label='Culture Prep')
curd_formation   = Transition(label='Curd Formation')
whey_removal     = Transition(label='Whey Removal')
pressing_cheese  = Transition(label='Pressing Cheese')
salt_application = Transition(label='Salt Application')
aging_setup      = Transition(label='Aging Setup')
microbial_check  = Transition(label='Microbial Check')
sensory_test     = Transition(label='Sensory Test')
packaging_prep   = Transition(label='Packaging Prep')
sensor_embed     = Transition(label='Sensor Embed')
label_printing   = Transition(label='Label Printing')
storage_monitor  = Transition(label='Storage Monitor')
logistics_plan   = Transition(label='Logistics Plan')
retail_delivery  = Transition(label='Retail Delivery')
customer_feedback= Transition(label='Customer Feedback')

# Build the partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing, milk_testing, culture_prep, curd_formation, whey_removal,
    pressing_cheese, salt_application, aging_setup,
    microbial_check, sensory_test,
    packaging_prep, sensor_embed, label_printing,
    storage_monitor, logistics_plan, retail_delivery, customer_feedback
])

# Sequencing edges
root.order.add_edge(milk_sourcing,  milk_testing)
root.order.add_edge(milk_testing,   culture_prep)
root.order.add_edge(culture_prep,   curd_formation)
root.order.add_edge(curd_formation, whey_removal)
root.order.add_edge(whey_removal,   pressing_cheese)
root.order.add_edge(pressing_cheese,salt_application)
root.order.add_edge(salt_application, aging_setup)

# Quality‐control branches (parallel)
root.order.add_edge(aging_setup,    microbial_check)
root.order.add_edge(aging_setup,    sensory_test)

# Join back to packaging
root.order.add_edge(microbial_check, packaging_prep)
root.order.add_edge(sensory_test,    packaging_prep)

# Packaging and labeling
root.order.add_edge(packaging_prep,  sensor_embed)
root.order.add_edge(sensor_embed,    label_printing)

# Storage monitoring and distribution
root.order.add_edge(label_printing,  storage_monitor)
root.order.add_edge(storage_monitor, logistics_plan)
root.order.add_edge(logistics_plan,  retail_delivery)
root.order.add_edge(retail_delivery, customer_feedback)