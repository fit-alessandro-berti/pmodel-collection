# Generated from: 891bb27b-4d17-41c9-b64d-772c3ac3b812.json
# Description: This process involves the meticulous examination and validation of antique artifacts to establish their authenticity and provenance. Specialists conduct multi-layered inspections including material analysis, historical cross-referencing, and forensic imaging. The process integrates expert consultations, database verification, and environmental impact assessments to ensure each item’s legitimacy. It also includes restoration feasibility studies, market valuation, and legal compliance checks related to cultural heritage protections before final certification and archival documentation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Initial_Review = Transition(label='Initial Review')
Material_Scan = Transition(label='Material Scan')
Provenance_Check = Transition(label='Provenance Check')
Historical_Match = Transition(label='Historical Match')
Forensic_Imaging = Transition(label='Forensic Imaging')
Expert_Consult = Transition(label='Expert Consult')
Database_Search = Transition(label='Database Search')
Condition_Report = Transition(label='Condition Report')
Restoration_Plan = Transition(label='Restoration Plan')
Market_Valuation = Transition(label='Market Valuation')
Legal_Review = Transition(label='Legal Review')
Cultural_Audit = Transition(label='Cultural Audit')
Environmental_Test = Transition(label='Environmental Test')
Certification = Transition(label='Certification')
Archival_Entry = Transition(label='Archival Entry')
Final_Approval = Transition(label='Final Approval')

# Create the meticulous inspection partial order:
# Material Scan, Historical Match, Forensic Imaging run in parallel after Initial Review,
# but Historical Match depends on Provenance Check which depends on Material Scan
inspection_PO = StrictPartialOrder(nodes=[
    Material_Scan,
    Provenance_Check,
    Historical_Match,
    Forensic_Imaging
])
inspection_PO.order.add_edge(Material_Scan, Provenance_Check)
inspection_PO.order.add_edge(Provenance_Check, Historical_Match)
# Forensic Imaging runs concurrently with Historical Match (no dependencies)

# Expert consultation and database verification run in parallel
consult_database_PO = StrictPartialOrder(nodes=[Expert_Consult, Database_Search])

# Environmental impact assessments and cultural audit run in parallel and independent from above
env_cultural_PO = StrictPartialOrder(nodes=[Environmental_Test, Cultural_Audit])
env_cultural_PO.order  # empty order, fully concurrent

# Condition report comes after inspections (inspection_PO),
# then Restoration Plan, Market Valuation, Legal Review, and Cultural Audit + Environmental Test integrate
# We model Restoration Plan, Market Valuation and Legal Review after Condition Report
# Legal Review depends also on Cultural Audit
# Condition report depends on Expert Consult and Database Search

condition_plan_PO = StrictPartialOrder(nodes=[
    Expert_Consult,
    Database_Search,
    Condition_Report,
    Restoration_Plan,
    Market_Valuation,
    Legal_Review,
    Cultural_Audit,
    Environmental_Test
])
condition_plan_PO.order.add_edge(Expert_Consult, Condition_Report)
condition_plan_PO.order.add_edge(Database_Search, Condition_Report)
condition_plan_PO.order.add_edge(Condition_Report, Restoration_Plan)
condition_plan_PO.order.add_edge(Restoration_Plan, Market_Valuation)
condition_plan_PO.order.add_edge(Market_Valuation, Legal_Review)
condition_plan_PO.order.add_edge(Cultural_Audit, Legal_Review)
condition_plan_PO.order.add_edge(Environmental_Test, Legal_Review)

# Certification after legal review
# Archival entry after certification
# Final approval after archival entry

final_PO = StrictPartialOrder(nodes=[
    Legal_Review,
    Certification,
    Archival_Entry,
    Final_Approval
])
final_PO.order.add_edge(Legal_Review, Certification)
final_PO.order.add_edge(Certification, Archival_Entry)
final_PO.order.add_edge(Archival_Entry, Final_Approval)

# Compose the whole process partial order combining all parts:
# Initial Review --> inspection_PO --> consult_database_PO & env_cultural_PO in parallel -->
# condition_plan_PO --> final_PO
root = StrictPartialOrder(nodes=[
    Initial_Review,
    inspection_PO,
    consult_database_PO,
    env_cultural_PO,
    condition_plan_PO,
    final_PO
])

root.order.add_edge(Initial_Review, inspection_PO)
root.order.add_edge(inspection_PO, consult_database_PO)
root.order.add_edge(inspection_PO, env_cultural_PO)
root.order.add_edge(consult_database_PO, condition_plan_PO)
root.order.add_edge(env_cultural_PO, condition_plan_PO)
root.order.add_edge(condition_plan_PO, final_PO)