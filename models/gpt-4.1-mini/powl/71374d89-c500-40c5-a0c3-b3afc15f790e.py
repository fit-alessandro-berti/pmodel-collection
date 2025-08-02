# Generated from: 71374d89-c500-40c5-a0c3-b3afc15f790e.json
# Description: This process involves the intricate steps of crafting bespoke artisan perfumes tailored to individual client preferences. Starting from scent profiling and raw material sourcing, the process continues with small-batch formulation, iterative scent testing, and refinement cycles. It includes blending natural and synthetic essences, aging mixtures for maturation, and quality evaluation through expert panels. Packaging design aligns with brand philosophy, and limited edition numbering ensures exclusivity. Final steps include regulatory compliance checks, marketing collateral development, and personalized client delivery with feedback collection for continuous improvement. The process requires coordination across creative, technical, and logistical teams to ensure a unique olfactory experience for each customer.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Scent_Profiling = Transition(label='Scent Profiling')
Material_Sourcing = Transition(label='Material Sourcing')
Batch_Formulation = Transition(label='Batch Formulation')
Scent_Testing = Transition(label='Scent Testing')
Blend_Refinement = Transition(label='Blend Refinement')
Essence_Aging = Transition(label='Essence Aging')
Quality_Evaluation = Transition(label='Quality Evaluation')
Packaging_Design = Transition(label='Packaging Design')
Edition_Numbering = Transition(label='Edition Numbering')
Compliance_Check = Transition(label='Compliance Check')
Marketing_Prep = Transition(label='Marketing Prep')
Client_Delivery = Transition(label='Client Delivery')
Feedback_Collection = Transition(label='Feedback Collection')
Inventory_Audit = Transition(label='Inventory Audit')
Supplier_Negotiation = Transition(label='Supplier Negotiation')
Creative_Review = Transition(label='Creative Review')
Logistics_Planning = Transition(label='Logistics Planning')

# Creative Team partial order: Inventory Audit -> Supplier Negotiation -> Creative Review
creative_team = StrictPartialOrder(nodes=[Inventory_Audit, Supplier_Negotiation, Creative_Review])
creative_team.order.add_edge(Inventory_Audit, Supplier_Negotiation)
creative_team.order.add_edge(Supplier_Negotiation, Creative_Review)

# Technical Team partial order: 
# Batch Formulation -> Loop(Scent Testing, Blend Refinement) -> Essence Aging -> Quality Evaluation
scent_testing_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Scent_Testing, Blend_Refinement]
)
technical_team = StrictPartialOrder(nodes=[Batch_Formulation, scent_testing_loop, Essence_Aging, Quality_Evaluation])
technical_team.order.add_edge(Batch_Formulation, scent_testing_loop)
technical_team.order.add_edge(scent_testing_loop, Essence_Aging)
technical_team.order.add_edge(Essence_Aging, Quality_Evaluation)

# Logistical Team partial order:
# Packaging Design -> Edition Numbering -> Compliance Check -> Marketing Prep -> Client Delivery -> Feedback Collection -> Logistics Planning
logistical_team = StrictPartialOrder(nodes=[
    Packaging_Design, Edition_Numbering, Compliance_Check,
    Marketing_Prep, Client_Delivery, Feedback_Collection, Logistics_Planning
])
logistical_team.order.add_edge(Packaging_Design, Edition_Numbering)
logistical_team.order.add_edge(Edition_Numbering, Compliance_Check)
logistical_team.order.add_edge(Compliance_Check, Marketing_Prep)
logistical_team.order.add_edge(Marketing_Prep, Client_Delivery)
logistical_team.order.add_edge(Client_Delivery, Feedback_Collection)
logistical_team.order.add_edge(Feedback_Collection, Logistics_Planning)

# Initial step partial order: Scent Profiling -> Material Sourcing
initial = StrictPartialOrder(nodes=[Scent_Profiling, Material_Sourcing])
initial.order.add_edge(Scent_Profiling, Material_Sourcing)

# Combine initial with creative team and technical team and logistical team
# Material Sourcing must precede both creative and technical teams (as sourcing enables formulation and audits)
# We assume creative and logistical teams run concurrently with technical team after sourcing.

root = StrictPartialOrder(
    nodes=[initial, creative_team, technical_team, logistical_team]
)
# Order:
# initial --> creative_team and technical_team
root.order.add_edge(initial, creative_team)
root.order.add_edge(initial, technical_team)
# quality evaluation (end of technical team) must precede packaging design (start of logistical_team)
# enforcing technical to logistical sequence
root.order.add_edge(technical_team, logistical_team)