# Generated from: 54f18c52-7824-4427-addd-235ba9f433e9.json
# Description: This process outlines the detailed steps involved in authenticating rare historical artifacts for acquisition by a museum. It begins with initial artifact intake and cataloging, followed by provenance verification through archival research and expert consultations. Scientific analysis includes material composition testing and radiocarbon dating. Parallel activities involve digital imaging and 3D modeling for condition assessment. Subsequently, a multidisciplinary review committee evaluates all gathered evidence to confirm authenticity or flag discrepancies. Final approval triggers secure documentation creation and integration into the museum's digital registry. Each step demands meticulous record-keeping and cross-referencing to ensure the artifact's legitimacy before public exhibition or storage, thereby minimizing risks of fraud or misattribution.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
ArtifactIntake = Transition(label='Artifact Intake')
CatalogEntry = Transition(label='Catalog Entry')

ProvenanceCheck = Transition(label='Provenance Check')
ArchiveResearch = Transition(label='Archive Research')
ExpertConsult = Transition(label='Expert Consult')

MaterialTest = Transition(label='Material Test')
RadiocarbonDate = Transition(label='Radiocarbon Date')

DigitalImaging = Transition(label='Digital Imaging')
ThreeDModeling = Transition(label='3D Modeling')

ConditionReview = Transition(label='Condition Review')

EvidenceCollate = Transition(label='Evidence Collate')
ReviewMeeting = Transition(label='Review Meeting')
AuthenticityVote = Transition(label='Authenticity Vote')

Documentation = Transition(label='Documentation')
RegistryUpdate = Transition(label='Registry Update')

FinalApproval = Transition(label='Final Approval')

# ProvenanceCheck is composed of ArchiveResearch and ExpertConsult in partial order (concurrent)
provenance_nodes = [ArchiveResearch, ExpertConsult]
provenance_po = StrictPartialOrder(nodes=provenance_nodes)
# No order edges, they are concurrent
# ProvenanceCheck is a label for this subprocess, create a PO wrapping these two activities.
# But since we need "Provenance Check" as an activity that encompasses the two, 
# but the instructions say to use exactly those activities.
# So we interpret "Provenance Check" as a single activity, and ArchiveResearch and ExpertConsult as its subactivities done in parallel.
# Because "Provenance Check" is named separately, we'll model ProvenanceCheck as an XOR of ProvenanceCheck and the subactivities? 
# The prompt says "provenance verification through archival research and expert consultations", so likely ArchiveResearch and ExpertConsult are part of ProvenanceCheck.
# So we can make ProvenanceCheck be a partial order consisting of ArchiveResearch and ExpertConsult only,
# or alternatively, treat ProvenanceCheck as a silent transition with ArchiveResearch and ExpertConsult as children.
# But ProvenanceCheck is also part of the main activities list.
# We'll create ProvenanceCheck as a PO with ArchiveResearch and ExpertConsult while labeling it as ProvenanceCheck by a PO named ProvenanceCheck.
# To keep definitions consistent, we'll create a PO named ProvenanceCheckPO and then relate ProvenanceCheck activity before and after it isn't needed,
# just treat ProvenanceCheck as covering the two tasks in parallel as a subprocess named ProvenanceCheckPO.

provenance_check_po = StrictPartialOrder(nodes=[ArchiveResearch, ExpertConsult])

# Scientific analysis partial order: MaterialTest and RadiocarbonDate concurrent
scientific_analysis_po = StrictPartialOrder(nodes=[MaterialTest, RadiocarbonDate])
# no edges => concurrent execution

# Parallel activities: DigitalImaging and 3DModeling
parallel_imaging_po = StrictPartialOrder(nodes=[DigitalImaging, ThreeDModeling])
# no edges => concurrent execution

# Construct provenance verification subprocess including ProvenanceCheck label:
# Since ProvenanceCheck is an activity itself, but we have subactivities Archive Research & Expert Consult,
# One way is to have ProvenanceCheck --> ProvenanceSubPO (ArchiveResearch and ExpertConsult concurrent)
# but this duplicates the activity ProvenanceCheck.
# Another way: treat ProvenanceCheck as a silent node and use ArchiveResearch and ExpertConsult as subactivities instead:
# But "Provenance Check" is in the activity list and supposed to be used.
# We can model ProvenanceCheck as a PO containing ArchiveResearch and ExpertConsult (without ProvenanceCheck node), 
# but the prompt says use exactly those activity labels.
# Alternatively, ProvenanceCheck can be modeled as containing X(ArchiveResearch, ExpertConsult) — but the prompt says parallel, not choice.
# So use partial order with no edges: concurrent activities ArchiveResearch and ExpertConsult.
# Then at higher level, ProvenanceCheck PO node can represent the two activities.
# We'll omit the separate ProvenanceCheck Transition to avoid confusion and only use ArchiveResearch and ExpertConsult in PO.

