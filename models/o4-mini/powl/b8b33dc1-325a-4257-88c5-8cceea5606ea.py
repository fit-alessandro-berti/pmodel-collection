# Generated from: b8b33dc1-325a-4257-88c5-8cceea5606ea.json
# Description: This process outlines the complex supply chain for artisan cheese production, starting from sourcing rare milk varieties from remote farms, through specialized fermentation and aging techniques, to quality certification, custom packaging, and niche market distribution. It involves multiple quality checkpoints, seasonal inventory adjustments, and compliance with strict food safety regulations, while coordinating artisanal producers, logistics partners, and boutique retailers to maintain product uniqueness and freshness in a highly competitive gourmet food sector.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
milk_sourcing   = Transition(label="Milk Sourcing")
farm_audit      = Transition(label="Farm Audit")
milk_testing    = Transition(label="Milk Testing")
starter_prep    = Transition(label="Starter Prep")
coagulation     = Transition(label="Coagulation")
curd_cutting    = Transition(label="Curd Cutting")
whey_drain      = Transition(label="Whey Drain")
molding_press   = Transition(label="Molding Press")
salting_phase   = Transition(label="Salting Phase")
aging_control   = Transition(label="Aging Control")
quality_check   = Transition(label="Quality Check")
compliance_review = Transition(label="Compliance Review")
packaging_design  = Transition(label="Packaging Design")
label_printing    = Transition(label="Label Printing")
order_scheduling  = Transition(label="Order Scheduling")
logistics_coord   = Transition(label="Logistics Coord")
retail_delivery   = Transition(label="Retail Delivery")

# Loop for repeated aging & quality checkpoints
#   Execute 'Aging Control' once, then loop: do 'Quality Check' then 'Aging Control' again, until exit
aging_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[aging_control, quality_check]
)

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    farm_audit,
    milk_testing,
    starter_prep,
    coagulation,
    curd_cutting,
    whey_drain,
    molding_press,
    salting_phase,
    aging_loop,
    compliance_review,
    packaging_design,
    label_printing,
    order_scheduling,
    logistics_coord,
    retail_delivery
])

# Define the control‐flow dependencies
root.order.add_edge(milk_sourcing,   farm_audit)
root.order.add_edge(farm_audit,      milk_testing)
root.order.add_edge(milk_testing,    starter_prep)
root.order.add_edge(starter_prep,    coagulation)
root.order.add_edge(coagulation,     curd_cutting)
root.order.add_edge(curd_cutting,    whey_drain)
root.order.add_edge(whey_drain,      molding_press)
root.order.add_edge(molding_press,   salting_phase)
root.order.add_edge(salting_phase,   aging_loop)
root.order.add_edge(aging_loop,      compliance_review)
root.order.add_edge(compliance_review, packaging_design)
root.order.add_edge(packaging_design,   label_printing)
root.order.add_edge(label_printing,     order_scheduling)
root.order.add_edge(order_scheduling,   logistics_coord)
root.order.add_edge(logistics_coord,    retail_delivery)