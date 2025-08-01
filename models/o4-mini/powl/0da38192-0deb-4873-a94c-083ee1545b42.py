# Generated from: 0da38192-0deb-4873-a94c-083ee1545b42.json
# Description: This process involves managing the leasing of physical and digital assets through a decentralized blockchain platform. It includes asset registration, verification, dynamic pricing based on market demand, automated smart contract generation, multi-party consensus validation, real-time usage tracking, dispute resolution via decentralized arbitration, and seamless payment settlements. The process ensures transparency, reduces intermediaries, and enables fractional leasing, while maintaining compliance with regulatory frameworks through automated reporting and audit trails. Stakeholders include asset owners, lessees, validators, and compliance officers, all interacting within a secure, distributed environment to optimize asset utilization and revenue streams.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define basic activities
ar = Transition(label='Asset Register')
vo = Transition(label='Verify Ownership')
pe = Transition(label='Price Evaluate')
cd = Transition(label='Contract Draft')
cc = Transition(label='Consensus Check')
la = Transition(label='Lease Approve')
ut = Transition(label='Usage Track')
pi = Transition(label='Payment Initiate')
ds = Transition(label='Dispute Submit')
ar2 = Transition(label='Arbitration Review')
sp = Transition(label='Settlement Process')
ct = Transition(label='Contract Terminate')
caud = Transition(label='Compliance Audit')
rg = Transition(label='Report Generate')
ac = Transition(label='Access Control')

# Silent transitions for XOR choices
skip_frac = SilentTransition()
skip_disp = SilentTransition()

# XOR for fractional leasing (either do fractional lease, or skip it)
fl = Transition(label='Fractional Lease')
xor_frac = OperatorPOWL(operator=Operator.XOR, children=[fl, skip_frac])

# Loop for ongoing usage tracking and payment
loop_usage = OperatorPOWL(operator=Operator.LOOP, children=[ut, pi])

# Sub‐process for dispute resolution
po_dispute = StrictPartialOrder(nodes=[ds, ar2, sp])
po_dispute.order.add_edge(ds, ar2)
po_dispute.order.add_edge(ar2, sp)

# XOR for dispute resolution (either handle a dispute or skip)
xor_disp = OperatorPOWL(operator=Operator.XOR, children=[po_dispute, skip_disp])

# Assemble the top‐level partial order
root = StrictPartialOrder(nodes=[
    ar, vo, pe, cd, cc, la,
    xor_frac,
    ac,
    loop_usage,
    xor_disp,
    ct,
    caud, rg
])

# Define the control‐flow dependencies
# 1. Linear sequence up to lease approval
root.order.add_edge(ar, vo)
root.order.add_edge(vo, pe)
root.order.add_edge(pe, cd)
root.order.add_edge(cd, cc)
root.order.add_edge(cc, la)

# 2. Fractional lease choice after lease approval
root.order.add_edge(la, xor_frac)

# 3. After fractional lease decision, grant access and start usage loop in parallel
root.order.add_edge(xor_frac, ac)
root.order.add_edge(xor_frac, loop_usage)

# 4. Once access control and usage loop complete, optionally handle disputes
root.order.add_edge(ac, xor_disp)
root.order.add_edge(loop_usage, xor_disp)

# 5. After dispute resolution, terminate the contract
root.order.add_edge(xor_disp, ct)

# 6. After termination, run compliance audit and report generation in parallel
root.order.add_edge(ct, caud)
root.order.add_edge(ct, rg)