# Generated from: 69089497-e31a-400c-9c4d-2c83876646f1.json
# Description: This process involves the intricate steps required to produce, age, and distribute artisan cheese from small-scale farms to niche markets. It begins with selecting rare milk varieties, followed by specialized fermentation and aging techniques under strict environmental controls. Quality control includes microbial analysis and texture testing. Packaging involves eco-friendly materials and personalized labeling. Finally, distribution leverages boutique logistics partners to maintain freshness and unique branding, targeting gourmet retailers and exclusive restaurants. This atypical supply chain emphasizes craftsmanship, traceability, and sustainability throughout every stage of production and delivery, ensuring the final product meets artisanal standards and consumer expectations for rare cheeses.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
milk_selection = Transition(label='Milk Selection')
milk_testing = Transition(label='Milk Testing')
starter_culture = Transition(label='Starter Culture')
curd_formation = Transition(label='Curd Formation')
whey_separation = Transition(label='Whey Separation')
molding_cheese = Transition(label='Molding Cheese')
pressing_cheese = Transition(label='Pressing Cheese')
salting_process = Transition(label='Salting Process')
aging_control = Transition(label='Aging Control')
humidity_check = Transition(label='Humidity Check')
microbial_test = Transition(label='Microbial Test')
texture_check = Transition(label='Texture Check')
packaging_prep = Transition(label='Packaging Prep')
label_printing = Transition(label='Label Printing')
eco_packing = Transition(label='Eco Packing')
cold_storage = Transition(label='Cold Storage')
boutique_shipping = Transition(label='Boutique Shipping')

# Partial Order 1: Milk Selection --> Milk Testing
po_milk = StrictPartialOrder(nodes=[milk_selection, milk_testing])
po_milk.order.add_edge(milk_selection, milk_testing)

# Partial Order 2: Starter Culture --> Curd Formation --> Whey Separation
po_curd = StrictPartialOrder(nodes=[starter_culture, curd_formation, whey_separation])
po_curd.order.add_edge(starter_culture, curd_formation)
po_curd.order.add_edge(curd_formation, whey_separation)

# Partial Order 3: Molding Cheese --> Pressing Cheese --> Salting Process
po_molding = StrictPartialOrder(nodes=[molding_cheese, pressing_cheese, salting_process])
po_molding.order.add_edge(molding_cheese, pressing_cheese)
po_molding.order.add_edge(pressing_cheese, salting_process)

# Partial Order 4: Aging Control & Humidity Check (concurrent)
po_aging = StrictPartialOrder(nodes=[aging_control, humidity_check])
# no order edges, concurrent

# Partial Order 5: Microbial Test & Texture Check (concurrent)
po_quality = StrictPartialOrder(nodes=[microbial_test, texture_check])
# no order edges, concurrent

# Packaging steps partial order: Packaging Prep --> Label Printing --> Eco Packing
po_packaging = StrictPartialOrder(nodes=[packaging_prep, label_printing, eco_packing])
po_packaging.order.add_edge(packaging_prep, label_printing)
po_packaging.order.add_edge(label_printing, eco_packing)

# Partial Order 6: Cold Storage --> Boutique Shipping
po_distribution = StrictPartialOrder(nodes=[cold_storage, boutique_shipping])
po_distribution.order.add_edge(cold_storage, boutique_shipping)

# Compose the full process partial order:
# High level order according to description:
# Milk Selection --> Milk Testing --> Starter Culture --> Curd Formation --> Whey Separation --> Molding Cheese --> Pressing Cheese --> Salting Process -->
# Aging and checks (Aging Control, Humidity Check), Quality Control (Microbial Test, Texture Check),
# then Packaging Prep process --> Packaging --> Distribution

# To represent Aging Control & Humidity Check and Microbial Test & Texture Check as concurrent sets after Salting Process,
# we connect Salting Process to both Aging Control and Microbial Test (start nodes of these concurrent groups),
# then after them we proceed to Packaging Prep

# So create a top level strict partial order including all these nodes and sub-pos

# First collect all nodes for the final PO:
# We'll use all nodes plus combine partial orders via edges

nodes_all = [
    milk_selection, milk_testing,
    starter_culture, curd_formation, whey_separation,
    molding_cheese, pressing_cheese, salting_process,
    aging_control, humidity_check,
    microbial_test, texture_check,
    packaging_prep, label_printing, eco_packing,
    cold_storage, boutique_shipping
]

root = StrictPartialOrder(nodes=nodes_all)

# Add all internal partial orders' edges:

# Milk selection -> Milk testing
root.order.add_edge(milk_selection, milk_testing)

# Milk testing -> Starter culture
root.order.add_edge(milk_testing, starter_culture)

# Starter culture -> Curd formation -> Whey separation
root.order.add_edge(starter_culture, curd_formation)
root.order.add_edge(curd_formation, whey_separation)

# Whey separation -> Molding cheese
root.order.add_edge(whey_separation, molding_cheese)

# Molding cheese -> Pressing cheese -> Salting process
root.order.add_edge(molding_cheese, pressing_cheese)
root.order.add_edge(pressing_cheese, salting_process)

# Salting process -> Aging control & Humidity check (concurrent)
root.order.add_edge(salting_process, aging_control)
root.order.add_edge(salting_process, humidity_check)

# Salting process -> Microbial test & Texture check (concurrent)
root.order.add_edge(salting_process, microbial_test)
root.order.add_edge(salting_process, texture_check)

# After Aging control & Humidity check and Microbial test & Texture check, proceed to Packaging Prep
root.order.add_edge(aging_control, packaging_prep)
root.order.add_edge(humidity_check, packaging_prep)
root.order.add_edge(microbial_test, packaging_prep)
root.order.add_edge(texture_check, packaging_prep)

# Packaging Prep -> Label printing -> Eco packing
root.order.add_edge(packaging_prep, label_printing)
root.order.add_edge(label_printing, eco_packing)

# Eco packing -> Cold storage -> Boutique shipping
root.order.add_edge(eco_packing, cold_storage)
root.order.add_edge(cold_storage, boutique_shipping)