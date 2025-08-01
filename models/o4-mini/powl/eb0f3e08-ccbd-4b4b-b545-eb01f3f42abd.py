# Generated from: eb0f3e08-ccbd-4b4b-b545-eb01f3f42abd.json
# Description: This process manages an adaptive urban farming system integrating IoT sensor data, local weather forecasts, and community input to optimize crop growth cycles in constrained city environments. It involves real-time monitoring, dynamic resource allocation, pest detection with AI, nutrient adjustment, and community-driven crop selection. The system adapts to sudden environmental changes and market demand fluctuations by recalibrating planting schedules and harvesting plans, ensuring sustainable yield and waste minimization while promoting local engagement and education.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activity transitions
ss  = Transition(label='Sensor Setup')
dc  = Transition(label='Data Collection')
wc  = Transition(label='Weather Check')
st  = Transition(label='Soil Testing')
com = Transition(label='Community Poll')
cs  = Transition(label='Crop Selection')
ra  = Transition(label='Resource Assign')
ia  = Transition(label='Irrigation Adjust')
ps  = Transition(label='Pest Scan')
nm  = Transition(label='Nutrient Mix')
gm  = Transition(label='Growth Monitor')
su  = Transition(label='Schedule Update')
hp  = Transition(label='Harvest Plan')
ws  = Transition(label='Waste Sort')
yr  = Transition(label='Yield Report')

# Define the maintenance sequence A = irrigation -> pest -> nutrient -> growth
maintenance_seq = StrictPartialOrder(nodes=[ia, ps, nm, gm])
maintenance_seq.order.add_edge(ia, ps)
maintenance_seq.order.add_edge(ps, nm)
maintenance_seq.order.add_edge(nm, gm)

# Define the loop: do maintenance_seq, then either exit or do schedule update then repeat
maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[maintenance_seq, su])

# Build the overall workflow as a partial order
root = StrictPartialOrder(nodes=[
    ss, dc, wc, st, com,    # setup and inputs
    cs,                     # crop selection
    ra,                     # resource allocation
    maintenance_loop,       # adaptive maintenance loop
    hp, ws, yr              # harvesting and reporting
])

# Sensor Setup must precede initial data tasks
root.order.add_edge(ss, dc)
root.order.add_edge(ss, wc)
root.order.add_edge(ss, st)

# Data, weather, soil tests and community poll feed into crop selection
root.order.add_edge(dc, cs)
root.order.add_edge(wc, cs)
root.order.add_edge(st, cs)
root.order.add_edge(com, cs)

# Crop selection -> resource assignment -> maintenance loop
root.order.add_edge(cs, ra)
root.order.add_edge(ra, maintenance_loop)

# After exiting the loop, plan harvest then sort waste and report yield
root.order.add_edge(maintenance_loop, hp)
root.order.add_edge(hp, ws)
root.order.add_edge(hp, yr)