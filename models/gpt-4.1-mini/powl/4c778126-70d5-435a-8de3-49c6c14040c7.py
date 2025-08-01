# Generated from: 4c778126-70d5-435a-8de3-49c6c14040c7.json
# Description: This process outlines the complex and multidisciplinary steps required to establish a sustainable urban rooftop farming system. It involves site assessment for structural integrity, microclimate analysis, soil and water testing, design of modular planting beds, installation of automated irrigation and nutrient delivery systems, integration of renewable energy sources, implementation of pest management strategies, staff training on urban agriculture techniques, and ongoing monitoring of crop health and yield. The process also includes community engagement to promote urban farming awareness, securing permits and compliance with local regulations, and establishing supply chains for distribution. This atypical but realistic process ensures efficient utilization of rooftop spaces to produce fresh, local food in densely populated urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SiteAssess = Transition(label='Site Assess')
LoadTest = Transition(label='Load Test')
ClimateScan = Transition(label='Climate Scan')
SoilSample = Transition(label='Soil Sample')
WaterCheck = Transition(label='Water Check')
BedDesign = Transition(label='Bed Design')
IrrigationSetup = Transition(label='Irrigation Setup')
EnergyInstall = Transition(label='Energy Install')
PestControl = Transition(label='Pest Control')
StaffTrain = Transition(label='Staff Train')
PermitAcquire = Transition(label='Permit Acquire')
CommunityMeet = Transition(label='Community Meet')
SupplyChain = Transition(label='Supply Chain')
CropMonitor = Transition(label='Crop Monitor')
YieldReport = Transition(label='Yield Report')
WasteRecycle = Transition(label='Waste Recycle')

# First phase: site assessment and testing in partial order
# SiteAssess --> LoadTest (structural integrity)
# ClimateScan concurrent with SoilSample and WaterCheck (microclimate and soil/water tests)
# SoilSample and WaterCheck concurrent
assessment = StrictPartialOrder(
    nodes=[SiteAssess, LoadTest, ClimateScan, SoilSample, WaterCheck]
)
assessment.order.add_edge(SiteAssess, LoadTest)
# SiteAssess --> ClimateScan, SoilSample, WaterCheck (these after structural tests)
assessment.order.add_edge(SiteAssess, ClimateScan)
assessment.order.add_edge(SiteAssess, SoilSample)
assessment.order.add_edge(SiteAssess, WaterCheck)

# Design and installation phase after assessments
# BedDesign after all assessments (LoadTest, ClimateScan, SoilSample, WaterCheck)
design = StrictPartialOrder(
    nodes=[BedDesign]
)
# We'll link design after all assessment activities finish
# We'll do this linking at the root POWL by ordering assessment.last_nodes --> design

# IrrigationSetup and EnergyInstall can be done in parallel after BedDesign
install = StrictPartialOrder(
    nodes=[IrrigationSetup, EnergyInstall]
)

# PestControl after installation parallel activities
pest = PestControl

# StaffTrain can start after PestControl
staff_train = StaffTrain

# CommunityMeet and PermitAcquire can happen in parallel after StaffTrain
comm_permit = StrictPartialOrder(
    nodes=[CommunityMeet, PermitAcquire]
)

# SupplyChain after permits and community meeting
supply = SupplyChain

# CropMonitor and YieldReport after SupplyChain (monitoring happens during and reporting after)
monitor_report = StrictPartialOrder(
    nodes=[CropMonitor, YieldReport]
)
monitor_report.order.add_edge(CropMonitor, YieldReport)

# WasteRecycle can be concurrent with CropMonitor/YieldReport (ongoing sustainability)
# We'll add WasteRecycle concurrently at same level as monitoring

# Now building the layers with proper dependencies

# Layer 1: assessment
layer1 = assessment

# Layer 2: BedDesign after all assessments
layer2 = BedDesign

# Layer 3: install irrigation and energy in parallel
layer3 = install

# Layer 4: PestControl after install
layer4 = pest

# Layer 5: StaffTrain after PestControl
layer5 = staff_train

# Layer 6: CommunityMeet and PermitAcquire in parallel after StaffTrain
layer6 = comm_permit

# Layer 7: SupplyChain after community and permits
layer7 = supply

# Layer 8: CropMonitor and YieldReport in order
layer8 = monitor_report

# WasteRecycle concurrent with CropMonitor and YieldReport
layer9 = WasteRecycle

# Build root partial order
root = StrictPartialOrder(
    nodes=[layer1, layer2, layer3, layer4, layer5, layer6, layer7, layer8, layer9]
)

# order edges
# layer1 -> layer2
root.order.add_edge(layer1, layer2)
# layer2 -> layer3
root.order.add_edge(layer2, layer3)
# layer3 -> layer4
root.order.add_edge(layer3, layer4)
# layer4 -> layer5
root.order.add_edge(layer4, layer5)
# layer5 -> layer6
root.order.add_edge(layer5, layer6)
# layer6 -> layer7
root.order.add_edge(layer6, layer7)
# layer7 -> layer8
root.order.add_edge(layer7, layer8)
# layer7 -> layer9  (WasteRecycle concurrent with monitoring/report)
root.order.add_edge(layer7, layer9)

# Additionally, we must make sure within assessment all 4 activities get proper ordering:
# This was done already with explicit edges in assessment

# Also within install, irrigation and energy are concurrent, no order edges

# Within comm_permit CommunityMeet and PermitAcquire are concurrent

# Within monitor_report CropMonitor -> YieldReport edge exists

# Return root