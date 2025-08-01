# Generated from: c62b5a91-83cd-4608-93f7-1167a18bc655.json
# Description: This process involves the intricate verification and authentication of historical artifacts before acquisition by a museum. It begins with initial artifact intake and condition assessment, followed by provenance research utilizing multidisciplinary experts. Scientific testing methods such as radiocarbon dating and spectroscopy are employed to validate authenticity. Concurrently, legal clearance and cultural heritage compliance checks are performed to ensure ethical acquisition. The workflow also includes digital documentation, expert committee reviews, and final acquisition approval. Post-approval, artifacts undergo conservation planning and secure storage preparations. Throughout, communication with external stakeholders like historians, legal advisors, and cultural representatives is maintained to ensure transparency and adherence to international standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activity transitions
artifact_intake    = Transition(label="Artifact Intake")
condition_check    = Transition(label="Condition Check")
provenance_research = Transition(label="Provenance Research")
scientific_testing  = Transition(label="Scientific Testing")
radiocarbon_dating  = Transition(label="Radiocarbon Dating")
spectroscopy_scan   = Transition(label="Spectroscopy Scan")
legal_clearance     = Transition(label="Legal Clearance")
heritage_compliance = Transition(label="Heritage Compliance")
digital_archiving   = Transition(label="Digital Archiving")
expert_review       = Transition(label="Expert Review")
committee_vote      = Transition(label="Committee Vote")
acquisition_approval= Transition(label="Acquisition Approval")
conservation_plan   = Transition(label="Conservation Plan")
storage_setup       = Transition(label="Storage Setup")
stakeholder_update  = Transition(label="Stakeholder Update")

# Build the partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    condition_check,
    provenance_research,
    scientific_testing,
    radiocarbon_dating,
    spectroscopy_scan,
    legal_clearance,
    heritage_compliance,
    digital_archiving,
    expert_review,
    committee_vote,
    acquisition_approval,
    conservation_plan,
    storage_setup,
    stakeholder_update
])

# Sequence: Intake -> Condition Check -> Provenance Research
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(condition_check, provenance_research)

# After Provenance Research: spawn Scientific Testing, Legal Clearance, Heritage Compliance (all concurrent)
root.order.add_edge(provenance_research, scientific_testing)
root.order.add_edge(provenance_research, legal_clearance)
root.order.add_edge(provenance_research, heritage_compliance)

# Under Scientific Testing: Radiocarbon Dating and Spectroscopy Scan (concurrent)
root.order.add_edge(scientific_testing, radiocarbon_dating)
root.order.add_edge(scientific_testing, spectroscopy_scan)

# After all testing/legal/heritage: go to Digital Archiving
root.order.add_edge(radiocarbon_dating, digital_archiving)
root.order.add_edge(spectroscopy_scan, digital_archiving)
root.order.add_edge(legal_clearance, digital_archiving)
root.order.add_edge(heritage_compliance, digital_archiving)

# Then Expert Review -> Committee Vote -> Acquisition Approval
root.order.add_edge(digital_archiving, expert_review)
root.order.add_edge(expert_review, committee_vote)
root.order.add_edge(committee_vote, acquisition_approval)

# After approval: Conservation Plan and Storage Setup (concurrent)
root.order.add_edge(acquisition_approval, conservation_plan)
root.order.add_edge(acquisition_approval, storage_setup)

# Stakeholder updates are fully concurrent (no edges to/from stakeholder_update)
# (They can happen anytime in the process)

# `root` now holds the complete POWL model