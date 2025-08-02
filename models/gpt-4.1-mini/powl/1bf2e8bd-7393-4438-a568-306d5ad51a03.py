# Generated from: 1bf2e8bd-7393-4438-a568-306d5ad51a03.json
# Description: This process outlines the comprehensive steps involved in authenticating historical artifacts for a museum acquisition. It begins with preliminary research to establish provenance, followed by multi-disciplinary scientific testing including radiocarbon dating and material analysis. Concurrently, expert consultations are scheduled to verify stylistic consistency and historical accuracy. Documentation is meticulously gathered and cross-referenced against existing databases. Legal clearance is then obtained to ensure proper ownership transfer, while ethical considerations regarding cultural sensitivity are reviewed. The artifact undergoes condition assessment and conservation planning before final authentication approval is granted. The workflow concludes with digital archiving and preparation for public exhibition, ensuring transparency and traceability throughout the entire process.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
Initial_Research = Transition(label='Initial Research')
Provenance_Check = Transition(label='Provenance Check')
Radiocarbon_Test = Transition(label='Radiocarbon Test')
Material_Analysis = Transition(label='Material Analysis')
Style_Verify = Transition(label='Style Verify')
Expert_Review = Transition(label='Expert Review')
Database_Crosscheck = Transition(label='Database Crosscheck')
Legal_Clearance = Transition(label='Legal Clearance')
Ethics_Review = Transition(label='Ethics Review')
Condition_Assess = Transition(label='Condition Assess')
Conservation_Plan = Transition(label='Conservation Plan')
Approval_Meeting = Transition(label='Approval Meeting')
Digital_Archive = Transition(label='Digital Archive')
Exhibit_Prep = Transition(label='Exhibit Prep')
Final_Report = Transition(label='Final Report')

# Step 1: Initial research followed by provenance check (sequential)
research_flow = StrictPartialOrder(nodes=[Initial_Research, Provenance_Check])
research_flow.order.add_edge(Initial_Research, Provenance_Check)

# Step 2: Scientific testing including Radiocarbon Test and Material Analysis (concurrent)
scientific_testing = StrictPartialOrder(nodes=[Radiocarbon_Test, Material_Analysis])
# no edges = concurrent

# Step 3: Expert consultations including Style Verify and Expert Review (concurrent)
expert_consult = StrictPartialOrder(nodes=[Style_Verify, Expert_Review])
# no edges = concurrent

# Step 4: Documentation gathering and cross-check (Database Crosscheck)
documentation = Database_Crosscheck

# Step 5: Legal clearance and ethics review (sequential or concurrent? 
# The description says "while ethical considerations... reviewed" so concurrent)
legal_ethics = StrictPartialOrder(nodes=[Legal_Clearance, Ethics_Review])
# no edges = concurrent

# Step 6: Condition assessment and conservation planning (sequential)
condition_flow = StrictPartialOrder(nodes=[Condition_Assess, Conservation_Plan])
condition_flow.order.add_edge(Condition_Assess, Conservation_Plan)

# Step 7: Final authentication approval (Approval Meeting)
approval = Approval_Meeting

# Step 8: Digital archiving and exhibit preparation (concurrent)
final_prep = StrictPartialOrder(nodes=[Digital_Archive, Exhibit_Prep])
# no edges = concurrent

# Step 9: Final report (end activity)
final_report = Final_Report

# Build the overall partial order

# Step 2 and Step 3 happen concurrently but after Provenance Check
# So create a PO for scientific_testing and expert_consult concurrently
science_and_expert = StrictPartialOrder(nodes=[scientific_testing, expert_consult])
# no edges between scientific_testing and expert_consult

# After step 1 (research_flow) then step 2&3 concurrently (science_and_expert)
overall1 = StrictPartialOrder(nodes=[research_flow, science_and_expert])
overall1.order.add_edge(research_flow, science_and_expert)

# Documentation (Database Crosscheck) after concurrent testing and expert consult 
# So sequential order from overall1 to documentation
overall2 = StrictPartialOrder(nodes=[overall1, documentation])
overall2.order.add_edge(overall1, documentation)

# Legal clearance and ethics review concurrent, after documentation
overall3 = StrictPartialOrder(nodes=[overall2, legal_ethics])
overall3.order.add_edge(overall2, legal_ethics)

# Condition assessment and conservation plan sequential after legal & ethics
overall4 = StrictPartialOrder(nodes=[overall3, condition_flow])
overall4.order.add_edge(overall3, condition_flow)

# Approval meeting after condition flow
overall5 = StrictPartialOrder(nodes=[overall4, approval])
overall5.order.add_edge(overall4, approval)

# Digital archive and exhibit prep concurrent after approval
overall6 = StrictPartialOrder(nodes=[overall5, final_prep])
overall6.order.add_edge(overall5, final_prep)

# Final report after final prep
root = StrictPartialOrder(nodes=[overall6, final_report])
root.order.add_edge(overall6, final_report)