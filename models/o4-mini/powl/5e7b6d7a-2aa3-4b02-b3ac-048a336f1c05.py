# Generated from: 5e7b6d7a-2aa3-4b02-b3ac-048a336f1c05.json
# Description: This process involves the systematic verification and validation of ancient artifacts using interdisciplinary techniques combining historical research, material science, and digital imaging. Activities include provenance tracing, carbon dating, spectral analysis, and expert consultations. The workflow ensures accurate authentication for museums or private collectors, mitigating risks of forgery while preserving cultural heritage. The process further integrates legal compliance checks, condition assessment, and secure transportation planning to maintain artifact integrity throughout the chain of custody. Anomalies detected prompt iterative re-examinations and final certification issuance.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
p_check    = Transition(label='Provenance Check')
h_review   = Transition(label='Historical Review')
m_sampling = Transition(label='Material Sampling')
c_dating   = Transition(label='Carbon Dating')
s_scan     = Transition(label='Spectral Scan')
m_exam     = Transition(label='Microscopic Exam')
expert     = Transition(label='Expert Consult')
condition  = Transition(label='Condition Report')
forgery    = Transition(label='Forgery Screening')
legal      = Transition(label='Legal Review')
rest_plan  = Transition(label='Restoration Plan')
transport  = Transition(label='Transport Setup')
security   = Transition(label='Security Audit')
cert       = Transition(label='Certification')
reexam     = Transition(label='Reexamination')

# Build the analysis sub‐process (to be looped)
analysis_po = StrictPartialOrder(nodes=[
    m_sampling, c_dating, s_scan, m_exam,
    expert, condition, forgery
])
# Material Sampling → Carbon Dating, Spectral Scan, Microscopic Exam
analysis_po.order.add_edge(m_sampling, c_dating)
analysis_po.order.add_edge(m_sampling, s_scan)
analysis_po.order.add_edge(m_sampling, m_exam)
# All analyses → Expert Consult
analysis_po.order.add_edge(c_dating, expert)
analysis_po.order.add_edge(s_scan, expert)
analysis_po.order.add_edge(m_exam, expert)
# Expert Consult → Condition Report & Forgery Screening
analysis_po.order.add_edge(expert, condition)
analysis_po.order.add_edge(expert, forgery)

# Loop: perform analysis, on anomalies re‐examination then repeat analysis
loop = OperatorPOWL(operator=Operator.LOOP, children=[analysis_po, reexam])

# Assemble the overall process
root = StrictPartialOrder(nodes=[
    p_check, h_review, loop,
    legal, rest_plan, transport, security,
    cert
])
# Provenance Check → Historical Review → Loop(ed analysis)
root.order.add_edge(p_check, h_review)
root.order.add_edge(h_review, loop)
# After successful analysis loop → Legal Review
root.order.add_edge(loop, legal)
# Legal Review → Restoration Plan, Transport Setup, Security Audit (in parallel)
root.order.add_edge(legal, rest_plan)
root.order.add_edge(legal, transport)
root.order.add_edge(legal, security)
# All final preparations → Certification
root.order.add_edge(rest_plan, cert)
root.order.add_edge(transport, cert)
root.order.add_edge(security, cert)