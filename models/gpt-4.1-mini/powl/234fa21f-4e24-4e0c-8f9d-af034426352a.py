# Generated from: 234fa21f-4e24-4e0c-8f9d-af034426352a.json
# Description: This process involves the planning, construction, and operational setup of a multi-layered urban vertical farm within a repurposed commercial building. It begins with site analysis and environmental assessment, followed by structural modifications and installation of hydroponic systems. Subsequent activities include climate control calibration, nutrient solution preparation, seed selection and planting, automated monitoring integration, and workforce training. The process concludes with trial harvests, quality control assessments, and adjustments to optimize yield while minimizing resource consumption and environmental impact in a dense urban setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# define transitions
SiteSurvey = Transition(label='Site Survey')
StructuralCheck = Transition(label='Structural Check')
Permitting = Transition(label='Permitting')
HydroSetup = Transition(label='Hydro Setup')
ClimateSetup = Transition(label='Climate Setup')
NutrientMix = Transition(label='Nutrient Mix')
SeedSelection = Transition(label='Seed Selection')
Planting = Transition(label='Planting')
SensorInstall = Transition(label='Sensor Install')
AutomationConfig = Transition(label='Automation Config')
StaffHiring = Transition(label='Staff Hiring')
Training = Transition(label='Training')
TrialHarvest = Transition(label='Trial Harvest')
QualityCheck = Transition(label='Quality Check')
YieldReview = Transition(label='Yield Review')
ResourceAudit = Transition(label='Resource Audit')

# Phase 1: Site analysis and environmental assessment: Site Survey --> Structural Check --> Permitting
phase1 = StrictPartialOrder(nodes=[SiteSurvey, StructuralCheck, Permitting])
phase1.order.add_edge(SiteSurvey, StructuralCheck)
phase1.order.add_edge(StructuralCheck, Permitting)

# Phase 2: Structural modifications and installation of hydroponic systems: Hydro Setup
phase2 = HydroSetup

# Phase 3: Climate control calibration, nutrient solution preparation
phase3 = StrictPartialOrder(nodes=[ClimateSetup, NutrientMix])
# No order specified, can be concurrent

# Phase 4: Seed selection and planting
phase4 = StrictPartialOrder(nodes=[SeedSelection, Planting])
phase4.order.add_edge(SeedSelection, Planting)

# Phase 5: Automated monitoring integration (Sensor Install --> Automation Config)
phase5 = StrictPartialOrder(nodes=[SensorInstall, AutomationConfig])
phase5.order.add_edge(SensorInstall, AutomationConfig)

# Phase 6: Workforce training (Staff Hiring --> Training)
phase6 = StrictPartialOrder(nodes=[StaffHiring, Training])
phase6.order.add_edge(StaffHiring, Training)

# Assemble phases 2 to 6 into a partial order (Hydro Setup --> phase3 --> phase4 --> phase5 --> phase6)
phases2to6 = StrictPartialOrder(nodes=[phase2, phase3, phase4, phase5, phase6])
phases2to6.order.add_edge(phase2, phase3)
phases2to6.order.add_edge(phase3, phase4)
phases2to6.order.add_edge(phase4, phase5)
phases2to6.order.add_edge(phase5, phase6)

# Phase 7: Trial harvest, quality check, yield review, resource audit
# Trial Harvest --> Quality Check --> Yield Review --> Resource Audit
phase7 = StrictPartialOrder(nodes=[TrialHarvest, QualityCheck, YieldReview, ResourceAudit])
phase7.order.add_edge(TrialHarvest, QualityCheck)
phase7.order.add_edge(QualityCheck, YieldReview)
phase7.order.add_edge(YieldReview, ResourceAudit)

# Full process:
# phase1 --> phases2to6 --> phase7
root = StrictPartialOrder(nodes=[phase1, phases2to6, phase7])
root.order.add_edge(phase1, phases2to6)
root.order.add_edge(phases2to6, phase7)