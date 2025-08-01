# Generated from: 0118959c-dea9-49d7-b296-7aee7e449369.json
# Description: This process governs the detailed restoration of valuable antiques, combining historical research, material analysis, and delicate repair techniques to preserve authenticity while enhancing structural integrity. It involves documentation, condition assessment, sourcing period-appropriate materials, and employing specialized cleaning and consolidation methods. Experts coordinate with conservation scientists to ensure reversible interventions, aesthetic fidelity, and compliance with legal and ethical standards. The workflow also includes digital archiving of restoration stages and client consultations to balance preservation goals with market value considerations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity
ItemSurvey = Transition(label='Item Survey')
HistoryCheck = Transition(label='History Check')
MaterialTest = Transition(label='Material Test')
DamageMap = Transition(label='Damage Map')
SourceParts = Transition(label='Source Parts')
CleanSurface = Transition(label='Clean Surface')
StabilizeBase = Transition(label='Stabilize Base')
RepairJoints = Transition(label='Repair Joints')
RetouchPaint = Transition(label='Retouch Paint')
ConsolidateWood = Transition(label='Consolidate Wood')
DocumentChanges = Transition(label='Document Changes')
DigitalArchive = Transition(label='Digital Archive')
ClientReview = Transition(label='Client Review')
LegalVerify = Transition(label='Legal Verify')
FinalPolish = Transition(label='Final Polish')
QualityAudit = Transition(label='Quality Audit')
ShippingPrep = Transition(label='Shipping Prep')

# Partial order of research and assessment phase
research_assess = StrictPartialOrder(nodes=[
    ItemSurvey,
    HistoryCheck,
    MaterialTest,
    DamageMap
])
research_assess.order.add_edge(ItemSurvey, HistoryCheck)
research_assess.order.add_edge(ItemSurvey, MaterialTest)
research_assess.order.add_edge(ItemSurvey, DamageMap)

# Sourcing materials after research & assessment
sourcing = SourceParts

# Cleaning and consolidation methods after sourcing
clean_and_stabilize = StrictPartialOrder(nodes=[
    CleanSurface,
    StabilizeBase,
    ConsolidateWood
])
# These three can be concurrent (no order)

# Repair and retouch phase (these are sequential)
repair_phase = StrictPartialOrder(nodes=[
    RepairJoints,
    RetouchPaint
])
repair_phase.order.add_edge(RepairJoints, RetouchPaint)

# Documentation and archiving can be concurrent but after repair phase
doc_archive = StrictPartialOrder(nodes=[
    DocumentChanges,
    DigitalArchive
])
# no order between these two

# Coordination and verification: LegalVerify and ClientReview can be done in parallel
coordination = StrictPartialOrder(nodes=[
    LegalVerify,
    ClientReview
])
# no edge between these two

# Final polish and quality audit sequential
final_check = StrictPartialOrder(nodes=[
    FinalPolish,
    QualityAudit
])
final_check.order.add_edge(FinalPolish, QualityAudit)

# Shipping prep after all
# Compose the entire order:

# Step 1: Research and assess
# Step 2: Source parts
# Step 3: Clean and stabilize (concurrent)
# Step 4: Repair phase sequential
# Step 5: Documentation and archiving concurrent
# Step 6: Coordination (legal & client) concurrent
# Step 7: Final check sequential
# Step 8: Shipping prep

# Combine clean_and_stabilize and repair to one PO where repair after both clean+stabilize done:
step3_4 = StrictPartialOrder(nodes=[clean_and_stabilize, repair_phase])
step3_4.order.add_edge(clean_and_stabilize, repair_phase)

# Combine doc_archive and coordination concurrent:
step5_6 = StrictPartialOrder(nodes=[doc_archive, coordination])
# no order edges -> concurrent

# Combine all steps in order:
root = StrictPartialOrder(nodes=[
    research_assess,
    sourcing,
    step3_4,
    step5_6,
    final_check,
    ShippingPrep
])

root.order.add_edge(research_assess, sourcing)
root.order.add_edge(sourcing, step3_4)
root.order.add_edge(step3_4, step5_6)
root.order.add_edge(step5_6, final_check)
root.order.add_edge(final_check, ShippingPrep)