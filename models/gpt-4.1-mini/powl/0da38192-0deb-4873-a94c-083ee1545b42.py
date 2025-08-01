# Generated from: 0da38192-0deb-4873-a94c-083ee1545b42.json
# Description: This process involves managing the leasing of physical and digital assets through a decentralized blockchain platform. It includes asset registration, verification, dynamic pricing based on market demand, automated smart contract generation, multi-party consensus validation, real-time usage tracking, dispute resolution via decentralized arbitration, and seamless payment settlements. The process ensures transparency, reduces intermediaries, and enables fractional leasing, while maintaining compliance with regulatory frameworks through automated reporting and audit trails. Stakeholders include asset owners, lessees, validators, and compliance officers, all interacting within a secure, distributed environment to optimize asset utilization and revenue streams.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Asset_Register = Transition(label='Asset Register')
Verify_Ownership = Transition(label='Verify Ownership')
Price_Evaluate = Transition(label='Price Evaluate')
Contract_Draft = Transition(label='Contract Draft')
Consensus_Check = Transition(label='Consensus Check')
Lease_Approve = Transition(label='Lease Approve')
Payment_Initiate = Transition(label='Payment Initiate')
Usage_Track = Transition(label='Usage Track')
Dispute_Submit = Transition(label='Dispute Submit')
Arbitration_Review = Transition(label='Arbitration Review')
Settlement_Process = Transition(label='Settlement Process')
Compliance_Audit = Transition(label='Compliance Audit')
Report_Generate = Transition(label='Report Generate')
Fractional_Lease = Transition(label='Fractional Lease')
Access_Control = Transition(label='Access Control')
Contract_Terminate = Transition(label='Contract Terminate')

# Silent step for internal synchronization if needed
skip = SilentTransition()

# Loop structure for dispute management:
# loop body = Dispute_Submit -> Arbitration_Review
dispute_loop_body = StrictPartialOrder(nodes=[Dispute_Submit, Arbitration_Review])
dispute_loop_body.order.add_edge(Dispute_Submit, Arbitration_Review)
dispute_management = OperatorPOWL(operator=Operator.LOOP, children=[dispute_loop_body, skip])

# Loop for usage tracking and fractional leasing (they may repeat until contract termination)
usage_fractional = StrictPartialOrder(nodes=[Usage_Track, Fractional_Lease])
usage_fractional.order.add_edge(Usage_Track, Fractional_Lease)
usage_loop = OperatorPOWL(operator=Operator.LOOP, children=[usage_fractional, skip])

# Compliance sub-process: Compliance_Audit -> Report_Generate
compliance_sub = StrictPartialOrder(nodes=[Compliance_Audit, Report_Generate])
compliance_sub.order.add_edge(Compliance_Audit, Report_Generate)

# Contract lifecycle: Contract_Draft -> Consensus_Check -> Lease_Approve -> Access_Control
contract_lifecycle = StrictPartialOrder(
    nodes=[Contract_Draft, Consensus_Check, Lease_Approve, Access_Control]
)
contract_lifecycle.order.add_edge(Contract_Draft, Consensus_Check)
contract_lifecycle.order.add_edge(Consensus_Check, Lease_Approve)
contract_lifecycle.order.add_edge(Lease_Approve, Access_Control)

# Payment and settlement: Payment_Initiate -> Settlement_Process
payment_sub = StrictPartialOrder(nodes=[Payment_Initiate, Settlement_Process])
payment_sub.order.add_edge(Payment_Initiate, Settlement_Process)

# Root partial order nodes and structure follow main sequence:
# Asset_Register -> Verify_Ownership -> Price_Evaluate -> contract_lifecycle -> payment_sub
# -> usage_loop (Usage_Track + Fractional_Lease repeating)
# Meanwhile compliance_sub and dispute_management are concurrent with usage_loop and payment

root = StrictPartialOrder(
    nodes=[
        Asset_Register,
        Verify_Ownership,
        Price_Evaluate,
        contract_lifecycle,
        payment_sub,
        usage_loop,
        dispute_management,
        compliance_sub,
        Contract_Terminate,
    ]
)

# Define control flow dependencies:
root.order.add_edge(Asset_Register, Verify_Ownership)
root.order.add_edge(Verify_Ownership, Price_Evaluate)
root.order.add_edge(Price_Evaluate, contract_lifecycle)
root.order.add_edge(contract_lifecycle, payment_sub)
root.order.add_edge(payment_sub, usage_loop)

# Contract terminate should happen after usage and dispute resolution finish
root.order.add_edge(usage_loop, Contract_Terminate)
root.order.add_edge(dispute_management, Contract_Terminate)

# Compliance audit and reporting can happen concurrently with usage_loop and dispute_management,
# but for clarity place it after Price_Evaluate and concurrent with contract lifecycle
root.order.add_edge(Price_Evaluate, compliance_sub)

# Compliance and dispute management do not depend on each other or usage_loop strongly,
# They all precede Contract_Terminate.

# No explicit order edges between compliance_sub, usage_loop, dispute_management to represent concurrency.

# Final POWL model is root