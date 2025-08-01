# Generated from: f21c1481-c6ba-490a-8659-af67394d09af.json
# Description: This process involves the detailed verification and authentication of historical artifacts sourced from multiple private collections and public auctions worldwide. It includes multidisciplinary scientific testing, provenance research, legal ownership validation, and ethical compliance checks before final acquisition or exhibition. The process ensures that artifacts are genuine, legally obtained, and preserved according to international standards, involving coordination among historians, scientists, legal teams, and curators. Complex logistics and secure transport arrangements are also integral to maintain artifact integrity throughout the process.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
collection_survey = Transition(label='Collection Survey')
provenance_check = Transition(label='Provenance Check')
legal_review = Transition(label='Legal Review')
scientific_test = Transition(label='Scientific Test')
material_analysis = Transition(label='Material Analysis')
ownership_audit = Transition(label='Ownership Audit')
ethical_screening = Transition(label='Ethical Screening')
condition_report = Transition(label='Condition Report')
expert_consultation = Transition(label='Expert Consultation')
transport_planning = Transition(label='Transport Planning')
secure_packing = Transition(label='Secure Packing')
customs_clearance = Transition(label='Customs Clearance')
insurance_setup = Transition(label='Insurance Setup')
exhibit_preparation = Transition(label='Exhibit Preparation')
final_approval = Transition(label='Final Approval')
skip = SilentTransition()

# Scientific testing partial order (scientific_test and material_analysis concurrent)
scientific_partial = StrictPartialOrder(nodes=[scientific_test, material_analysis])  # concurrent

# Legal and ethical checks partial order (legal_review --> ownership_audit --> ethical_screening)
legal_ethics_po = StrictPartialOrder(
    nodes=[legal_review, ownership_audit, ethical_screening]
)
legal_ethics_po.order.add_edge(legal_review, ownership_audit)
legal_ethics_po.order.add_edge(ownership_audit, ethical_screening)

# Condition and expert consultation partial order (condition_report <--> expert_consultation concurrent)
condition_expert_po = StrictPartialOrder(nodes=[condition_report, expert_consultation])  # concurrent

# Secure transport partial order (transport_planning --> secure_packing --> customs_clearance)
transport_po = StrictPartialOrder(
    nodes=[transport_planning, secure_packing, customs_clearance]
)
transport_po.order.add_edge(transport_planning, secure_packing)
transport_po.order.add_edge(secure_packing, customs_clearance)

# Insurance setup and exhibit preparation (insurance_setup --> exhibit_preparation)
insurance_exhibit_po = StrictPartialOrder(
    nodes=[insurance_setup, exhibit_preparation]
)
insurance_exhibit_po.order.add_edge(insurance_setup, exhibit_preparation)

# Assemble verification phase: provenance_check and legal_ethics_po concurrent
verification_phase = StrictPartialOrder(
    nodes=[provenance_check, legal_ethics_po]
)  # concurrent
# Add edges to connect all nodes of legal_ethics_po after provenance_check
verification_phase.order.add_edge(provenance_check, legal_ethics_po)

# Assemble scientific phase: scientific_partial and condition_expert_po concurrent
scientific_phase = StrictPartialOrder(
    nodes=[scientific_partial, condition_expert_po]
)  # concurrent

# Assemble pre-transport phase: verification_phase and scientific_phase concurrent
pre_transport_phase = StrictPartialOrder(
    nodes=[verification_phase, scientific_phase]
)  # concurrent

# Assemble transport phase: transport_po and insurance_exhibit_po concurrent
transport_phase = StrictPartialOrder(
    nodes=[transport_po, insurance_exhibit_po]
)  # concurrent

# Final partial order:
# collection_survey --> pre_transport_phase --> transport_phase --> final_approval
root = StrictPartialOrder(
    nodes=[collection_survey, pre_transport_phase, transport_phase, final_approval]
)
root.order.add_edge(collection_survey, pre_transport_phase)
root.order.add_edge(pre_transport_phase, transport_phase)
root.order.add_edge(transport_phase, final_approval)