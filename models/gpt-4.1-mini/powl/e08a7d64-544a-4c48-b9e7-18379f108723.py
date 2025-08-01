# Generated from: e08a7d64-544a-4c48-b9e7-18379f108723.json
# Description: This process outlines the intricate steps involved in authenticating rare historical artifacts for museums or private collectors. Beginning with initial provenance research, the workflow includes multidisciplinary scientific testing, expert consultations, and legal verifications to ensure authenticity and compliance with international cultural property laws. The process further addresses risk assessments, insurance appraisals, digital cataloging, and final certification issuance. Throughout the workflow, collaboration between historians, chemists, legal advisors, and logistics coordinators is critical to maintain integrity and transparency, culminating in secure artifact transfer or exhibition planning.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Provenance_Check = Transition(label='Provenance Check')
Material_Testing = Transition(label='Material Testing')
Expert_Review = Transition(label='Expert Review')
Legal_Verify = Transition(label='Legal Verify')
Risk_Assess = Transition(label='Risk Assess')
Insurance_Quote = Transition(label='Insurance Quote')
Catalog_Entry = Transition(label='Catalog Entry')
Digital_Scan = Transition(label='Digital Scan')
Condition_Report = Transition(label='Condition Report')
Transport_Plan = Transition(label='Transport Plan')
Customs_Clear = Transition(label='Customs Clear')
Certification = Transition(label='Certification')
Exhibit_Setup = Transition(label='Exhibit Setup')
Owner_Notify = Transition(label='Owner Notify')
Final_Audit = Transition(label='Final Audit')

# Collaboration between historians, chemists, legal advisors and logistics coordinators:
# 
# Logical partial order inferred:
# 1) Provenance_Check
# 2) Scientific Testing (Material_Testing) and Expert Review happen in parallel after Provenance_Check
# 3) Legal_Verify depends on Expert_Review
# 4) Next Risk_Assess and Insurance_Quote run in parallel after Material_Testing and Legal_Verify
# 5) Catalog_Entry and Digital_Scan are parallel and depend on Risk_Assess and Insurance_Quote
# 6) Condition_Report depends on Catalog_Entry and Digital_Scan (concurrent)
# 7) Transport_Plan depends on Condition_Report
# 8) Customs_Clear depends on Transport_Plan
# 9) Certification depends on Customs_Clear, Expert_Review and Legal_Verify
# 10) Exhibit_Setup and Owner_Notify are parallel after Certification
# 11) Final_Audit depends on Exhibit_Setup and Owner_Notify

# Build partial orders progressively:

# Step 1
step1 = Provenance_Check

# Step 2: Material_Testing and Expert_Review concurrent after Provenance_Check
step2 = StrictPartialOrder(nodes=[Material_Testing, Expert_Review])
# No order between them

# Link step1 --> step2 nodes
step1_to_step2 = StrictPartialOrder(nodes=[step1, step2])
step1_to_step2.order.add_edge(step1, step2)  # Provenance_Check --> (Material_Testing and Expert_Review concurrent)

# Actually, we need a flat structure, so we flatten nodes
# pm4py expects all nodes as individual activities or operators,
# so instead of nesting StrictPartialOrder, we merge nodes and add edges accordingly

# For clarity and proper construction, let's define the whole graph flatly:

nodes = [
    Provenance_Check,
    Material_Testing,
    Expert_Review,
    Legal_Verify,
    Risk_Assess,
    Insurance_Quote,
    Catalog_Entry,
    Digital_Scan,
    Condition_Report,
    Transport_Plan,
    Customs_Clear,
    Certification,
    Exhibit_Setup,
    Owner_Notify,
    Final_Audit,
]

root = StrictPartialOrder(nodes=nodes)

# Edges following the dependency described

# Provenance_Check --> Material_Testing and Expert_Review
root.order.add_edge(Provenance_Check, Material_Testing)
root.order.add_edge(Provenance_Check, Expert_Review)

# Expert_Review --> Legal_Verify
root.order.add_edge(Expert_Review, Legal_Verify)

# Material_Testing --> Risk_Assess
root.order.add_edge(Material_Testing, Risk_Assess)

# Legal_Verify --> Risk_Assess (risk assessment after legal verification too)
root.order.add_edge(Legal_Verify, Risk_Assess)

# Risk_Assess --> Catalog_Entry and Digital_Scan
root.order.add_edge(Risk_Assess, Catalog_Entry)
root.order.add_edge(Risk_Assess, Digital_Scan)

# Insurance_Quote depends on Risk_Assess as parallel task
root.order.add_edge(Risk_Assess, Insurance_Quote)

# Insurance_Quote --> Catalog_Entry and Digital_Scan (parallel dependencies)
root.order.add_edge(Insurance_Quote, Catalog_Entry)
root.order.add_edge(Insurance_Quote, Digital_Scan)

# Catalog_Entry and Digital_Scan --> Condition_Report
root.order.add_edge(Catalog_Entry, Condition_Report)
root.order.add_edge(Digital_Scan, Condition_Report)

# Condition_Report --> Transport_Plan
root.order.add_edge(Condition_Report, Transport_Plan)

# Transport_Plan --> Customs_Clear
root.order.add_edge(Transport_Plan, Customs_Clear)

# Customs_Clear --> Certification
root.order.add_edge(Customs_Clear, Certification)

# Expert_Review --> Certification (as dependency)
root.order.add_edge(Expert_Review, Certification)

# Legal_Verify --> Certification (as dependency)
root.order.add_edge(Legal_Verify, Certification)

# Certification --> Exhibit_Setup and Owner_Notify (parallel)
root.order.add_edge(Certification, Exhibit_Setup)
root.order.add_edge(Certification, Owner_Notify)

# Exhibit_Setup and Owner_Notify --> Final_Audit
root.order.add_edge(Exhibit_Setup, Final_Audit)
root.order.add_edge(Owner_Notify, Final_Audit)