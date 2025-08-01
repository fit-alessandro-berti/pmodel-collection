# Generated from: ebe69634-86f5-4294-9a1c-020b1fb61df4.json
# Description: This process involves brokering custom artificial intelligence models between specialized developers and niche industry clients. It starts with client requirements gathering, followed by matching suitable AI developers with specific domain expertise. After initial vetting, prototype models are created and iteratively refined through collaborative feedback loops. Licensing agreements and intellectual property negotiations take place before final deployment. Post-deployment monitoring and optimization services ensure models remain effective. The process integrates legal, technical, and commercial teams to balance innovation with compliance, resulting in tailored AI solutions delivered through a secure and transparent platform.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as transitions
Client_Intake = Transition(label='Client Intake')
Needs_Analysis = Transition(label='Needs Analysis')
Developer_Match = Transition(label='Developer Match')
Expert_Vetting = Transition(label='Expert Vetting')
Prototype_Build = Transition(label='Prototype Build')
Feedback_Loop = Transition(label='Feedback Loop')
Model_Refinement = Transition(label='Model Refinement')
License_Draft = Transition(label='License Draft')
IP_Negotiation = Transition(label='IP Negotiation')
Contract_Sign = Transition(label='Contract Sign')
Deployment_Prep = Transition(label='Deployment Prep')
Go_Live = Transition(label='Go Live')
Monitor_Model = Transition(label='Monitor Model')
Optimize_AI = Transition(label='Optimize AI')
Support_Handoff = Transition(label='Support Handoff')
Compliance_Check = Transition(label='Compliance Check')
Final_Review = Transition(label='Final Review')

# Define the iterative feedback loop part as a loop:
# Loop body A = Prototype Build
# Loop condition B = Feedback Loop and Model Refinement in partial order (Feedback Loop --> Model Refinement)
feedback_partial = StrictPartialOrder(nodes=[Feedback_Loop, Model_Refinement])
feedback_partial.order.add_edge(Feedback_Loop, Model_Refinement)
loop = OperatorPOWL(operator=Operator.LOOP, children=[Prototype_Build, feedback_partial])

# Define the legal negotiation partial order: License Draft --> IP Negotiation --> Contract Sign
legal_partial = StrictPartialOrder(nodes=[License_Draft, IP_Negotiation, Contract_Sign])
legal_partial.order.add_edge(License_Draft, IP_Negotiation)
legal_partial.order.add_edge(IP_Negotiation, Contract_Sign)

# Define the post deployment partial order: Monitor Model --> Optimize AI --> Support Handoff
post_deploy_partial = StrictPartialOrder(nodes=[Monitor_Model, Optimize_AI, Support_Handoff])
post_deploy_partial.order.add_edge(Monitor_Model, Optimize_AI)
post_deploy_partial.order.add_edge(Optimize_AI, Support_Handoff)

# Compliance Check and Final Review after Contract Sign but before Deployment Prep
# Deployment Prep and Go Live sequence
deployment_partial = StrictPartialOrder(nodes=[Compliance_Check, Final_Review, Deployment_Prep, Go_Live])
deployment_partial.order.add_edge(Compliance_Check, Final_Review)
deployment_partial.order.add_edge(Final_Review, Deployment_Prep)
deployment_partial.order.add_edge(Deployment_Prep, Go_Live)

# Main partial order nodes
# Client Intake --> Needs Analysis --> Developer Match --> Expert Vetting --> loop --> legal_partial --> deployment_partial --> post_deploy_partial
nodes_main = [Client_Intake, Needs_Analysis, Developer_Match, Expert_Vetting, loop, legal_partial, deployment_partial, post_deploy_partial]

root = StrictPartialOrder(nodes=nodes_main)
root.order.add_edge(Client_Intake, Needs_Analysis)
root.order.add_edge(Needs_Analysis, Developer_Match)
root.order.add_edge(Developer_Match, Expert_Vetting)
root.order.add_edge(Expert_Vetting, loop)
root.order.add_edge(loop, legal_partial)
root.order.add_edge(legal_partial, deployment_partial)
root.order.add_edge(deployment_partial, post_deploy_partial)