# Generated from: bd773453-981b-4e97-ab52-ff163ec9a0a6.json
# Description: This process outlines the complex and multifaceted steps involved in establishing a sustainable urban rooftop farm. It includes site assessment, structural analysis, soil preparation, microclimate evaluation, and installation of automated irrigation systems. The process also integrates community engagement, local regulatory compliance, crop selection based on seasonal data, and ongoing monitoring for pest control and yield optimization. Additionally, it incorporates waste recycling from the farm into compost, energy management through solar panels, and distribution logistics to local markets. The process ensures environmental sustainability while maximizing crop productivity in an unconventional urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ts = Transition(label="Site Survey")
lt = Transition(label="Load Test")
pc = Transition(label="Permit Check")
ms = Transition(label="Microclimate Map")
soil = Transition(label="Soil Prep")
cp = Transition(label="Crop Plan")
cm = Transition(label="Community Meet")
ir = Transition(label="Irrigation Setup")
si = Transition(label="Solar Install")
ea = Transition(label="Energy Audit")
wc = Transition(label="Waste Cycle")
cb = Transition(label="Compost Build")
pm = Transition(label="Pest Monitor")
dl = Transition(label="Data Logging")
yr = Transition(label="Yield Review")
ml = Transition(label="Market Link")

# Silent transition for loops
skip = SilentTransition()

# Loop for waste recycling: Waste Cycle then optionally Compost Build then repeat
loop_waste = OperatorPOWL(operator=Operator.LOOP, children=[wc, cb])

# Loop for ongoing monitoring: Pest Monitor -> Data Logging -> Yield Review, then repeat
monitoring_body = StrictPartialOrder(nodes=[pm, dl, yr])
monitoring_body.order.add_edge(pm, dl)
monitoring_body.order.add_edge(dl, yr)
loop_mon = OperatorPOWL(operator=Operator.LOOP, children=[monitoring_body, skip])

# Root partial order
root = StrictPartialOrder(nodes=[
    ts, lt, pc,
    ms, soil, cm,
    cp, ir, si, ea,
    loop_waste, loop_mon,
    ml
])

# Define the control-flow dependencies
root.order.add_edge(ts, lt)
root.order.add_edge(lt, pc)

# After permit check: microclimate, soil prep, community meet, irrigation prep, solar install
root.order.add_edge(pc, ms)
root.order.add_edge(pc, soil)
root.order.add_edge(pc, cm)
root.order.add_edge(pc, ir)
root.order.add_edge(pc, si)

# Structural load test also needed for irrigation and solar
root.order.add_edge(lt, ir)
root.order.add_edge(lt, si)

# Crop plan depends on microclimate analysis
root.order.add_edge(ms, cp)
# Irrigation setup also depends on crop plan
root.order.add_edge(cp, ir)

# Energy audit after solar install
root.order.add_edge(si, ea)

# Start loops after irrigation setup and energy audit complete
root.order.add_edge(ir, loop_waste)
root.order.add_edge(ea, loop_waste)
root.order.add_edge(ir, loop_mon)
root.order.add_edge(ea, loop_mon)

# After both loops finish, proceed to market link
root.order.add_edge(loop_waste, ml)
root.order.add_edge(loop_mon, ml)