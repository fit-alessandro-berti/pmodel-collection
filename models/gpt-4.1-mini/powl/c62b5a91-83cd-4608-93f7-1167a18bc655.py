# Generated from: c62b5a91-83cd-4608-93f7-1167a18bc655.json
# Description: This process involves the intricate verification and authentication of historical artifacts before acquisition by a museum. It begins with initial artifact intake and condition assessment, followed by provenance research utilizing multidisciplinary experts. Scientific testing methods such as radiocarbon dating and spectroscopy are employed to validate authenticity. Concurrently, legal clearance and cultural heritage compliance checks are performed to ensure ethical acquisition. The workflow also includes digital documentation, expert committee reviews, and final acquisition approval. Post-approval, artifacts undergo conservation planning and secure storage preparations. Throughout, communication with external stakeholders like historians, legal advisors, and cultural representatives is maintained to ensure transparency and adherence to international standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
Artifact_Intake = Transition(label='Artifact Intake')
Condition_Check = Transition(label='Condition Check')
Provenance_Research = Transition(label='Provenance Research')
Scientific_Testing = Transition(label='Scientific Testing')
Radiocarbon_Dating = Transition(label='Radiocarbon Dating')
Spectroscopy_Scan = Transition(label='Spectroscopy Scan')
Legal_Clearance = Transition(label='Legal Clearance')
Heritage_Compliance = Transition(label='Heritage Compliance')
Digital_Archiving = Transition(label='Digital Archiving')
Expert_Review = Transition(label='Expert Review')
Committee_Vote = Transition(label='Committee Vote')
Acquisition_Approval = Transition(label='Acquisition Approval')
Conservation_Plan = Transition(label='Conservation Plan')
Storage_Setup = Transition(label='Storage Setup')
Stakeholder_Update = Transition(label='Stakeholder Update')

# Scientific Testing partial order: Radiocarbon Dating and Spectroscopy Scan are concurrent subtasks, then Scientific Testing
scientific_subtasks = StrictPartialOrder(nodes=[Radiocarbon_Dating, Spectroscopy_Scan])
# Radiocarbon Dating and Spectroscopy Scan are concurrent, so no edges added
scientific_testing_po = StrictPartialOrder(nodes=[scientific_subtasks, Scientific_Testing])
scientific_testing_po.order.add_edge(scientific_subtasks, Scientific_Testing)

# Legal Clearance and Heritage Compliance are concurrent
legal_heritage_po = StrictPartialOrder(nodes=[Legal_Clearance, Heritage_Compliance])

# Parallel activities after Provenance Research: Scientific Testing and Legal/Heritage checks
# We'll create a partial order with these two concurrent:
post_prov_parallel = StrictPartialOrder(nodes=[scientific_testing_po, legal_heritage_po])

# Post-approval parallel: Conservation Plan and Storage Setup
post_approval_parallel = StrictPartialOrder(nodes=[Conservation_Plan, Storage_Setup])

# Expert Review depends after Digital Archiving, then Committee Vote, then Acquisition Approval
review_order = StrictPartialOrder(nodes=[Digital_Archiving, Expert_Review, Committee_Vote, Acquisition_Approval])
review_order.order.add_edge(Digital_Archiving, Expert_Review)
review_order.order.add_edge(Expert_Review, Committee_Vote)
review_order.order.add_edge(Committee_Vote, Acquisition_Approval)

# Stakeholder Update concurrent throughout - model as concurrent with main flow (concurrent with Expert Review and Committee Vote stages and possible others)
# To simplify, we put Stakeholder Update concurrent with the review order and post_approval_parallel

# Start: Artifact Intake -> Condition Check -> Provenance Research
start_seq = StrictPartialOrder(nodes=[Artifact_Intake, Condition_Check, Provenance_Research])
start_seq.order.add_edge(Artifact_Intake, Condition_Check)
start_seq.order.add_edge(Condition_Check, Provenance_Research)

# After Provenance Research comes the parallel Scientific Testing and Legal/Heritage compliance
# Combine start_seq, post_prov_parallel in sequence:
start_and_parallel = StrictPartialOrder(nodes=[start_seq, post_prov_parallel])
start_and_parallel.order.add_edge(start_seq, post_prov_parallel)

# Next Digital Archiving and review sequence after the parallel checks
start_parallel_and_review = StrictPartialOrder(nodes=[start_and_parallel, review_order])
start_parallel_and_review.order.add_edge(start_and_parallel, review_order)

# Stakeholder Update concurrent with review_order and post_approval_parallel
# Combine review_order and Stakeholder_Update concurrently:
review_and_stakeholder = StrictPartialOrder(nodes=[review_order, Stakeholder_Update])

# Because Stakeholder Update "throughout" is concurrent with major later activities, 
# let's take review_and_stakeholder substitute review_order in main flow

# After acquisition approval, Conservation Plan and Storage Setup parallel
# Sequence from review to post approval parallel
review_and_post = StrictPartialOrder(nodes=[review_and_stakeholder, post_approval_parallel])
review_and_post.order.add_edge(review_and_stakeholder, post_approval_parallel)

# Combine all:
root = StrictPartialOrder(nodes=[start_seq, post_prov_parallel, review_and_stakeholder, post_approval_parallel])
root.order.add_edge(start_seq, post_prov_parallel)
root.order.add_edge(post_prov_parallel, review_and_stakeholder)
root.order.add_edge(review_and_stakeholder, post_approval_parallel)