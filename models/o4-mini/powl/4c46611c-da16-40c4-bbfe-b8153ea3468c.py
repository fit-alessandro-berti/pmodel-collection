# Generated from: 4c46611c-da16-40c4-bbfe-b8153ea3468c.json
# Description: This process manages the end-to-end supply chain of an urban vertical farming operation, integrating automated planting, environmental monitoring, nutrient delivery, and harvest scheduling with downstream distribution logistics. It involves coordination between IoT sensors, AI-driven growth optimization, quality inspections, packaging automation, and last-mile delivery to retailers and consumers within a metropolitan area. The process ensures minimal waste, energy efficiency, and freshness, while adapting dynamically to demand fluctuations and seasonal variations, requiring continuous data analysis and prompt decision-making across multiple departments and external partners.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ss = Transition(label='Seed Selection')
tp = Transition(label='Tray Preparation')
ap = Transition(label='Automated Planting')
em = Transition(label='Env Monitoring')
nd = Transition(label='Nutrient Delivery')
ga = Transition(label='Growth Analysis')
pd = Transition(label='Pest Detection')
eo = Transition(label='Energy Optimization')
hs = Transition(label='Harvest Scheduling')
qi = Transition(label='Quality Inspection')
pkg = Transition(label='Automated Packaging')
it = Transition(label='Inventory Tracking')
df = Transition(label='Demand Forecast')
op = Transition(label='Order Processing')
ld = Transition(label='Last-Mile Dispatch')
cf = Transition(label='Customer Feedback')
wm = Transition(label='Waste Management')
skip = SilentTransition()

# Define the growth-monitoring cycle as a partial order
monitor_cycle = StrictPartialOrder(nodes=[em, nd, ga, pd, eo])
monitor_cycle.order.add_edge(em, nd)
monitor_cycle.order.add_edge(nd, ga)
monitor_cycle.order.add_edge(nd, pd)
monitor_cycle.order.add_edge(ga, eo)
monitor_cycle.order.add_edge(pd, eo)

# Wrap the monitoring cycle into a loop (iterate until exit)
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_cycle, skip])

# Build the overall process as a partial order with concurrency, joins, and waste handling
root = StrictPartialOrder(nodes=[
    ss, tp, ap,
    growth_loop,
    hs, qi, pkg, it,
    df, op, ld, cf, wm
])

# Seed-to-planting sequence
root.order.add_edge(ss, tp)
root.order.add_edge(tp, ap)
root.order.add_edge(ap, growth_loop)

# After planting: trigger harvest scheduling and demand forecast in parallel
root.order.add_edge(growth_loop, hs)
root.order.add_edge(growth_loop, df)

# Harvest path: scheduling -> inspection -> packaging -> inventory tracking
root.order.add_edge(hs, qi)
root.order.add_edge(qi, pkg)
root.order.add_edge(pkg, it)

# Demand + inventory join for order processing
root.order.add_edge(df, op)
root.order.add_edge(it, op)

# Downstream logistics
root.order.add_edge(op, ld)
root.order.add_edge(ld, cf)

# Waste handling from inspection and from customer feedback
root.order.add_edge(qi, wm)
root.order.add_edge(cf, wm)