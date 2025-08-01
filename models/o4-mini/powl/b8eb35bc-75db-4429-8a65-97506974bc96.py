# Generated from: b8eb35bc-75db-4429-8a65-97506974bc96.json
# Description: This process manages the end-to-end supply chain for an urban beekeeping business that sources local raw honey, produces artisanal bee products, and distributes them through niche urban markets. It involves site scouting for rooftop hives, hive installation, bee health monitoring, honey extraction, product formulation including beeswax candles and propolis tinctures, quality testing, branding, and eco-friendly packaging. The process also integrates community education workshops, urban pollination tracking, and sustainability reporting to ensure environmental compliance and social impact. Complexities arise due to variability in urban flora, seasonal bee activity, and tight regulatory constraints on food and agricultural products within city limits.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic transitions
site_scouting       = Transition(label='Site Scouting')
hive_setup          = Transition(label='Hive Setup')
bee_monitoring      = Transition(label='Bee Monitoring')
pest_control        = Transition(label='Pest Control')
honey_harvest       = Transition(label='Honey Harvest')
wax_processing      = Transition(label='Wax Processing')
product_blending    = Transition(label='Product Blending')
quality_testing     = Transition(label='Quality Testing')
regulatory_review   = Transition(label='Regulatory Review')
sustainability_audit= Transition(label='Sustainability Audit')
brand_design        = Transition(label='Brand Design')
eco_packaging       = Transition(label='Eco Packaging')
market_analysis     = Transition(label='Market Analysis')
pollination_track   = Transition(label='Pollination Track')
community_workshop  = Transition(label='Community Workshop')
order_fulfillment   = Transition(label='Order Fulfillment')
customer_feedback   = Transition(label='Customer Feedback')

# Loop: monitoring followed by optional pest control then monitoring again
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[bee_monitoring, pest_control]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_scouting,
    hive_setup,
    monitor_loop,
    honey_harvest,
    wax_processing,
    product_blending,
    quality_testing,
    regulatory_review,
    sustainability_audit,
    brand_design,
    eco_packaging,
    market_analysis,
    pollination_track,
    community_workshop,
    order_fulfillment,
    customer_feedback
])

# Add sequencing edges
root.order.add_edge(site_scouting, hive_setup)
root.order.add_edge(hive_setup, monitor_loop)
root.order.add_edge(monitor_loop, honey_harvest)
root.order.add_edge(honey_harvest, wax_processing)
root.order.add_edge(wax_processing, product_blending)

# After blending: quality testing and parallel tasks
root.order.add_edge(product_blending, quality_testing)
root.order.add_edge(product_blending, brand_design)
root.order.add_edge(product_blending, eco_packaging)
root.order.add_edge(product_blending, market_analysis)
root.order.add_edge(product_blending, pollination_track)
root.order.add_edge(product_blending, community_workshop)

# Quality → regulatory → audit
root.order.add_edge(quality_testing, regulatory_review)
root.order.add_edge(regulatory_review, sustainability_audit)

# All branches must complete before order fulfillment
for predecessor in [
    sustainability_audit,
    brand_design,
    eco_packaging,
    market_analysis,
    pollination_track,
    community_workshop
]:
    root.order.add_edge(predecessor, order_fulfillment)

# Final feedback
root.order.add_edge(order_fulfillment, customer_feedback)