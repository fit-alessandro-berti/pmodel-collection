# Generated from: 995c2cbb-f830-4d59-a07a-db1b594d0e11.json
# Description: This process outlines the intricate journey of artisan cheese from small-scale farms to niche gourmet retailers. It involves unique steps such as microbial culture selection, controlled aging environments, and sensory quality evaluation by expert tasters. The process requires coordination between farmers, microbiologists, transporters, and retailers to maintain product integrity and flavor consistency. Special attention is given to seasonal variations in milk quality and the impact on fermentation. Additionally, packaging includes biodegradable materials to align with sustainability goals. Real-time tracking ensures freshness while bespoke marketing campaigns educate consumers on cheese provenance and pairing suggestions. This atypical supply chain balances traditional craftsmanship with modern logistics and consumer engagement strategies.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
milk_sourcing = Transition(label='Milk Sourcing')
culture_prep = Transition(label='Culture Prep')
coagulation = Transition(label='Coagulation')
curd_cutting = Transition(label='Curd Cutting')
whey_draining = Transition(label='Whey Draining')
molding_press = Transition(label='Molding Press')
initial_salting = Transition(label='Initial Salting')
controlled_aging = Transition(label='Controlled Aging')
microbial_testing = Transition(label='Microbial Testing')
sensory_panel = Transition(label='Sensory Panel')
seasonal_adjust = Transition(label='Seasonal Adjust')
eco_packaging = Transition(label='Eco Packaging')
cold_transport = Transition(label='Cold Transport')
retail_setup = Transition(label='Retail Setup')
consumer_edu = Transition(label='Consumer Edu')
feedback_loop = Transition(label='Feedback Loop')
inventory_audit = Transition(label='Inventory Audit')

# The feedback loop involves returning from feedback_loop to cultural prep to adjust process
# or exit the loop; model as LOOP with body = culture_prep -> ... -> inventory_audit, redo from culture_prep or exit

# Partial order inside the loop body: from Culture Prep to inventory audit end
loop_body_nodes = [
    culture_prep,
    coagulation,
    curd_cutting,
    whey_draining,
    molding_press,
    initial_salting,
    controlled_aging,
    microbial_testing,
    sensory_panel,
    seasonal_adjust,
    eco_packaging,
    cold_transport,
    retail_setup,
    consumer_edu,
    feedback_loop,
    inventory_audit
]

loop_body = StrictPartialOrder(nodes=loop_body_nodes)
loop_body.order.add_edge(culture_prep, coagulation)
loop_body.order.add_edge(coagulation, curd_cutting)
loop_body.order.add_edge(curd_cutting, whey_draining)
loop_body.order.add_edge(whey_draining, molding_press)
loop_body.order.add_edge(molding_press, initial_salting)
loop_body.order.add_edge(initial_salting, controlled_aging)
loop_body.order.add_edge(controlled_aging, microbial_testing)
loop_body.order.add_edge(microbial_testing, sensory_panel)
loop_body.order.add_edge(sensory_panel, seasonal_adjust)
loop_body.order.add_edge(seasonal_adjust, eco_packaging)
loop_body.order.add_edge(eco_packaging, cold_transport)
loop_body.order.add_edge(cold_transport, retail_setup)
loop_body.order.add_edge(retail_setup, consumer_edu)
loop_body.order.add_edge(consumer_edu, feedback_loop)
loop_body.order.add_edge(feedback_loop, inventory_audit)

# LOOP operator: (culture_prep ...) body with loop from feedback_loop back to culture_prep, or exit
# The LOOP operator requires two children: A (initial) and B (loop body condition)

# Here, we set A as culture prep (start of loop body), B as the rest nodes excluding culture prep
# However, LOOP semantics are: execute A, then choose exit or do B then A again
# So to keep the sequence, let A = culture_prep
# B = StrictPartialOrder(nodes=loop_body_nodes excluding culture_prep)
loop_B_nodes = [
    coagulation,
    curd_cutting,
    whey_draining,
    molding_press,
    initial_salting,
    controlled_aging,
    microbial_testing,
    sensory_panel,
    seasonal_adjust,
    eco_packaging,
    cold_transport,
    retail_setup,
    consumer_edu,
    feedback_loop,
    inventory_audit
]
loop_B = StrictPartialOrder(nodes=loop_B_nodes)
loop_B.order.add_edge(coagulation, curd_cutting)
loop_B.order.add_edge(curd_cutting, whey_draining)
loop_B.order.add_edge(whey_draining, molding_press)
loop_B.order.add_edge(molding_press, initial_salting)
loop_B.order.add_edge(initial_salting, controlled_aging)
loop_B.order.add_edge(controlled_aging, microbial_testing)
loop_B.order.add_edge(microbial_testing, sensory_panel)
loop_B.order.add_edge(sensory_panel, seasonal_adjust)
loop_B.order.add_edge(seasonal_adjust, eco_packaging)
loop_B.order.add_edge(eco_packaging, cold_transport)
loop_B.order.add_edge(cold_transport, retail_setup)
loop_B.order.add_edge(retail_setup, consumer_edu)
loop_B.order.add_edge(consumer_edu, feedback_loop)
loop_B.order.add_edge(feedback_loop, inventory_audit)

loop = OperatorPOWL(operator=Operator.LOOP, children=[culture_prep, loop_B])

# Milk sourcing happens before the loop starts
# Build the entire partial order from milk_sourcing to loop start

# After loop ends (inventory_audit), process ends

root = StrictPartialOrder(nodes=[milk_sourcing, loop])
root.order.add_edge(milk_sourcing, loop)