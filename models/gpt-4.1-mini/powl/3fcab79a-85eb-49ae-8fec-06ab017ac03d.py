# Generated from: 3fcab79a-85eb-49ae-8fec-06ab017ac03d.json
# Description: This process governs the complex flow of licensing dynamic, generative art pieces to multiple digital platforms under varying usage rights and time-bound exclusivity. It involves continuous monitoring of artwork versioning, real-time negotiation of terms based on AI-generated demand forecasts, adaptive royalty recalculations, cross-platform synchronization of rights management, and automated dispute resolution triggered by unauthorized derivative works or usage breaches. The process requires coordination between legal, technical, and creative teams to ensure compliance, optimize revenue streams, and maintain artistic integrity while navigating multi-jurisdictional intellectual property laws and evolving digital distribution standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
ArtSubmission = Transition(label='Art Submission')
VersionControl = Transition(label='Version Control')
DemandForecast = Transition(label='Demand Forecast')
RightsReview = Transition(label='Rights Review')
TermNegotiation = Transition(label='Term Negotiation')
ContractDraft = Transition(label='Contract Draft')
RoyaltySetup = Transition(label='Royalty Setup')
PlatformSync = Transition(label='Platform Sync')
UsageMonitor = Transition(label='Usage Monitor')
DisputeTrigger = Transition(label='Dispute Trigger')
LegalConsult = Transition(label='Legal Consult')
PaymentProcess = Transition(label='Payment Process')
ComplianceCheck = Transition(label='Compliance Check')
DataBackup = Transition(label='Data Backup')
ReportGenerate = Transition(label='Report Generate')
RenewalAlert = Transition(label='Renewal Alert')

# The process description suggests these general partial orders and loops:
# 1) Art submission -> Version control -> Demand forecast
# 2) After Demand forecast, Rights review and Term negotiation are done in sequence
# 3) Contract draft follows Term negotiation, then Royalty setup
# 4) Platform sync happens after Royalty setup and is concurrent with Usage monitor
# 5) Usage monitor leads to Dispute trigger possibility, which leads to Legal consult and then Payment process
# 6) Compliance check and Data backup run concurrently after Payment process
# 7) Report generate depends on Compliance check and Data backup
# 8) Renewal alert involves looping over part of the process, typically after Report generate back to Term negotiation for contract renewal

# Construct a loop for renewal cycles:
# Loop body is renewal activities starting from Term negotiation, Contract draft, Royalty setup, Platform sync, Usage monitor, Dispute Trigger, Legal Consult, Payment Process, Compliance Check, Data Backup, Report Generate
# After Report Generate, option to exit or loop again via Renewal Alert to Term Negotiation

# Build the PO partial order for the main flow within the loop body

loop_body_nodes = [
    TermNegotiation,
    ContractDraft,
    RoyaltySetup,
    PlatformSync,
    UsageMonitor,
    DisputeTrigger,
    LegalConsult,
    PaymentProcess,
    ComplianceCheck,
    DataBackup,
    ReportGenerate
]

loop_body = StrictPartialOrder(nodes=loop_body_nodes)

# Add order edges inside loop body

# Term negotiation -> Contract draft -> Royalty setup
loop_body.order.add_edge(TermNegotiation, ContractDraft)
loop_body.order.add_edge(ContractDraft, RoyaltySetup)

# Royalty setup -> Platform sync and Usage monitor concurrent start
loop_body.order.add_edge(RoyaltySetup, PlatformSync)
loop_body.order.add_edge(RoyaltySetup, UsageMonitor)

# Usage monitor -> Dispute trigger
loop_body.order.add_edge(UsageMonitor, DisputeTrigger)

# Dispute trigger -> Legal consult -> Payment process
loop_body.order.add_edge(DisputeTrigger, LegalConsult)
loop_body.order.add_edge(LegalConsult, PaymentProcess)

# Payment process -> Compliance check and Data backup concurrent start
loop_body.order.add_edge(PaymentProcess, ComplianceCheck)
loop_body.order.add_edge(PaymentProcess, DataBackup)

# Compliance check and Data backup -> Report generate
loop_body.order.add_edge(ComplianceCheck, ReportGenerate)
loop_body.order.add_edge(DataBackup, ReportGenerate)

# Renewal alert triggers a loop: choose to exit or to renew the loop with Term negotiation again

# Construct the loop node
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, RenewalAlert])

# Now build the initial partial order before the loop:

initial_nodes = [
    ArtSubmission,
    VersionControl,
    DemandForecast,
    RightsReview,
    loop
]

initial_po = StrictPartialOrder(nodes=initial_nodes)

# Add orders:

# Art Submission -> Version Control -> Demand Forecast
initial_po.order.add_edge(ArtSubmission, VersionControl)
initial_po.order.add_edge(VersionControl, DemandForecast)

# Demand Forecast -> Rights Review -> loop starts at Term Negotiation (inside loop)
initial_po.order.add_edge(DemandForecast, RightsReview)
initial_po.order.add_edge(RightsReview, loop)

# Final root is the initial partial order with the loop as part of the flow

root = initial_po