# To respect activity list, we keep ProvenanceCheck Transition and model ArchiveResearch and ExpertConsult as children in PO after ProvenanceCheck.
# Sequence is: ProvenanceCheck --> parallel ArchiveResearch and ExpertConsult

provenance_sub_po = StrictPartialOrder(nodes=[ArchiveResearch, ExpertConsult])
# no edges => parallel

provenance_po = StrictPartialOrder(nodes=[ProvenanceCheck, provenance_sub_po])
provenance_po.order.add_edge(ProvenanceCheck, provenance_sub_po)

# Now build scientific analysis and parallel imaging and 3D modeling as separate PO's.

# Merge digital imaging and 3D modeling with condition review in sequence:
# As per description, "Parallel activities involve digital imaging and 3D modeling for condition assessment", 
# then "Condition Review" is subsequent.

imaging_po = StrictPartialOrder(nodes=[parallel_imaging_po, ConditionReview])
imaging_po.order.add_edge(parallel_imaging_po, ConditionReview)

# Then Evidence Collate, Review Meeting, Authenticity Vote happen in sequence:

review_po = StrictPartialOrder(nodes=[EvidenceCollate, ReviewMeeting, AuthenticityVote])
review_po.order.add_edge(EvidenceCollate, ReviewMeeting)
review_po.order.add_edge(ReviewMeeting, AuthenticityVote)

# Final Approval triggers Documentation and Registry Update in sequence:

final_doc_po = StrictPartialOrder(nodes=[Documentation, RegistryUpdate])
final_doc_po.order.add_edge(Documentation, RegistryUpdate)

# Final Approval before Documentation etc.

final_approval_po = StrictPartialOrder(nodes=[FinalApproval, final_doc_po])
final_approval_po.order.add_edge(FinalApproval, final_doc_po)

# Now build the main flow:

# Artifact Intake -> Catalog Entry -> Provenance Check (with subactivities) -> Scientific Analysis (concurrent MaterialTest and RadiocarbonDate)
# Scientific Analysis and Imaging PO's are parallel (both after provenance)
# Then after both finish, ConditionReview (already in imaging_po after parallel imaging)
# Evidence Collate -> Review Meeting -> Authenticity Vote
# Final Approval
# Documentation and Registry Update

# We need to merge these parts respecting order:

# First part: Artifact Intake --> Catalog Entry --> Provenance Check PO

start_po = StrictPartialOrder(nodes=[ArtifactIntake, CatalogEntry, provenance_po])
start_po.order.add_edge(ArtifactIntake, CatalogEntry)
start_po.order.add_edge(CatalogEntry, provenance_po)

# Scientific Analysis PO nodes
# material and radiocarbon test parallel:
scientific_analysis_po = StrictPartialOrder(nodes=[MaterialTest, RadiocarbonDate])

# After provenance_check finishes, scientific_analysis and parallel imaging_po run concurrently
# So create a PO with nodes=[scientific_analysis_po, imaging_po]

sci_and_imaging_po = StrictPartialOrder(nodes=[scientific_analysis_po, imaging_po])
# These are parallel, no order edges

# ConditionReview already after parallel imaging steps inside imaging_po

# Next after scientific_analysis_po and imaging_po finish, Evidence Collate starts
# So need order edges: scientific_analysis_po --> EvidenceCollate, imaging_po --> EvidenceCollate

# EvidenceCollate is first in review_po
# review_po.order is EvidenceCollate->ReviewMeeting, ReviewMeeting->AuthenticityVote

# We need to combine sci_and_imaging_po and review_po in one PO with edges:

# So create a big PO with nodes=[start_po, sci_and_imaging_po, review_po, final_approval_po]

root = StrictPartialOrder(
    nodes=[start_po, scientific_analysis_po, imaging_po, review_po, final_approval_po]
)

# But scientific_analysis_po and imaging_po are already inside sci_and_imaging_po — correct that

root = StrictPartialOrder(
    nodes=[start_po, sci_and_imaging_po, review_po, final_approval_po]
)

# Add edges from start_po to sci_and_imaging_po:

root.order.add_edge(start_po, sci_and_imaging_po)

# Add edges from sci_and_imaging_po to review_po

root.order.add_edge(sci_and_imaging_po, review_po)

# Add edges from review_po to final_approval_po

root.order.add_edge(review_po, final_approval_po)

# Final model stored in 'root'