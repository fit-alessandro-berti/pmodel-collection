# Generated from: 83701a0c-9c83-4db6-9381-7e2721291820.json
# Description: This process outlines the steps involved in authenticating rare historical artifacts for museum acquisition. It begins with initial appraisal and provenance research, followed by material analysis and expert consultations. The workflow incorporates unconventional activities such as multispectral imaging and isotope testing to verify origin. Legal compliance checks and ethical sourcing evaluations are included before final authentication. Documentation and digital archiving ensure traceability. The process concludes with a presentation to the acquisition committee and secure transport arrangements, ensuring the artifact's integrity is maintained throughout the workflow.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
initial_appraisal   = Transition(label='Initial Appraisal')
provenance_check    = Transition(label='Provenance Check')
material_sampling   = Transition(label='Material Sampling')
isotope_testing     = Transition(label='Isotope Testing')
imaging_scan        = Transition(label='Imaging Scan')
expert_review       = Transition(label='Expert Review')
condition_report    = Transition(label='Condition Report')
historical_context  = Transition(label='Historical Context')
ethics_audit        = Transition(label='Ethics Audit')
legal_verify        = Transition(label='Legal Verify')
digital_archive     = Transition(label='Digital Archive')
acquisition_pitch   = Transition(label='Acquisition Pitch')
security_clearance  = Transition(label='Security Clearance')
transport_prep      = Transition(label='Transport Prep')
final_approval      = Transition(label='Final Approval')

# Build the partial order
root = StrictPartialOrder(nodes=[
    initial_appraisal,
    provenance_check,
    material_sampling,
    isotope_testing,
    imaging_scan,
    expert_review,
    condition_report,
    historical_context,
    ethics_audit,
    legal_verify,
    digital_archive,
    acquisition_pitch,
    security_clearance,
    transport_prep,
    final_approval
])

# Order dependencies
root.order.add_edge(initial_appraisal, provenance_check)
root.order.add_edge(provenance_check, material_sampling)

# Material analysis (sampling → (isotope & imaging) → expert review)
root.order.add_edge(material_sampling, isotope_testing)
root.order.add_edge(material_sampling, imaging_scan)
root.order.add_edge(isotope_testing, expert_review)
root.order.add_edge(imaging_scan, expert_review)

# Documentation before compliance
root.order.add_edge(expert_review, condition_report)
root.order.add_edge(expert_review, historical_context)

# Compliance evaluations (after both reports)
root.order.add_edge(condition_report, ethics_audit)
root.order.add_edge(historical_context, ethics_audit)
root.order.add_edge(condition_report, legal_verify)
root.order.add_edge(historical_context, legal_verify)

# Archiving after compliance
root.order.add_edge(ethics_audit, digital_archive)
root.order.add_edge(legal_verify, digital_archive)

# Final steps: pitch, clearance, transport, approval
root.order.add_edge(digital_archive, acquisition_pitch)
root.order.add_edge(acquisition_pitch, security_clearance)
root.order.add_edge(security_clearance, transport_prep)
root.order.add_edge(transport_prep, final_approval)