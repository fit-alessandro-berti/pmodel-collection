# Generated from: ca0bdec8-02cf-4b5a-8cfe-76126ef90914.json
# Description: This process describes the intricate supply chain of artisan cheese production, from sourcing rare regional milk varieties to aging and packaging. The cycle includes quality testing at multiple stages, managing seasonal fluctuations, coordinating with small-scale farmers, monitoring microbial cultures, ensuring compliance with food safety standards, and adapting recipes based on environmental conditions. The process also involves niche marketing strategies, direct-to-consumer distribution, and feedback loops for continuous product refinement. Each activity requires precise timing and expert knowledge to maintain the unique flavor profiles and artisanal quality that differentiate the product in a competitive market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
milk_sourcing      = Transition(label='Milk Sourcing')
market_research    = Transition(label='Market Research')
quality_testing    = Transition(label='Quality Testing')
culture_prep       = Transition(label='Culture Prep')
milk_pasteurize    = Transition(label='Milk Pasteurize')
curd_cutting       = Transition(label='Curd Cutting')
whey_draining      = Transition(label='Whey Draining')
molding_cheese     = Transition(label='Molding Cheese')
pressing_blocks    = Transition(label='Pressing Blocks')
salting_process    = Transition(label='Salting Process')
aging_monitoring   = Transition(label='Aging Monitoring')
flavor_profiling   = Transition(label='Flavor Profiling')
compliance_check   = Transition(label='Compliance Check')
packaging_design   = Transition(label='Packaging Design')
direct_shipping    = Transition(label='Direct Shipping')
customer_feedback  = Transition(label='Customer Feedback')
recipe_adjust      = Transition(label='Recipe Adjust')

# Silent transition for optional/choice branches
skip = SilentTransition()

# Control‐flow operators
# 1) Optional market research step
market_xor    = OperatorPOWL(operator=Operator.XOR,  children=[market_research, skip])
# 2) Quality testing loop (test → optionally adjust recipe → re‐test → …)
quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_testing, recipe_adjust])
# 3) Compliance check loop (check → if fail adjust recipe → re‐check → …)
compliance_loop = OperatorPOWL(operator=Operator.LOOP, children=[compliance_check, recipe_adjust])
# 4) Customer feedback loop (feedback → if needed adjust recipe → re‐feedback → …)
feedback_loop  = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback, recipe_adjust])

# Build the partial order
root = StrictPartialOrder(
    nodes=[
        market_xor,
        milk_sourcing,
        quality_loop,
        culture_prep,
        milk_pasteurize,
        curd_cutting,
        whey_draining,
        molding_cheese,
        pressing_blocks,
        salting_process,
        aging_monitoring,
        flavor_profiling,
        compliance_loop,
        packaging_design,
        direct_shipping,
        feedback_loop
    ]
)

# Define the control‐flow dependencies
root.order.add_edge(market_xor,    milk_sourcing)
root.order.add_edge(milk_sourcing, quality_loop)
root.order.add_edge(quality_loop,  culture_prep)
root.order.add_edge(culture_prep,  milk_pasteurize)
root.order.add_edge(milk_pasteurize, curd_cutting)
root.order.add_edge(curd_cutting,    whey_draining)
root.order.add_edge(whey_draining,   molding_cheese)
root.order.add_edge(molding_cheese,  pressing_blocks)
root.order.add_edge(pressing_blocks, salting_process)
root.order.add_edge(salting_process, aging_monitoring)
root.order.add_edge(aging_monitoring, flavor_profiling)
root.order.add_edge(flavor_profiling, compliance_loop)
root.order.add_edge(compliance_loop,  packaging_design)
root.order.add_edge(packaging_design, direct_shipping)
root.order.add_edge(direct_shipping,  feedback_loop)