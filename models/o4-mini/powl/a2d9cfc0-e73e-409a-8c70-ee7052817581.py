# Generated from: a2d9cfc0-e73e-409a-8c70-ee7052817581.json
# Description: This process involves the systematic examination and verification of antique artifacts to determine authenticity and provenance. It integrates multidisciplinary assessments including material analysis, historical context evaluation, stylistic comparison, and provenance research. Experts collaborate to detect forgeries, restorations, or alterations while ensuring compliance with legal and ethical standards. The process culminates in certification, documentation, and recommendations for conservation or sale, tailored to the artifact’s unique characteristics and market demand.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
initial_review    = Transition(label="Initial Review")
provenance_check  = Transition(label="Provenance Check")
material_sampling = Transition(label="Material Sampling")
spectral_scan     = Transition(label="Spectral Scan")
stylistic_match   = Transition(label="Stylistic Match")
historical_ctx    = Transition(label="Historical Context")
forgery_detect    = Transition(label="Forgery Detection")
restoration_check = Transition(label="Restoration Check")
expert_consult    = Transition(label="Expert Consultation")
legal_assess      = Transition(label="Legal Assessment")
ethics_screen     = Transition(label="Ethics Screening")
condition_report  = Transition(label="Condition Report")
cert_prep         = Transition(label="Certification Prep")
documentation     = Transition(label="Documentation")
final_approval    = Transition(label="Final Approval")
conservation_plan = Transition(label="Conservation Plan")
market_analysis   = Transition(label="Market Analysis")

# Final choice: either Conservation Plan or Market Analysis
final_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[conservation_plan, market_analysis]
)

# Build the root partial order
root = StrictPartialOrder(
    nodes=[
        initial_review,
        provenance_check,
        material_sampling,
        spectral_scan,
        stylistic_match,
        historical_ctx,
        forgery_detect,
        restoration_check,
        expert_consult,
        legal_assess,
        ethics_screen,
        condition_report,
        cert_prep,
        documentation,
        final_approval,
        final_choice
    ]
)

# 1. Initial Review precedes all core assessments
for nxt in [provenance_check, material_sampling, stylistic_match, historical_ctx]:
    root.order.add_edge(initial_review, nxt)

# Material Sampling -> Spectral Scan
root.order.add_edge(material_sampling, spectral_scan)

# 2. After all assessments, perform detection & consulting in parallel
for src in [provenance_check, spectral_scan, stylistic_match, historical_ctx]:
    for tgt in [forgery_detect, restoration_check, expert_consult]:
        root.order.add_edge(src, tgt)

# 3. After detection/consultation, do legal & ethics in parallel
for src in [forgery_detect, restoration_check, expert_consult]:
    root.order.add_edge(src, legal_assess)
    root.order.add_edge(src, ethics_screen)

# 4. Then produce the condition report
root.order.add_edge(legal_assess, condition_report)
root.order.add_edge(ethics_screen, condition_report)

# 5. Then certification prep & documentation in parallel
root.order.add_edge(condition_report, cert_prep)
root.order.add_edge(condition_report, documentation)

# 6. Then final approval
root.order.add_edge(cert_prep, final_approval)
root.order.add_edge(documentation, final_approval)

# 7. After final approval choose between conservation or market analysis
root.order.add_edge(final_approval, final_choice)