# Generated from: 45d8a5fc-3d39-4d23-8f46-97e8bef5f613.json
# Description: This process outlines the complex and multidisciplinary approach required to establish a sustainable urban rooftop farm in a densely populated city. It begins with site assessment and structural evaluation, followed by obtaining permits and integrating smart irrigation systems. The workflow includes soil testing, modular bed installation, seed selection, and pest management planning. Additionally, the process incorporates community engagement initiatives, renewable energy integration, crop monitoring through IoT devices, and waste composting strategies. Finally, it concludes with harvest scheduling and urban market distribution logistics, ensuring environmental compliance and maximizing yield within limited rooftop spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
SiteAssess = Transition(label='Site Assess')
StructureTest = Transition(label='Structure Test')
PermitAcquire = Transition(label='Permit Acquire')
IrrigationPlan = Transition(label='Irrigation Plan')
SoilAnalyze = Transition(label='Soil Analyze')
BedInstall = Transition(label='Bed Install')
SeedChoose = Transition(label='Seed Choose')
PestControl = Transition(label='Pest Control')
CommunityMeet = Transition(label='Community Meet')
EnergySetup = Transition(label='Energy Setup')
CropMonitor = Transition(label='Crop Monitor')
WasteCompost = Transition(label='Waste Compost')
HarvestPlan = Transition(label='Harvest Plan')
MarketShip = Transition(label='Market Ship')
ComplianceCheck = Transition(label='Compliance Check')

# Build the initial assessments sequence
assessment = StrictPartialOrder(nodes=[SiteAssess, StructureTest])
assessment.order.add_edge(SiteAssess, StructureTest)

# Permits and irrigation after assessments, irrigation after permits
perm_irrig = StrictPartialOrder(nodes=[PermitAcquire, IrrigationPlan])
perm_irrig.order.add_edge(PermitAcquire, IrrigationPlan)

# Soil Analyze, Bed Install, Seed Choose, Pest Control form a partial order.
# Arrange them in a loose sequence (SoilAnalyze -> BedInstall -> SeedChoose -> PestControl)
soil_seq = StrictPartialOrder(nodes=[SoilAnalyze, BedInstall, SeedChoose, PestControl])
soil_seq.order.add_edge(SoilAnalyze, BedInstall)
soil_seq.order.add_edge(BedInstall, SeedChoose)
soil_seq.order.add_edge(SeedChoose, PestControl)

# CommunityMeet, EnergySetup, CropMonitor and WasteCompost are concurrent (can happen in parallel)
engagement_nodes = [CommunityMeet, EnergySetup, CropMonitor, WasteCompost]
engagement = StrictPartialOrder(nodes=engagement_nodes)

# Final sequence: HarvestPlan -> MarketShip -> ComplianceCheck
final_seq = StrictPartialOrder(nodes=[HarvestPlan, MarketShip, ComplianceCheck])
final_seq.order.add_edge(HarvestPlan, MarketShip)
final_seq.order.add_edge(MarketShip, ComplianceCheck)

# Now compose the whole process with the correct control flow:
# Start with assessments -> permits/irrigation -> soil-related -> engagement (concurrent)
# engagement nodes are concurrent, happen after soil_seq
# Then final sequence, after engagement

# Combine assessment and perm_irrig in sequence
first_part = StrictPartialOrder(nodes=[assessment, perm_irrig])
first_part.order.add_edge(assessment, perm_irrig)

# Next combine first_part and soil_seq in sequence
second_part = StrictPartialOrder(nodes=[first_part, soil_seq])
second_part.order.add_edge(first_part, soil_seq)

# Combine second_part and engagement in sequence
third_part = StrictPartialOrder(nodes=[second_part, engagement])
third_part.order.add_edge(second_part, engagement)

# Finally combine third_part and final_seq in sequence
root = StrictPartialOrder(nodes=[third_part, final_seq])
root.order.add_edge(third_part, final_seq)