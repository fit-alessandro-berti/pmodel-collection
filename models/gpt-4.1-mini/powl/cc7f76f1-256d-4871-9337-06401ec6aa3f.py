# Generated from: cc7f76f1-256d-4871-9337-06401ec6aa3f.json
# Description: This process involves identifying, monitoring, and mitigating potential corporate espionage threats within a multinational organization. It begins with intelligence gathering from open and covert sources, followed by risk assessment and internal audits. Suspicious activities are flagged through behavioral analytics and network monitoring tools. Legal and compliance teams collaborate to ensure all countermeasures adhere to regulations. Employee training and awareness programs are conducted regularly to reduce insider threats. The process also includes incident response planning, simulation exercises, and continuous improvement cycles based on lessons learned from detected espionage attempts. Finally, partnerships with external cybersecurity firms and law enforcement agencies are maintained to strengthen overall defense capabilities and ensure rapid response to emerging threats.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Intel_Gathering = Transition(label='Intel Gathering')
Risk_Assess = Transition(label='Risk Assess')
Audit_Conduct = Transition(label='Audit Conduct')

Behavior_Scan = Transition(label='Behavior Scan')
Network_Monitor = Transition(label='Network Monitor')

Flag_Suspicion = Transition(label='Flag Suspicion')

Legal_Review = Transition(label='Legal Review')
Compliance_Check = Transition(label='Compliance Check')

Employee_Train = Transition(label='Employee Train')

Threat_Simulate = Transition(label='Threat Simulate')
Incident_Plan = Transition(label='Incident Plan')
Response_Drill = Transition(label='Response Drill')

Data_Encrypt = Transition(label='Data Encrypt')

Partner_Liaison = Transition(label='Partner Liaison')

Report_Generate = Transition(label='Report Generate')

Feedback_Loop = Transition(label='Feedback Loop')

# Step 1: Intelligence gathering sequence (Intel Gathering -> Risk Assess -> Audit Conduct)
intel_sequence = StrictPartialOrder(nodes=[Intel_Gathering, Risk_Assess, Audit_Conduct])
intel_sequence.order.add_edge(Intel_Gathering, Risk_Assess)
intel_sequence.order.add_edge(Risk_Assess, Audit_Conduct)

# Step 2: Behavioral analytics and network monitoring can run concurrently after auditing
behavior_network = StrictPartialOrder(nodes=[Behavior_Scan, Network_Monitor])
# no order between them means concurrent

# Step 3: Flag Suspicion depends on behavior and network monitoring
flag_after_monitors = StrictPartialOrder(
    nodes=[behavior_network, Flag_Suspicion]
)
flag_after_monitors.order.add_edge(behavior_network, Flag_Suspicion)

# Step 4: Legal Review and Compliance Check work collaboratively (concurrent)
legal_compliance = StrictPartialOrder(nodes=[Legal_Review, Compliance_Check])

# Both depend on Flag Suspicion
legal_compliance_after_flag = StrictPartialOrder(
    nodes=[flag_after_monitors, legal_compliance]
)
legal_compliance_after_flag.order.add_edge(flag_after_monitors, legal_compliance)

# Step 5: Employee Training is independent but logically after legal_compliance
emp_train_after_legal = StrictPartialOrder(
    nodes=[legal_compliance_after_flag, Employee_Train]
)
emp_train_after_legal.order.add_edge(legal_compliance_after_flag, Employee_Train)

# Step 6: Incident response planning (includes Incident Plan, Threat Simulate, Response Drill)
incident_response = StrictPartialOrder(
    nodes=[Incident_Plan, Threat_Simulate, Response_Drill]
)
# Incident Plan -> Threat Simulate -> Response Drill
incident_response.order.add_edge(Incident_Plan, Threat_Simulate)
incident_response.order.add_edge(Threat_Simulate, Response_Drill)

# Step 7: Data Encrypt after Incident Drill (maybe securing data after drills)
data_encrypt_after_response = StrictPartialOrder(
    nodes=[incident_response, Data_Encrypt]
)
data_encrypt_after_response.order.add_edge(incident_response, Data_Encrypt)

