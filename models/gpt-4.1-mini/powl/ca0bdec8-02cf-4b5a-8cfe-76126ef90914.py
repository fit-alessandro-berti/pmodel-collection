# Generated from: ca0bdec8-02cf-4b5a-8cfe-76126ef90914.json
# Description: This process describes the intricate supply chain of artisan cheese production, from sourcing rare regional milk varieties to aging and packaging. The cycle includes quality testing at multiple stages, managing seasonal fluctuations, coordinating with small-scale farmers, monitoring microbial cultures, ensuring compliance with food safety standards, and adapting recipes based on environmental conditions. The process also involves niche marketing strategies, direct-to-consumer distribution, and feedback loops for continuous product refinement. Each activity requires precise timing and expert knowledge to maintain the unique flavor profiles and artisanal quality that differentiate the product in a competitive market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
culture_prep = Transition(label='Culture Prep')
milk_pasteurize = Transition(label='Milk Pasteurize')
curd_cutting = Transition(label='Curd Cutting')
whey_draining = Transition(label='Whey Draining')
molding_cheese = Transition(label='Molding Cheese')
pressing_blocks = Transition(label='Pressing Blocks')
salting_process = Transition(label='Salting Process')
aging_monitoring = Transition(label='Aging Monitoring')
flavor_profiling = Transition(label='Flavor Profiling')
packaging_design = Transition(label='Packaging Design')
compliance_check = Transition(label='Compliance Check')
market_research = Transition(label='Market Research')
direct_shipping = Transition(label='Direct Shipping')
customer_feedback = Transition(label='Customer Feedback')
recipe_adjust = Transition(label='Recipe Adjust')

# Model the main production partial order:
# Milk Sourcing --> Quality Testing --> Culture Prep
# then Milk Pasteurize --> Curd Cutting --> Whey Draining
# then Molding Cheese --> Pressing Blocks --> Salting Process 
# then Aging Monitoring (monitored in parallel with Flavor Profiling)

# After Aging and Flavor Profiling, Packaging Design and Compliance Check proceed.
# Market Research and Direct Shipping happen concurrently after packaging.
# There is a feedback loop: Customer Feedback and Recipe Adjust 
# that loops back to Flavor Profiling and subsequently Aging Monitoring.

# Define the sub partial order for the base production line before aging
base_production = StrictPartialOrder(
    nodes=[
        milk_sourcing, quality_testing, culture_prep,
        milk_pasteurize, curd_cutting, whey_draining,
        molding_cheese, pressing_blocks, salting_process
    ]
)
base_production.order.add_edge(milk_sourcing, quality_testing)
base_production.order.add_edge(quality_testing, culture_prep)

base_production.order.add_edge(culture_prep, milk_pasteurize)
base_production.order.add_edge(milk_pasteurize, curd_cutting)
base_production.order.add_edge(curd_cutting, whey_draining)

base_production.order.add_edge(whey_draining, molding_cheese)
base_production.order.add_edge(molding_cheese, pressing_blocks)
base_production.order.add_edge(pressing_blocks, salting_process)

# Aging Monitoring and Flavor Profiling happen in parallel, after Salting Process
aging_and_flavor = StrictPartialOrder(
    nodes=[aging_monitoring, flavor_profiling],
    # no edges to indicate parallelism
)

# Packaging Design and Compliance Check, sequential after aging and flavor
packaging_and_compliance = StrictPartialOrder(
    nodes=[packaging_design, compliance_check]
)
packaging_and_compliance.order.add_edge(packaging_design, compliance_check)

# Market Research and Direct Shipping happen concurrently after compliance check
market_and_shipping = StrictPartialOrder(
    nodes=[market_research, direct_shipping]
)
# no edges between market_research and direct_shipping (concurrent)

# Feedback and Recipe Adjust form a loop back to flavor profiling and aging monitoring

# Loop body: after customer feedback and recipe adjust, back to flavor and aging monitoring
feedback = StrictPartialOrder(
    nodes=[customer_feedback, recipe_adjust]
)

# Inside the loop: feedback then flavor_profiling then aging_monitoring
loop_body_inner = StrictPartialOrder(
    nodes=[feedback, flavor_profiling, aging_monitoring]
)
# feedback before flavor_profiling
loop_body_inner.order.add_edge(feedback, flavor_profiling)
# flavor_profiling before aging_monitoring
loop_body_inner.order.add_edge(flavor_profiling, aging_monitoring)

# Loop operator: 
# A = the initial steps before the loop (packaging_and_compliance + market_and_shipping)
# B = feedback cycle (loop_body_inner)
# However, aging_monitoring and flavor_profiling are part of the loop body as well,
# so we have to treat them consistently.

# Combine packaging_and_compliance and market_and_shipping into one PO concurrent
post_aging = StrictPartialOrder(
    nodes=[packaging_design, compliance_check, market_research, direct_shipping]
)
post_aging.order.add_edge(packaging_design, compliance_check)
# market_research and direct_shipping concurrent, no edges needed

# Define initial aging and flavor profiling steps that lead into loop:
# We'll treat aging_monitoring and flavor_profiling and the loop cycle with feedback and recipe adjust as a loop

# Loop consists of:
# A: post_aging (packaging, compliance, market research, direct shipping)
# B: feedback + flavor_profiling + aging_monitoring cycle

# However, logically the feedback loop affects product refinement before final packaging.
# So more precise to have the loop be on flavor_profiling -> aging_monitoring -> feedback -> recipe_adjust -> loop again.

# Let's model loop as:
# A: aging_monitoring and flavor_profiling (initial step in loop)
# B: feedback and recipe_adjust

# For that, we define a partial order for nodes A: aging_monitoring and flavor_profiling (parallel)
A = StrictPartialOrder(nodes=[aging_monitoring, flavor_profiling])

# Partial order for nodes B: feedback and recipe_adjust (parallel)
B = StrictPartialOrder(nodes=[customer_feedback, recipe_adjust])

loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Finally, connect all parts:
# base_production --> loop --> packaging_and_compliance and market_and_shipping concurrent

pre_loop = StrictPartialOrder(
    nodes=[
        milk_sourcing, quality_testing, culture_prep,
        milk_pasteurize, curd_cutting, whey_draining,
        molding_cheese, pressing_blocks, salting_process
    ]
)
pre_loop.order.add_edge(milk_sourcing, quality_testing)
pre_loop.order.add_edge(quality_testing, culture_prep)
pre_loop.order.add_edge(culture_prep, milk_pasteurize)
pre_loop.order.add_edge(milk_pasteurize, curd_cutting)
pre_loop.order.add_edge(curd_cutting, whey_draining)
pre_loop.order.add_edge(whey_draining, molding_cheese)
pre_loop.order.add_edge(molding_cheese, pressing_blocks)
pre_loop.order.add_edge(pressing_blocks, salting_process)

# Packaging and compliance and market and shipping combined (no edges between market/shipping and packaging/compliance)
post_loop = StrictPartialOrder(
    nodes=[packaging_design, compliance_check, market_research, direct_shipping]
)
post_loop.order.add_edge(packaging_design, compliance_check)

# root PO with three components: pre_loop --> loop --> post_loop
root = StrictPartialOrder(
    nodes=[pre_loop, loop, post_loop]
)

root.order.add_edge(pre_loop, loop)
root.order.add_edge(loop, post_loop)