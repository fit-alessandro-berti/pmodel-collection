# Generated from: 82c7bb20-1887-47ca-af33-3e9835c913b3.json
# Description: This process details the intricate supply chain of artisanal cheese production from sourcing rare milk varieties through microscopic bacterial culture preparation, carefully timed aging in controlled environments, to bespoke packaging and niche market distribution. Each step requires precision to maintain quality and heritage, including quality sampling, microbial testing, seasonal adjustments, and artisan collaboration, culminating in a high-value product favored by connoisseurs and specialty retailers worldwide.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as labeled transitions
milk_sourcing = Transition(label='Milk Sourcing')
culture_prep = Transition(label='Culture Prep')
curd_cutting = Transition(label='Curd Cutting')
whey_draining = Transition(label='Whey Draining')
mold_inoculation = Transition(label='Mold Inoculation')
pressing_cheese = Transition(label='Pressing Cheese')
salting_phase = Transition(label='Salting Phase')
aging_setup = Transition(label='Aging Setup')
humidity_control = Transition(label='Humidity Control')
flavor_testing = Transition(label='Flavor Testing')
microbial_check = Transition(label='Microbial Check')
batch_tracking = Transition(label='Batch Tracking')
packaging_design = Transition(label='Packaging Design')
market_research = Transition(label='Market Research')
distribution_plan = Transition(label='Distribution Plan')
retail_partnering = Transition(label='Retail Partnering')
customer_feedback = Transition(label='Customer Feedback')

# Construct partial orders reflecting the likely process logic and dependencies

# Cheese production core sequence (ordering steps that need to be sequential):
# Milk Sourcing -> Culture Prep -> Curd Cutting -> Whey Draining -> Mold Inoculation 
# -> Pressing Cheese -> Salting Phase -> Aging Setup
production_core = StrictPartialOrder(nodes=[milk_sourcing, culture_prep, curd_cutting, whey_draining,
                                            mold_inoculation, pressing_cheese, salting_phase, aging_setup])
production_core.order.add_edge(milk_sourcing, culture_prep)
production_core.order.add_edge(culture_prep, curd_cutting)
production_core.order.add_edge(curd_cutting, whey_draining)
production_core.order.add_edge(whey_draining, mold_inoculation)
production_core.order.add_edge(mold_inoculation, pressing_cheese)
production_core.order.add_edge(pressing_cheese, salting_phase)
production_core.order.add_edge(salting_phase, aging_setup)

# Aging setup is followed by parallel quality & environment monitoring and batch tracking
quality_and_tracking = StrictPartialOrder(
    nodes=[humidity_control, flavor_testing, microbial_check, batch_tracking])
# No explicit order between these nodes, they can happen concurrently/independently

# Market & packaging sequence, some ordering implied:
# Packaging Design -> Market Research -> Distribution Plan -> Retail Partnering -> Customer Feedback
market_packaging = StrictPartialOrder(nodes=[packaging_design, market_research, distribution_plan,
                                            retail_partnering, customer_feedback])
market_packaging.order.add_edge(packaging_design, market_research)
market_packaging.order.add_edge(market_research, distribution_plan)
market_packaging.order.add_edge(distribution_plan, retail_partnering)
market_packaging.order.add_edge(retail_partnering, customer_feedback)

# Combine quality/tracking and market_packaging nodes concurrently, but both start after aging_setup
# So create a PO with nodes: aging_setup, quality_and_tracking, market_packaging,
# with edges aging_setup --> quality_and_tracking and aging_setup --> market_packaging

root = StrictPartialOrder(
    nodes=[production_core, quality_and_tracking, market_packaging]
)
root.order.add_edge(production_core, quality_and_tracking)
root.order.add_edge(production_core, market_packaging)