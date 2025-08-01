# Generated from: 3dc0e89a-5f7a-4cab-b261-21f2f039671c.json
# Description: This process outlines the steps involved in authenticating rare historical artifacts before acquisition by a museum. It begins with preliminary provenance verification followed by scientific material analysis using spectroscopy and radiocarbon dating. Experts then conduct microscopic examinations and stylistic comparison against known examples. Concurrently, digital imaging technology is employed to detect restorations or forgeries. Results are compiled and reviewed in a cross-disciplinary panel including historians, chemists, and conservators. If authenticity is confirmed, legal ownership documentation is finalized and the artifact is prepared for insured transport. The process ensures thorough validation combining historical, scientific, and legal perspectives to mitigate risks of acquiring counterfeit or misrepresented items.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Basic activities
vp   = Transition(label="Verify Provenance")
cs   = Transition(label="Collect Samples")
s1   = Transition(label="Conduct Spectroscopy")
r1   = Transition(label="Radiocarbon Test")
me   = Transition(label="Microscopic Exam")
sc   = Transition(label="Stylistic Check")
di   = Transition(label="Digital Imaging")
fd   = Transition(label="Forgery Detection")
cr   = Transition(label="Compile Results")
pr   = Transition(label="Panel Review")
lv   = Transition(label="Legal Verification")
isup = Transition(label="Insurance Setup")
pt   = Transition(label="Prepare Transport")
ot   = Transition(label="Ownership Transfer")
fa   = Transition(label="Finalize Acquisition")
skip = SilentTransition()

# Sub-process: scientific analysis (spectroscopy & radiocarbon in parallel)
analysis = StrictPartialOrder(nodes=[s1, r1])
# Sub-process: expert examinations (microscopic & stylistic in parallel)
expert = StrictPartialOrder(nodes=[me, sc])
# Sub-process: imaging pipeline (digital imaging → forgery detection)
imaging = StrictPartialOrder(nodes=[di, fd])
imaging.order.add_edge(di, fd)

# Sub-process: legal & logistics sequence
legal_seq = StrictPartialOrder(nodes=[lv, isup, pt, ot, fa])
legal_seq.order.add_edge(lv, isup)
legal_seq.order.add_edge(isup, pt)
legal_seq.order.add_edge(pt, ot)
legal_seq.order.add_edge(ot, fa)

# Choice: either proceed with legal/logistics or exit if not authentic
legal_choice = OperatorPOWL(operator=Operator.XOR, children=[legal_seq, skip])

# Root partial order
root = StrictPartialOrder(nodes=[vp, cs, analysis, expert, imaging, cr, pr, legal_choice])
# Dependencies
root.order.add_edge(vp, cs)
root.order.add_edge(cs, analysis)
root.order.add_edge(analysis, expert)
root.order.add_edge(analysis, imaging)
root.order.add_edge(expert, cr)
root.order.add_edge(imaging, cr)
root.order.add_edge(cr, pr)
root.order.add_edge(pr, legal_choice)