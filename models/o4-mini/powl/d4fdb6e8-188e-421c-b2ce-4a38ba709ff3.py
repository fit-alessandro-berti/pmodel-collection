# Generated from: d4fdb6e8-188e-421c-b2ce-4a38ba709ff3.json
# Description: This process involves the detailed authentication of rare historical artifacts before acquisition by museums or private collectors. It combines scientific analysis, provenance research, expert consultations, and legal verifications. The workflow includes physical examination, chemical testing, archival research, digital imaging, cross-referencing databases, expert panel review, and final certification. Additional steps ensure cultural sensitivity and compliance with international heritage laws, followed by secure transport arrangements and insurance validation. The process concludes with archival documentation and publication of findings to maintain transparency and historical integrity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# define all activities as transitions
Artifact_Receipt     = Transition(label='Artifact Receipt')
Initial_Inspection   = Transition(label='Initial Inspection')
Material_Testing     = Transition(label='Material Testing')
Provenance_Check     = Transition(label='Provenance Check')
Digital_Imaging      = Transition(label='Digital Imaging')
Database_Search      = Transition(label='Database Search')
Expert_Consult       = Transition(label='Expert Consult')
Legal_Review         = Transition(label='Legal Review')
Cultural_Audit       = Transition(label='Cultural Audit')
Condition_Report     = Transition(label='Condition Report')
Risk_Assessment      = Transition(label='Risk Assessment')
Insurance_Setup      = Transition(label='Insurance Setup')
Transport_Plan       = Transition(label='Transport Plan')
Final_Certification  = Transition(label='Final Certification')
Archive_Entry        = Transition(label='Archive Entry')
Publication_Prep     = Transition(label='Publication Prep')

# build the partial order
root = StrictPartialOrder(nodes=[
    Artifact_Receipt,
    Initial_Inspection,
    Material_Testing,
    Provenance_Check,
    Digital_Imaging,
    Database_Search,
    Expert_Consult,
    Legal_Review,
    Cultural_Audit,
    Condition_Report,
    Risk_Assessment,
    Insurance_Setup,
    Transport_Plan,
    Final_Certification,
    Archive_Entry,
    Publication_Prep
])

# define the control‐flow dependencies
root.order.add_edge(Artifact_Receipt, Initial_Inspection)

root.order.add_edge(Initial_Inspection, Material_Testing)
root.order.add_edge(Initial_Inspection, Digital_Imaging)
root.order.add_edge(Initial_Inspection, Provenance_Check)

root.order.add_edge(Digital_Imaging, Database_Search)
root.order.add_edge(Provenance_Check, Database_Search)

root.order.add_edge(Material_Testing, Expert_Consult)
root.order.add_edge(Database_Search, Expert_Consult)

root.order.add_edge(Provenance_Check, Legal_Review)
root.order.add_edge(Database_Search, Legal_Review)

root.order.add_edge(Legal_Review, Cultural_Audit)

root.order.add_edge(Expert_Consult, Condition_Report)
root.order.add_edge(Legal_Review, Condition_Report)
root.order.add_edge(Cultural_Audit, Condition_Report)

root.order.add_edge(Condition_Report, Risk_Assessment)
root.order.add_edge(Risk_Assessment, Insurance_Setup)
root.order.add_edge(Insurance_Setup, Transport_Plan)
root.order.add_edge(Transport_Plan, Final_Certification)
root.order.add_edge(Final_Certification, Archive_Entry)
root.order.add_edge(Archive_Entry, Publication_Prep)