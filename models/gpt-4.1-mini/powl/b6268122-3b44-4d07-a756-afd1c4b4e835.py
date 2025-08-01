# Generated from: b6268122-3b44-4d07-a756-afd1c4b4e835.json
# Description: This process involves verifying the authenticity and provenance of rare artifacts through multidisciplinary methods. It begins with initial visual inspection, followed by advanced material analysis and historical context research. The artifact undergoes comparative studies with known pieces, expert consultations, and digital imaging. Next, scientific dating techniques are applied, and provenance documentation is cross-verified. Once all data is consolidated, a risk assessment is conducted to identify potential forgery indicators. The final step involves generating a detailed authentication report, which is then reviewed by a certification board before the artifact is officially authenticated and cataloged in a secure database for future reference and insurance purposes.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Visual_Check = Transition(label='Visual Check')
Material_Scan = Transition(label='Material Scan')
Context_Study = Transition(label='Context Study')
Comparative_Review = Transition(label='Comparative Review')
Expert_Consult = Transition(label='Expert Consult')
Digital_Imaging = Transition(label='Digital Imaging')
Carbon_Dating = Transition(label='Carbon Dating')
Provenance_Check = Transition(label='Provenance Check')
Data_Consolidate = Transition(label='Data Consolidate')
Forgery_Assess = Transition(label='Forgery Assess')
Report_Draft = Transition(label='Report Draft')
Board_Review = Transition(label='Board Review')
Certification = Transition(label='Certification')
Catalog_Entry = Transition(label='Catalog Entry')
Secure_Storage = Transition(label='Secure Storage')

# Construct the partial order model according to the description

# Nodes include all transitions
nodes = [
    Visual_Check,
    Material_Scan,
    Context_Study,
    Comparative_Review,
    Expert_Consult,
    Digital_Imaging,
    Carbon_Dating,
    Provenance_Check,
    Data_Consolidate,
    Forgery_Assess,
    Report_Draft,
    Board_Review,
    Certification,
    Catalog_Entry,
    Secure_Storage,
]

root = StrictPartialOrder(nodes=nodes)

# Add edges representing the described partial order

# Start with initial visual inspection
root.order.add_edge(Visual_Check, Material_Scan)
root.order.add_edge(Visual_Check, Context_Study)

# Advanced material analysis and historical context research happen after Visual Check concurrently
# Then, the artifact undergoes comparative studies, expert consultations, and digital imaging.
root.order.add_edge(Material_Scan, Comparative_Review)
root.order.add_edge(Context_Study, Comparative_Review)
root.order.add_edge(Context_Study, Expert_Consult)
root.order.add_edge(Context_Study, Digital_Imaging)
root.order.add_edge(Material_Scan, Expert_Consult)
root.order.add_edge(Material_Scan, Digital_Imaging)

# Comparative Review, Expert Consult, and Digital Imaging must be all done before scientific dating and provenance check
# Model them as concurrent but all feeding into the next steps
root.order.add_edge(Comparative_Review, Carbon_Dating)
root.order.add_edge(Expert_Consult, Carbon_Dating)
root.order.add_edge(Digital_Imaging, Carbon_Dating)
root.order.add_edge(Comparative_Review, Provenance_Check)
root.order.add_edge(Expert_Consult, Provenance_Check)
root.order.add_edge(Digital_Imaging, Provenance_Check)

# Next, scientific dating techniques and provenance are done concurrently but both must complete before data consolidate
root.order.add_edge(Carbon_Dating, Data_Consolidate)
root.order.add_edge(Provenance_Check, Data_Consolidate)

# Once all data is consolidated, a risk assessment is conducted
root.order.add_edge(Data_Consolidate, Forgery_Assess)

# Then generate report draft
root.order.add_edge(Forgery_Assess, Report_Draft)

# Reviewed by certification board
root.order.add_edge(Report_Draft, Board_Review)

# Then certification
root.order.add_edge(Board_Review, Certification)

# Finally catalog entry and secure storage happen sequentially
root.order.add_edge(Certification, Catalog_Entry)
root.order.add_edge(Catalog_Entry, Secure_Storage)