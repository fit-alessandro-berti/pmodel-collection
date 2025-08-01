# Generated from: 177afcd8-21b2-46ac-b9a7-7849076acae8.json
# Description: This process involves the intricate planning and establishment of a vertical farming system within an urban environment, integrating advanced hydroponic techniques, renewable energy sources, and smart automation. It begins with site analysis and zoning compliance, followed by modular unit design and nutrient solution formulation. The process includes climate control calibration, seed selection, and planting schedules tailored for maximum yield in limited space. Continuous monitoring through IoT sensors ensures optimal growth conditions, while waste recycling loops convert organic residues into biofertilizers. Post-harvest procedures encompass automated picking, quality grading, and packaging for local distribution. Stakeholder coordination and periodic system audits guarantee sustainable operation and scalability in dense city landscapes.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
SiteAnalysis = Transition(label='Site Analysis')
ZoningCheck = Transition(label='Zoning Check')
UnitDesign = Transition(label='Unit Design')
NutrientPrep = Transition(label='Nutrient Prep')
ClimateSetup = Transition(label='Climate Setup')
SeedSelection = Transition(label='Seed Selection')
PlantingPlan = Transition(label='Planting Plan')
SensorInstall = Transition(label='Sensor Install')
GrowthMonitor = Transition(label='Growth Monitor')
WasteRecycle = Transition(label='Waste Recycle')
BiofertilizerMake = Transition(label='Biofertilizer Make')
AutomatedHarvest = Transition(label='Automated Harvest')
QualityGrade = Transition(label='Quality Grade')
PackagingPrep = Transition(label='Packaging Prep')
LocalDispatch = Transition(label='Local Dispatch')
StakeholderMeet = Transition(label='Stakeholder Meet')
SystemAudit = Transition(label='System Audit')

# Waste recycle loop: WasteRecycle -> BiofertilizerMake repeated
# Loop structure: execute WasteRecycle, then choose to exit or do BiofertilizerMake then WasteRecycle again
waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[WasteRecycle, BiofertilizerMake])

# Post-harvest sequential: AutomatedHarvest -> QualityGrade -> PackagingPrep -> LocalDispatch
post_harvest_po = StrictPartialOrder(
    nodes=[AutomatedHarvest, QualityGrade, PackagingPrep, LocalDispatch]
)
post_harvest_po.order.add_edge(AutomatedHarvest, QualityGrade)
post_harvest_po.order.add_edge(QualityGrade, PackagingPrep)
post_harvest_po.order.add_edge(PackagingPrep, LocalDispatch)

# Monitoring cluster: SensorInstall -> GrowthMonitor -> waste_loop (monitoring + recycling)
monitoring_po = StrictPartialOrder(
    nodes=[SensorInstall, GrowthMonitor, waste_loop]
)
monitoring_po.order.add_edge(SensorInstall, GrowthMonitor)
monitoring_po.order.add_edge(GrowthMonitor, waste_loop)

# Planting plan cluster: SeedSelection -> PlantingPlan -> monitoring_po
planting_po = StrictPartialOrder(
    nodes=[SeedSelection, PlantingPlan, monitoring_po]
)
planting_po.order.add_edge(SeedSelection, PlantingPlan)
planting_po.order.add_edge(PlantingPlan, monitoring_po)

# Climate and nutrient cluster: ClimateSetup and NutrientPrep concurrent, then both before planting_po
climate_nutrient_po = StrictPartialOrder(
    nodes=[ClimateSetup, NutrientPrep]
)
# concurrent, no order edges

pre_planting_po = StrictPartialOrder(
    nodes=[climate_nutrient_po, planting_po]
)
pre_planting_po.order.add_edge(climate_nutrient_po, planting_po)

# Design cluster: UnitDesign before pre_planting_po
design_po = StrictPartialOrder(
    nodes=[UnitDesign, pre_planting_po]
)
design_po.order.add_edge(UnitDesign, pre_planting_po)

# Regulatory cluster: SiteAnalysis -> ZoningCheck
regulatory_po = StrictPartialOrder(
    nodes=[SiteAnalysis, ZoningCheck]
)
regulatory_po.order.add_edge(SiteAnalysis, ZoningCheck)

# Stakeholder coordination loop: StakeholderMeet then choose to exit or SystemAudit then StakeholderMeet again
stakeholder_loop = OperatorPOWL(operator=Operator.LOOP, children=[StakeholderMeet, SystemAudit])

# Entire initial flow: regulatory -> design -> stakeholder_loop and post_harvest in concurrency after design and stakeholder
# We know after design and stakeholder_loop, post_harvest happens

# Combine regulatory and design sequentially
reg_design_po = StrictPartialOrder(
    nodes=[regulatory_po, design_po]
)
reg_design_po.order.add_edge(regulatory_po, design_po)

# Concurrent stakeholder and reg_design
concurrent_main = StrictPartialOrder(
    nodes=[reg_design_po, stakeholder_loop]
)
# concurrent, no order edges between reg_design_po and stakeholder_loop

# After these two completion, post-harvest happens
root = StrictPartialOrder(
    nodes=[concurrent_main, post_harvest_po]
)
root.order.add_edge(concurrent_main, post_harvest_po)