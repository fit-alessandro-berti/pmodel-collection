# Generated from: 83949f83-41f0-4238-9d5f-75e2b1c86095.json
# Description: This process outlines the multi-disciplinary steps involved in authenticating historical artifacts for a museum acquisition. It begins with preliminary research and provenance verification, followed by scientific analysis including material composition and radiocarbon dating. Concurrently, expert stylistic evaluation and comparative studies are performed. Legal clearance and export permits are secured, while conservation specialists assess restoration needs. The artifact's digital archiving and cataloging are completed before final acquisition approval. Throughout, risk assessments and stakeholder communications ensure integrity and compliance with international regulations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
preliminary_research = Transition(label='Preliminary Research')
provenance_check = Transition(label='Provenance Check')
material_analysis = Transition(label='Material Analysis')
radiocarbon_test = Transition(label='Radiocarbon Test')
stylistic_review = Transition(label='Stylistic Review')
comparative_study = Transition(label='Comparative Study')
legal_clearance = Transition(label='Legal Clearance')
export_permit = Transition(label='Export Permit')
conservation_eval = Transition(label='Conservation Eval')
restoration_plan = Transition(label='Restoration Plan')
risk_assessment = Transition(label='Risk Assessment')
stakeholder_sync = Transition(label='Stakeholder Sync')
digital_archive = Transition(label='Digital Archive')
catalog_entry = Transition(label='Catalog Entry')
acquisition_vote = Transition(label='Acquisition Vote')

# Model scientific analysis as a partial order: Material Analysis --> Radiocarbon Test
scientific_analysis = StrictPartialOrder(nodes=[material_analysis, radiocarbon_test])
scientific_analysis.order.add_edge(material_analysis, radiocarbon_test)

# Model expert evaluation concurrently: Stylistic Review and Comparative Study concurrent
expert_evaluation = StrictPartialOrder(nodes=[stylistic_review, comparative_study])
# no edges, concurrent

# Model legal permits as partial order: Legal Clearance --> Export Permit
legal_permits = StrictPartialOrder(nodes=[legal_clearance, export_permit])
legal_permits.order.add_edge(legal_clearance, export_permit)

# Model conservation steps as partial order: Conservation Eval --> Restoration Plan
conservation = StrictPartialOrder(nodes=[conservation_eval, restoration_plan])
conservation.order.add_edge(conservation_eval, restoration_plan)

# Now concurrent activities during or after scientific and expert evaluations:
# Combine scientific_analysis and expert_evaluation concurrently
science_and_expert = StrictPartialOrder(
    nodes=[scientific_analysis, expert_evaluation]
)
# no order edges between them so concurrent

# Concurrent other activities related to risk and stakeholder communication
risk_and_stakeholder = StrictPartialOrder(nodes=[risk_assessment, stakeholder_sync])
# no edges: concurrent

# After the concurrent blocks of science+expert and legal_permits + conservation + risk/stakeholder:
# we combine all concurrent blocks

# All concurrent nodes after provenance check:
concurrent_nodes_after_provenance = StrictPartialOrder(
    nodes=[science_and_expert, legal_permits, conservation, risk_and_stakeholder]
)
# no edges between them - fully concurrent

# Digital Archive and Catalog Entry done before final Acquisition Vote, in order
final_archiving = StrictPartialOrder(nodes=[digital_archive, catalog_entry])
final_archiving.order.add_edge(digital_archive, catalog_entry)

# Final after archiving: Acquisition Vote
final_sequence = StrictPartialOrder(nodes=[final_archiving, acquisition_vote])
final_sequence.order.add_edge(final_archiving, acquisition_vote)

# Partial order from Preliminary Research --> Provenance Check
initial_sequence = StrictPartialOrder(nodes=[preliminary_research, provenance_check])
initial_sequence.order.add_edge(preliminary_research, provenance_check)

# Then provenance_check --> concurrent activities
initial_to_concurrent = StrictPartialOrder(
    nodes=[initial_sequence, concurrent_nodes_after_provenance]
)
initial_to_concurrent.order.add_edge(initial_sequence, concurrent_nodes_after_provenance)

# concurrent activities --> final archiving & acquisition_vote
full_process = StrictPartialOrder(
    nodes=[initial_to_concurrent, final_sequence]
)
full_process.order.add_edge(initial_to_concurrent, final_sequence)

# root is the full process
root = full_process