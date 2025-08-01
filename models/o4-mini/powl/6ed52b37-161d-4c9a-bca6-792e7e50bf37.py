# Generated from: 6ed52b37-161d-4c9a-bca6-792e7e50bf37.json
# Description: This process involves verifying the authenticity and provenance of rare cultural artifacts before acquisition by a museum or private collector. It includes multi-stage scientific testing, historical record analysis, expert consultations across various domains, and coordination with international regulatory agencies. The process ensures comprehensive validation of artifact origin, condition assessment, legal clearance, and ethical sourcing. It incorporates iterative hypothesis refinement, cross-referencing with global databases, and final certification issuance, aiming to prevent fraud and protect cultural heritage while facilitating secure and transparent transactions in the artifact market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
artifact_intake      = Transition(label='Artifact Intake')
initial_survey       = Transition(label='Initial Survey')
material_testing     = Transition(label='Material Testing')
historical_audit     = Transition(label='Historical Audit')
provenance_check     = Transition(label='Provenance Check')
database_query       = Transition(label='Database Query')
condition_report     = Transition(label='Condition Report')
hypothesis_update    = Transition(label='Hypothesis Update')
expert_review        = Transition(label='Expert Review')
ethics_assessment    = Transition(label='Ethics Assessment')
legal_screening      = Transition(label='Legal Screening')
regulatory_liaison   = Transition(label='Regulatory Liaison')
certification_prep   = Transition(label='Certification Prep')
final_validation     = Transition(label='Final Validation')
ownership_transfer   = Transition(label='Ownership Transfer')

# Loop for iterative hypothesis refinement: Material Testing then Hypothesis Update
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[material_testing, hypothesis_update])

# Build the partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    initial_survey,
    loop_node,
    historical_audit,
    provenance_check,
    database_query,
    condition_report,
    expert_review,
    ethics_assessment,
    legal_screening,
    regulatory_liaison,
    certification_prep,
    final_validation,
    ownership_transfer
])

# Define ordering relations
root.order.add_edge(artifact_intake, initial_survey)

# After initial survey, run testing loop and historical audit in parallel
root.order.add_edge(initial_survey, loop_node)
root.order.add_edge(initial_survey, historical_audit)

# Historical branch
root.order.add_edge(historical_audit, provenance_check)
root.order.add_edge(provenance_check, database_query)

# Testing branch and output
root.order.add_edge(loop_node, condition_report)

# Join branches before expert review
root.order.add_edge(condition_report, expert_review)
root.order.add_edge(database_query, expert_review)

# Expert review to ethics assessment
root.order.add_edge(expert_review, ethics_assessment)

# Ethics assessment to both legal and regulatory screening in parallel
root.order.add_edge(ethics_assessment, legal_screening)
root.order.add_edge(ethics_assessment, regulatory_liaison)

# Both screenings must complete before certification prep
root.order.add_edge(legal_screening, certification_prep)
root.order.add_edge(regulatory_liaison, certification_prep)

# Final steps
root.order.add_edge(certification_prep, final_validation)
root.order.add_edge(final_validation, ownership_transfer)