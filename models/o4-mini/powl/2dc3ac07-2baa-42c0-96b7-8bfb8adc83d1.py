# Generated from: 2dc3ac07-2baa-42c0-96b7-8bfb8adc83d1.json
# Description: This process involves designing and executing a multi-sensory marketing campaign that integrates tactile, olfactory, auditory, and visual stimuli to enhance consumer engagement across physical and digital channels. The process starts with sensory research to identify optimal stimuli combinations, followed by prototype development where physical samples and digital assets are created. Next, a pilot test is conducted in select markets to measure sensory impact and consumer response using biometric feedback and surveys. Data from the pilot feeds into optimization cycles refining stimuli intensity, timing, and channel synchronization. After final adjustments, the campaign is launched simultaneously across retail stores, mobile apps, social media, and experiential events. Post-launch, ongoing monitoring collects real-time sensory engagement metrics, enabling adaptive modulation of stimuli based on consumer mood and environmental factors. The process concludes with comprehensive performance analysis and lessons learned to inform future sensory marketing initiatives.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
sr = Transition(label='Sensory Research')
sd = Transition(label='Stimuli Design')
ap = Transition(label='Asset Production')
pb = Transition(label='Prototype Build')
pt = Transition(label='Pilot Testing')
da = Transition(label='Data Analysis')
sa = Transition(label='Stimuli Adjust')
cs = Transition(label='Channel Sync')
ml = Transition(label='Market Launch')
ee = Transition(label='Experience Event')
et = Transition(label='Engagement Track')
fg = Transition(label='Feedback Gather')
at = Transition(label='Adaptive Tuning')
pr = Transition(label='Performance Review')
ll = Transition(label='Lessons Learned')

# Optimization loop: Stimuli Adjust -> Channel Sync (repeatable)
opt_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[sa, cs]
)

# Post-launch feedback loop: do Engagement Track, then optionally (Feedback Gather -> Adaptive Tuning) then repeat
po_feedback = StrictPartialOrder(nodes=[fg, at])
po_feedback.order.add_edge(fg, at)
post_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[et, po_feedback]
)

# Launch phase: Market Launch and Experience Event in parallel
launch_phase = StrictPartialOrder(nodes=[ml, ee])

# Root partial order tying everything together
root = StrictPartialOrder(nodes=[
    sr, sd, ap, pb, pt, da,
    opt_loop,
    launch_phase,
    post_loop,
    pr, ll
])

# Define the control-flow dependencies
root.order.add_edge(sr, sd)
root.order.add_edge(sd, ap)
root.order.add_edge(ap, pb)
root.order.add_edge(pb, pt)
root.order.add_edge(pt, da)
root.order.add_edge(da, opt_loop)
root.order.add_edge(opt_loop, launch_phase)
root.order.add_edge(launch_phase, post_loop)
root.order.add_edge(post_loop, pr)
root.order.add_edge(pr, ll)