# Generated from: 1f89efe7-ec88-4d7f-9894-d7709bae3106.json
# Description: This process describes the comprehensive workflow for authenticating rare historical artifacts before acquisition by a museum. It involves initial provenance research, multispectral imaging analysis, expert consultations across various disciplines, chemical composition testing, and digital ledger registration. The process ensures artifacts are verified for authenticity, legal ownership, and cultural significance, minimizing risks of forgery or illicit acquisition. It also incorporates stakeholder approvals, insurance appraisal, and final archival documentation, integrating technology with traditional expertise to uphold ethical and scholarly standards in artifact curation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
provenance_check = Transition(label="Provenance Check")
visual_survey    = Transition(label="Visual Survey")
material_scan    = Transition(label="Material Scan")
xray_imaging     = Transition(label="XRay Imaging")
spectral_analysis= Transition(label="Spectral Analysis")
carbon_dating    = Transition(label="Carbon Dating")
expert_review    = Transition(label="Expert Review")
legal_verify     = Transition(label="Legal Verify")
ownership_trace  = Transition(label="Ownership Trace")
cultural_assess  = Transition(label="Cultural Assess")
stakeholder_meet = Transition(label="Stakeholder Meet")
insurance_quote  = Transition(label="Insurance Quote")
risk_assess      = Transition(label="Risk Assess")
ledger_entry     = Transition(label="Ledger Entry")
archive_update   = Transition(label="Archive Update")
final_approval   = Transition(label="Final Approval")

# Build the partial‐order model
root = StrictPartialOrder(
    nodes=[
        provenance_check,
        visual_survey,
        material_scan,
        xray_imaging,
        spectral_analysis,
        carbon_dating,
        expert_review,
        legal_verify,
        ownership_trace,
        cultural_assess,
        stakeholder_meet,
        insurance_quote,
        risk_assess,
        ledger_entry,
        archive_update,
        final_approval,
    ]
)

# Initial provenance check must complete before any technical analyses
for tech in [visual_survey, material_scan, xray_imaging, spectral_analysis, carbon_dating]:
    root.order.add_edge(provenance_check, tech)

# All technical analyses feed into the expert review
for tech in [visual_survey, material_scan, xray_imaging, spectral_analysis, carbon_dating]:
    root.order.add_edge(tech, expert_review)

# Expert review branches into legal, ownership, and cultural verifications (can run in parallel)
for ver in [legal_verify, ownership_trace, cultural_assess]:
    root.order.add_edge(expert_review, ver)

# All verifications must complete before stakeholder meeting
for ver in [legal_verify, ownership_trace, cultural_assess]:
    root.order.add_edge(ver, stakeholder_meet)

# Stakeholder meeting -> insurance quote -> risk assessment
root.order.add_edge(stakeholder_meet, insurance_quote)
root.order.add_edge(insurance_quote, risk_assess)

# After risk assessment, register to ledger and update archive (in parallel)
root.order.add_edge(risk_assess, ledger_entry)
root.order.add_edge(risk_assess, archive_update)

# Ledger entry and archive update must finish before final approval
root.order.add_edge(ledger_entry, final_approval)
root.order.add_edge(archive_update, final_approval)