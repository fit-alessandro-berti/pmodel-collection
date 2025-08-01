# Generated from: 4bd82eb5-49a2-4073-b827-5f1d42be5ccd.json
# Description: This process outlines the comprehensive steps involved in establishing a sustainable urban rooftop farm on a commercial building. It includes site assessment, structural analysis, soil preparation using hydroponic techniques, and installation of automated irrigation systems. The process also covers regulatory compliance checks, sourcing of organic seeds, pest control planning, and community engagement for local produce distribution. Continuous monitoring of crop health through IoT sensors and data analytics ensures optimal growth conditions while minimizing resource use. Finally, the process integrates seasonal crop rotation planning and waste recycling protocols to maintain long-term farm productivity and environmental sustainability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
SiteSurvey = Transition(label='Site Survey')
StructureCheck = Transition(label='Structure Check')
SoilPrep = Transition(label='Soil Prep')
HydroponicSetup = Transition(label='Hydroponic Setup')
IrrigationInstall = Transition(label='Irrigation Install')
ComplianceReview = Transition(label='Compliance Review')
SeedSourcing = Transition(label='Seed Sourcing')
PestPlan = Transition(label='Pest Plan')
CommunityMeet = Transition(label='Community Meet')
SensorDeploy = Transition(label='Sensor Deploy')
DataMonitor = Transition(label='Data Monitor')
CropRotation = Transition(label='Crop Rotation')
WasteManage = Transition(label='Waste Manage')
HarvestPlan = Transition(label='Harvest Plan')
Distribution = Transition(label='Distribution')

# Site assessment partial order: Site Survey --> Structure Check
site_assessment = StrictPartialOrder(nodes=[SiteSurvey, StructureCheck])
site_assessment.order.add_edge(SiteSurvey, StructureCheck)

# Soil preparation partial order: Soil Prep --> Hydroponic Setup
soil_prep = StrictPartialOrder(nodes=[SoilPrep, HydroponicSetup])
soil_prep.order.add_edge(SoilPrep, HydroponicSetup)

# Automated irrigation and compliance parallel activities: Irrigation Install and Compliance Review concurrent
# So combine both as nodes in PO without order
irrigation_compliance = StrictPartialOrder(nodes=[IrrigationInstall, ComplianceReview])

# Regulatory compliance, seed sourcing, pest planning, community meet partial order:
# Compliance Review --> Seed Sourcing --> Pest Plan --> Community Meet
regulatory_source_plan_community = StrictPartialOrder(nodes=[ComplianceReview, SeedSourcing, PestPlan, CommunityMeet])
regulatory_source_plan_community.order.add_edge(ComplianceReview, SeedSourcing)
regulatory_source_plan_community.order.add_edge(SeedSourcing, PestPlan)
regulatory_source_plan_community.order.add_edge(PestPlan, CommunityMeet)

# Crop health monitoring partial order: Sensor Deploy --> Data Monitor
crop_monitoring = StrictPartialOrder(nodes=[SensorDeploy, DataMonitor])
crop_monitoring.order.add_edge(SensorDeploy, DataMonitor)

# Final planning: Crop Rotation --> Waste Manage --> Harvest Plan --> Distribution
final_planning = StrictPartialOrder(nodes=[CropRotation, WasteManage, HarvestPlan, Distribution])
final_planning.order.add_edge(CropRotation, WasteManage)
final_planning.order.add_edge(WasteManage, HarvestPlan)
final_planning.order.add_edge(HarvestPlan, Distribution)

# Overall process reconciliation:

# 1) site_assessment --> soil_prep --> irrigation_compliance & regulatory_source_plan_community parallel
# Since irrigation_compliance and regulatory_source_plan_community share ComplianceReview, better to merge ComplianceReview once

# We merge ComplianceReview into irrigation_compliance + regulatory_source_plan_community: so regulatory_source_plan_community starts after ComplianceReview,
# but irrigation_compliance has ComplianceReview node as well, so combine irrigation_compliance and regulatory_source_plan_community with shared ComplianceReview node

# So we build a combined "post soil prep" phase:

# Combine irrigation_compliance and regulatory_source_plan_community with shared ComplianceReview node,
# nodes = {IrrigationInstall, ComplianceReview, SeedSourcing, PestPlan, CommunityMeet}
post_soil_prep_nodes = [IrrigationInstall, ComplianceReview, SeedSourcing, PestPlan, CommunityMeet]
post_soil_prep = StrictPartialOrder(nodes=post_soil_prep_nodes)
# regulatory_source_plan_community order edges
post_soil_prep.order.add_edge(ComplianceReview, SeedSourcing)
post_soil_prep.order.add_edge(SeedSourcing, PestPlan)
post_soil_prep.order.add_edge(PestPlan, CommunityMeet)
# irrigation_compliance has no order edges, but ComplianceReview and IrrigationInstall concurrent, so no order edge between them

# Overall:
# site_assessment --> soil_prep --> post_soil_prep --> crop_monitoring --> final_planning

# Build the overall partial order nodes and edges incrementally:

all_nodes = [
    SiteSurvey, StructureCheck,
    SoilPrep, HydroponicSetup,
    IrrigationInstall, ComplianceReview, SeedSourcing, PestPlan, CommunityMeet,
    SensorDeploy, DataMonitor,
    CropRotation, WasteManage, HarvestPlan, Distribution
]

root = StrictPartialOrder(nodes=all_nodes)

# Add site assessment order
root.order.add_edge(SiteSurvey, StructureCheck)
# Soil prep order
root.order.add_edge(SoilPrep, HydroponicSetup)
# Link site assessment to soil prep (StructureCheck --> SoilPrep)
root.order.add_edge(StructureCheck, SoilPrep)
# Link soil prep to post_soil_prep (HydroponicSetup --> IrrigationInstall and HydroponicSetup --> ComplianceReview)
root.order.add_edge(HydroponicSetup, IrrigationInstall)
root.order.add_edge(HydroponicSetup, ComplianceReview)
# regulatory_source_plan_community order edges within post soil prep
root.order.add_edge(ComplianceReview, SeedSourcing)
root.order.add_edge(SeedSourcing, PestPlan)
root.order.add_edge(PestPlan, CommunityMeet)
# Crop monitoring order
root.order.add_edge(SensorDeploy, DataMonitor)
# Link post_soil_prep to crop_monitoring (CommunityMeet --> SensorDeploy and IrrigationInstall --> SensorDeploy)
root.order.add_edge(CommunityMeet, SensorDeploy)
root.order.add_edge(IrrigationInstall, SensorDeploy)
# Final planning order
root.order.add_edge(CropRotation, WasteManage)
root.order.add_edge(WasteManage, HarvestPlan)
root.order.add_edge(HarvestPlan, Distribution)
# Link crop_monitoring to final_planning (DataMonitor --> CropRotation)
root.order.add_edge(DataMonitor, CropRotation)

# Note concurrency: 
# - Between SiteSurvey and HydroponicSetup no edges except defined above.
# - IrrigationInstall and ComplianceReview concurrent except when ordering with other nodes.
# - Crop Rotation and Waste etc serial.

# The loop and choice operators are not explicitly requested or apparent from description.

# Final root is defined above