# Generated from: cc4866fb-c7b9-4b96-a1a6-9804ec515ea9.json
# Description: This process outlines the complex and multi-disciplinary approach to establishing a sustainable urban vertical farm within a repurposed industrial building. It involves coordinating architectural redesign, hydroponic system installation, energy optimization, crop selection, and regulatory compliance. The process integrates smart sensor deployment for environmental control, waste recycling systems for nutrient management, and market analysis for crop profitability. It also includes staff training in urban agriculture techniques and community engagement to promote local food initiatives. Each step requires detailed project management to ensure that the facility operates efficiently, sustainably, and profitably in an urban context with limited space and resources.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
SiteSurvey = Transition(label='Site Survey')
DesignPlanning = Transition(label='Design Planning')
PermitFiling = Transition(label='Permit Filing')
StructuralReinforce = Transition(label='Structural Reinforce')
HydroponicSetup = Transition(label='Hydroponic Setup')
SensorInstall = Transition(label='Sensor Install')
EnergyAudit = Transition(label='Energy Audit')
CropSelection = Transition(label='Crop Selection')
NutrientMix = Transition(label='Nutrient Mix')
WasteProcess = Transition(label='Waste Process')
ClimateControl = Transition(label='Climate Control')
StaffTraining = Transition(label='Staff Training')
MarketStudy = Transition(label='Market Study')
CommunityMeet = Transition(label='Community Meet')
LaunchTrial = Transition(label='Launch Trial')
DataMonitor = Transition(label='Data Monitor')

# Overall process construction

# Step 1: Site survey before design and permitting
# Site Survey precedes Design Planning and Permit Filing concurrently
s1 = StrictPartialOrder(nodes=[SiteSurvey, DesignPlanning, PermitFiling])
s1.order.add_edge(SiteSurvey, DesignPlanning)
s1.order.add_edge(SiteSurvey, PermitFiling)

# Step 2: Structural reinforcement after Permit Filing
s2 = StrictPartialOrder(nodes=[PermitFiling, StructuralReinforce])
s2.order.add_edge(PermitFiling, StructuralReinforce)

# Step 3: Hydroponic setup requires Structural Reinforce done
s3 = StrictPartialOrder(nodes=[StructuralReinforce, HydroponicSetup])
s3.order.add_edge(StructuralReinforce, HydroponicSetup)

# Step 4: Sensor Install and Energy Audit can run concurrently after Hydroponic Setup
s4 = StrictPartialOrder(nodes=[HydroponicSetup, SensorInstall, EnergyAudit])
s4.order.add_edge(HydroponicSetup, SensorInstall)
s4.order.add_edge(HydroponicSetup, EnergyAudit)

# Step 5: Crop Selection is after Energy Audit and Sensor Install (both must complete)
s5 = StrictPartialOrder(nodes=[SensorInstall, EnergyAudit, CropSelection])
s5.order.add_edge(SensorInstall, CropSelection)
s5.order.add_edge(EnergyAudit, CropSelection)

# Step 6: Nutrient Mix and Waste Process run concurrently after Crop Selection
s6 = StrictPartialOrder(nodes=[CropSelection, NutrientMix, WasteProcess])
s6.order.add_edge(CropSelection, NutrientMix)
s6.order.add_edge(CropSelection, WasteProcess)

# Step 7: Climate Control after Nutrient Mix and Waste Process (both required)
s7 = StrictPartialOrder(nodes=[NutrientMix, WasteProcess, ClimateControl])
s7.order.add_edge(NutrientMix, ClimateControl)
s7.order.add_edge(WasteProcess, ClimateControl)

# Step 8: Staff Training after Climate Control
s8 = StrictPartialOrder(nodes=[ClimateControl, StaffTraining])
s8.order.add_edge(ClimateControl, StaffTraining)

# Step 9: Market Study and Community Meet run concurrently after Staff Training
s9 = StrictPartialOrder(nodes=[StaffTraining, MarketStudy, CommunityMeet])
s9.order.add_edge(StaffTraining, MarketStudy)
s9.order.add_edge(StaffTraining, CommunityMeet)

# Step 10: Launch Trial after Market Study and Community Meet (both required)
s10 = StrictPartialOrder(nodes=[MarketStudy, CommunityMeet, LaunchTrial])
s10.order.add_edge(MarketStudy, LaunchTrial)
s10.order.add_edge(CommunityMeet, LaunchTrial)

# Step 11: Data Monitor after Launch Trial for continuous monitoring (could represent loop)
# Model a loop for Data Monitor and Launch Trial
# Execute Launch Trial then either exit or do Data Monitor then re-execute Launch Trial
loop = OperatorPOWL(operator=Operator.LOOP, children=[LaunchTrial, DataMonitor])

# Combine Step 9 and Step 10/11: after Market Study and Community Meet, loop
s9_loop = StrictPartialOrder(nodes=[s9, loop])
s9_loop.order.add_edge(s9, loop)

# Now combine all partial orders in sequence according to main dependencies

# Start with s1 (Site Survey --> Design Planning & Permit Filing)
# s2 after Permit Filing (part of s1)
# s3 after Structural Reinforce (part of s2)
# s4 after Hydroponic Setup (part of s3)
# s5 after Sensor Install & Energy Audit (part of s4)
# s6 after Crop Selection (part of s5)
# s7 after Nutrient Mix & Waste Process (part of s6)
# s8 after Climate Control (part of s7)
# s9_loop after Staff Training, Market Study, and Community Meet (part of s8 and s9)

# We merge these steps into one big StrictPartialOrder preserving partial order edges

# Build root PO nodes and edges:

# Nodes:
nodes = [
    SiteSurvey,
    DesignPlanning,
    PermitFiling,
    StructuralReinforce,
    HydroponicSetup,
    SensorInstall,
    EnergyAudit,
    CropSelection,
    NutrientMix,
    WasteProcess,
    ClimateControl,
    StaffTraining,
    MarketStudy,
    CommunityMeet,
    loop
]

root = StrictPartialOrder(nodes=nodes)

# Add edges for step 1
root.order.add_edge(SiteSurvey, DesignPlanning)
root.order.add_edge(SiteSurvey, PermitFiling)

# step 2
root.order.add_edge(PermitFiling, StructuralReinforce)

# step 3
root.order.add_edge(StructuralReinforce, HydroponicSetup)

# step 4
root.order.add_edge(HydroponicSetup, SensorInstall)
root.order.add_edge(HydroponicSetup, EnergyAudit)

# step 5
root.order.add_edge(SensorInstall, CropSelection)
root.order.add_edge(EnergyAudit, CropSelection)

# step 6
root.order.add_edge(CropSelection, NutrientMix)
root.order.add_edge(CropSelection, WasteProcess)

# step 7
root.order.add_edge(NutrientMix, ClimateControl)
root.order.add_edge(WasteProcess, ClimateControl)

# step 8
root.order.add_edge(ClimateControl, StaffTraining)

# step 9
root.order.add_edge(StaffTraining, MarketStudy)
root.order.add_edge(StaffTraining, CommunityMeet)

# step 10/11 with loop
root.order.add_edge(MarketStudy, loop)
root.order.add_edge(CommunityMeet, loop)