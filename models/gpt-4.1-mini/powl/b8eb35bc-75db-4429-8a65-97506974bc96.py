# Generated from: b8eb35bc-75db-4429-8a65-97506974bc96.json
# Description: This process manages the end-to-end supply chain for an urban beekeeping business that sources local raw honey, produces artisanal bee products, and distributes them through niche urban markets. It involves site scouting for rooftop hives, hive installation, bee health monitoring, honey extraction, product formulation including beeswax candles and propolis tinctures, quality testing, branding, and eco-friendly packaging. The process also integrates community education workshops, urban pollination tracking, and sustainability reporting to ensure environmental compliance and social impact. Complexities arise due to variability in urban flora, seasonal bee activity, and tight regulatory constraints on food and agricultural products within city limits.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
site_scouting = Transition(label='Site Scouting')
hive_setup = Transition(label='Hive Setup')
bee_monitoring = Transition(label='Bee Monitoring')
pest_control = Transition(label='Pest Control')
honey_harvest = Transition(label='Honey Harvest')
wax_processing = Transition(label='Wax Processing')
product_blending = Transition(label='Product Blending')
quality_testing = Transition(label='Quality Testing')
brand_design = Transition(label='Brand Design')
eco_packaging = Transition(label='Eco Packaging')
market_analysis = Transition(label='Market Analysis')
community_workshop = Transition(label='Community Workshop')
pollination_track = Transition(label='Pollination Track')
sustainability_audit = Transition(label='Sustainability Audit')
regulatory_review = Transition(label='Regulatory Review')
order_fulfillment = Transition(label='Order Fulfillment')
customer_feedback = Transition(label='Customer Feedback')

# Silent transition for internal control or loop exits
skip = SilentTransition()

# Loop for Bee Monitoring with Pest Control repeating until bee health stable (modeled as a loop)
# LOOP(bee_monitoring, pest_control)
monitoring_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[bee_monitoring, pest_control]
)

# Product formulation partial order: wax_processing and honey_harvest can happen concurrently, then product_blending
product_partial = StrictPartialOrder(
    nodes=[honey_harvest, wax_processing, product_blending]
)
product_partial.order.add_edge(honey_harvest, product_blending)
product_partial.order.add_edge(wax_processing, product_blending)

# Branding and packaging after product formulation
brand_and_pack = StrictPartialOrder(
    nodes=[brand_design, eco_packaging]
)
# They can be concurrent, no ordering

# Market analysis, community workshop, pollination tracking, sustainability audit, regulatory review happen after hive setup and monitoring loop
# Partial order for community and compliance tasks
compliance_tasks = StrictPartialOrder(
    nodes=[market_analysis, community_workshop, pollination_track, sustainability_audit, regulatory_review]
)
# No order between them, all concurrent

# Order fulfillment and customer feedback after quality testing and brand/packaging
fulfillment_flow = StrictPartialOrder(
    nodes=[order_fulfillment, customer_feedback]
)
fulfillment_flow.order.add_edge(order_fulfillment, customer_feedback)

# Quality testing after product blending
# Order: product_partial --> quality_testing
# quality_testing --> brand_and_pack

# Build main partial order of core activities before community/compliance and fulfillment flows
core_activities = StrictPartialOrder(
    nodes=[site_scouting, hive_setup, monitoring_loop, product_partial, quality_testing, brand_and_pack]
)
core_activities.order.add_edge(site_scouting, hive_setup)
core_activities.order.add_edge(hive_setup, monitoring_loop)
core_activities.order.add_edge(monitoring_loop, product_partial)
core_activities.order.add_edge(product_partial, quality_testing)
core_activities.order.add_edge(quality_testing, brand_and_pack)

# final main partial order combining core activities, compliance tasks and fulfillment flow
root = StrictPartialOrder(
    nodes=[core_activities, compliance_tasks, fulfillment_flow]
)
root.order.add_edge(core_activities, compliance_tasks)
root.order.add_edge(core_activities, fulfillment_flow)
root.order.add_edge(compliance_tasks, fulfillment_flow)