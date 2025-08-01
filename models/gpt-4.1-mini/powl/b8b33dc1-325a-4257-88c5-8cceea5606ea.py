# Generated from: b8b33dc1-325a-4257-88c5-8cceea5606ea.json
# Description: This process outlines the complex supply chain for artisan cheese production, starting from sourcing rare milk varieties from remote farms, through specialized fermentation and aging techniques, to quality certification, custom packaging, and niche market distribution. It involves multiple quality checkpoints, seasonal inventory adjustments, and compliance with strict food safety regulations, while coordinating artisanal producers, logistics partners, and boutique retailers to maintain product uniqueness and freshness in a highly competitive gourmet food sector.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Milk_Sourcing = Transition(label='Milk Sourcing')
Farm_Audit = Transition(label='Farm Audit')
Milk_Testing = Transition(label='Milk Testing')
Starter_Prep = Transition(label='Starter Prep')
Coagulation = Transition(label='Coagulation')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Drain = Transition(label='Whey Drain')
Molding_Press = Transition(label='Molding Press')
Salting_Phase = Transition(label='Salting Phase')
Aging_Control = Transition(label='Aging Control')
Quality_Check = Transition(label='Quality Check')
Packaging_Design = Transition(label='Packaging Design')
Label_Printing = Transition(label='Label Printing')
Compliance_Review = Transition(label='Compliance Review')
Order_Scheduling = Transition(label='Order Scheduling')
Logistics_Coord = Transition(label='Logistics Coord')
Retail_Delivery = Transition(label='Retail Delivery')

# Silent transitions for control flow
skip = SilentTransition()

# Quality checkpoints can be modeled as a choice after Aging Control:
# either Quality Check passes or requires Compliance Review (recheck)
quality_check_branch = OperatorPOWL(
    operator=Operator.XOR,
    children=[Quality_Check, Compliance_Review]
)

# Seasonal inventory adjustments and compliance modeled as a loop around Compliance Review and Quality Check
# Loop: after Quality Check or Compliance Review, either exit or do Compliance Review then Quality Check again
quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[Quality_Check, Compliance_Review])

# Because Compliance Review alone doesn't advance the process, let's refine the loop:
# Loop semantics: (Quality_Check, Compliance_Review)
# But Compliance_Review must be inside the loop body, Quality_Check is "A", Compliance_Review is "B"
# So loop = *(Quality_Check, Compliance_Review)
# But Quality_Check is "A"
quality_compliance_loop = OperatorPOWL(operator=Operator.LOOP, children=[Quality_Check, Compliance_Review])

# Packaging sequence: Packaging Design -> Label Printing
packaging_po = StrictPartialOrder(nodes=[Packaging_Design, Label_Printing])
packaging_po.order.add_edge(Packaging_Design, Label_Printing)

# Distribution sequence: Order Scheduling -> Logistics Coord -> Retail Delivery
distribution_po = StrictPartialOrder(nodes=[Order_Scheduling, Logistics_Coord, Retail_Delivery])
distribution_po.order.add_edge(Order_Scheduling, Logistics_Coord)
distribution_po.order.add_edge(Logistics_Coord, Retail_Delivery)

# Initial milk processing partial order:
# Milk Sourcing -> Farm Audit and Milk Testing (concurrent)
init_quality_po = StrictPartialOrder(
    nodes=[Milk_Sourcing, Farm_Audit, Milk_Testing]
)
init_quality_po.order.add_edge(Milk_Sourcing, Farm_Audit)
init_quality_po.order.add_edge(Milk_Sourcing, Milk_Testing)

# Starter Prep after both Farm Audit and Milk Testing
starter_po = StrictPartialOrder(
    nodes=[init_quality_po, Starter_Prep]
)
starter_po.order.add_edge(init_quality_po, Starter_Prep)

# Cheese making steps in partial order:
# Coagulation -> Curd Cutting -> Whey Drain -> Molding Press -> Salting Phase
# Then Aging Control
cheese_making_po = StrictPartialOrder(
    nodes=[Coagulation, Curd_Cutting, Whey_Drain, Molding_Press, Salting_Phase, Aging_Control]
)
cheese_making_po.order.add_edge(Coagulation, Curd_Cutting)
cheese_making_po.order.add_edge(Curd_Cutting, Whey_Drain)
cheese_making_po.order.add_edge(Whey_Drain, Molding_Press)
cheese_making_po.order.add_edge(Molding_Press, Salting_Phase)
cheese_making_po.order.add_edge(Salting_Phase, Aging_Control)

# Connect Starter Prep to Coagulation (start cheese making once starter prep done)
starter_cheese_po = StrictPartialOrder(
    nodes=[starter_po, cheese_making_po]
)
starter_cheese_po.order.add_edge(starter_po, cheese_making_po)

# After Aging Control comes the quality compliance loop
quality_stage = StrictPartialOrder(
    nodes=[starter_cheese_po, quality_compliance_loop]
)
quality_stage.order.add_edge(starter_cheese_po, quality_compliance_loop)

# After quality passed, proceed to packaging (packaging_po)
# and distribution (distribution_po) concurrency: packaging and distribution can be parallel

pack_dist_po = StrictPartialOrder(
    nodes=[packaging_po, distribution_po]
)
# no order edges between packaging and distribution to support concurrency

# Final root PO combining quality stage and packaging+distribution
root = StrictPartialOrder(
    nodes=[quality_stage, pack_dist_po]
)
root.order.add_edge(quality_stage, pack_dist_po)