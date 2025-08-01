# Generated from: 441dbe43-9f37-4789-b026-6390875ce577.json
# Description: This process involves sourcing rare raw materials from remote locations, verifying artisan credentials, custom-designing product prototypes, coordinating multi-vendor collaboration, managing quality inspections at various stages, handling bespoke packaging, and organizing niche market distribution. Additionally, it includes real-time artisan feedback integration, dynamic inventory allocation, and adaptive pricing strategies based on limited-edition demand fluctuations, ensuring a seamless blend of tradition and innovation in a highly specialized supply chain network.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
t_ms = Transition(label='Material Sourcing')
t_cc = Transition(label='Credential Check')
t_vs = Transition(label='Vendor Sync')
t_pd = Transition(label='Prototype Design')
t_fc = Transition(label='Feedback Collect')
t_qi = Transition(label='Quality Inspect')
t_pkg = Transition(label='Packaging Design')
t_ma = Transition(label='Market Analysis')
t_df = Transition(label='Demand Forecast')
t_pa = Transition(label='Price Adjust')
t_ia = Transition(label='Inventory Allocate')
t_op = Transition(label='Order Processing')
t_sp = Transition(label='Shipping Plan')
t_dr = Transition(label='Data Review')
t_sr = Transition(label='Sales Report')

# Loop for design + artisan feedback integration
design_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[t_pd, t_fc]
)

# Loop for dynamic pricing based on demand forecast
price_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[t_df, t_pa]
)

# Loop for iterative quality inspection & packaging design
quality_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[t_qi, t_pkg]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    t_ms, t_cc,      # start tasks
    t_vs,            # sync after sourcing & credential check
    design_loop,     # prototype & feedback
    quality_loop,    # iterative quality/packaging
    t_ma,            # market analysis
    price_loop,      # pricing loop
    t_ia,            # inventory allocation
    t_op,            # order processing
    t_sp,            # shipping plan
    t_dr,            # data review
    t_sr             # final sales report
])

# Define the dependencies (partial order edges)
# Material Sourcing + Credential Check --> Vendor Sync
root.order.add_edge(t_ms, t_vs)
root.order.add_edge(t_cc, t_vs)

# Vendor Sync --> Design & Feedback loop
root.order.add_edge(t_vs, design_loop)

# After design loop --> Quality/Packaging loop
root.order.add_edge(design_loop, quality_loop)

# After quality loop --> Market Analysis AND Pricing loop
root.order.add_edge(quality_loop, t_ma)
root.order.add_edge(quality_loop, price_loop)

# After Market Analysis & Pricing --> Inventory Allocation
root.order.add_edge(t_ma, t_ia)
root.order.add_edge(price_loop, t_ia)

# Then Order Processing --> Shipping --> Data Review --> Sales Report
root.order.add_edge(t_ia, t_op)
root.order.add_edge(t_op, t_sp)
root.order.add_edge(t_sp, t_dr)
root.order.add_edge(t_dr, t_sr)