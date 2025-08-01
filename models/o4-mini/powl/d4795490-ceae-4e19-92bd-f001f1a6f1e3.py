# Generated from: d4795490-ceae-4e19-92bd-f001f1a6f1e3.json
# Description: This process involves sourcing rare coffee beans from remote, eco-sensitive farms, ensuring sustainable harvesting practices. Beans undergo micro-lot selection, followed by specialized fermentation and drying techniques tailored to each batch's unique profile. Quality control includes chemical and sensory analysis. The beans are then roasted using variable profiles depending on target markets. Packaging incorporates biodegradable materials with embedded QR codes for traceability. Distribution logistics optimize cold-chain transport to preserve freshness, integrating real-time environmental monitoring. Customer feedback loops inform continuous process refinement and personalized subscription adjustments, blending artisanal craftsmanship with advanced technology to deliver premium coffee experiences globally.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
farm             = Transition(label='Farm Sourcing')
lot              = Transition(label='Lot Selection')
sort_beans       = Transition(label='Bean Sorting')
fermentation     = Transition(label='Fermentation')
drying           = Transition(label='Drying Process')
quality          = Transition(label='Quality Control')
chemical         = Transition(label='Chemical Testing')
sensory          = Transition(label='Sensory Analysis')
roast            = Transition(label='Roast Profiling')
eco_pack         = Transition(label='Eco Packaging')
trace_qr         = Transition(label='Traceability QR')
cold             = Transition(label='Cold Transport')
env_monitor      = Transition(label='Env Monitoring')
feedback         = Transition(label='Customer Feedback')
subscription     = Transition(label='Subscription Adjust')

# Sub-process: chemical & sensory analysis happen concurrently under Quality Control
qc_sub = StrictPartialOrder(nodes=[chemical, sensory])

# Sub-process: eco‐packaging & QR embedding happen concurrently
pack_sub = StrictPartialOrder(nodes=[eco_pack, trace_qr])

# Loop: Customer Feedback, then either exit or Subscription Adjust + repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback, subscription])

# Root partial order combining all steps
root = StrictPartialOrder(
    nodes=[
        farm, lot, sort_beans, fermentation, drying,
        quality, qc_sub, roast, pack_sub,
        cold, env_monitor, loop
    ]
)

# Define the control‐flow dependencies
root.order.add_edge(farm, lot)
root.order.add_edge(lot, sort_beans)
root.order.add_edge(sort_beans, fermentation)
root.order.add_edge(fermentation, drying)
root.order.add_edge(drying, quality)
root.order.add_edge(quality, qc_sub)
root.order.add_edge(qc_sub, roast)
root.order.add_edge(roast, pack_sub)
root.order.add_edge(pack_sub, cold)
root.order.add_edge(cold, env_monitor)
root.order.add_edge(env_monitor, loop)