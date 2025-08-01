# Generated from: 0352a4e8-91a1-4107-a8a2-4c0681356a07.json
# Description: This process outlines the creation and deployment of a custom urban farming system tailored for small rooftop spaces. It involves site analysis, environmental data collection, modular design planning, resource procurement, automated irrigation setup, sensor integration for real-time monitoring, community stakeholder engagement, pilot testing, iterative adjustments based on collected data, compliance verification with local regulations, training sessions for end-users, and final deployment with ongoing remote support to ensure sustainable urban agriculture in constrained environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions with the exact given labels
SiteSurvey = Transition(label='Site Survey')
DataCapture = Transition(label='Data Capture')
DesignLayout = Transition(label='Design Layout')
MaterialOrder = Transition(label='Material Order')
ModuleBuild = Transition(label='Module Build')
IrrigationSetup = Transition(label='Irrigation Setup')
SensorInstall = Transition(label='Sensor Install')
SoftwareConfig = Transition(label='Software Config')
StakeholderMeet = Transition(label='Stakeholder Meet')
PilotDeploy = Transition(label='Pilot Deploy')
FeedbackGather = Transition(label='Feedback Gather')
AdjustDesign = Transition(label='Adjust Design')
ComplianceCheck = Transition(label='Compliance Check')
UserTraining = Transition(label='User Training')
FinalLaunch = Transition(label='Final Launch')
RemoteSupport = Transition(label='Remote Support')

# Construct the loop for iterative adjustments:
# LOOP(
#   A = FeedbackGather -> AdjustDesign
#   B = (empty, we just repeat the loop after B then A)
# )
# But per definition, loop is * (A, B), where:
# execute A, then choose exit or execute B then A again.
# We have FeedbackGather and AdjustDesign repeated, so:
# First execute FeedbackGather then AdjustDesign (A),
# then B is empty or silent transition (no activities),
# which makes no sense.
# Actually, we want to loop over FeedbackGather and AdjustDesign
# till exit.
#
# But definition of * (A, B) is:
# do A,
# then choose: exit OR
# do B then A again, repeat.
#
# So, we can define:
# A = sequence FeedbackGather->AdjustDesign
# B = silent
# So loop is * (A, silent)
#
# But we need to represent sequence A=FeedbackGather->AdjustDesign,
# so partial order with order FeedbackGather->AdjustDesign.
#
# Let's build A as partial order with nodes {FeedbackGather, AdjustDesign},
# ordered FeedbackGather -> AdjustDesign
#
from pm4py.objects.powl.obj import StrictPartialOrder, SilentTransition

A_loop = StrictPartialOrder(nodes=[FeedbackGather, AdjustDesign])
A_loop.order.add_edge(FeedbackGather, AdjustDesign)

skip = SilentTransition()

loop_adjust = OperatorPOWL(operator=Operator.LOOP, children=[A_loop, skip])

# Build the entire PO in partial order (where concurrency can be respected)

# Construct the main process partial order:

# From description, natural order of activities:

# 1. Site Survey
# 2. Data Capture
# 3. Design Layout
# 4. Material Order
# 5. Module Build
# 6. Irrigation Setup
# 7. Sensor Install
# 8. Software Config
# 9. Stakeholder Meet
# 10. Pilot Deploy
# 11. loop over Feedback Gather & Adjust Design
# 12. Compliance Check
# 13. User Training
# 14. Final Launch
# 15. Remote Support

# Let's create the nodes list:
nodes = [
    SiteSurvey,
    DataCapture,
    DesignLayout,
    MaterialOrder,
    ModuleBuild,
    IrrigationSetup,
    SensorInstall,
    SoftwareConfig,
    StakeholderMeet,
    PilotDeploy,
    loop_adjust,
    ComplianceCheck,
    UserTraining,
    FinalLaunch,
    RemoteSupport,
]

root = StrictPartialOrder(nodes=nodes)

# Add order edges to reflect described order:

root.order.add_edge(SiteSurvey, DataCapture)
root.order.add_edge(DataCapture, DesignLayout)
root.order.add_edge(DesignLayout, MaterialOrder)
root.order.add_edge(MaterialOrder, ModuleBuild)
root.order.add_edge(ModuleBuild, IrrigationSetup)
root.order.add_edge(IrrigationSetup, SensorInstall)
root.order.add_edge(SensorInstall, SoftwareConfig)
root.order.add_edge(SoftwareConfig, StakeholderMeet)
root.order.add_edge(StakeholderMeet, PilotDeploy)
root.order.add_edge(PilotDeploy, loop_adjust)
root.order.add_edge(loop_adjust, ComplianceCheck)
root.order.add_edge(ComplianceCheck, UserTraining)
root.order.add_edge(UserTraining, FinalLaunch)
root.order.add_edge(FinalLaunch, RemoteSupport)