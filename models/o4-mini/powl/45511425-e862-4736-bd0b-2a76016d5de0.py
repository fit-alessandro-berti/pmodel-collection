# Generated from: 45511425-e862-4736-bd0b-2a76016d5de0.json
# Description: This process involves verifying the authenticity of rare cultural artifacts sourced globally through a multi-layered approach combining scientific analysis, provenance research, and expert consultations. It begins with initial artifact intake and condition assessment, followed by advanced material composition testing and historical document cross-referencing. The process integrates blockchain registration for immutable provenance tracking and concludes with a final certification report issued to clients. Throughout, coordination with international regulatory bodies and ethical compliance reviews ensures that every artifact is legally and ethically validated before entering the market or museum collections, minimizing fraud and preserving cultural heritage integrity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
ai = Transition(label='Artifact Intake')
cc = Transition(label='Condition Check')
mt = Transition(label='Material Testing')
da = Transition(label='Document Analysis')
pr = Transition(label='Provenance Review')
ec = Transition(label='Expert Consult')
be = Transition(label='Blockchain Entry')
ea = Transition(label='Ethics Audit')
lv = Transition(label='Legal Verification')
rl = Transition(label='Regulator Liaison')
ms = Transition(label='Market Scan')
rd = Transition(label='Report Draft')
cr = Transition(label='Client Review')
fc = Transition(label='Final Certification')
as_t = Transition(label='Archival Storage')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    ai, cc, mt, da, pr, ec, be,
    ea, lv, rl, ms, rd, cr, fc, as_t
])

# Initial sequence: intake → condition check
root.order.add_edge(ai, cc)

# Parallel testing and analysis after condition check
root.order.add_edge(cc, mt)
root.order.add_edge(cc, da)

# Provenance research after both material testing and document analysis
root.order.add_edge(mt, pr)
root.order.add_edge(da, pr)

# Expert consultation follows provenance review
root.order.add_edge(pr, ec)

# Blockchain registration after expert consult
root.order.add_edge(ec, be)

# Compliance checks in parallel after blockchain entry
root.order.add_edge(be, ea)
root.order.add_edge(be, lv)
root.order.add_edge(be, rl)

# Market scan once all compliance checks are done
root.order.add_edge(ea, ms)
root.order.add_edge(lv, ms)
root.order.add_edge(rl, ms)

# Reporting and certification
root.order.add_edge(ms, rd)
root.order.add_edge(rd, cr)
root.order.add_edge(cr, fc)

# Final archival storage
root.order.add_edge(fc, as_t)