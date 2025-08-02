# Generated from: 79e65744-531b-40f0-9898-51d3498290bc.json
# Description: This process involves the meticulous examination and verification of rare antique artifacts to determine their authenticity, provenance, and historical significance. It includes initial visual screening, advanced imaging techniques, material composition analysis, historical record cross-referencing, expert consultations, and final certification. The process ensures that collectors and institutions acquire genuine pieces while preventing forgeries from entering the market. It also incorporates secure documentation, digital archiving, and legal compliance checks to maintain integrity throughout the artifact's lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities (Transitions)
Initial_Screening = Transition(label='Initial Screening')     # initial visual screening
Visual_Inspection = Transition(label='Visual Inspection')     # detailed visual inspection
Imaging_Capture = Transition(label='Imaging Capture')         # advanced imaging techniques

Material_Testing = Transition(label='Material Testing')       # material composition analysis

Provenance_Check = Transition(label='Provenance Check')       # provenance verification
Database_Search = Transition(label='Database Search')         # historical record cross-referencing

Expert_Review = Transition(label='Expert Review')             # expert consultations
Condition_Report = Transition(label='Condition Report')       # detailed condition report
Forgery_Analysis = Transition(label='Forgery Analysis')       # forgery detection

Historical_Crossref = Transition(label='Historical Crossref') # additional historical crossreferencing in loop

Legal_Compliance = Transition(label='Legal Compliance')       # legal compliance checks
Certificate_Issue = Transition(label='Certificate Issue')     # final certification

Digital_Archive = Transition(label='Digital Archive')         # digital archiving
Client_Presentation = Transition(label='Client Presentation') # presentation to client
Final_Approval = Transition(label='Final Approval')           # final approval of artifact
Secure_Storage = Transition(label='Secure Storage')           # secure storage of artifact

# Model construction

# Step 1: Initial screening: Initial Screening -> Visual Inspection -> Imaging Capture
first_seq = StrictPartialOrder(nodes=[Initial_Screening, Visual_Inspection, Imaging_Capture])
first_seq.order.add_edge(Initial_Screening, Visual_Inspection)
first_seq.order.add_edge(Visual_Inspection, Imaging_Capture)

# Step 2: Material Testing after Imaging Capture
material_test_po = StrictPartialOrder(nodes=[Imaging_Capture, Material_Testing])
material_test_po.order.add_edge(Imaging_Capture, Material_Testing)

# Step 3: Provenance check (Provenance Check AND Database Search concurrently after Material Testing)
prov_conc = StrictPartialOrder(nodes=[Material_Testing, Provenance_Check, Database_Search])
prov_conc.order.add_edge(Material_Testing, Provenance_Check)
prov_conc.order.add_edge(Material_Testing, Database_Search)

# Step 4: Merge Provenance Check and Database Search into Expert Review branch
expert_path = StrictPartialOrder(nodes=[Provenance_Check, Database_Search, Expert_Review])
expert_path.order.add_edge(Provenance_Check, Expert_Review)
expert_path.order.add_edge(Database_Search, Expert_Review)

# Step 5: Condition report and forgery analysis concurrent after Expert Review
cond_forgery = StrictPartialOrder(nodes=[Expert_Review, Condition_Report, Forgery_Analysis])
cond_forgery.order.add_edge(Expert_Review, Condition_Report)
cond_forgery.order.add_edge(Expert_Review, Forgery_Analysis)

# Step 6: Loop with historical crossref before legal compliance:
# LOOP(
#   A = Historical_Crossref
#   B = SilentTransition (skip)
# )
loop_historical = OperatorPOWL(operator=Operator.LOOP, children=[Historical_Crossref, SilentTransition()])

# Step 7: After condition report and forgery analysis concurrently complete, loop_historical
conf_loop = StrictPartialOrder(
    nodes=[Condition_Report, Forgery_Analysis, loop_historical]
)
conf_loop.order.add_edge(Condition_Report, loop_historical)
conf_loop.order.add_edge(Forgery_Analysis, loop_historical)

