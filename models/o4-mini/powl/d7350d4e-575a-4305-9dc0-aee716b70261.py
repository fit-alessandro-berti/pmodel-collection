# Generated from: d7350d4e-575a-4305-9dc0-aee716b70261.json
# Description: This process involves the comprehensive authentication of rare historical artifacts before acquisition by a museum. It begins with preliminary provenance research, followed by multi-modal scientific analysis including spectroscopy and radiocarbon dating. Expert consultations assess cultural significance and authenticity. Legal clearances ensure compliance with international heritage laws. Digitization of findings supports archival and future reference. The artifact then undergoes conservation planning with specialized restorers. Finally, a detailed report is compiled, and acquisition approval is secured through stakeholder review. This atypical process integrates scientific, legal, and cultural evaluations to ensure the artifact's legitimacy and preservation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
prov = Transition(label='Provenance Check')
sample = Transition(label='Sample Collection')
spec = Transition(label='Spectroscopy Test')
carbon = Transition(label='Carbon Dating')
expert = Transition(label='Expert Review')
legal = Transition(label='Legal Clearance')
cultural = Transition(label='Cultural Assessment')
digit = Transition(label='Digital Scan')
arch = Transition(label='Archival Entry')
cond = Transition(label='Condition Report')
rest = Transition(label='Restoration Plan')
report = Transition(label='Report Draft')
stake = Transition(label='Stakeholder Meet')
vote = Transition(label='Acquisition Vote')
final = Transition(label='Final Approval')

# Build the partial order
root = StrictPartialOrder(nodes=[
    prov, sample, spec, carbon, expert, legal, cultural,
    digit, arch, cond, rest, report, stake, vote, final
])

# Preliminary research → sample collection
root.order.add_edge(prov, sample)

# Sample collection → parallel tests
root.order.add_edge(sample, spec)
root.order.add_edge(sample, carbon)

# Tests → expert/legal/cultural and digitization
for src in (spec, carbon):
    root.order.add_edge(src, expert)
    root.order.add_edge(src, cultural)
    root.order.add_edge(src, legal)
    root.order.add_edge(src, digit)

# Digitization → archival entry and condition report
root.order.add_edge(digit, arch)
root.order.add_edge(digit, cond)

# Condition report → restoration planning
root.order.add_edge(cond, rest)

# Expert/legal/cultural + restoration → report drafting
root.order.add_edge(expert, report)
root.order.add_edge(legal, report)
root.order.add_edge(cultural, report)
root.order.add_edge(rest, report)

# Report → stakeholder review → vote → final approval
root.order.add_edge(report, stake)
root.order.add_edge(stake, vote)
root.order.add_edge(vote, final)