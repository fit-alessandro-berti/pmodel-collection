# Generated from: 43d71985-3c41-41b1-8cda-9680ac9d5899.json
# Description: This process outlines the creation of a bespoke artisanal perfume, starting from raw material sourcing to the final personalized packaging. It involves selecting rare botanical extracts, formulating unique scent blends through iterative testing, aging the mixture to enhance aroma complexity, and conducting sensory evaluations with expert panels. The process also integrates sustainable harvesting methods, custom bottle design, and client feedback incorporation to ensure a distinct and high-quality product tailored to individual preferences. Documentation and quality assurance steps are embedded to maintain consistency and traceability throughout production.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Activities as transitions
Material_Sourcing = Transition(label='Material Sourcing')
Sustainable_Harvest = Transition(label='Sustainable Harvest')
Extract_Distill = Transition(label='Extract Distill')

# Loop for Blend Testing, Formula Adjust, and Scent Aging (iterative formulation testing)
Blend_Testing = Transition(label='Blend Testing')
Formula_Adjust = Transition(label='Formula Adjust')
Scent_Aging = Transition(label='Scent Aging')
loop_body = StrictPartialOrder(nodes=[Formula_Adjust, Scent_Aging])
loop_body.order.add_edge(Formula_Adjust, Scent_Aging)

# Loop: execute Blend Testing, then choose exit or execute (Formula Adjust -> Scent Aging) then Blend Testing again
loop = OperatorPOWL(operator=Operator.LOOP, children=[Blend_Testing, loop_body])

Sensory_Panel = Transition(label='Sensory Panel')
Client_Sampling = Transition(label='Client Sampling')
Feedback_Review = Transition(label='Feedback Review')

Bottle_Design = Transition(label='Bottle Design')
Packaging_Print = Transition(label='Packaging Print')
Batch_Labeling = Transition(label='Batch Labeling')

Quality_Audit = Transition(label='Quality Audit')
Inventory_Check = Transition(label='Inventory Check')
Order_Dispatch = Transition(label='Order Dispatch')

# Partial order for initial sourcing and extraction (Material Sourcing -> Sustainable Harvest -> Extract Distill)
initial_PO = StrictPartialOrder(nodes=[Material_Sourcing, Sustainable_Harvest, Extract_Distill])
initial_PO.order.add_edge(Material_Sourcing, Sustainable_Harvest)
initial_PO.order.add_edge(Sustainable_Harvest, Extract_Distill)

# Partial order for sensory evaluation and feedback incorporation (Sensory Panel -> Client Sampling -> Feedback Review)
feedback_PO = StrictPartialOrder(nodes=[Sensory_Panel, Client_Sampling, Feedback_Review])
feedback_PO.order.add_edge(Sensory_Panel, Client_Sampling)
feedback_PO.order.add_edge(Client_Sampling, Feedback_Review)

# Partial order for packaging design and labeling (Bottle Design -> Packaging Print -> Batch Labeling)
packaging_PO = StrictPartialOrder(nodes=[Bottle_Design, Packaging_Print, Batch_Labeling])
packaging_PO.order.add_edge(Bottle_Design, Packaging_Print)
packaging_PO.order.add_edge(Packaging_Print, Batch_Labeling)

# Partial order for final quality assurance and dispatch (Quality Audit -> Inventory Check -> Order Dispatch)
final_PO = StrictPartialOrder(nodes=[Quality_Audit, Inventory_Check, Order_Dispatch])
final_PO.order.add_edge(Quality_Audit, Inventory_Check)
final_PO.order.add_edge(Inventory_Check, Order_Dispatch)

# Overall partial order connecting phases:
# initial_PO -> loop -> Sensory Panel phase -> packaging_PO -> final_PO

root = StrictPartialOrder(
    nodes=[initial_PO, loop, feedback_PO, packaging_PO, final_PO]
)
root.order.add_edge(initial_PO, loop)
root.order.add_edge(loop, feedback_PO)
root.order.add_edge(feedback_PO, packaging_PO)
root.order.add_edge(packaging_PO, final_PO)