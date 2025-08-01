# Generated from: cca328f3-2447-456e-b391-2bce065af679.json
# Description: This process involves the thorough evaluation and verification of historical artifacts in a museum setting. It starts with initial artifact intake, followed by detailed provenance research, material composition analysis using advanced spectroscopy, and stylistic comparison against known samples. Concurrently, digital imaging captures high-resolution visuals for documentation. Expert consultations are arranged to assess cultural significance and authenticity. The process includes cross-referencing with global artifact databases and legal compliance checks regarding ownership and export laws. After synthesis of all data, a final authenticity report is prepared, archived, and the artifact is either approved for display, returned to the lender, or flagged for further investigation. This atypical process requires coordination across departments including curators, scientists, legal advisors, and archivists, ensuring comprehensive and credible authentication outcomes.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
intake     = Transition(label='Artifact Intake')
prov       = Transition(label='Provenance Check')
scan       = Transition(label='Material Scan')
style      = Transition(label='Style Compare')
digital    = Transition(label='Digital Capture')
expert     = Transition(label='Expert Review')
db         = Transition(label='Database Search')
legal      = Transition(label='Legal Audit')
cultural   = Transition(label='Cultural Assess')
synth      = Transition(label='Data Synthesis')
draft      = Transition(label='Report Draft')
archival   = Transition(label='Archival Store')
disp       = Transition(label='Display Approve')
lender     = Transition(label='Lender Notify')
flag       = Transition(label='Investigation Flag')

# Build the XOR‐choice for the final outcome
# (artifact is either approved for display, returned to lender, or flagged)
xor_end = OperatorPOWL(operator=Operator.XOR, children=[disp, lender, flag])

# Build the overall partial‐order workflow
root = StrictPartialOrder(nodes=[
    intake,
    prov, scan, style, digital, expert, db, legal, cultural,
    synth, draft, archival,
    xor_end
])

# After intake, the eight analyses/evaluations can run in parallel
for t in [prov, scan, style, digital, expert, db, legal, cultural]:
    root.order.add_edge(intake, t)
    # all must complete before synthesis
    root.order.add_edge(t, synth)

# Then the linear remainder of the process
root.order.add_edge(synth, draft)
root.order.add_edge(draft, archival)
# Finally, choose one of the three end‐states
root.order.add_edge(archival, xor_end)