# Generated from: 1f72ab4f-2100-4627-8513-58da6c1f1f92.json
# Description: This process involves the intricate steps required to authenticate and verify the provenance of rare cultural artifacts. Beginning with initial artifact intake and preliminary condition assessment, it includes multi-layered historical research and provenance tracing through archival databases. Following this, scientific material analysis and radiocarbon dating are performed to validate period authenticity. Concurrently, expert panel reviews and comparative stylistic analysis ensure contextual accuracy. The process also incorporates digital fingerprinting and 3D scanning to create a secure, immutable record. Final stages involve legal documentation, insurance appraisal, and secure archival storage planning. This atypical but realistic process ensures thorough verification, safeguarding cultural heritage and providing confidence to collectors and institutions alike.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
ai = Transition(label='Artifact Intake')
cc = Transition(label='Condition Check')
hr = Transition(label='History Research')
pt = Transition(label='Provenance Trace')
mt = Transition(label='Material Testing')
rd = Transition(label='Radiocarbon Date')
er = Transition(label='Expert Review')
sc = Transition(label='Stylistic Compare')
ds = Transition(label='Digital Scan')
fp = Transition(label='Fingerprinting')
lr = Transition(label='Legal Review')
ia = Transition(label='Insurance Appraise')
ap = Transition(label='Archival Plan')
rs = Transition(label='Record Secure')
fa = Transition(label='Final Approval')

# Build partial order with concurrency and sequencing
root = StrictPartialOrder(nodes=[ai, cc, hr, pt, mt, rd, er, sc, ds, fp, lr, ia, ap, rs, fa])

# Sequence: Intake -> Check
root.order.add_edge(ai, cc)

# After check, history research and provenance trace can run in parallel
root.order.add_edge(cc, hr)
root.order.add_edge(cc, pt)

# Both research branches must finish before material testing
root.order.add_edge(hr, mt)
root.order.add_edge(pt, mt)

# Then radiocarbon dating
root.order.add_edge(mt, rd)

# After dating, four tasks run concurrently
root.order.add_edge(rd, er)
root.order.add_edge(rd, sc)
root.order.add_edge(rd, ds)
root.order.add_edge(rd, fp)

# All four must complete before legal review
for t in [er, sc, ds, fp]:
    root.order.add_edge(t, lr)

# Final stages in sequence
root.order.add_edge(lr, ia)
root.order.add_edge(ia, ap)
root.order.add_edge(ap, rs)
root.order.add_edge(rs, fa)