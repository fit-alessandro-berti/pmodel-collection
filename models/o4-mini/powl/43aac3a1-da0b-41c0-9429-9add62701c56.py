# Generated from: 43aac3a1-da0b-41c0-9429-9add62701c56.json
# Description: This process outlines a strategic approach for managing unforeseen crises affecting multiple business units and external stakeholders simultaneously. It involves rapid assessment, cross-functional coordination, resource reallocation, real-time communication through diverse channels, and iterative feedback loops. The goal is to minimize operational disruption, safeguard brand reputation, and ensure compliance with regulatory requirements by leveraging data analytics and stakeholder engagement strategies. This atypical yet realistic process integrates emergency protocols with business continuity planning in a dynamic environment requiring agility and precision.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
alert = Transition(label='Alert Trigger')
init = Transition(label='Initial Assess')
stake = Transition(label='Stakeholder Map')
reschk = Transition(label='Resource Check')
impact = Transition(label='Impact Forecast')
team = Transition(label='Team Mobilize')
chan = Transition(label='Channel Setup')
msg = Transition(label='Message Draft')
legal = Transition(label='Legal Review')
send = Transition(label='Send Alerts')
monitor = Transition(label='Monitor Feedback')
analytics = Transition(label='Data Analytics')
adjust = Transition(label='Adjust Strategy')
liaise = Transition(label='External Liaise')
report = Transition(label='Report Compile')
debrief = Transition(label='Debrief Session')

# 1) Concurrent initial assessments: Stakeholder Map, Resource Check, Impact Forecast
assessPO = StrictPartialOrder(nodes=[stake, reschk, impact])
# no internal ordering => all three run in parallel

# 2) Primary mobilization sequence: Alert Trigger -> Initial Assess -> [assessPO] -> Team Mobilize -> Channel Setup -> External Liaise
primaryPO = StrictPartialOrder(nodes=[alert, init, assessPO, team, chan, liaise])
primaryPO.order.add_edge(alert, init)
primaryPO.order.add_edge(init, assessPO)
primaryPO.order.add_edge(assessPO, team)
primaryPO.order.add_edge(team, chan)
primaryPO.order.add_edge(chan, liaise)

# 3) One-off messaging workflow: Message Draft -> Legal Review -> Send Alerts
msgPO = StrictPartialOrder(nodes=[msg, legal, send])
msgPO.order.add_edge(msg, legal)
msgPO.order.add_edge(legal, send)

# 4) Iterative feedback loop:
#    Body: Monitor Feedback and Data Analytics in parallel
body = StrictPartialOrder(nodes=[monitor, analytics])
#    Redo: Adjust Strategy -> Message Draft -> Legal Review -> Send Alerts
redo = StrictPartialOrder(nodes=[adjust, msg, legal, send])
redo.order.add_edge(adjust, msg)
redo.order.add_edge(msg, legal)
redo.order.add_edge(legal, send)
#    LOOP operator: do 'body', then either exit or do 'redo' and repeat
loopOp = OperatorPOWL(operator=Operator.LOOP, children=[body, redo])

# 5) Final wrap-up: Report Compile -> Debrief Session
finalPO = StrictPartialOrder(nodes=[report, debrief])
finalPO.order.add_edge(report, debrief)

# Root model: partial order of the major blocks
root = StrictPartialOrder(
    nodes=[primaryPO, msgPO, loopOp, finalPO]
)
root.order.add_edge(primaryPO, msgPO)
root.order.add_edge(msgPO, loopOp)
root.order.add_edge(loopOp, finalPO)