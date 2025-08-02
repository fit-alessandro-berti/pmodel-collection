# Generated from: 05332ff8-4cf2-481c-8a8b-8175180b81db.json
# Description: This process involves integrating disparate industry insights to generate breakthrough innovations. It begins with cross-sector trend scanning, followed by ideation workshops leveraging diverse experts. Concepts undergo rapid prototyping paired with real-time user feedback loops. Concurrently, risk assessments and regulatory reviews ensure viability. Iterative refinement cycles incorporate market simulation data. Final outputs include scalable business models and tailored go-to-market strategies, all orchestrated through agile governance and continuous knowledge sharing across departments to accelerate adoption and impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Trend_Scan = Transition(label='Trend Scan')
Expert_Sync = Transition(label='Expert Sync')
Idea_Sprint = Transition(label='Idea Sprint')
Proto_Build = Transition(label='Proto Build')
User_Test = Transition(label='User Test')
Risk_Review = Transition(label='Risk Review')
Reg_Review = Transition(label='Reg Review')
Market_Sim = Transition(label='Market Sim')
Feedback_Loop = Transition(label='Feedback Loop')
Model_Design = Transition(label='Model Design')
Strategy_Plan = Transition(label='Strategy Plan')
Agile_Align = Transition(label='Agile Align')
Data_Share = Transition(label='Data Share')
Impact_Assess = Transition(label='Impact Assess')
Launch_Prep = Transition(label='Launch Prep')

# Loop: iterative refinement cycles incorporating market simulation data
# Loop body B: (Market Sim --> Feedback Loop)
loop_B = StrictPartialOrder(nodes=[Market_Sim, Feedback_Loop])
loop_B.order.add_edge(Market_Sim, Feedback_Loop)

# Loop body A: (Model Design --> Strategy Plan)
loop_A = StrictPartialOrder(nodes=[Model_Design, Strategy_Plan])
loop_A.order.add_edge(Model_Design, Strategy_Plan)

# Create loop node: execute A, then either exit or execute B then A again
refinement_loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_A, loop_B])

# Partial Order: proto build + user test sequential
proto_user = StrictPartialOrder(nodes=[Proto_Build, User_Test])
proto_user.order.add_edge(Proto_Build, User_Test)

# Risk and regulatory reviews concurrent
risk_reg = StrictPartialOrder(nodes=[Risk_Review, Reg_Review])  # no edges means concurrent

# Agile Align, Data Share, Impact Assess concurrent (continuous knowledge sharing and governance)
governance_concurrent = StrictPartialOrder(nodes=[Agile_Align, Data_Share, Impact_Assess])  # concurrent

# Final outputs in sequence: Model Design (from loop), Strategy Plan (from loop), Launch Prep
final_outputs = StrictPartialOrder(nodes=[refinement_loop, Launch_Prep])
final_outputs.order.add_edge(refinement_loop, Launch_Prep)

# Partial order for concept prototyping and feedback loops concurrent with risk and reg reviews
proto_risk_reg = StrictPartialOrder(nodes=[proto_user, risk_reg])
# No order edges between proto_user and risk_reg means they run concurrently

# Next phase after ideation workshops is the prototyping+user test + risk&reg reviews concurrency
# Sequence: Trend Scan --> Expert Sync --> Idea Sprint --> (proto_risk_reg concurrent) --> final_outputs and governance

# Combine top-level sequence nodes first: Trend_Scan --> Expert_Sync --> Idea_Sprint
start_seq = StrictPartialOrder(nodes=[Trend_Scan, Expert_Sync, Idea_Sprint])
start_seq.order.add_edge(Trend_Scan, Expert_Sync)
start_seq.order.add_edge(Expert_Sync, Idea_Sprint)

# Combine Idea Sprint --> proto_risk_reg concurrent (proto_user and risk_reg)
partial_after_idea = StrictPartialOrder(nodes=[Idea_Sprint, proto_user, risk_reg])
partial_after_idea.order.add_edge(Idea_Sprint, proto_user)
partial_after_idea.order.add_edge(Idea_Sprint, risk_reg)

# Combine entire process with final outputs and governance concurrent after proto_risk_reg
final_phase = StrictPartialOrder(nodes=[proto_risk_reg, final_outputs, governance_concurrent])
# proto_risk_reg must finish before final_outputs and governance start
final_phase.order.add_edge(proto_risk_reg, final_outputs)
final_phase.order.add_edge(proto_risk_reg, governance_concurrent)

# Now the root model nodes are start_seq, partial_after_idea, final_phase
root = StrictPartialOrder(nodes=[start_seq, partial_after_idea, final_phase])
root.order.add_edge(start_seq, partial_after_idea)
root.order.add_edge(partial_after_idea, final_phase)