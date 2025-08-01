# Generated from: 0d5885af-ffa2-40ad-a09c-10bf6b812536.json
# Description: This process involves the detailed verification and authentication of antique assets before acquisition or sale. It requires cross-referencing provenance records, conducting material analysis, consulting with historical experts, and validating ownership history. The process also includes condition assessment, restoration feasibility studies, legal compliance checks for cultural heritage, and coordinating with insurance providers to appraise value. Final approval must be documented in a secure ledger to ensure traceability and authenticity, integrating technological tools like blockchain for enhanced security and transparency in asset handling.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities as labeled transitions
Record_Review = Transition(label='Record Review')
Material_Test = Transition(label='Material Test')
Provenance_Check = Transition(label='Provenance Check')
Expert_Consult = Transition(label='Expert Consult')
Ownership_Confirm = Transition(label='Ownership Confirm')
Condition_Assess = Transition(label='Condition Assess')
Restoration_Plan = Transition(label='Restoration Plan')
Legal_Verify = Transition(label='Legal Verify')
Insurance_Quote = Transition(label='Insurance Quote')
Value_Appraise = Transition(label='Value Appraise')
Ledger_Entry = Transition(label='Ledger Entry')
Blockchain_Log = Transition(label='Blockchain Log')
Risk_Evaluate = Transition(label='Risk Evaluate')
Report_Draft = Transition(label='Report Draft')
Final_Approval = Transition(label='Final Approval')
Client_Notify = Transition(label='Client Notify')

# Partial orders for parallel verification activities after Record Review

# Verification branch 1: provenance, expert consult, ownership confirm
verif1_nodes = [Provenance_Check, Expert_Consult, Ownership_Confirm]
verif1 = StrictPartialOrder(nodes=verif1_nodes)
verif1.order.add_edge(Provenance_Check, Expert_Consult)
verif1.order.add_edge(Provenance_Check, Ownership_Confirm)
# Expert Consult and Ownership Confirm can be concurrent after Provenance Check
# (no order between Expert_Consult and Ownership_Confirm)

# Verification branch 2: Material Test
verif2 = Material_Test

# Combine verif1 and verif2 in partial order concurrency: both start after Record Review
verification = StrictPartialOrder(nodes=[verif1, verif2])
verification.order.add_edge(verif1, verif2)
# Actually, since both start after Record Review and concurrent, 
# make them concurrent - no edge
# So remove the above edge; make concurrent:
verification = StrictPartialOrder(nodes=[verif1, verif2])

# Restoration feasibility and condition assessment must be after verification
restoration = StrictPartialOrder(nodes=[Condition_Assess, Restoration_Plan])
restoration.order.add_edge(Condition_Assess, Restoration_Plan)

# Legal Verify and Insurance Quote can be concurrent after restoration
legal_insurance = StrictPartialOrder(nodes=[Legal_Verify, Insurance_Quote])
# No order between Legal Verify and Insurance Quote (concurrent)

# Value Appraise after legal and insurance
value_appraise = Value_Appraise

# Ledger Entry and Blockchain Log in parallel (integrated security and traceability)
ledger_blockchain = StrictPartialOrder(nodes=[Ledger_Entry, Blockchain_Log])
# concurrent, no edge

# Risk Evaluate and Report Draft can be concurrent
risk_report = StrictPartialOrder(nodes=[Risk_Evaluate, Report_Draft])

# Final Approval after ledger_blockchain and risk_report
final_approval = Final_Approval

# Client Notify after final_approval
client_notify = Client_Notify

# Build partial orders and edges stepwise:

# Step 1: After Record Review -> verification (verif1 and verif2 concurrent)
step1 = StrictPartialOrder(nodes=[Record_Review, verification])
step1.order.add_edge(Record_Review, verification)

# Step 2: After verification -> restoration (Condition Assess -> Restoration Plan)
step2 = StrictPartialOrder(nodes=[step1, restoration])
step2.order.add_edge(step1, restoration)

# Step 3: After restoration -> legal & insurance (concurrent)
step3 = StrictPartialOrder(nodes=[step2, legal_insurance])
step3.order.add_edge(step2, legal_insurance)

# Step 4: After legal_insurance -> Value Appraise
step4 = StrictPartialOrder(nodes=[step3, value_appraise])
step4.order.add_edge(step3, value_appraise)

# Step 5: After Value Appraise -> ledger_blockchain (concurrent Ledger Entry & Blockchain Log)
step5 = StrictPartialOrder(nodes=[step4, ledger_blockchain])
step5.order.add_edge(step4, ledger_blockchain)

# Step 6: After ledger_blockchain -> risk_report (Risk Evaluate & Report Draft concurrent)
step6 = StrictPartialOrder(nodes=[step5, risk_report])
step6.order.add_edge(step5, risk_report)

# Step 7: After risk_report -> Final Approval
step7 = StrictPartialOrder(nodes=[step6, final_approval])
step7.order.add_edge(step6, final_approval)

# Step 8: After Final Approval -> Client Notify
root = StrictPartialOrder(nodes=[step7, client_notify])
root.order.add_edge(step7, client_notify)