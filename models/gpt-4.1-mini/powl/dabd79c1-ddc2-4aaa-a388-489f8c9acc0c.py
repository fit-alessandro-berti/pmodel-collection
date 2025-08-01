# Generated from: dabd79c1-ddc2-4aaa-a388-489f8c9acc0c.json
# Description: This process involves the detailed authentication of historical artifacts to verify provenance and ensure authenticity before acquisition or exhibition. It begins with initial documentation review, followed by scientific testing such as radiocarbon dating and material composition analysis. Experts in art history then conduct stylistic evaluations, comparing findings against known databases. Concurrently, legal checks assess ownership history and export permissions. If discrepancies arise, a secondary expert panel convenes for arbitration. Upon successful validation, conservation specialists recommend preservation methods. Final approval is granted by the acquisitions committee, after which logistics coordinate secure transport and insurance. This workflow ensures that artifacts entering collections are genuine and legally obtained, minimizing risks associated with forgery or illicit trade.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Transitions for each activity
Document_Review = Transition(label='Document Review')

# Scientific testing subprocess: Radiocarbon Date and Material Testing (Note order Radiocarbon Date --> Material Testing)
Radiocarbon_Date = Transition(label='Radiocarbon Date')
Material_Testing = Transition(label='Material Testing')

# Stylistic evaluations subprocess: Stylistic Eval -> Database Check
Stylistic_Eval = Transition(label='Stylistic Eval')
Database_Check = Transition(label='Database Check')

# Legal checks subprocess: Ownership Audit -> Export Verify
Ownership_Audit = Transition(label='Ownership Audit')
Export_Verify = Transition(label='Export Verify')

# Arbitration subprocess – triggered only if discrepancies
Expert_Arbitration = Transition(label='Expert Arbitration')

# Conservation and risk assessment subprocess: Conservation Plan -> Risk Assessment
Conservation_Plan = Transition(label='Conservation Plan')
Risk_Assessment = Transition(label='Risk Assessment')

# Approval and logistics subprocess:
Approval_Review = Transition(label='Approval Review')
Acquisitions_Meet = Transition(label='Acquisitions Meet')
Secure_Transport = Transition(label='Secure Transport')
Insurance_Setup = Transition(label='Insurance Setup')

Final_Documentation = Transition(label='Final Documentation')

# 1) Model Radiocarbon Date --> Material Testing sequence partial order
scientific_testing = StrictPartialOrder(nodes=[Radiocarbon_Date, Material_Testing])
scientific_testing.order.add_edge(Radiocarbon_Date, Material_Testing)

# 2) Model Stylistic Eval --> Database Check partial order
stylistic_eval_po = StrictPartialOrder(nodes=[Stylistic_Eval, Database_Check])
stylistic_eval_po.order.add_edge(Stylistic_Eval, Database_Check)

# 3) Legal checks Ownership Audit --> Export Verify partial order
legal_checks = StrictPartialOrder(nodes=[Ownership_Audit, Export_Verify])
legal_checks.order.add_edge(Ownership_Audit, Export_Verify)

# 4) Stylistic and legal checks run concurrently after scientific testing
# partial order of concurrency: no edges between stylistic_eval_po and legal_checks

# 5) Document Review --> scientific testing --> stylistic_eval_po & legal_checks (concurrent)
first_part = StrictPartialOrder(
    nodes=[Document_Review, scientific_testing, stylistic_eval_po, legal_checks]
)
first_part.order.add_edge(Document_Review, scientific_testing)
first_part.order.add_edge(Document_Review, stylistic_eval_po)
first_part.order.add_edge(Document_Review, legal_checks)
first_part.order.add_edge(scientific_testing, stylistic_eval_po)
first_part.order.add_edge(scientific_testing, legal_checks)

# 6) Choice: If discrepancies arise after stylistic and legal checks,
#   Expert Arbitration is triggered, else skip (silent)
skip = SilentTransition()
arbitration_choice = OperatorPOWL(operator=Operator.XOR, children=[Expert_Arbitration, skip])

# Model that arbitration is enabled only after both stylistic evaluations and legal checks are done
post_checks = StrictPartialOrder(
    nodes=[first_part, arbitration_choice]
)
post_checks.order.add_edge(first_part, arbitration_choice)

# 7) After arbitration choice, loop to retry might happen or proceed
# However the description states arbitration is only triggered if discrepancies, no loop back stated,
# so this is exclusive choice only, no loop

# 8) After arbitration choice, conservation and risk assessment sequential
conservation_risk = StrictPartialOrder(nodes=[Conservation_Plan, Risk_Assessment])
conservation_risk.order.add_edge(Conservation_Plan, Risk_Assessment)

# 9) Approval and logistics subprocess:
#   Approval Review -> Acquisitions Meet -> (Secure Transport and Insurance Setup concurrent)
transport_insurance = StrictPartialOrder(nodes=[Secure_Transport, Insurance_Setup])  # concurrent

approval_and_logistics = StrictPartialOrder(nodes=[Approval_Review, Acquisitions_Meet, transport_insurance])
approval_and_logistics.order.add_edge(Approval_Review, Acquisitions_Meet)
approval_and_logistics.order.add_edge(Acquisitions_Meet, transport_insurance)

# 10) Final Documentation after logistics
finalize = StrictPartialOrder(nodes=[approval_and_logistics, Final_Documentation])
finalize.order.add_edge(approval_and_logistics, Final_Documentation)

# 11) Compose whole process partial order:
root = StrictPartialOrder(
    nodes=[post_checks, conservation_risk, approval_and_logistics, Final_Documentation]
)
# root will contain post_checks, conservation_risk, approval_and_logistics, Final Documentation node
# But note Final_Documentation is inside finalize and listed above - we need to connect properly

# Rebuild final for correct connections:
# post_checks --> conservation_risk --> approval_and_logistics --> Final_Documentation

root = StrictPartialOrder(
    nodes=[post_checks, conservation_risk, approval_and_logistics, Final_Documentation]
)
root.order.add_edge(post_checks, conservation_risk)
root.order.add_edge(conservation_risk, approval_and_logistics)
root.order.add_edge(approval_and_logistics, Final_Documentation)