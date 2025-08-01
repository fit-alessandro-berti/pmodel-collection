# Generated from: df2f1ca6-a5b7-40f1-8bc5-5a24fc96e65c.json
# Description: This process manages the end-to-end supply chain for handcrafted artisan goods, integrating unique sourcing, bespoke production, and customized distribution. It involves identifying rare raw materials, coordinating with local artisans, ensuring quality through multi-stage inspections, managing limited batch productions, and tailoring delivery schedules to niche markets. The process also incorporates dynamic demand forecasting based on cultural trends and seasonal events, alongside adaptive pricing models that reflect scarcity and craftsmanship value, ensuring sustainable artisan livelihoods while maintaining exclusivity and customer satisfaction.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# define all activities as Transitions
Material_Sourcing = Transition(label='Material Sourcing')
Artisan_Vetting = Transition(label='Artisan Vetting')
Sample_Review = Transition(label='Sample Review')
Design_Finalize = Transition(label='Design Finalize')
Batch_Scheduling = Transition(label='Batch Scheduling')
Quality_Check = Transition(label='Quality Check')
Custom_Packaging = Transition(label='Custom Packaging')
Demand_Forecast = Transition(label='Demand Forecast')
Price_Adjust = Transition(label='Price Adjust')
Inventory_Sync = Transition(label='Inventory Sync')
Order_Processing = Transition(label='Order Processing')
Craft_Coordination = Transition(label='Craft Coordination')
Shipment_Plan = Transition(label='Shipment Plan')
Market_Analysis = Transition(label='Market Analysis')
Feedback_Loop = Transition(label='Feedback Loop')
Trend_Monitor = Transition(label='Trend Monitor')

# Based on description, organize workflow partial order and control-flow constructs:

# 1) Initial sourcing and artisan vetting in parallel
#    - Material Sourcing and Artisan Vetting are concurrent and both precede Sample Review.
start_PO = StrictPartialOrder(nodes=[Material_Sourcing, Artisan_Vetting, Sample_Review])
start_PO.order.add_edge(Material_Sourcing, Sample_Review)
start_PO.order.add_edge(Artisan_Vetting, Sample_Review)

# 2) After Sample Review, Design Finalize happens
#    and then Batch Scheduling
design_batch_PO = StrictPartialOrder(nodes=[Sample_Review, Design_Finalize, Batch_Scheduling])
design_batch_PO.order.add_edge(Sample_Review, Design_Finalize)
design_batch_PO.order.add_edge(Design_Finalize, Batch_Scheduling)

# 3) Quality Check follows Batch Scheduling
# 4) Custom Packaging after Quality Check
quality_pack_PO = StrictPartialOrder(nodes=[Batch_Scheduling, Quality_Check, Custom_Packaging])
quality_pack_PO.order.add_edge(Batch_Scheduling, Quality_Check)
quality_pack_PO.order.add_edge(Quality_Check, Custom_Packaging)

# 5) Demand Forecast and Price Adjust happen in parallel after Market Analysis and Trend Monitor
market_trend_PO = StrictPartialOrder(nodes=[Market_Analysis, Trend_Monitor])
# No order edges - concurrent

demand_price_PO = StrictPartialOrder(nodes=[Demand_Forecast, Price_Adjust])
# Concurrent, both depend on market_trend_PO, make a PO combining

market_trend_demand_price = StrictPartialOrder(
    nodes=[Market_Analysis, Trend_Monitor, Demand_Forecast, Price_Adjust]
)
market_trend_demand_price.order.add_edge(Market_Analysis, Demand_Forecast)
market_trend_demand_price.order.add_edge(Market_Analysis, Price_Adjust)
market_trend_demand_price.order.add_edge(Trend_Monitor, Demand_Forecast)
market_trend_demand_price.order.add_edge(Trend_Monitor, Price_Adjust)

# 6) Inventory Sync follows after Demand Forecast and Price Adjust
inventory_PO = StrictPartialOrder(nodes=[Demand_Forecast, Price_Adjust, Inventory_Sync])
inventory_PO.order.add_edge(Demand_Forecast, Inventory_Sync)
inventory_PO.order.add_edge(Price_Adjust, Inventory_Sync)

# 7) Order Processing and Craft Coordination follow Inventory Sync
order_craft_PO = StrictPartialOrder(nodes=[Inventory_Sync, Order_Processing, Craft_Coordination])
order_craft_PO.order.add_edge(Inventory_Sync, Order_Processing)
order_craft_PO.order.add_edge(Inventory_Sync, Craft_Coordination)

# 8) Shipment Plan follows Craft Coordination and Custom Packaging
ship_plan_PO = StrictPartialOrder(nodes=[Craft_Coordination, Custom_Packaging, Shipment_Plan])
ship_plan_PO.order.add_edge(Craft_Coordination, Shipment_Plan)
ship_plan_PO.order.add_edge(Custom_Packaging, Shipment_Plan)

# 9) Feedback Loop is a looping node starting from Feedback Loop activity
# The loop models adaptive improvements triggered by feedback.

# We use a loop: * (Feedback_Loop, Market_Analysis)
# It executes Feedback Loop, then either exits or executes Market Analysis then repeats.

feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Loop, Market_Analysis])

# 10) Trend Monitor runs concurrently with Feedback Loop (covered via order edges later)

# Now build top-level PO combining subparts with order edges matching logical flow:

# Combine all nodes at root level:
root_nodes = [
    start_PO,
    design_batch_PO,
    quality_pack_PO,
    market_trend_demand_price,
    inventory_PO,
    order_craft_PO,
    ship_plan_PO,
    feedback_loop,
    Trend_Monitor,  # Trend Monitor is involved in market_trend_demand_price above but still kept for explicit concurrency with loop
]

root = StrictPartialOrder(nodes=root_nodes)

# Add edges between these nodes for partial order:

# start_PO --> design_batch_PO (Sample Review done before Design Finalize)
root.order.add_edge(start_PO, design_batch_PO)

# design_batch_PO --> quality_pack_PO (Batch Scheduling then Quality Check)
root.order.add_edge(design_batch_PO, quality_pack_PO)

# quality_pack_PO --> order_craft_PO (Packaging done before Craft Coordination and Order Processing)
root.order.add_edge(quality_pack_PO, order_craft_PO)

# market_trend_demand_price --> inventory_PO
root.order.add_edge(market_trend_demand_price, inventory_PO)

# inventory_PO --> order_craft_PO (Inventory Sync before Order Processing, Craft Coordination)
root.order.add_edge(inventory_PO, order_craft_PO)

# order_craft_PO --> ship_plan_PO
root.order.add_edge(order_craft_PO, ship_plan_PO)

# feedback_loop executes concurrently but logically impacts market analysis and trend monitor:
# Connect feedback_loop to market_trend_demand_price to ensure synchronization
root.order.add_edge(feedback_loop, market_trend_demand_price)

# Trend Monitor inside market_trend_demand_price, but the external Trend_Monitor node to ensure concurrency with feedback_loop
# Let root keep Trend_Monitor as separate, concurrent node to feedback_loop (no edges)

# No edge between Trend_Monitor and feedback_loop => concurrent

# This models concurrency of artisans' and material sourcing at start,
# then flows to design/batch, quality/packaging,
# while demand forecasting and pricing adapt through market and feedback loops
# followed by inventory, order processing, crafting coordination, and shipment planning.

# Final 'root' represents the entire supply chain workflow as a POWL model.