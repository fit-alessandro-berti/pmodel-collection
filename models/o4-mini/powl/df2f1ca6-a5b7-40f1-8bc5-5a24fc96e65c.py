# Generated from: df2f1ca6-a5b7-40f1-8bc5-5a24fc96e65c.json
# Description: This process manages the end-to-end supply chain for handcrafted artisan goods, integrating unique sourcing, bespoke production, and customized distribution. It involves identifying rare raw materials, coordinating with local artisans, ensuring quality through multi-stage inspections, managing limited batch productions, and tailoring delivery schedules to niche markets. The process also incorporates dynamic demand forecasting based on cultural trends and seasonal events, alongside adaptive pricing models that reflect scarcity and craftsmanship value, ensuring sustainable artisan livelihoods while maintaining exclusivity and customer satisfaction.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
material_sourcing   = Transition(label='Material Sourcing')
artisan_vetting     = Transition(label='Artisan Vetting')
craft_coordination  = Transition(label='Craft Coordination')
sample_review       = Transition(label='Sample Review')
design_finalize     = Transition(label='Design Finalize')
batch_scheduling    = Transition(label='Batch Scheduling')
quality_check       = Transition(label='Quality Check')
custom_packaging    = Transition(label='Custom Packaging')
shipment_plan       = Transition(label='Shipment Plan')
order_processing    = Transition(label='Order Processing')
market_analysis     = Transition(label='Market Analysis')
trend_monitor       = Transition(label='Trend Monitor')
demand_forecast     = Transition(label='Demand Forecast')
price_adjust        = Transition(label='Price Adjust')
inventory_sync      = Transition(label='Inventory Sync')
feedback_loop       = Transition(label='Feedback Loop')

# Production sub‐workflow: design → batch → quality
sub_production = StrictPartialOrder(nodes=[design_finalize, batch_scheduling, quality_check])
sub_production.order.add_edge(design_finalize, batch_scheduling)
sub_production.order.add_edge(batch_scheduling, quality_check)

# Loop for re‐work on sample review if quality check fails
loop_production = OperatorPOWL(
    operator=Operator.LOOP,
    children=[sub_production, sample_review]
)

# Forecasting sequence: market analysis → trend monitor → demand forecast → price adjust → inventory sync
forecast_seq = StrictPartialOrder(nodes=[
    market_analysis,
    trend_monitor,
    demand_forecast,
    price_adjust,
    inventory_sync
])
forecast_seq.order.add_edge(market_analysis, trend_monitor)
forecast_seq.order.add_edge(trend_monitor, demand_forecast)
forecast_seq.order.add_edge(demand_forecast, price_adjust)
forecast_seq.order.add_edge(price_adjust, inventory_sync)

# Loop forecasting with feedback
loop_forecast = OperatorPOWL(
    operator=Operator.LOOP,
    children=[forecast_seq, feedback_loop]
)

# Main workflow partial order
root = StrictPartialOrder(nodes=[
    material_sourcing,
    artisan_vetting,
    craft_coordination,
    sample_review,
    loop_production,
    custom_packaging,
    shipment_plan,
    order_processing,
    loop_forecast
])
root.order.add_edge(material_sourcing, artisan_vetting)
root.order.add_edge(artisan_vetting, craft_coordination)
root.order.add_edge(craft_coordination, sample_review)
root.order.add_edge(sample_review, loop_production)
root.order.add_edge(loop_production, custom_packaging)
root.order.add_edge(custom_packaging, shipment_plan)
root.order.add_edge(shipment_plan, order_processing)
root.order.add_edge(order_processing, loop_forecast)