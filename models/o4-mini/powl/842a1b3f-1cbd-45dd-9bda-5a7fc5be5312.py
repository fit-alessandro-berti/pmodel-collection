# Generated from: 842a1b3f-1cbd-45dd-9bda-5a7fc5be5312.json
# Description: This process involves managing the leasing of physical and digital assets through a decentralized blockchain platform. It includes asset registration, verification, dynamic pricing based on market demand, automated smart contract deployment, real-time usage monitoring, dispute mediation via decentralized arbitration, and revenue distribution to multiple stakeholders. The process ensures transparency, security, and efficiency by leveraging cryptographic proofs and tokenized incentives while accommodating fluctuating availability and multi-party agreements across different jurisdictions. It also incorporates periodic audits, renewal notifications, and cross-chain asset interoperability to maintain compliance and maximize utilization.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
reg = Transition(label='Asset Register')
verify = Transition(label='Verify Identity')
pricing = Transition(label='Set Pricing')
deploy = Transition(label='Deploy Contract')
monitor = Transition(label='Monitor Usage')
sync = Transition(label='Cross-Chain Sync')
payment = Transition(label='Collect Payment')
dispute = Transition(label='Dispute Review')
vote = Transition(label='Arbitration Vote')
dist = Transition(label='Distribute Fees')
update = Transition(label='Stakeholder Update')
renew = Transition(label='Renew Lease')
audit = Transition(label='Audit Records')
notify = Transition(label='Notify Parties')
adjust = Transition(label='Adjust Terms')

# Dispute-resolution choice: either do review+vote or skip
skip = SilentTransition()
dispute_branch = StrictPartialOrder(nodes=[dispute, vote])
dispute_branch.order.add_edge(dispute, vote)
dispute_xor = OperatorPOWL(operator=Operator.XOR, children=[dispute_branch, skip])

# Core leasing cycle
core = StrictPartialOrder(
    nodes=[pricing, deploy, monitor, sync, payment, dispute_xor, dist, update]
)
core.order.add_edge(pricing, deploy)
core.order.add_edge(deploy, monitor)
core.order.add_edge(deploy, sync)
core.order.add_edge(monitor, payment)
core.order.add_edge(sync, payment)
core.order.add_edge(payment, dispute_xor)
core.order.add_edge(dispute_xor, dist)
core.order.add_edge(dist, update)

# Renewal/adaptation steps to repeat
renewal_steps = StrictPartialOrder(nodes=[renew, audit, notify, adjust])
renewal_steps.order.add_edge(renew, audit)
renewal_steps.order.add_edge(audit, notify)
renewal_steps.order.add_edge(notify, adjust)

# Loop: execute core cycle, then optionally do renewal steps and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[core, renewal_steps])

# Root process: registration, identity check, then leasing loop
root = StrictPartialOrder(nodes=[reg, verify, loop])
root.order.add_edge(reg, verify)
root.order.add_edge(verify, loop)