# Generated from: 842a1b3f-1cbd-45dd-9bda-5a7fc5be5312.json
# Description: This process involves managing the leasing of physical and digital assets through a decentralized blockchain platform. It includes asset registration, verification, dynamic pricing based on market demand, automated smart contract deployment, real-time usage monitoring, dispute mediation via decentralized arbitration, and revenue distribution to multiple stakeholders. The process ensures transparency, security, and efficiency by leveraging cryptographic proofs and tokenized incentives while accommodating fluctuating availability and multi-party agreements across different jurisdictions. It also incorporates periodic audits, renewal notifications, and cross-chain asset interoperability to maintain compliance and maximize utilization.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
ar = Transition(label='Asset Register')
vi = Transition(label='Verify Identity')
sp = Transition(label='Set Pricing')
dc = Transition(label='Deploy Contract')
mu = Transition(label='Monitor Usage')
cp = Transition(label='Collect Payment')
dr = Transition(label='Dispute Review')
av = Transition(label='Arbitration Vote')
df = Transition(label='Distribute Fees')
rl = Transition(label='Renew Lease')
au = Transition(label='Audit Records')
np = Transition(label='Notify Parties')
ccs = Transition(label='Cross-Chain Sync')
at = Transition(label='Adjust Terms')
su = Transition(label='Stakeholder Update')
skip = SilentTransition()

# Model dispute handling loop: Dispute Review followed by Arbitration Vote could repeat until exit
dispute_loop = OperatorPOWL(operator=Operator.LOOP, children=[dr, av])

# Revenue distribution after possible disputes handled
distribute_and_update = StrictPartialOrder(nodes=[df, su])
# df and su likely parallel (both stakeholder-relevant activities)
# no edges => concurrent

# Define audit and notification as a partial order where audit precedes notify
audit_notify = StrictPartialOrder(nodes=[au, np])
audit_notify.order.add_edge(au, np)

# The "Adjust Terms" and "Cross-Chain Sync" can be concurrent after usage monitoring and renewal
adjust_crosschain = StrictPartialOrder(nodes=[at, ccs])

# Lease renewal after notification, before adjustments
renew_process = StrictPartialOrder(nodes=[rl, audit_notify, adjust_crosschain])

# Set edges in renew_process
renew_process.order.add_edge(rl, audit_notify)
renew_process.order.add_edge(audit_notify, adjust_crosschain)
# The order.add_edge with StrictPartialOrder and with nodes being OperatorPOWL and StrictPartialOrder is allowed

# The assets registration and verification are sequential initial activities
init_seq = StrictPartialOrder(nodes=[ar, vi, sp])
init_seq.order.add_edge(ar, vi)
init_seq.order.add_edge(vi, sp)

# After pricing, deploy contract
deploy_after_pricing = StrictPartialOrder(nodes=[sp, dc])
deploy_after_pricing.order.add_edge(sp, dc)

# Collect Payment and Monitor Usage are concurrent activities after contract deployment
usage_payment = StrictPartialOrder(nodes=[mu, cp])
# no order, can happen concurrently

# After monitoring usage and collecting payment, dispute handling can happen (choice: dispute or no dispute)
dispute_choice = OperatorPOWL(operator=Operator.XOR, children=[dispute_loop, skip])

# Sequence: deploy contract --> (monitor usage & collect payment) --> dispute_choice
after_deploy_seq = StrictPartialOrder(nodes=[dc, usage_payment, dispute_choice])
after_deploy_seq.order.add_edge(dc, usage_payment)
after_deploy_seq.order.add_edge(usage_payment, dispute_choice)

# After dispute resolved / skipped, distribute fees and stakeholder update concurrent
# Then renewal process (notify, audit, adjust, cross-chain)
final_seq = StrictPartialOrder(nodes=[distribute_and_update, renew_process])
final_seq.order.add_edge(distribute_and_update, renew_process)

# Compose whole model in partial order:
# Initialization sequence -> deploy contract after pricing -> concurrent monitor & collect -> dispute choice -> final sequence

# For clarity, capture deploy_after_pricing and init_seq such that deploy_after_pricing overlaps with init_seq

# We will create a unified initial sequence: ar -> vi -> sp -> dc
initial_deploy = StrictPartialOrder(nodes=[ar, vi, sp, dc])
initial_deploy.order.add_edge(ar, vi)
initial_deploy.order.add_edge(vi, sp)
initial_deploy.order.add_edge(sp, dc)

# usage_payment after deploy
stage1 = StrictPartialOrder(nodes=[initial_deploy, usage_payment])
stage1.order.add_edge(initial_deploy, usage_payment)

# dispute_choice after usage_payment
stage2 = StrictPartialOrder(nodes=[stage1, dispute_choice])
stage2.order.add_edge(stage1, dispute_choice)

# final_seq after dispute_choice
root = StrictPartialOrder(nodes=[stage2, final_seq])
root.order.add_edge(stage2, final_seq)