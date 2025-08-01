# Generated from: eceb2fab-1690-40f3-8ace-ff7a5cbeee79.json
# Description: This process involves the identification, evaluation, and meticulous restoration of antique assets for resale or exhibition. It begins with provenance research and condition assessment, followed by careful dismantling, cleaning, and material analysis to determine appropriate restoration techniques. Specialists perform stabilization, reconstruction, and aesthetic enhancement while preserving originality. Each restoration phase is documented for authenticity and compliance. Finally, the asset undergoes quality validation, market valuation, and targeted marketing before delivery to collectors or museums, ensuring historical value and investment potential are maintained throughout the process.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
ProvenanceCheck = Transition(label='Provenance Check')
ConditionScan = Transition(label='Condition Scan')
MaterialTest = Transition(label='Material Test')
Disassembly = Transition(label='Disassembly')
SurfaceClean = Transition(label='Surface Clean')
StabilizeParts = Transition(label='Stabilize Parts')
StructuralRepair = Transition(label='Structural Repair')
Reconstruction = Transition(label='Reconstruction')
FinishMatch = Transition(label='Finish Match')
Documentation = Transition(label='Documentation')
QualityAudit = Transition(label='Quality Audit')
Valuation = Transition(label='Valuation')
MarketAnalysis = Transition(label='Market Analysis')
TargetOutreach = Transition(label='Target Outreach')
DeliveryPrep = Transition(label='Delivery Prep')
ClientFeedback = Transition(label='Client Feedback')

# Define sub-partial orders based on phases:

# Phase 1: Provenance Check and Condition Scan (initial phase)
phase1 = StrictPartialOrder(nodes=[ProvenanceCheck, ConditionScan])
phase1.order.add_edge(ProvenanceCheck, ConditionScan)

# Phase 2: Disassembly, Surface Clean, Material Test in partial order:
# Disassembly -> Surface Clean and Material Test concurrent after Surface Clean 
phase2 = StrictPartialOrder(nodes=[Disassembly, SurfaceClean, MaterialTest])
phase2.order.add_edge(Disassembly, SurfaceClean)
phase2.order.add_edge(SurfaceClean, MaterialTest)

# Phase 3: Stabilize Parts, Structural Repair, Reconstruction, Finish Match
# According to the description, specialists do Stabilize, Reconstruction, and Finish Match preserving originality.
# Stabilize Parts first, then Structural Repair and Reconstruction and Finish Match in parallel
# But Reconstruction and Finish Match depend on Structural Repair. So:
#
# Stabilize Parts -> Structural Repair -> (Reconstruction and Finish Match concurrent)
phase3 = StrictPartialOrder(nodes=[StabilizeParts, StructuralRepair, Reconstruction, FinishMatch])
phase3.order.add_edge(StabilizeParts, StructuralRepair)
phase3.order.add_edge(StructuralRepair, Reconstruction)
phase3.order.add_edge(StructuralRepair, FinishMatch)

# Phase 4: Documentation after each restoration phase
# It should document StabilizeParts, StructuralRepair, Reconstruction, FinishMatch phases
# So documentation after all these? Or after each? 
# We'll model Documentation after Finish Match only for simplicity.
# Could also be parallel or sequential. We'll assume sequential after FinishMatch:
phase4 = StrictPartialOrder(nodes=[FinishMatch, Documentation])
phase4.order.add_edge(FinishMatch, Documentation)

# Phase 5: Quality Audit
phase5 = StrictPartialOrder(nodes=[Documentation, QualityAudit])
phase5.order.add_edge(Documentation, QualityAudit)

# Phase 6: Valuation, Market Analysis, Target Outreach (before delivery)
# These three likely partially ordered. Description suggests these steps: 
# Quality Audit -> Valuation -> Market Analysis -> Target Outreach
phase6 = StrictPartialOrder(nodes=[QualityAudit, Valuation, MarketAnalysis, TargetOutreach])
phase6.order.add_edge(QualityAudit, Valuation)
phase6.order.add_edge(Valuation, MarketAnalysis)
phase6.order.add_edge(MarketAnalysis, TargetOutreach)

# Phase 7: Delivery Prep and Client Feedback after Target Outreach
phase7 = StrictPartialOrder(nodes=[TargetOutreach, DeliveryPrep, ClientFeedback])
phase7.order.add_edge(TargetOutreach, DeliveryPrep)
phase7.order.add_edge(DeliveryPrep, ClientFeedback)

# Compose all into one final StrictPartialOrder with proper ordering:
# phase1 -> phase2 -> phase3 -> phase4 -> phase5 -> phase6 -> phase7
nodes = [phase1, phase2, phase3, phase4, phase5, phase6, phase7]

root = StrictPartialOrder(nodes=nodes)
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, phase3)
root.order.add_edge(phase3, phase4)
root.order.add_edge(phase4, phase5)
root.order.add_edge(phase5, phase6)
root.order.add_edge(phase6, phase7)