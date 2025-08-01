# Generated from: a7c6b397-5c50-4fc1-9524-1ac62acc999a.json
# Description: This process outlines the artisanal cheese supply chain from raw milk sourcing to final retail distribution. It involves sourcing milk from local farms, quality testing, traditional cheese curdling, aging under controlled conditions, packaging using eco-friendly materials, coordinating with niche retailers, managing seasonal demand fluctuations, and ensuring traceability through blockchain-based records. Each step requires meticulous attention to maintain flavor profiles and comply with health regulations while minimizing environmental impact and supporting local economies.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Curd_Formation = Transition(label='Curd Formation')
Whey_Separation = Transition(label='Whey Separation')
Mold_Inoculation = Transition(label='Mold Inoculation')
Cheese_Aging = Transition(label='Cheese Aging')
Humidity_Control = Transition(label='Humidity Control')
Flavor_Profiling = Transition(label='Flavor Profiling')
Eco_Packaging = Transition(label='Eco Packaging')
Inventory_Audit = Transition(label='Inventory Audit')
Order_Processing = Transition(label='Order Processing')
Retail_Coordination = Transition(label='Retail Coordination')
Demand_Forecast = Transition(label='Demand Forecast')
Traceability_Log = Transition(label='Traceability Log')
Regulation_Check = Transition(label='Regulation Check')

# Construct partial orders according to process description and possible partial concurrency

# 1. Initial sourcing and testing sequence
source_and_test = StrictPartialOrder(
    nodes=[Milk_Sourcing, Quality_Testing, Milk_Pasteurize]
)
source_and_test.order.add_edge(Milk_Sourcing, Quality_Testing)
source_and_test.order.add_edge(Quality_Testing, Milk_Pasteurize)

# 2. Cheese production subprocess
# Curd Formation and Whey Separation are sequential
# Mold Inoculation comes after Whey Separation
curd_and_whey = StrictPartialOrder(
    nodes=[Curd_Formation, Whey_Separation, Mold_Inoculation]
)
curd_and_whey.order.add_edge(Curd_Formation, Whey_Separation)
curd_and_whey.order.add_edge(Whey_Separation, Mold_Inoculation)

# 3. Aging subprocess has loop control for Humidity and Flavor profiling repeatedly until aging completes
# Model aging loop: LOOP(Aging, loop body)
aging_body = StrictPartialOrder(
    nodes=[Humidity_Control, Flavor_Profiling]
)
# Humidity Control and Flavor Profiling can be concurrent (no order edges)
loop_aging = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Cheese_Aging, aging_body]
)

# 4. Packaging node after aging loop
packaging = Eco_Packaging

# 5. Inventory audit and order processing can be concurrent after packaging
inventory_and_order = StrictPartialOrder(
    nodes=[Inventory_Audit, Order_Processing]
)

# 6. Retail and demand forecasting concurrently after inventory and order
retail_and_demand = StrictPartialOrder(
    nodes=[Retail_Coordination, Demand_Forecast]
)

# 7. Traceability logging and regulation check at the end, concurrent
final_checks = StrictPartialOrder(
    nodes=[Traceability_Log, Regulation_Check]
)

# Build entire process partial order linking

# Level 1 --> Level 2
# After Milk Pasteurize, start Curd Formation
p1_p2 = StrictPartialOrder(
    nodes=[source_and_test, curd_and_whey]
)
p1_p2.order.add_edge(source_and_test, curd_and_whey)

# Level 2 --> Aging Loop
p2_aging = StrictPartialOrder(
    nodes=[curd_and_whey, loop_aging]
)
p2_aging.order.add_edge(curd_and_whey, loop_aging)

# Aging Loop --> Packaging
aging_packaging = StrictPartialOrder(
    nodes=[loop_aging, packaging]
)
aging_packaging.order.add_edge(loop_aging, packaging)

# Packaging --> Inventory & Order
pack_inventory_order = StrictPartialOrder(
    nodes=[packaging, inventory_and_order]
)
pack_inventory_order.order.add_edge(packaging, inventory_and_order)

# Inventory & Order --> Retail & Demand
inv_ord_retail_dem = StrictPartialOrder(
    nodes=[inventory_and_order, retail_and_demand]
)
inv_ord_retail_dem.order.add_edge(inventory_and_order, retail_and_demand)

# Retail & Demand --> Final Checks
retail_final = StrictPartialOrder(
    nodes=[retail_and_demand, final_checks]
)
retail_final.order.add_edge(retail_and_demand, final_checks)

# Now combine all into one root PO by nested partial orders:

# Helper to flatten nested StrictPartialOrders into single level with merged edges might be useful
# But POWL allows nested PO nodes. So we can construct it stepwise:

# Compose stepwise nested POs:

step1 = StrictPartialOrder(
    nodes=[source_and_test, curd_and_whey]
)
step1.order.add_edge(source_and_test, curd_and_whey)

step2 = StrictPartialOrder(
    nodes=[step1, loop_aging]
)
step2.order.add_edge(step1, loop_aging)

step3 = StrictPartialOrder(
    nodes=[step2, packaging]
)
step3.order.add_edge(step2, packaging)

step4 = StrictPartialOrder(
    nodes=[step3, inventory_and_order]
)
step4.order.add_edge(step3, inventory_and_order)

step5 = StrictPartialOrder(
    nodes=[step4, retail_and_demand]
)
step5.order.add_edge(step4, retail_and_demand)

root = StrictPartialOrder(
    nodes=[step5, final_checks]
)
root.order.add_edge(step5, final_checks)