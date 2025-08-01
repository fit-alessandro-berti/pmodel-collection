# Generated from: 4ce95f45-d14e-4994-9620-d3f2aaa494d8.json
# Description: This process involves the intricate verification and authentication of rare historical artifacts sourced from various global locations. It includes provenance research, material analysis, expert consultations, and legal clearance to ensure authenticity and compliance with cultural property laws. The process demands collaboration between historians, scientists, legal experts, and logistics teams to accurately assess, document, and secure each artifact before acquisition or exhibition. Each step must be meticulously recorded to maintain traceability and uphold ethical standards, addressing challenges such as forgery detection, cross-border regulations, and preservation requirements.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# define activities
src_artifact       = Transition(label='Source Artifact')
initial_inspection = Transition(label='Initial Inspection')
provenance_check   = Transition(label='Provenance Check')
material_testing   = Transition(label='Material Testing')
condition_report   = Transition(label='Condition Report')
cultural_audit     = Transition(label='Cultural Audit')
expert_review      = Transition(label='Expert Review')
forgery_analysis   = Transition(label='Forgery Analysis')
legal_clearance    = Transition(label='Legal Clearance')
documentation      = Transition(label='Documentation')
insurance_setup    = Transition(label='Insurance Setup')
customs_filing     = Transition(label='Customs Filing')
secure_packaging   = Transition(label='Secure Packaging')
transport_planning = Transition(label='Transport Planning')
final_approval     = Transition(label='Final Approval')
exhibit_preparation= Transition(label='Exhibit Preparation')

# build the partial order
root = StrictPartialOrder(nodes=[
    src_artifact,
    initial_inspection,
    provenance_check,
    material_testing,
    condition_report,
    cultural_audit,
    expert_review,
    forgery_analysis,
    legal_clearance,
    documentation,
    insurance_setup,
    customs_filing,
    secure_packaging,
    transport_planning,
    final_approval,
    exhibit_preparation
])

# define control dependencies
root.order.add_edge(src_artifact,       initial_inspection)

root.order.add_edge(initial_inspection, provenance_check)
root.order.add_edge(initial_inspection, material_testing)
root.order.add_edge(initial_inspection, condition_report)
root.order.add_edge(initial_inspection, cultural_audit)

root.order.add_edge(provenance_check,   expert_review)
root.order.add_edge(material_testing,   expert_review)
root.order.add_edge(condition_report,   expert_review)
root.order.add_edge(cultural_audit,     expert_review)

root.order.add_edge(expert_review,      forgery_analysis)
root.order.add_edge(expert_review,      legal_clearance)

root.order.add_edge(forgery_analysis,   documentation)
root.order.add_edge(legal_clearance,    documentation)

root.order.add_edge(documentation,      insurance_setup)
root.order.add_edge(documentation,      customs_filing)
root.order.add_edge(documentation,      secure_packaging)

root.order.add_edge(insurance_setup,    transport_planning)
root.order.add_edge(customs_filing,     transport_planning)
root.order.add_edge(secure_packaging,   transport_planning)

root.order.add_edge(transport_planning, final_approval)
root.order.add_edge(final_approval,     exhibit_preparation)