# Generated from: dc8d320c-660d-4071-ac0c-2bb1701c5a96.json
# Description: This process involves the detailed verification and authentication of antique artifacts before acquisition or sale. It includes provenance research, material analysis, historical context validation, expert consultation, and legal compliance checks. Each artifact undergoes multi-stage verification to ensure authenticity, prevent fraud, and assess value accurately. The process also incorporates digital cataloging, condition reporting, and restoration recommendations, culminating in final approval or rejection for market entry.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

ArtifactIntake = Transition(label='Artifact Intake')

# Multi-stage verification as a partial order of provenance research, material analysis, historical review
ProvenanceCheck = Transition(label='Provenance Check')
MaterialTesting = Transition(label='Material Testing')
HistoricalReview = Transition(label='Historical Review')
VerificationPO = StrictPartialOrder(nodes=[ProvenanceCheck, MaterialTesting, HistoricalReview])
# All concurrent (no order edges)

# Expert consultation and forgery detection in parallel after verification
ExpertInterview = Transition(label='Expert Interview')
ForgeryDetection = Transition(label='Forgery Detection')
ExpertForgeryPO = StrictPartialOrder(nodes=[ExpertInterview, ForgeryDetection])
# concurrent

# Condition audit and digital catalog in parallel after expert/forgery checks
ConditionAudit = Transition(label='Condition Audit')
DigitalCatalog = Transition(label='Digital Catalog')
ConditionDigitalPO = StrictPartialOrder(nodes=[ConditionAudit, DigitalCatalog])
# concurrent

# Legal compliance check after condition and digital catalog
LegalCompliance = Transition(label='Legal Compliance')

# Restoration plan, valuation and market analysis after legal compliance, partially ordered with Restoration before Valuation and MarketAnalysis concurrent
RestorationPlan = Transition(label='Restoration Plan')
ValuationReport = Transition(label='Valuation Report')
MarketAnalysis = Transition(label='Market Analysis')

RestorationValuationMarketPO = StrictPartialOrder(nodes=[RestorationPlan, ValuationReport, MarketAnalysis])
RestorationValuationMarketPO.order.add_edge(RestorationPlan, ValuationReport)
# MarketAnalysis concurrent with both

# Final approval and sale preparation after those
FinalApproval = Transition(label='Final Approval')
SalePreparation = Transition(label='Sale Preparation')
# SalePreparation after FinalApproval
FinalSalePO = StrictPartialOrder(nodes=[FinalApproval, SalePreparation])
FinalSalePO.order.add_edge(FinalApproval, SalePreparation)

# Client notification last
ClientNotification = Transition(label='Client Notification')

# Construct the full process partial orders and combine in sequence with appropriate ordering

# Step 1: Artifact Intake -> VerificationPO (Provenance, Material, Historical)
Step1and2 = StrictPartialOrder(nodes=[ArtifactIntake, VerificationPO])
Step1and2.order.add_edge(ArtifactIntake, VerificationPO)

# Step 3: ExpertForgeryPO after VerificationPO
Step3 = StrictPartialOrder(nodes=[Step1and2, ExpertForgeryPO])
Step3.order.add_edge(Step1and2, ExpertForgeryPO)

# Step 4: ConditionDigitalPO after ExpertForgeryPO
Step4 = StrictPartialOrder(nodes=[Step3, ConditionDigitalPO])
Step4.order.add_edge(Step3, ConditionDigitalPO)

# Step 5: Legal Compliance after Step 4
Step5 = StrictPartialOrder(nodes=[Step4, LegalCompliance])
Step5.order.add_edge(Step4, LegalCompliance)

# Step 6: RestorationValuationMarketPO after Legal Compliance
Step6 = StrictPartialOrder(nodes=[Step5, RestorationValuationMarketPO])
Step6.order.add_edge(Step5, RestorationValuationMarketPO)

# Step 7: FinalSalePO after Step 6
Step7 = StrictPartialOrder(nodes=[Step6, FinalSalePO])
Step7.order.add_edge(Step6, FinalSalePO)

# Step 8: Client Notification after Step 7
root = StrictPartialOrder(nodes=[Step7, ClientNotification])
root.order.add_edge(Step7, ClientNotification)