# Generated from: 84048b70-2ae7-4fad-9179-f21b702cd13b.json
# Description: This process outlines the complex and atypical steps required to onboard new employees into a fully remote, globally distributed team. It includes not only the standard HR and IT setup activities but also unique steps such as virtual cultural immersion, asynchronous mentorship pairing, equipment shipping logistics, timezone alignment workshops, and digital workspace personalization. The process ensures new hires are fully integrated into the company’s remote ecosystem, fostering engagement and productivity despite physical distances. It also handles compliance with varying international labor laws and data privacy regulations, requiring coordination among multiple departments and external vendors to deliver a seamless onboarding experience.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ps = Transition(label='Profile Setup')
es = Transition(label='Equipment Ship')
ag = Transition(label='Access Grant')
pr = Transition(label='Policy Review')
mm = Transition(label='Mentor Match')
ct = Transition(label='Culture Tour')
ts = Transition(label='Timezone Sync')
ws = Transition(label='Workspace Setup')
st = Transition(label='Security Training')
cc = Transition(label='Compliance Check')
im = Transition(label='Intro Meeting')
fl = Transition(label='Feedback Loop')
tt = Transition(label='Tool Training')
ni = Transition(label='Network Intro')
pv = Transition(label='Progress Review')

# Loop for iterative progress review & feedback
loop = OperatorPOWL(operator=Operator.LOOP, children=[pv, fl])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    ps, es, ag, pr,
    cc, im,
    mm, ct, ts,
    ws, st, tt, ni,
    loop
])

# Initial setup: after profile setup, run equipment shipping, access grant, and policy review in parallel
root.order.add_edge(ps, es)
root.order.add_edge(ps, ag)
root.order.add_edge(ps, pr)

# After those complete, perform compliance check
root.order.add_edge(es, cc)
root.order.add_edge(ag, cc)
root.order.add_edge(pr, cc)

# After compliance, have the intro meeting
root.order.add_edge(cc, im)

# After intro meeting, start cultural immersion, mentorship pairing, and timezone sync in parallel
root.order.add_edge(im, mm)
root.order.add_edge(im, ct)
root.order.add_edge(im, ts)

# Once those three are done, start workspace setup, tool training, security training, and network intro in parallel
for pre in [mm, ct, ts]:
    for post in [ws, tt, st, ni]:
        root.order.add_edge(pre, post)

# After all setup and trainings, enter the review-feedback loop
for pre in [ws, tt, st, ni]:
    root.order.add_edge(pre, loop)