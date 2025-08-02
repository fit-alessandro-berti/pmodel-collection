# Generated from: 4ce95f45-d14e-4994-9620-d3f2aaa494d8.json
# Description: This process involves the intricate verification and authentication of rare historical artifacts sourced from various global locations. It includes provenance research, material analysis, expert consultations, and legal clearance to ensure authenticity and compliance with cultural property laws. The process demands collaboration between historians, scientists, legal experts, and logistics teams to accurately assess, document, and secure each artifact before acquisition or exhibition. Each step must be meticulously recorded to maintain traceability and uphold ethical standards, addressing challenges such as forgery detection, cross-border regulations, and preservation requirements.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
source_artifact = Transition(label='Source Artifact')
initial_inspection = Transition(label='Initial Inspection')

# Provenance Check and Material Testing can happen in parallel after Initial Inspection
provenance_check = Transition(label='Provenance Check')
material_testing = Transition(label='Material Testing')

# Expert Review depends on Provenance Check and Material Testing both
expert_review = Transition(label='Expert Review')

# Legal Clearance depends on Expert Review, including a loop to handle Forgery Analysis before proceeding
legal_clearance = Transition(label='Legal Clearance')
forgery_analysis = Transition(label='Forgery Analysis')

# Loop for legal clearance: execute Legal Clearance, then either exit or Forgery Analysis then loop again
loop_legal = OperatorPOWL(operator=Operator.LOOP, children=[legal_clearance, forgery_analysis])

# Condition Report and Cultural Audit happen in parallel after legal clearance
condition_report = Transition(label='Condition Report')
cultural_audit = Transition(label='Cultural Audit')

# After these two, Transport Planning
transport_planning = Transition(label='Transport Planning')

# Customs Filing and Insurance Setup can be done in parallel after Transport Planning
customs_filing = Transition(label='Customs Filing')
insurance_setup = Transition(label='Insurance Setup')

# Secure Packaging depends on Customs Filing and Insurance Setup
secure_packaging = Transition(label='Secure Packaging')

# Documentation depends on Secure Packaging
documentation = Transition(label='Documentation')

# Final Approval depends on Documentation
final_approval = Transition(label='Final Approval')

# Exhibit Preparation depends on Final Approval
exhibit_preparation = Transition(label='Exhibit Preparation')

# Build the partial order

# Nodes: 
# - source_artifact
# - initial_inspection
# - provenance_check, material_testing (parallel)
# - expert_review
# - loop_legal (loop over legal clearance and forgery analysis)
# - condition_report, cultural_audit (parallel)
# - transport_planning
# - customs_filing, insurance_setup (parallel)
# - secure_packaging
# - documentation
# - final_approval
# - exhibit_preparation

# Create StrictPartialOrder node list
nodes = [source_artifact,
         initial_inspection,
         provenance_check, material_testing,
         expert_review,
         loop_legal,
         condition_report, cultural_audit,
         transport_planning,
         customs_filing, insurance_setup,
         secure_packaging,
         documentation,
         final_approval,
         exhibit_preparation]

root = StrictPartialOrder(nodes=nodes)

# Define order edges according to the dependencies described

root.order.add_edge(source_artifact, initial_inspection)

root.order.add_edge(initial_inspection, provenance_check)
root.order.add_edge(initial_inspection, material_testing)

root.order.add_edge(provenance_check, expert_review)
root.order.add_edge(material_testing, expert_review)

root.order.add_edge(expert_review, loop_legal)  # Loop starts after expert review

root.order.add_edge(loop_legal, condition_report)
root.order.add_edge(loop_legal, cultural_audit)

root.order.add_edge(condition_report, transport_planning)
root.order.add_edge(cultural_audit, transport_planning)

root.order.add_edge(transport_planning, customs_filing)
root.order.add_edge(transport_planning, insurance_setup)

root.order.add_edge(customs_filing, secure_packaging)
root.order.add_edge(insurance_setup, secure_packaging)

root.order.add_edge(secure_packaging, documentation)

root.order.add_edge(documentation, final_approval)

root.order.add_edge(final_approval, exhibit_preparation)