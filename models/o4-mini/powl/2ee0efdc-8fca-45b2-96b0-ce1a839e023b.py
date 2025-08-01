# Generated from: 2ee0efdc-8fca-45b2-96b0-ce1a839e023b.json
# Description: This process involves the detailed verification and validation of antique artifacts to determine their authenticity and provenance. Experts collaborate to perform material analysis, historical research, and stylistic comparisons, while coordinating with legal authorities for ownership checks. The process includes advanced imaging, carbon dating, and provenance documentation, followed by expert panel review and final certification. This atypical yet realistic procedure ensures that artifacts entering collections or markets are genuine, legally owned, and accurately described, minimizing fraud and preserving cultural heritage.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define transitions
intake = Transition(label='Artifact Intake')
survey = Transition(label='Initial Survey')
mt = Transition(label='Material Testing')
cd = Transition(label='Carbon Dating')
ic = Transition(label='Imaging Scan')
sc = Transition(label='Style Compare')
hc = Transition(label='Historical Check')
pt = Transition(label='Provenance Trace')
ov = Transition(label='Ownership Verify')
lr = Transition(label='Legal Review')
cr = Transition(label='Condition Report')
ec = Transition(label='Expert Consult')
pr = Transition(label='Panel Review')
cf = Transition(label='Certification')
fa = Transition(label='Final Archive')

# Build the partial order model
root = StrictPartialOrder(nodes=[
    intake, survey,
    mt, cd, ic, sc, hc,
    pt, ov, lr,
    cr, ec, pr, cf, fa
])

# Sequence: Intake -> Initial Survey
root.order.add_edge(intake, survey)

# From survey to all parallel analysis & provenance start
for t in [mt, cd, ic, sc, hc, pt]:
    root.order.add_edge(survey, t)

# Provenance chain: Trace -> Verify -> Legal Review
root.order.add_edge(pt, ov)
root.order.add_edge(ov, lr)

# All analyses and legal review must finish before condition report
for t in [mt, cd, ic, sc, hc, lr]:
    root.order.add_edge(t, cr)

# Final sequential steps
root.order.add_edge(cr, ec)
root.order.add_edge(ec, pr)
root.order.add_edge(pr, cf)
root.order.add_edge(cf, fa)