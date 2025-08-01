# Generated from: 47809530-bd4c-40d7-a8d8-2d5a068251c4.json
# Description: This process outlines the end-to-end setup of an urban vertical farming system within a repurposed industrial building. It begins with site evaluation and structural reinforcement, followed by installation of hydroponic racks, climate control units, and automated nutrient delivery systems. Subsequent activities include sensor calibration, seed selection, germination, and crop rotation planning. The process incorporates energy optimization, waste recycling, and integration of AI-driven growth monitoring to maximize yield. Finally, it covers staff training, compliance audits, and launch coordination to ensure sustainable, high-efficiency urban agriculture operations in a constrained environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
SiteEval = Transition(label='Site Eval')
StructureCheck = Transition(label='Structure Check')
RackInstall = Transition(label='Rack Install')
ClimateSetup = Transition(label='Climate Setup')
NutrientConfig = Transition(label='Nutrient Config')
SensorCalibrate = Transition(label='Sensor Calibrate')
SeedSelect = Transition(label='Seed Select')
Germination = Transition(label='Germination')
CropPlan = Transition(label='Crop Plan')
EnergyAudit = Transition(label='Energy Audit')
WasteSetup = Transition(label='Waste Setup')
AIIntegrate = Transition(label='AI Integrate')
StaffTrain = Transition(label='Staff Train')
ComplianceReview = Transition(label='Compliance Review')
LaunchPrep = Transition(label='Launch Prep')

# Structural reinforcement after site evaluation
first_po = StrictPartialOrder(nodes=[SiteEval, StructureCheck])
first_po.order.add_edge(SiteEval, StructureCheck)

# Installation group (Rack, Climate, Nutrient) done in partial order (can be parallel except nutrient after climate assumed)
install_po = StrictPartialOrder(
    nodes=[RackInstall, ClimateSetup, NutrientConfig]
)
install_po.order.add_edge(RackInstall, NutrientConfig)
install_po.order.add_edge(ClimateSetup, NutrientConfig)
# RackInstall and ClimateSetup concurrent before NutrientConfig

# Calibration and preparation group with partial order (sensor calibration then seed select/germination/crop plan)
prep_po = StrictPartialOrder(
    nodes=[SensorCalibrate, SeedSelect, Germination, CropPlan]
)
prep_po.order.add_edge(SensorCalibrate, SeedSelect)
prep_po.order.add_edge(SeedSelect, Germination)
prep_po.order.add_edge(Germination, CropPlan)

# Optimization group partially concurrent: energy audit, waste setup, AI integration can be parallel
opt_po = StrictPartialOrder(nodes=[EnergyAudit, WasteSetup, AIIntegrate])

# Final group: staff training before compliance review before launch prep
final_po = StrictPartialOrder(nodes=[StaffTrain, ComplianceReview, LaunchPrep])
final_po.order.add_edge(StaffTrain, ComplianceReview)
final_po.order.add_edge(ComplianceReview, LaunchPrep)

# Compose the full process as a global partial order connecting these groups in sequence:
# [first_po (SiteEval->StructureCheck)] -> [install_po] -> [prep_po] -> [opt_po] -> [final_po]

root = StrictPartialOrder(
    nodes=[first_po, install_po, prep_po, opt_po, final_po]
)
root.order.add_edge(first_po, install_po)
root.order.add_edge(install_po, prep_po)
root.order.add_edge(prep_po, opt_po)
root.order.add_edge(opt_po, final_po)