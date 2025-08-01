# Generated from: 5c1cd56a-bca9-4a40-9c23-97919ef2118e.json
# Description: This process outlines the complex workflow involved in leasing customized drones for industrial inspection purposes. It includes client consultation to determine specific requirements, drone design adjustments, regulatory compliance checks, prototype testing, contract negotiation, insurance setup, pilot training scheduling, deployment planning, real-time monitoring, maintenance scheduling, data analytics delivery, feedback collection, renewal assessment, and end-of-lease asset recovery. Each step requires coordination between engineering, legal, operations, and customer service teams to ensure tailored solutions meet safety standards and client expectations while optimizing operational efficiency and minimizing downtime.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Client_Consult = Transition(label='Client Consult')
Design_Adjust = Transition(label='Design Adjust')
Compliance_Check = Transition(label='Compliance Check')
Prototype_Test = Transition(label='Prototype Test')
Contract_Sign = Transition(label='Contract Sign')
Insurance_Setup = Transition(label='Insurance Setup')
Pilot_Train = Transition(label='Pilot Train')
Deploy_Plan = Transition(label='Deploy Plan')
Realtime_Monitor = Transition(label='Real-time Monitor')
Schedule_Maintenance = Transition(label='Schedule Maintenance')
Data_Analytics = Transition(label='Data Analytics')
Collect_Feedback = Transition(label='Collect Feedback')
Renewal_Assess = Transition(label='Renewal Assess')
Asset_Recover = Transition(label='Asset Recover')
Invoice_Process = Transition(label='Invoice Process')

# Model the loop for ongoing operation & maintenance: 
# After deployment planning, monitoring ongoing operations, maintenance scheduling,
# data analytics, feedback collection, and renewal assessment may loop before final asset recovery.

# Loop body: from Real-time Monitor to Renewal Assess (except Asset Recover and Invoice Process)
operational_loop_nodes = [
    Realtime_Monitor,
    Schedule_Maintenance,
    Data_Analytics,
    Collect_Feedback,
    Renewal_Assess
]
operational_loop = StrictPartialOrder(nodes=operational_loop_nodes)
operational_loop.order.add_edge(Realtime_Monitor, Schedule_Maintenance)
operational_loop.order.add_edge(Schedule_Maintenance, Data_Analytics)
operational_loop.order.add_edge(Data_Analytics, Collect_Feedback)
operational_loop.order.add_edge(Collect_Feedback, Renewal_Assess)

# Loop: after Renewal Assess, either exit loop or return to Realtime_Monitor
loop = OperatorPOWL(operator=Operator.LOOP, children=[Realtime_Monitor, operational_loop])

# Strict partial order for the initial linear workflow up to deployment planning
initial_seq_nodes = [
    Client_Consult,
    Design_Adjust,
    Compliance_Check,
    Prototype_Test,
    Contract_Sign,
    Insurance_Setup,
    Pilot_Train,
    Deploy_Plan
]

initial_seq = StrictPartialOrder(nodes=initial_seq_nodes)
initial_seq.order.add_edge(Client_Consult, Design_Adjust)
initial_seq.order.add_edge(Design_Adjust, Compliance_Check)
initial_seq.order.add_edge(Compliance_Check, Prototype_Test)
initial_seq.order.add_edge(Prototype_Test, Contract_Sign)
initial_seq.order.add_edge(Contract_Sign, Insurance_Setup)
initial_seq.order.add_edge(Insurance_Setup, Pilot_Train)
initial_seq.order.add_edge(Pilot_Train, Deploy_Plan)

# Final steps after loop completion: Asset Recover and Invoice Process in sequence
final_seq = StrictPartialOrder(nodes=[Asset_Recover, Invoice_Process])
final_seq.order.add_edge(Asset_Recover, Invoice_Process)

# Combine initial sequence, loop, and final sequence in partial order
root = StrictPartialOrder(nodes=[initial_seq, loop, final_seq])
root.order.add_edge(initial_seq, loop)
root.order.add_edge(loop, final_seq)