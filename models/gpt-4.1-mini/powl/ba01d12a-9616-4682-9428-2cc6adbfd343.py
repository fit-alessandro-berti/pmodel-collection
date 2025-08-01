# Generated from: ba01d12a-9616-4682-9428-2cc6adbfd343.json
# Description: This process manages the end-to-end supply chain for handcrafted artisan goods, integrating unique sourcing methods, bespoke quality checks, and personalized logistics. It begins with raw material scouting in remote locations, followed by artisan selection based on skill and style alignment. Materials undergo custom treatment before distribution to workshops. Each artisan crafts unique pieces verified through multi-stage quality audits involving both automated sensors and expert appraisal. Finished goods are then personalized with client-specific branding and packed using eco-friendly methods. Finally, logistics coordination ensures delivery via specialty carriers that maintain product integrity and cultural authenticity, while gathering consumer feedback for continuous process refinement. This atypical supply chain blends traditional craftsmanship with modern technology and sustainability principles, requiring careful coordination of diverse activities to maintain product uniqueness and market appeal.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities as transitions
MaterialScout = Transition(label='Material Scout')
ArtisanSelect = Transition(label='Artisan Select')
MaterialTreat = Transition(label='Material Treat')
WorkshopAssign = Transition(label='Workshop Assign')
CraftMonitor = Transition(label='Craft Monitor')
QualityAudit = Transition(label='Quality Audit')
SensorCheck = Transition(label='Sensor Check')
ExpertReview = Transition(label='Expert Review')
BrandPersonalize = Transition(label='Brand Personalize')
EcoPack = Transition(label='Eco Pack')
CarrierSelect = Transition(label='Carrier Select')
DeliverySchedule = Transition(label='Delivery Schedule')
IntegrityCheck = Transition(label='Integrity Check')
FeedbackGather = Transition(label='Feedback Gather')
ProcessRefine = Transition(label='Process Refine')
MarketAlign = Transition(label='Market Align')

# Model the multi-stage Quality Audit as a partial order:
# QualityAudit --> {SensorCheck, ExpertReview} concurrent after QualityAudit
QualityAuditPhase = StrictPartialOrder(
    nodes=[QualityAudit, SensorCheck, ExpertReview]
)
QualityAuditPhase.order.add_edge(QualityAudit, SensorCheck)
QualityAuditPhase.order.add_edge(QualityAudit, ExpertReview)
# SensorCheck and ExpertReview are concurrent (no order edge between them)

# Assemble the crafting part:
# WorkshopAssign --> CraftMonitor --> QualityAuditPhase
CraftQualityPart = StrictPartialOrder(
    nodes=[WorkshopAssign, CraftMonitor, QualityAuditPhase]
)
CraftQualityPart.order.add_edge(WorkshopAssign, CraftMonitor)
CraftQualityPart.order.add_edge(CraftMonitor, QualityAuditPhase)

# Personalization and packing partial order (BrandPersonalize concurrent with EcoPack?)
# Usually personalization before packing, so chain: BrandPersonalize --> EcoPack
PersonalizationPacking = StrictPartialOrder(
    nodes=[BrandPersonalize, EcoPack]
)
PersonalizationPacking.order.add_edge(BrandPersonalize, EcoPack)

# Logistics coordination partial order:
# CarrierSelect --> DeliverySchedule --> IntegrityCheck
LogisticsCoordination = StrictPartialOrder(
    nodes=[CarrierSelect, DeliverySchedule, IntegrityCheck]
)
LogisticsCoordination.order.add_edge(CarrierSelect, DeliverySchedule)
LogisticsCoordination.order.add_edge(DeliverySchedule, IntegrityCheck)

# Feedback and process refinement loop:
# FeedbackGather --> ProcessRefine --> (loop back to FeedbackGather or exit)
FeedbackRefineLoop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        FeedbackGather,
        ProcessRefine
    ]
)
# Loop semantics: execute FeedbackGather; then choose exit or ProcessRefine + FeedbackGather again.

# Final Market Alignment activity after loop (assumed last)
# Integrate the entire model as partial order:
# MaterialScout --> ArtisanSelect --> MaterialTreat --> CraftQualityPart --> PersonalizationPacking --> LogisticsCoordination --> FeedbackRefineLoop --> MarketAlign

root = StrictPartialOrder(
    nodes=[
        MaterialScout,
        ArtisanSelect,
        MaterialTreat,
        CraftQualityPart,
        PersonalizationPacking,
        LogisticsCoordination,
        FeedbackRefineLoop,
        MarketAlign
    ]
)

root.order.add_edge(MaterialScout, ArtisanSelect)
root.order.add_edge(ArtisanSelect, MaterialTreat)
root.order.add_edge(MaterialTreat, CraftQualityPart)
root.order.add_edge(CraftQualityPart, PersonalizationPacking)
root.order.add_edge(PersonalizationPacking, LogisticsCoordination)
root.order.add_edge(LogisticsCoordination, FeedbackRefineLoop)
root.order.add_edge(FeedbackRefineLoop, MarketAlign)