# Step 8: Legal Compliance depends on loop_historical finish
legal_cert = StrictPartialOrder(nodes=[loop_historical, Legal_Compliance, Certificate_Issue])
legal_cert.order.add_edge(loop_historical, Legal_Compliance)
legal_cert.order.add_edge(Legal_Compliance, Certificate_Issue)

# Step 9: Final activities after certification: Digital Archive -> Client Presentation -> Final Approval -> Secure Storage
final_seq = StrictPartialOrder(nodes=[Certificate_Issue, Digital_Archive, Client_Presentation, Final_Approval, Secure_Storage])
final_seq.order.add_edge(Certificate_Issue, Digital_Archive)
final_seq.order.add_edge(Digital_Archive, Client_Presentation)
final_seq.order.add_edge(Client_Presentation, Final_Approval)
final_seq.order.add_edge(Final_Approval, Secure_Storage)

# Compose whole process with partial orders linked:

# Compose first sequence and material_test_po (material testing after Imaging Capture)
seq_1_2 = StrictPartialOrder(nodes=[Initial_Screening, Visual_Inspection, Imaging_Capture, Material_Testing])
seq_1_2.order.add_edge(Initial_Screening, Visual_Inspection)
seq_1_2.order.add_edge(Visual_Inspection, Imaging_Capture)
seq_1_2.order.add_edge(Imaging_Capture, Material_Testing)

# Compose provenance concurrent branches (Provenance Check and Database Search):
prov_po = StrictPartialOrder(nodes=[Provenance_Check, Database_Search])
# concurrent, no edges

# Compose expert branch after provenance
expert_branch = StrictPartialOrder(nodes=[Expert_Review])
# Must come after both provenance activities

# Compose cond_report and forgery_analysis concurrent after expert review
cond_forg_po = StrictPartialOrder(nodes=[Condition_Report, Forgery_Analysis])
# concurrent

# Build full ordering:

# Create list of all nodes that will appear in root
nodes_all = [
    Initial_Screening, Visual_Inspection, Imaging_Capture,
    Material_Testing, Provenance_Check, Database_Search, Expert_Review,
    Condition_Report, Forgery_Analysis, loop_historical,
    Legal_Compliance, Certificate_Issue,
    Digital_Archive, Client_Presentation, Final_Approval, Secure_Storage
]

root = StrictPartialOrder(nodes=nodes_all)

# Add edges for initial screening path
root.order.add_edge(Initial_Screening, Visual_Inspection)
root.order.add_edge(Visual_Inspection, Imaging_Capture)

# Imaging Capture -> Material Testing
root.order.add_edge(Imaging_Capture, Material_Testing)

# Material Testing -> Provenance Check and Database Search concurrently (both start after Material Testing)
root.order.add_edge(Material_Testing, Provenance_Check)
root.order.add_edge(Material_Testing, Database_Search)

# Provenance Check and Database Search both precede Expert Review
root.order.add_edge(Provenance_Check, Expert_Review)
root.order.add_edge(Database_Search, Expert_Review)

# Expert Review precedes Condition Report and Forgery Analysis concurrently
root.order.add_edge(Expert_Review, Condition_Report)
root.order.add_edge(Expert_Review, Forgery_Analysis)

# Condition Report and Forgery Analysis both precede loop_historical (loop on Historical Crossref)
root.order.add_edge(Condition_Report, loop_historical)
root.order.add_edge(Forgery_Analysis, loop_historical)

# loop_historical precedes Legal Compliance
root.order.add_edge(loop_historical, Legal_Compliance)

# Legal Compliance precedes Certificate Issue
root.order.add_edge(Legal_Compliance, Certificate_Issue)

# Certificate Issue precedes Digital Archive -> Client Presentation -> Final Approval -> Secure Storage
root.order.add_edge(Certificate_Issue, Digital_Archive)
root.order.add_edge(Digital_Archive, Client_Presentation)
root.order.add_edge(Client_Presentation, Final_Approval)
root.order.add_edge(Final_Approval, Secure_Storage)