# Step 8: Partner Liaison and Report Generate can happen concurrently after Data Encrypt
partner_report = StrictPartialOrder(
    nodes=[Partner_Liaison, Report_Generate]
)
# no order between them

partner_report_after_encrypt = StrictPartialOrder(
    nodes=[data_encrypt_after_response, partner_report]
)
partner_report_after_encrypt.order.add_edge(data_encrypt_after_response, partner_report)

# Step 9: Feedback Loop is a loop structure that triggered after reports/partner liaison,
# and goes back to Risk Assess for continuous improvement
# LOOP(body: Feedback Loop, redo: Risk Assess)
loop = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Loop, Risk_Assess])

# Step 10: Construct the main partial order of the process:
# (intel_sequence -> behavior_network -> Flag Suspicion -> legal_compliance -> employee train)
# then parallel incident response sequence and partner/report steps,
# and finally the loop for continuous improvement

# Compose behavior_network and Flag Suspicion already in flag_after_monitors

first_big_seq = StrictPartialOrder(
    nodes=[intel_sequence, flag_after_monitors, legal_compliance, Employee_Train]
)
first_big_seq.order.add_edge(intel_sequence, flag_after_monitors)
first_big_seq.order.add_edge(flag_after_monitors, legal_compliance)
first_big_seq.order.add_edge(legal_compliance, Employee_Train)

# incident response and data encrypt after employee train
second_seq = StrictPartialOrder(
    nodes=[Employee_Train, data_encrypt_after_response]
)
second_seq.order.add_edge(Employee_Train, data_encrypt_after_response)

# partner_report after data encrypt included already in partner_report_after_encrypt
# so connect data_encrypt_after_response to partner_report
# Actually partner_report_after_encrypt = data_encrypt_after_response + partner_report with order edge
# So combine with second_seq properly:

second_seq_plus = StrictPartialOrder(
    nodes=[Employee_Train, partner_report_after_encrypt]
)
second_seq_plus.order.add_edge(Employee_Train, partner_report_after_encrypt)

# Finally connect first_big_seq to second_seq_plus (employee_train is common node so must unify)
# To unify nodes, we need to merge first_big_seq and second_seq_plus nodes properly

# We can create a root PO with all main parts:

root_nodes = [intel_sequence, flag_after_monitors, legal_compliance, Employee_Train,
              incident_response, data_encrypt_after_response,
              partner_report, Feedback_Loop, loop]

# But note Feedback_Loop and loop are in loop structure, and Risk_Assess is in intel_sequence

# We'll make root with all main components:
# Actually Intel sequence contains Risk_Assess node needed in loop children.
# The loop children must be references to existing nodes not copies.

# So define nodes including loop children:

root = StrictPartialOrder(
    nodes=[
        intel_sequence,     # contains Intel_Gathering->Risk_Assess->Audit_Conduct
        flag_after_monitors,# behavior_network + Flag Suspicion
        legal_compliance,   # legal + compliance
        Employee_Train,
        incident_response,  # incident plan->simulate->drill
        data_encrypt_after_response, # incident_response + data_encrypt
        partner_report,     # partner + report generate
        loop                # Feedback Loop and Risk_Assess loop
    ]
)

# Define order edges connecting these nodes:

root.order.add_edge(intel_sequence, flag_after_monitors)
root.order.add_edge(flag_after_monitors, legal_compliance)
root.order.add_edge(legal_compliance, Employee_Train)
root.order.add_edge(Employee_Train, incident_response)
root.order.add_edge(incident_response, data_encrypt_after_response)
root.order.add_edge(data_encrypt_after_response, partner_report)

# Connect the loop:

root.order.add_edge(partner_report, loop)

# The loop children are [Feedback_Loop, Risk_Assess] - Risk_Assess is inside intel_sequence
# It's safe because Risk_Assess is already part of intel_sequence (shared node).
