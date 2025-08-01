# Generated from: d426f83b-d749-4be2-acd3-a6d5845915eb.json
# Description: This process involves the detailed verification and authentication of antique assets for high-value collectors and museums, incorporating provenance research, material analysis, expert consultation, and condition assessment. The process begins with initial asset intake, followed by multi-layered investigation including historical document cross-checking, scientific testing such as radiocarbon dating or spectroscopy, and comparative stylistic evaluation. Findings are then compiled into a detailed authentication report, which undergoes peer review by external specialists. The final step involves certification issuance and digital archiving of the asset’s verified profile. This atypical but realistic process ensures the legitimacy and value preservation of rare antiques in a market fraught with forgery risks.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ai   = Transition(label='Asset Intake')
hs   = Transition(label='Historical Search')
pc   = Transition(label='Provenance Check')
ms   = Transition(label='Material Sampling')
rt   = Transition(label='Radiocarbon Test')
sa   = Transition(label='Scientific Analysis')
sc   = Transition(label='Style Compare')
ec   = Transition(label='Expert Consult')
cr   = Transition(label='Condition Review')
dc   = Transition(label='Data Compilation')
rd   = Transition(label='Report Draft')
pr   = Transition(label='Peer Review')
cert = Transition(label='Certification')
da   = Transition(label='Digital Archive')
cd   = Transition(label='Client Delivery')

# Scientific testing: choose either Radiocarbon Test or Scientific Analysis
sci_xor = OperatorPOWL(operator=Operator.XOR, children=[rt, sa])
sci     = StrictPartialOrder(nodes=[ms, sci_xor])
sci.order.add_edge(ms, sci_xor)

# Provenance research: Historical Search then Provenance Check
prov = StrictPartialOrder(nodes=[hs, pc])
prov.order.add_edge(hs, pc)

# Root partial order: overall process
root = StrictPartialOrder(
    nodes=[
        ai,
        prov,
        sci,
        sc,
        ec,
        cr,
        dc,
        rd,
        pr,
        cert,
        da,
        cd
    ]
)

# Asset Intake precedes all investigation branches
for branch in [prov, sci, sc, ec, cr]:
    root.order.add_edge(ai, branch)

# All investigations must complete before Data Compilation
for branch in [prov, sci, sc, ec, cr]:
    root.order.add_edge(branch, dc)

# Sequential post‐compilation steps
root.order.add_edge(dc, rd)
root.order.add_edge(rd, pr)
root.order.add_edge(pr, cert)
root.order.add_edge(cert, da)
root.order.add_edge(da, cd)