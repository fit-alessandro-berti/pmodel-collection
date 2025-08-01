# Generated from: aa004019-3106-4022-b2a3-0bdb5ea46f8e.json
# Description: This process involves the meticulous verification and authentication of ancient artifacts sourced from various archaeological sites before they are approved for museum exhibitions or private collections. It begins with initial provenance research, followed by multi-disciplinary scientific analysis, including radiocarbon dating and material composition tests. Expert consultations are held to evaluate stylistic and cultural attributes. The findings are compiled into a detailed report, which undergoes peer review. If discrepancies arise, further investigative activities such as microscopic imaging and comparative historical analysis are conducted. Once the artifact passes all authentication phases, legal documentation is prepared to certify its authenticity and ownership. Finally, the artifact is cataloged into the digital archive system and prepared for secure transportation to its display location, ensuring compliance with international cultural heritage laws and ethical guidelines.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activity transitions
prov        = Transition(label='Provenance Check')
vis         = Transition(label='Visual Inspection')
rad         = Transition(label='Radiocarbon Test')
mat         = Transition(label='Material Analysis')
style       = Transition(label='Stylistic Review')
expert      = Transition(label='Expert Consult')
report1     = Transition(label='Report Draft')
peer        = Transition(label='Peer Review')
disc        = Transition(label='Discrepancy Audit')
micro       = Transition(label='Microscopic Scan')
hist        = Transition(label='Historical Compare')
report2     = Transition(label='Report Draft')  # separate instance for the loop
legal       = Transition(label='Legal Prepare')
cert        = Transition(label='Certification Issue')
catalog     = Transition(label='Catalog Entry')
compliance  = Transition(label='Compliance Verify')
transport   = Transition(label='Secure Transport')

# Build the "discrepancy handling" partial order B for the loop body
B = StrictPartialOrder(nodes=[disc, micro, hist, report2])
B.order.add_edge(disc, micro)
B.order.add_edge(disc, hist)
B.order.add_edge(micro, report2)
B.order.add_edge(hist, report2)

# Build the loop: peer-review then either exit or do B then peer-review again
loop = OperatorPOWL(operator=Operator.LOOP, children=[peer, B])

# Build the root partial order for the whole process
root = StrictPartialOrder(
    nodes=[
        prov, vis, rad, mat,        # provenance & scientific analyses
        style, expert,              # stylistic & expert evaluation
        report1,                    # initial report draft
        loop,                       # peer‐review + possible discrepancy cycle
        legal, cert,                # legal documentation
        catalog, compliance, transport  # cataloging, compliance, transport
    ]
)

# Define the control‐flow edges
# 1) Provenance check precedes all analyses
root.order.add_edge(prov, vis)
root.order.add_edge(prov, rad)
root.order.add_edge(prov, mat)
# 2) Analyses precede stylistic & expert review
root.order.add_edge(vis, style)
root.order.add_edge(rad, style)
root.order.add_edge(mat, style)
# 3) Stylistic review → expert consult → report draft
root.order.add_edge(style, expert)
root.order.add_edge(expert, report1)
# 4) Report draft → peer‐review loop
root.order.add_edge(report1, loop)
# 5) After loop exit, legal prepare → certification → cataloging → compliance → transport
root.order.add_edge(loop, legal)
root.order.add_edge(legal, cert)
root.order.add_edge(cert, catalog)
root.order.add_edge(catalog, compliance)
root.order.add_edge(compliance, transport)