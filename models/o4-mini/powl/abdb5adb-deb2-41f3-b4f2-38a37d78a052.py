# Generated from: abdb5adb-deb2-41f3-b4f2-38a37d78a052.json
# Description: This process governs the cyclical collaboration between multiple departments to foster continuous innovation within an organization. It begins with idea solicitation from all teams, followed by cross-functional brainstorming sessions. Selected concepts undergo rapid prototyping, internal testing, and iterative feedback collection. Simultaneously, risk assessments and market feasibility studies are conducted to ensure viability. Upon refinement, resource allocation and budget approval are secured before pilot deployment. Post-deployment analytics and stakeholder evaluations inform final adjustments. The cycle concludes with knowledge sharing and documentation to embed learnings into organizational best practices, thus promoting sustainable innovation across departments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ig = Transition(label="Idea Gathering")
cb = Transition(label="Cross Brainstorm")
cs = Transition(label="Concept Screening")
pb = Transition(label="Prototype Build")
it = Transition(label="Internal Testing")
fl = Transition(label="Feedback Loop")
rr = Transition(label="Risk Review")
ms = Transition(label="Market Study")
rp = Transition(label="Resource Plan")
ba = Transition(label="Budget Approval")
pl = Transition(label="Pilot Launch")
da = Transition(label="Data Analysis")
sm = Transition(label="Stakeholder Meet")
fa = Transition(label="Final Adjust")
ks = Transition(label="Knowledge Share")
skip = SilentTransition()

# Define the concurrent block: feedback loop, risk review, market study
concurrent_tasks = StrictPartialOrder(nodes=[fl, rr, ms])
# no edges => those three are concurrent

# Define the main body of one innovation cycle
body = StrictPartialOrder(
    nodes=[
        ig, cb, cs, pb, it,
        concurrent_tasks,
        rp, ba, pl, da, sm, fa, ks
    ]
)
# Sequential dependencies
body.order.add_edge(ig, cb)
body.order.add_edge(cb, cs)
body.order.add_edge(cs, pb)
body.order.add_edge(pb, it)
body.order.add_edge(it, concurrent_tasks)
body.order.add_edge(concurrent_tasks, rp)
body.order.add_edge(rp, ba)
body.order.add_edge(ba, pl)
body.order.add_edge(pl, da)
body.order.add_edge(da, sm)
body.order.add_edge(sm, fa)
body.order.add_edge(fa, ks)

# Wrap the cycle in a LOOP: do one cycle, then either exit or repeat
root = OperatorPOWL(operator=Operator.LOOP, children=[body, skip])