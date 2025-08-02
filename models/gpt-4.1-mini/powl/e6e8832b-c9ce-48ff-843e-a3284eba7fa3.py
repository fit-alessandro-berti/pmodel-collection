# Generated from: e6e8832b-c9ce-48ff-843e-a3284eba7fa3.json
# Description: This process outlines the steps for liquidating physical and digital assets located in multiple international jurisdictions without direct physical access. It involves remote valuation, compliance verification with local laws, digital auction setup, secure transfer of ownership, and final financial reconciliation. Given the complexity of cross-border regulations, fluctuating asset values, and cybersecurity risks, each activity must ensure transparency, legality, and efficient communication between remote teams, legal advisors, and buyers to maximize asset recovery while minimizing exposure to fraud and legal penalties.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity with exact labels
Asset_Listing = Transition(label='Asset Listing')
Valuation_Check = Transition(label='Valuation Check')
Compliance_Scan = Transition(label='Compliance Scan')
Legal_Review = Transition(label='Legal Review')
Remote_Audit = Transition(label='Remote Audit')
Auction_Setup = Transition(label='Auction Setup')
Bid_Monitoring = Transition(label='Bid Monitoring')
Fraud_Detection = Transition(label='Fraud Detection')
Ownership_Transfer = Transition(label='Ownership Transfer')
Payment_Clearing = Transition(label='Payment Clearing')
Tax_Calculation = Transition(label='Tax Calculation')
Fund_Allocation = Transition(label='Fund Allocation')
Dispute_Handling = Transition(label='Dispute Handling')
Report_Generation = Transition(label='Report Generation')
Stakeholder_Update = Transition(label='Stakeholder Update')

# Define fraud detection XOR choice (fraud detected or no fraud)
fraud_check = OperatorPOWL(operator=Operator.XOR, children=[Fraud_Detection, SilentTransition()])

# Define dispute handling choice: disputes handled or skipped
dispute = OperatorPOWL(operator=Operator.XOR, children=[Dispute_Handling, SilentTransition()])

# Define loop for bid monitoring and fraud detection (repeat bid monitoring if no fraud)
bid_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[Bid_Monitoring, fraud_check])

# Define final reconciliation partial order (tax calculation and fund allocation can be concurrent)
final_reconciliation = StrictPartialOrder(
    nodes=[Tax_Calculation, Fund_Allocation, dispute, Report_Generation, Stakeholder_Update]
)
# tax and fund allocation concurrent: no edges
# dispute after tax and fund allocation
final_reconciliation.order.add_edge(Tax_Calculation, dispute)
final_reconciliation.order.add_edge(Fund_Allocation, dispute)
# report generation after dispute handling
final_reconciliation.order.add_edge(dispute, Report_Generation)
# stakeholder update after report generation
final_reconciliation.order.add_edge(Report_Generation, Stakeholder_Update)

# Define the main partial order for the process
root = StrictPartialOrder(
    nodes=[
        Asset_Listing,
        Valuation_Check,
        Compliance_Scan,
        Legal_Review,
        Remote_Audit,
        Auction_Setup,
        bid_monitor_loop,
        Ownership_Transfer,
        Payment_Clearing,
        final_reconciliation,
    ]
)

# Define order edges according to logical process flow
root.order.add_edge(Asset_Listing, Valuation_Check)
root.order.add_edge(Valuation_Check, Compliance_Scan)
root.order.add_edge(Compliance_Scan, Legal_Review)
root.order.add_edge(Legal_Review, Remote_Audit)
root.order.add_edge(Remote_Audit, Auction_Setup)
root.order.add_edge(Auction_Setup, bid_monitor_loop)
root.order.add_edge(bid_monitor_loop, Ownership_Transfer)
root.order.add_edge(Ownership_Transfer, Payment_Clearing)
root.order.add_edge(Payment_Clearing, final_reconciliation)