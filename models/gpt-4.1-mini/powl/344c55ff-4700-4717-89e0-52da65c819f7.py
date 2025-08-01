# Generated from: 344c55ff-4700-4717-89e0-52da65c819f7.json
# Description: This process involves the systematic verification and authentication of rare historical artifacts for museum acquisition or private collection. It includes provenance research, material analysis, expert consultation, and legal clearance. Multiple specialists collaborate to ensure authenticity, condition assessment, and ethical compliance before final approval and documentation, integrating interdisciplinary methods and advanced technology to mitigate forgery risks and protect cultural heritage.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Initial_Review = Transition(label='Initial Review')
Provenance_Check = Transition(label='Provenance Check')
Material_Scan = Transition(label='Material Scan')
Carbon_Dating = Transition(label='Carbon Dating')
Expert_Consult = Transition(label='Expert Consult')
Condition_Report = Transition(label='Condition Report')
Forgery_Test = Transition(label='Forgery Test')
Ethics_Audit = Transition(label='Ethics Audit')
Legal_Review = Transition(label='Legal Review')
Ownership_Verify = Transition(label='Ownership Verify')
Appraisal_Estimate = Transition(label='Appraisal Estimate')
Risk_Assessment = Transition(label='Risk Assessment')
Final_Approval = Transition(label='Final Approval')
Documentation = Transition(label='Documentation')
Archive_Entry = Transition(label='Archive Entry')
Client_Brief = Transition(label='Client Brief')

# Build partial orders for provenance research branch:
# Provenance check then ownership verify and appraisal estimate in parallel, then risk assessment
provenance_PO = StrictPartialOrder(nodes=[Provenance_Check, Ownership_Verify, Appraisal_Estimate, Risk_Assessment])
provenance_PO.order.add_edge(Provenance_Check, Ownership_Verify)
provenance_PO.order.add_edge(Provenance_Check, Appraisal_Estimate)
provenance_PO.order.add_edge(Ownership_Verify, Risk_Assessment)
provenance_PO.order.add_edge(Appraisal_Estimate, Risk_Assessment)

# Material analysis branch:
# Material scan followed by carbon dating, followed by forgery test
material_PO = StrictPartialOrder(nodes=[Material_Scan, Carbon_Dating, Forgery_Test])
material_PO.order.add_edge(Material_Scan, Carbon_Dating)
material_PO.order.add_edge(Carbon_Dating, Forgery_Test)

# Expert consultation branch (can be parallel with material analysis):
# Expert consult then condition report
expert_PO = StrictPartialOrder(nodes=[Expert_Consult, Condition_Report])
expert_PO.order.add_edge(Expert_Consult, Condition_Report)

# Legal clearance branch:
# Ethics audit then legal review
legal_PO = StrictPartialOrder(nodes=[Ethics_Audit, Legal_Review])
legal_PO.order.add_edge(Ethics_Audit, Legal_Review)

# Final aggregation partial order:
# After initial review, provenance, material, expert, legal branches run concurrently
# and after they complete, final approval occurs, then documentation, archive entry and client brief sequentially.

# Combine all validation branches in parallel:
validation_branches = StrictPartialOrder(
    nodes=[provenance_PO, material_PO, expert_PO, legal_PO]
)
# No direct order edges between these branches => all are concurrent

# Combine initial review and validation branches:
initial_and_validation = StrictPartialOrder(
    nodes=[Initial_Review, provenance_PO, material_PO, expert_PO, legal_PO]
)
# initial review must precede all validation branches:
initial_and_validation.order.add_edge(Initial_Review, provenance_PO)
initial_and_validation.order.add_edge(Initial_Review, material_PO)
initial_and_validation.order.add_edge(Initial_Review, expert_PO)
initial_and_validation.order.add_edge(Initial_Review, legal_PO)

# After validation branches, final approval
after_validation = StrictPartialOrder(
    nodes=[validation_branches, Final_Approval]
)
after_validation.order.add_edge(validation_branches, Final_Approval)

# Documentation sequence: Documentation -> Archive Entry -> Client Brief
doc_seq = StrictPartialOrder(
    nodes=[Documentation, Archive_Entry, Client_Brief]
)
doc_seq.order.add_edge(Documentation, Archive_Entry)
doc_seq.order.add_edge(Archive_Entry, Client_Brief)

# Final process: initial and validation -> final approval -> documentation sequence
root = StrictPartialOrder(
    nodes=[initial_and_validation, Final_Approval, doc_seq]
)
root.order.add_edge(initial_and_validation, Final_Approval)
root.order.add_edge(Final_Approval, doc_seq)