# Generated from: e0f5dbd4-2150-4e6b-95ea-0cb652ef394d.json
# Description: This process outlines the setup and deployment of a custom drone delivery service tailored for remote locations with limited infrastructure. It involves designing unique drone specifications, securing regulatory approval, integrating adaptive navigation systems, coordinating with local partners for landing zones, training operators remotely, conducting phased testing under varying weather conditions, and establishing real-time monitoring protocols. The process ensures compliance with aviation laws, optimizes delivery routes using AI algorithms, manages supply chain logistics for spare parts, and implements customer feedback loops to refine service quality. Continuous risk assessment and emergency response planning are integral to maintain safety and reliability in challenging environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all atomic activities
DroneDesign      = Transition(label='Drone Design')
RegulatoryCheck  = Transition(label='Regulatory Check')
ComplianceAudit  = Transition(label='Compliance Audit')
NavSystem        = Transition(label='Nav System')
DataSync         = Transition(label='Data Sync')
PartnerSetup     = Transition(label='Partner Setup')
OperatorTraining = Transition(label='Operator Training')
TestFlights      = Transition(label='Test Flights')
WeatherReview    = Transition(label='Weather Review')
RouteOptimize    = Transition(label='Route Optimize')
PartsLogistics   = Transition(label='Parts Logistics')
FeedbackLoop     = Transition(label='Feedback Loop')
RiskAssess       = Transition(label='Risk Assess')
EmergencyPlan    = Transition(label='Emergency Plan')
ServiceLaunch    = Transition(label='Service Launch')

# Silent nodes for loop exits
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()

# 1) Loop for continuous risk assessment & emergency planning
seq_risk = StrictPartialOrder(nodes=[RiskAssess, EmergencyPlan])
seq_risk.order.add_edge(RiskAssess, EmergencyPlan)
loop_risk = OperatorPOWL(operator=Operator.LOOP, children=[seq_risk, skip1])

# 2) Loop for phased test flights under varying weather
seq_test = StrictPartialOrder(nodes=[TestFlights, WeatherReview])
seq_test.order.add_edge(TestFlights, WeatherReview)
loop_test = OperatorPOWL(operator=Operator.LOOP, children=[seq_test, skip2])

# 3) Loop for iterative customer feedback refinement
loop_feedback = OperatorPOWL(operator=Operator.LOOP, children=[FeedbackLoop, skip3])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    DroneDesign, RegulatoryCheck, ComplianceAudit, NavSystem, DataSync,
    PartnerSetup, OperatorTraining,
    loop_risk,           # continuous risk/emergency loop
    loop_test,           # testing + weather review loop
    RouteOptimize, PartsLogistics,
    loop_feedback,       # feedback loop
    ServiceLaunch
])

# Define the strict sequence of dependencies
root.order.add_edge(DroneDesign,      RegulatoryCheck)
root.order.add_edge(RegulatoryCheck,  ComplianceAudit)
root.order.add_edge(ComplianceAudit,  NavSystem)
root.order.add_edge(NavSystem,        DataSync)
root.order.add_edge(DataSync,         PartnerSetup)
root.order.add_edge(PartnerSetup,     OperatorTraining)
root.order.add_edge(OperatorTraining, loop_risk)
root.order.add_edge(loop_risk,        loop_test)
root.order.add_edge(loop_test,        RouteOptimize)
root.order.add_edge(RouteOptimize,    PartsLogistics)
root.order.add_edge(PartsLogistics,   loop_feedback)
root.order.add_edge(loop_feedback,    ServiceLaunch)