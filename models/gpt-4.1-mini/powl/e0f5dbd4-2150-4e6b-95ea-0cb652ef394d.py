# Generated from: e0f5dbd4-2150-4e6b-95ea-0cb652ef394d.json
# Description: This process outlines the setup and deployment of a custom drone delivery service tailored for remote locations with limited infrastructure. It involves designing unique drone specifications, securing regulatory approval, integrating adaptive navigation systems, coordinating with local partners for landing zones, training operators remotely, conducting phased testing under varying weather conditions, and establishing real-time monitoring protocols. The process ensures compliance with aviation laws, optimizes delivery routes using AI algorithms, manages supply chain logistics for spare parts, and implements customer feedback loops to refine service quality. Continuous risk assessment and emergency response planning are integral to maintain safety and reliability in challenging environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Drone_Design = Transition(label='Drone Design')
Regulatory_Check = Transition(label='Regulatory Check')
Nav_System = Transition(label='Nav System')
Partner_Setup = Transition(label='Partner Setup')
Operator_Training = Transition(label='Operator Training')
Test_Flights = Transition(label='Test Flights')
Weather_Review = Transition(label='Weather Review')
Route_Optimize = Transition(label='Route Optimize')
Parts_Logistics = Transition(label='Parts Logistics')
Feedback_Loop = Transition(label='Feedback Loop')
Risk_Assess = Transition(label='Risk Assess')
Emergency_Plan = Transition(label='Emergency Plan')
Compliance_Audit = Transition(label='Compliance Audit')
Data_Sync = Transition(label='Data Sync')
Service_Launch = Transition(label='Service Launch')

# Model the phased testing with weather review as a loop:
# Loop( 
#    A= Test Flights,
#    B= Weather Review
# )
Phased_Testing = OperatorPOWL(operator=Operator.LOOP, children=[Test_Flights, Weather_Review])

# Model customer feedback loop (Feedback Loop) likely repeats or is concurrent with Service Launch:
# We treat Feedback Loop as a concurrent activity to Service Launch

# Regulatory compliance and risk are likely sequential and parallel:
# Compliance Audit follows Regulatory Check and Risk Assess with Emergency Plan.

# Data Sync is likely after Feedback Loop and Risk/Emergency measures before final launch.

# Build partial order nodes
nodes = [
    Drone_Design,
    Regulatory_Check,
    Nav_System,
    Partner_Setup,
    Operator_Training,
    Phased_Testing,
    Route_Optimize,
    Parts_Logistics,
    Feedback_Loop,
    Risk_Assess,
    Emergency_Plan,
    Compliance_Audit,
    Data_Sync,
    Service_Launch,
]

root = StrictPartialOrder(nodes=nodes)

# Define order relations:
# 1) Drone Design is first activity
root.order.add_edge(Drone_Design, Regulatory_Check)
root.order.add_edge(Drone_Design, Nav_System)
root.order.add_edge(Drone_Design, Partner_Setup)

# 2) After Regulatory Check, Compliance Audit must be done
root.order.add_edge(Regulatory_Check, Compliance_Audit)

# 3) After Partner Setup and Nav System, Operator Training occurs
root.order.add_edge(Nav_System, Operator_Training)
root.order.add_edge(Partner_Setup, Operator_Training)

# 4) After Operator Training, start phased testing loop (Test Flights <-> Weather Review)
root.order.add_edge(Operator_Training, Phased_Testing)

# 5) After phased testing, optimize route and manage parts logistics
root.order.add_edge(Phased_Testing, Route_Optimize)
root.order.add_edge(Phased_Testing, Parts_Logistics)

# 6) Risk assess and emergency plan run in parallel sometime after Regulatory Check
root.order.add_edge(Regulatory_Check, Risk_Assess)
root.order.add_edge(Risk_Assess, Emergency_Plan)

# 7) Compliance Audit after Regulatory Check; Emergency Plan after Risk Assess.
# Let's allow Emergency Plan and Compliance Audit to proceed in parallel:
# Since Order edges already set (Regulatory_Check --> Compliance_Audit and Regulatory_Check --> Risk_Assess --> Emergency Plan)

# 8) Feedback Loop after parts logistics and route optimize (to gather feedback on operations)
root.order.add_edge(Route_Optimize, Feedback_Loop)
root.order.add_edge(Parts_Logistics, Feedback_Loop)

# 9) Data Sync after Feedback Loop and Emergency Plan
root.order.add_edge(Feedback_Loop, Data_Sync)
root.order.add_edge(Emergency_Plan, Data_Sync)

# 10) Service Launch after Data Sync and Compliance Audit
root.order.add_edge(Data_Sync, Service_Launch)
root.order.add_edge(Compliance_Audit, Service_Launch)