# Generated from: 8792e585-9a96-451e-9bed-69be84e0768c.json
# Description: This process involves the remote calibration of IoT sensor networks deployed in harsh and inaccessible environments such as deep forests or offshore platforms. The workflow starts with data acquisition from multiple sensor nodes, followed by anomaly detection using adaptive algorithms. Once anomalies are confirmed, the system initiates remote calibration commands, adjusting sensor parameters to maintain data accuracy. Periodic validation through cross-referencing sensor outputs ensures long-term reliability. Additionally, the process includes fallback manual overrides and synchronization with central data repositories to guarantee seamless integration and continuous monitoring despite network latency or disruptions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
DG = Transition(label="Data Grab")
AC = Transition(label="Anomaly Check")
SB = Transition(label="Signal Boost")
PA = Transition(label="Param Adjust")
ST = Transition(label="Sync Time")
VR = Transition(label="Validation Run")
CR = Transition(label="Cross Ref")
FA = Transition(label="Fallback Mode")
OC = Transition(label="Override Cmd")
SP = Transition(label="Status Poll")
EL = Transition(label="Error Log")
AS = Transition(label="Alert Send")
NR = Transition(label="Network Reset")
DA = Transition(label="Data Archive")
RG = Transition(label="Report Gen")
CE = Transition(label="Calibration End")

# 1) Calibration loop: check anomalies, if still present boost signal & adjust params, then repeat
B1 = StrictPartialOrder(nodes=[SB, PA])
B1.order.add_edge(SB, PA)
cal_loop = OperatorPOWL(operator=Operator.LOOP, children=[AC, B1])

# 2) Validation loop: run validation, then cross-reference, repeat until satisfied
val_loop = OperatorPOWL(operator=Operator.LOOP, children=[VR, CR])

# 3) Fallback branch: manual override sequence, then error handling, then alert/reset, then re-sync
# 3a) Error logging sequence
err_seq = StrictPartialOrder(nodes=[SP, EL])
err_seq.order.add_edge(SP, EL)
# 3b) Alert vs Reset choice
alert_reset = OperatorPOWL(operator=Operator.XOR, children=[AS, NR])
# 3c) full fallback branch
fb_nodes = [FA, OC, err_seq, alert_reset]
fallback_branch = StrictPartialOrder(nodes=fb_nodes)
fallback_branch.order.add_edge(FA, OC)
fallback_branch.order.add_edge(OC, err_seq)
fallback_branch.order.add_edge(err_seq, alert_reset)

# 4) Normal completion branch: archive, report, end
normal_branch = StrictPartialOrder(nodes=[DA, RG, CE])
normal_branch.order.add_edge(DA, RG)
normal_branch.order.add_edge(RG, CE)

# 5) Choice between normal completion or fallback
end_choice = OperatorPOWL(operator=Operator.XOR, children=[normal_branch, fallback_branch])

# 6) Assemble full workflow as a strict partial order
root = StrictPartialOrder(nodes=[DG, cal_loop, ST, val_loop, end_choice])
root.order.add_edge(DG, cal_loop)
root.order.add_edge(cal_loop, ST)
root.order.add_edge(ST, val_loop)
root.order.add_edge(val_loop, end_choice)