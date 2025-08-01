# Generated from: d332ca00-e8ed-4081-a918-5cef33d56a64.json
# Description: This process involves the meticulous examination and verification of rare artifacts to confirm their authenticity and provenance. It integrates multidisciplinary evaluations including historical research, material science analysis, and expert consultation. The process begins with initial artifact intake and documentation, followed by non-invasive imaging and chemical composition testing. Concurrently, provenance records are cross-checked against global databases. If anomalies arise, advanced forensic techniques and carbon dating are employed. The process culminates in a comprehensive authentication report, which informs acquisition decisions and insurance appraisals. Risk assessment and secure storage recommendations are also generated to preserve artifact integrity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
intake       = Transition(label='Intake Document')
visual       = Transition(label='Visual Inspect')
imaging      = Transition(label='Imaging Scan')
material     = Transition(label='Material Test')
db           = Transition(label='Database Cross')
provenance   = Transition(label='Provenance Check')
expert       = Transition(label='Expert Consult')
anomaly      = Transition(label='Anomaly Review')
carbon       = Transition(label='Carbon Dating')
forensic     = Transition(label='Forensic Analyze')
report       = Transition(label='Report Draft')
insurance    = Transition(label='Insurance Quote')
risk         = Transition(label='Risk Assess')
storage      = Transition(label='Storage Plan')
final        = Transition(label='Final Approval')
skip         = SilentTransition()

# Build the sub‐process for advanced analysis (if anomalies arise)
branch_seq = StrictPartialOrder(nodes=[carbon, forensic])
branch_seq.order.add_edge(carbon, forensic)

# XOR choice: either do advanced analysis or skip
xor_anomaly = OperatorPOWL(operator=Operator.XOR, children=[branch_seq, skip])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    intake, visual,
    imaging, material, db, provenance, expert,
    anomaly, xor_anomaly,
    report, insurance, risk, storage, final
])

# Define the control‐flow dependencies
root.order.add_edge(intake, visual)

# After visual inspection, these five analyses run in parallel
for nxt in [imaging, material, db, provenance, expert]:
    root.order.add_edge(visual, nxt)
    root.order.add_edge(nxt, anomaly)

# Anomaly review leads into the XOR branch
root.order.add_edge(anomaly, xor_anomaly)

# After the anomaly branch, draft the report and continue
root.order.add_edge(xor_anomaly, report)
root.order.add_edge(report, insurance)

# From insurance quote to risk assessment and storage planning (parallel)
root.order.add_edge(insurance, risk)
root.order.add_edge(insurance, storage)

# Both risk assessment and storage planning precede final approval
root.order.add_edge(risk, final)
root.order.add_edge(storage, final)