# Generated from: 7cc14e09-a736-4d18-90b0-966d6e46d20a.json
# Description: This process outlines the integration of urban beekeeping into municipal green initiatives, combining environmental sustainability with local community engagement. It begins with site identification and environmental assessment, followed by regulatory compliance checks and stakeholder consultations. Hive installation and bee colony introduction are coordinated alongside educational workshops for residents. Continuous monitoring of hive health and data collection on pollination impact are conducted, integrating insights into urban planning. Maintenance routines and crisis management protocols ensure bee welfare and public safety. Finally, feedback loops from community and environmental data guide iterative improvements, fostering a harmonious balance between urban development and ecological preservation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
siteSurvey       = Transition(label='Site Survey')
envAssessment    = Transition(label='Env Assessment')
regCheck         = Transition(label='Reg Check')
stakeholderMeet  = Transition(label='Stakeholder Meet')
permitApply      = Transition(label='Permit Apply')
hiveSetup        = Transition(label='Hive Setup')
colonyIntroduce  = Transition(label='Colony Introduce')
workshopHost     = Transition(label='Workshop Host')

# Define the loop head activity
healthMonitor    = Transition(label='Health Monitor')

# Define the body of the monitoring/analysis loop
dataCollect      = Transition(label='Data Collect')
impactAnalyze    = Transition(label='Impact Analyze')
feedbackGather   = Transition(label='Feedback Gather')
planUpdate       = Transition(label='Plan Update')
maintenance      = Transition(label='Maintenance')
crisisManage     = Transition(label='Crisis Manage')

monitorBody = StrictPartialOrder(nodes=[
    dataCollect, impactAnalyze, feedbackGather,
    planUpdate, maintenance, crisisManage
])
# Sequence within the loop body
monitorBody.order.add_edge(dataCollect,    impactAnalyze)
monitorBody.order.add_edge(impactAnalyze,  feedbackGather)
monitorBody.order.add_edge(feedbackGather, planUpdate)
monitorBody.order.add_edge(planUpdate,     maintenance)
monitorBody.order.add_edge(maintenance,    crisisManage)

# Define the loop: first do healthMonitor, then repeatedly do monitorBody + healthMonitor
loop = OperatorPOWL(operator=Operator.LOOP, children=[healthMonitor, monitorBody])

# Build the main partial order
root = StrictPartialOrder(nodes=[
    siteSurvey, envAssessment, regCheck, stakeholderMeet,
    permitApply, hiveSetup, colonyIntroduce, workshopHost,
    loop
])
# Sequence the main phases
root.order.add_edge(siteSurvey,      envAssessment)
root.order.add_edge(envAssessment,   regCheck)
root.order.add_edge(regCheck,        stakeholderMeet)
root.order.add_edge(stakeholderMeet, permitApply)
root.order.add_edge(permitApply,     hiveSetup)
root.order.add_edge(hiveSetup,       colonyIntroduce)
root.order.add_edge(colonyIntroduce, workshopHost)
root.order.add_edge(workshopHost,    loop)