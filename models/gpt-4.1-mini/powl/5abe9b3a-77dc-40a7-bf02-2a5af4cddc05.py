# Generated from: 5abe9b3a-77dc-40a7-bf02-2a5af4cddc05.json
# Description: This process involves the detailed examination and verification of rare artifacts obtained from private collectors and archaeological digs. Experts perform multi-disciplinary analyses including material composition testing, provenance tracing, and historical context validation. The process integrates advanced imaging techniques, chemical assays, and consultation with historians to confirm authenticity. Following authentication, artifacts undergo conservation assessment and are prepared for either museum display or private sale. Throughout, secure documentation and chain-of-custody protocols are strictly maintained to ensure legal compliance and provenance integrity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Artifact_Receipt = Transition(label='Artifact Receipt')
Initial_Inspection = Transition(label='Initial Inspection')

# Multi-disciplinary analyses (all concurrent except where order matters)
Material_Testing = Transition(label='Material Testing')
Imaging_Scan = Transition(label='Imaging Scan')
Provenance_Check = Transition(label='Provenance Check')
Historical_Review = Transition(label='Historical Review')
Chemical_Assay = Transition(label='Chemical Assay')
Forgery_Analysis = Transition(label='Forgery Analysis')
Expert_Consultation = Transition(label='Expert Consultation')

# Post authentication
Condition_Report = Transition(label='Condition Report')
Conservation_Plan = Transition(label='Conservation Plan')

# Documentation and chain-of-custody kept throughout but logically after initial inspection and concurrent with analyses
Documentation = Transition(label='Documentation')
Chain_Custody = Transition(label='Chain Custody')

Legal_Review = Transition(label='Legal Review')
Final_Approval = Transition(label='Final Approval')

# Choice after approval: Display Setup or Sale Preparation
Display_Setup = Transition(label='Display Setup')
Sale_Preparation = Transition(label='Sale Preparation')

# Build partial order model

# 1. Artifact Receipt --> Initial Inspection
# 2. After Initial Inspection, Documentation & Chain Custody start (concurrent with analyses)
# 3. Multi-disciplinary analyses run concurrently, but Forgery Analysis depends on Chemical Assay, and Expert Consultation depends on Historical Review and Provenance Check
# 4. After all analyses finish, Condition Report --> Conservation Plan
# 5. Then Legal Review --> Final Approval
# 6. Then choice between Display Setup OR Sale Preparation

# Create a StrictPartialOrder for the analyses dependencies and concurrency

# Define the analyses nodes as POWL
# Define dependencies within analyses:
# Chemical Assay --> Forgery Analysis
# Provenance Check and Historical Review --> Expert Consultation

# We'll create those dependencies:

# Create a StrictPartialOrder analyses_po for analyses & their dependencies
analyses_nodes = [
    Material_Testing,
    Imaging_Scan,
    Provenance_Check,
    Historical_Review,
    Chemical_Assay,
    Forgery_Analysis,
    Expert_Consultation
]
analyses_po = StrictPartialOrder(nodes=analyses_nodes)
analyses_po.order.add_edge(Chemical_Assay, Forgery_Analysis)
analyses_po.order.add_edge(Provenance_Check, Expert_Consultation)
analyses_po.order.add_edge(Historical_Review, Expert_Consultation)

# Now group Documentation and Chain Custody, which run concurrently but must start after Initial Inspection
doc_chain_nodes = [Documentation, Chain_Custody]
doc_chain_po = StrictPartialOrder(nodes=doc_chain_nodes)

# After analyses and doc_chain finish, proceed to Condition Report and Conservation Plan sequentially:
post_analyses_nodes = [Condition_Report, Conservation_Plan]
post_analyses_po = StrictPartialOrder(nodes=post_analyses_nodes)
post_analyses_po.order.add_edge(Condition_Report, Conservation_Plan)

# Then Legal Review, Final Approval sequential:
final_approval_nodes = [Legal_Review, Final_Approval]
final_approval_po = StrictPartialOrder(nodes=final_approval_nodes)
final_approval_po.order.add_edge(Legal_Review, Final_Approval)

# Choice between Display Setup and Sale Preparation
choice_display_sale = OperatorPOWL(operator=Operator.XOR, children=[Display_Setup, Sale_Preparation])

# Now combine all parts with appropriate edges

# Compose initial steps and two parallel branches: analyses_po and doc_chain_po
# We'll create a big PO of initial Inspection leading to both analyses and doc_chain concurrently

initial_and_branches = StrictPartialOrder(
    nodes=[Initial_Inspection, analyses_po, doc_chain_po]
)
# Initial Inspection --> analyses_po and doc_chain_po
initial_and_branches.order.add_edge(Initial_Inspection, analyses_po)
initial_and_branches.order.add_edge(Initial_Inspection, doc_chain_po)

# Next combine initial_and_branches with Artifact Receipt
first_segment = StrictPartialOrder(nodes=[Artifact_Receipt, initial_and_branches])
first_segment.order.add_edge(Artifact_Receipt, initial_and_branches)

# Combine post analyses & post doc_chain with Condition Report sequence
# Condition Report depends on analyses_po and doc_chain_po
post_condition = StrictPartialOrder(
    nodes=[analyses_po, doc_chain_po, post_analyses_po]
)
post_condition.order.add_edge(analyses_po, post_analyses_po)
post_condition.order.add_edge(doc_chain_po, post_analyses_po)

# Combine post_condition with final approval sequential steps
mid_segment = StrictPartialOrder(
    nodes=[post_analyses_po, final_approval_po]
)
mid_segment.order.add_edge(post_analyses_po, final_approval_po)

# Combine everything with choice at the end
root = StrictPartialOrder(
    nodes=[first_segment, post_condition, mid_segment, choice_display_sale]
)
# Add edges connecting segments of the process
root.order.add_edge(first_segment, post_condition)
root.order.add_edge(post_condition, mid_segment)
root.order.add_edge(mid_segment, choice_display_sale)