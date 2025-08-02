# Generated from: a5110dcc-5ca4-4eae-b15f-5c56101a7d61.json
# Description: This process involves the end-to-end management of a remote drone fleet used for agricultural monitoring. It includes scheduling drone missions based on crop data, performing pre-flight health diagnostics, establishing secure communication channels, conducting autonomous flight operations, collecting multispectral imagery, transmitting data to cloud servers, processing images with AI algorithms, generating actionable insights for farmers, managing battery swaps and maintenance, updating firmware remotely, handling emergency recalls, coordinating with air traffic control, and archiving flight logs for regulatory compliance. The process ensures efficient and compliant drone utilization to optimize crop yields while minimizing operational risks and costs.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
MissionSetup = Transition(label='Mission Setup')
HealthCheck = Transition(label='Health Check')
CommLink = Transition(label='Comm Link')
FlightLaunch = Transition(label='Flight Launch')
DataCapture = Transition(label='Data Capture')
DataUpload = Transition(label='Data Upload')
ImageProcess = Transition(label='Image Process')
InsightGen = Transition(label='Insight Gen')
BatterySwap = Transition(label='Battery Swap')
FirmwareUpdate = Transition(label='Firmware Update')
RecallHandle = Transition(label='Recall Handle')
TrafficCoord = Transition(label='Traffic Coord')
LogArchive = Transition(label='Log Archive')
Maintenance = Transition(label='Maintenance')
ComplianceCheck = Transition(label='Compliance Check')

# Loop for maintenance with Battery Swap and Firmware Update
# MaintenanceLoop = *(Maintenance, BatterySwap + FirmwareUpdate + Maintenance)
# To model that maintenance can be done repeatedly along with Battery Swap and Firmware Update, we build a partial order of updates and then loop with Maintenance

# PartialOrder for battery swap and firmware update (concurrent)
BatteryAndFirmware = StrictPartialOrder(nodes=[BatterySwap, FirmwareUpdate])

# No order between BatterySwap and FirmwareUpdate -> concurrent

# loop body: choice of (BatteryAndFirmware or silent) then Maintenance
# We'll model B as a choice between performing BatteryAndFirmware or skip
skip = SilentTransition()

BatteryFirmwareChoice = OperatorPOWL(operator=Operator.XOR, children=[BatteryAndFirmware, skip])

MaintenanceLoop = OperatorPOWL(operator=Operator.LOOP, children=[Maintenance, BatteryFirmwareChoice])

# Loop for Emergency Recall and Traffic Coordination
# These two may happen concurrently or in any order; then loop repeated until exit

RecallTrafficPO = StrictPartialOrder(nodes=[RecallHandle, TrafficCoord])  # concurrent

RecallTrafficLoop = OperatorPOWL(operator=Operator.LOOP, children=[RecallTrafficPO, skip])  # loop with skip exit

# Main sequence partial order:

nodes = [
    MissionSetup,
    HealthCheck,
    CommLink,
    FlightLaunch,
    DataCapture,
    DataUpload,
    ImageProcess,
    InsightGen,
    MaintenanceLoop,
    RecallTrafficLoop,
    LogArchive,
    ComplianceCheck
]

root = StrictPartialOrder(nodes=nodes)

# Define partial order edges reflecting dependencies and concurrency

# Sequential flow from mission setup through insight generation
root.order.add_edge(MissionSetup, HealthCheck)
root.order.add_edge(HealthCheck, CommLink)
root.order.add_edge(CommLink, FlightLaunch)
root.order.add_edge(FlightLaunch, DataCapture)
root.order.add_edge(DataCapture, DataUpload)
root.order.add_edge(DataUpload, ImageProcess)
root.order.add_edge(ImageProcess, InsightGen)

# After Insight Gen, MaintenanceLoop and RecallTrafficLoop can occur concurrently
root.order.add_edge(InsightGen, MaintenanceLoop)
root.order.add_edge(InsightGen, RecallTrafficLoop)

# Both MaintenanceLoop and RecallTrafficLoop should finish before final compliance/log archiving
root.order.add_edge(MaintenanceLoop, LogArchive)
root.order.add_edge(RecallTrafficLoop, LogArchive)

# Log archive before Compliance Check
root.order.add_edge(LogArchive, ComplianceCheck)