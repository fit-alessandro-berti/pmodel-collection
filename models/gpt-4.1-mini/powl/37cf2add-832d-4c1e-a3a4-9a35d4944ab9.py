# Generated from: 37cf2add-832d-4c1e-a3a4-9a35d4944ab9.json
# Description: This process outlines the dynamic leasing of fine art pieces to corporate clients, combining inventory management, client preference analysis, and rotational logistics to ensure artworks remain fresh and relevant within office environments. The process begins with artwork acquisition and categorization, followed by personalized client profiling to match art styles with corporate branding. Contracts are negotiated with flexible duration terms, incorporating insurance and maintenance clauses. Logistics teams coordinate artwork delivery, installation, and periodic rotation based on client feedback and seasonal trends. Maintenance crews perform condition checks and restoration as needed. Billing cycles adapt to contract changes, while data analytics monitor client satisfaction and market trends to optimize the art portfolio. The process concludes with contract renewal discussions or artwork return, ensuring a seamless, evolving art leasing experience that balances client needs, artist exposure, and operational efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

ArtSourcing = Transition(label='Art Sourcing')
StyleAnalysis = Transition(label='Style Analysis')
ClientProfiling = Transition(label='Client Profiling')
ContractDrafting = Transition(label='Contract Drafting')
InsuranceSetup = Transition(label='Insurance Setup')
InventoryTagging = Transition(label='Inventory Tagging')
LogisticsPlanning = Transition(label='Logistics Planning')
ArtworkDelivery = Transition(label='Artwork Delivery')
InstallationSetup = Transition(label='Installation Setup')
RotationScheduling = Transition(label='Rotation Scheduling')
ConditionCheck = Transition(label='Condition Check')
RestorationWork = Transition(label='Restoration Work')
BillingProcess = Transition(label='Billing Process')
FeedbackCollection = Transition(label='Feedback Collection')
PortfolioReview = Transition(label='Portfolio Review')
ContractRenewal = Transition(label='Contract Renewal')
ReturnHandling = Transition(label='Return Handling')
skip = SilentTransition()

# Acquisition and categorization partial order
acquisition_po = StrictPartialOrder(nodes=[ArtSourcing, StyleAnalysis, ClientProfiling, InventoryTagging])
acquisition_po.order.add_edge(ArtSourcing, StyleAnalysis)
acquisition_po.order.add_edge(ArtSourcing, ClientProfiling)
acquisition_po.order.add_edge(ArtSourcing, InventoryTagging)

# Contract drafting branch (ContractDrafting -> InsuranceSetup)
contract_po = StrictPartialOrder(nodes=[ContractDrafting, InsuranceSetup])
contract_po.order.add_edge(ContractDrafting, InsuranceSetup)

# Logistics chain partial order
logistics_po = StrictPartialOrder(nodes=[LogisticsPlanning, ArtworkDelivery, InstallationSetup, RotationScheduling])
logistics_po.order.add_edge(LogisticsPlanning, ArtworkDelivery)
logistics_po.order.add_edge(ArtworkDelivery, InstallationSetup)
logistics_po.order.add_edge(InstallationSetup, RotationScheduling)

# Maintenance loop (Condition Check and Restoration Work repeated before next rotation)
maintenance_loop_child = StrictPartialOrder(nodes=[ConditionCheck, RestorationWork])
maintenance_loop_child.order.add_edge(ConditionCheck, RestorationWork)
maintenance = OperatorPOWL(operator=Operator.LOOP, children=[SilentTransition(), maintenance_loop_child])

# Rotation Scheduling followed by maintenance loop (RotationScheduling --> maintenance)
rotation_with_maintenance = StrictPartialOrder(nodes=[RotationScheduling, maintenance])
rotation_with_maintenance.order.add_edge(RotationScheduling, maintenance)

# Billing and feedback partial order
billing_feedback_po = StrictPartialOrder(nodes=[BillingProcess, FeedbackCollection])
billing_feedback_po.order.add_edge(BillingProcess, FeedbackCollection)

# Portfolio review and choice between Contract Renewal or Return Handling
contract_decision = OperatorPOWL(operator=Operator.XOR, children=[ContractRenewal, ReturnHandling])

# Portfolio review leads to contract decision choice
portfolio_decision_po = StrictPartialOrder(nodes=[PortfolioReview, contract_decision])
portfolio_decision_po.order.add_edge(PortfolioReview, contract_decision)

# Combine billing_feedback and portfolio_decision sequentially
billing_to_portfolio_po = StrictPartialOrder(nodes=[billing_feedback_po, portfolio_decision_po])
billing_to_portfolio_po.order.add_edge(billing_feedback_po, portfolio_decision_po)

# Combine all major blocks sequentially:
# acquisition_po -> contract_po -> logistics_po -> rotation_with_maintenance -> billing_to_portfolio_po

step1 = StrictPartialOrder(nodes=[acquisition_po, contract_po])
step1.order.add_edge(acquisition_po, contract_po)

step2 = StrictPartialOrder(nodes=[step1, logistics_po])
step2.order.add_edge(step1, logistics_po)

step3 = StrictPartialOrder(nodes=[step2, rotation_with_maintenance])
step3.order.add_edge(step2, rotation_with_maintenance)

root = StrictPartialOrder(nodes=[step3, billing_to_portfolio_po])
root.order.add_edge(step3, billing_to_portfolio_po)