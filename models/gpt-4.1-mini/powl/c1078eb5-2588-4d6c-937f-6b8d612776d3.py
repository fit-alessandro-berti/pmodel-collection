# Generated from: c1078eb5-2588-4d6c-937f-6b8d612776d3.json
# Description: This process details a comprehensive artifact authentication workflow used by museums and private collectors to verify the provenance and authenticity of rare historical items. It involves multidisciplinary expert evaluations, advanced material analysis, provenance record cross-checking, and digital fingerprinting technology. The workflow integrates collaboration between historians, chemists, and data scientists to ensure artifacts are genuine, mitigating risks of forgeries. Final verification results are documented and archived securely to support insurance and exhibition planning. The process requires iterative validation rounds and consensus building among experts before final certification is granted.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Initial_Review = Transition(label='Initial Review')
Provenance_Check = Transition(label='Provenance Check')
Material_Scan = Transition(label='Material Scan')
Historical_Compare = Transition(label='Historical Compare')
Expert_Consult = Transition(label='Expert Consult')
Digital_Imaging = Transition(label='Digital Imaging')
Fingerprint_Match = Transition(label='Fingerprint Match')
Chemical_Test = Transition(label='Chemical Test')
Radiocarbon_Date = Transition(label='Radiocarbon Date')
Context_Analysis = Transition(label='Context Analysis')
Forgery_Detection = Transition(label='Forgery Detection')
Consensus_Meeting = Transition(label='Consensus Meeting')
Certification_Prep = Transition(label='Certification Prep')
Documentation = Transition(label='Documentation')
Archive_Storage = Transition(label='Archive Storage')
Insurance_Liaison = Transition(label='Insurance Liaison')
Exhibit_Setup = Transition(label='Exhibit Setup')

# --- Build the model ---

# Expert evaluation branch (Historians, Chemists, Data Scientists):

# Historical Expert path: Historical Compare -> Expert Consult -> Consensus Meeting
hist_expert_PO = StrictPartialOrder(nodes=[Historical_Compare, Expert_Consult, Consensus_Meeting])
hist_expert_PO.order.add_edge(Historical_Compare, Expert_Consult)
hist_expert_PO.order.add_edge(Expert_Consult, Consensus_Meeting)

# Chemical Expert path: Chemical Test & Radiocarbon Date -> Consensus Meeting
# Chemical Test and Radiocarbon Date can run concurrently before Consensus Meeting
chem_PO = StrictPartialOrder(nodes=[Chemical_Test, Radiocarbon_Date, Consensus_Meeting])
chem_PO.order.add_edge(Chemical_Test, Consensus_Meeting)
chem_PO.order.add_edge(Radiocarbon_Date, Consensus_Meeting)

# Data Science Expert path: Digital Imaging -> Fingerprint Match -> Forgery Detection -> Consensus Meeting
data_science_PO = StrictPartialOrder(
    nodes=[Digital_Imaging, Fingerprint_Match, Forgery_Detection, Consensus_Meeting]
)
data_science_PO.order.add_edge(Digital_Imaging, Fingerprint_Match)
data_science_PO.order.add_edge(Fingerprint_Match, Forgery_Detection)
data_science_PO.order.add_edge(Forgery_Detection, Consensus_Meeting)

# Combine the three expert tracks concurrent except Consensus Meeting which synchronizes them:
# We can have Historical_Compare, Chemical_Test, Radiocarbon_Date, Digital_Imaging start in parallel,
# but all must precede Consensus_Meeting.

# For this, create a PO with nodes:
# Initial nodes: Historical_Compare, Chemical_Test, Radiocarbon_Date, Digital_Imaging
# Then: Expert_Consult, Fingerprint_Match, Forgery_Detection, Consensus_Meeting

# But the previous small POs have Consensus_Meeting included; we cannot reuse the same object
# in multiple places; instead, we create unique nodes representing those activities in the combined PO.

# Instead, let's unify them as distinct nodes with shared Consensus Meeting:
Consensus = Transition(label='Consensus Meeting')

# Redefine the nodes with unique ones for this combined PO:
Hist_Compare = Transition(label='Historical Compare')
Expert_Cons = Transition(label='Expert Consult')
Chem_Test = Transition(label='Chemical Test')
Radio_Date = Transition(label='Radiocarbon Date')
Dig_Imaging = Transition(label='Digital Imaging')
Fing_Match = Transition(label='Fingerprint Match')
Forg_Detect = Transition(label='Forgery Detection')

# Build combined expert evaluation PO:
nodes_expert = [
    Hist_Compare, Expert_Cons,
    Chem_Test, Radio_Date,
    Dig_Imaging, Fing_Match, Forg_Detect,
    Consensus
]

expert_PO = StrictPartialOrder(nodes=nodes_expert)

# Historical expert path edges
expert_PO.order.add_edge(Hist_Compare, Expert_Cons)
expert_PO.order.add_edge(Expert_Cons, Consensus)

# Chemical expert path edges (Chemical Test & Radiocarbon Date concurrent)
expert_PO.order.add_edge(Chem_Test, Consensus)
expert_PO.order.add_edge(Radio_Date, Consensus)

# Data Science expert path edges
expert_PO.order.add_edge(Dig_Imaging, Fing_Match)
expert_PO.order.add_edge(Fing_Match, Forg_Detect)
expert_PO.order.add_edge(Forg_Detect, Consensus)

# Initial Review leads to Provenance Check and Material Scan & Context Analysis
# which run concurrently before the expert evaluation
Provenance = Transition(label='Provenance Check')
Material = Transition(label='Material Scan')
Context = Transition(label='Context Analysis')

initial_PO = StrictPartialOrder(
    nodes=[Initial_Review, Provenance, Material, Context]
)
initial_PO.order.add_edge(Initial_Review, Provenance)
initial_PO.order.add_edge(Initial_Review, Material)
initial_PO.order.add_edge(Initial_Review, Context)

# After initial checks, Provenance Check leads into Expert Evaluation via Historical_Compare
# Material Scan leads to Data Science path via Digital Imaging
# Context Analysis leads to Chemical Tests

# Link initial_PO to expert_PO:
# Provenance -> Historical Compare
# Material -> Digital Imaging
# Context -> Chemical Test and Radiocarbon Date

# We cannot attach edges between two StrictPartialOrders directly;
# we combine all nodes into one big PO.

# Build the full node set:
nodes_all = [
    Initial_Review,

    Provenance,
    Material,
    Context,

    Hist_Compare, Expert_Cons,
    Chem_Test, Radio_Date,
    Dig_Imaging, Fing_Match, Forg_Detect,
    Consensus,

    # After Consensus: Certification Prep -> Documentation -> Archive Storage & Insurance Liaison (concurrent) -> Exhibit Setup

    Certification_Prep,
    Documentation,
    Archive_Storage,
    Insurance_Liaison,
    Exhibit_Setup
]

root = StrictPartialOrder(nodes=nodes_all)

# Orders:

# Initial phase concurrency after Initial Review
root.order.add_edge(Initial_Review, Provenance)
root.order.add_edge(Initial_Review, Material)
root.order.add_edge(Initial_Review, Context)

# Provenance leads to Historical Compare
root.order.add_edge(Provenance, Hist_Compare)
# Material leads to Digital Imaging
root.order.add_edge(Material, Dig_Imaging)
# Context leads to Chemical Test and Radiocarbon Date
root.order.add_edge(Context, Chem_Test)
root.order.add_edge(Context, Radio_Date)

# Historical expert path
root.order.add_edge(Hist_Compare, Expert_Cons)
root.order.add_edge(Expert_Cons, Consensus)

# Chemical expert path
root.order.add_edge(Chem_Test, Consensus)
root.order.add_edge(Radio_Date, Consensus)

# Data science expert path
root.order.add_edge(Dig_Imaging, Fing_Match)
root.order.add_edge(Fing_Match, Forg_Detect)
root.order.add_edge(Forg_Detect, Consensus)

# After Consensus, certification and final steps
root.order.add_edge(Consensus, Certification_Prep)
root.order.add_edge(Certification_Prep, Documentation)
root.order.add_edge(Documentation, Archive_Storage)
root.order.add_edge(Documentation, Insurance_Liaison)

# Archive Storage and Insurance Liaison run concurrently before Exhibit Setup
root.order.add_edge(Archive_Storage, Exhibit_Setup)
root.order.add_edge(Insurance_Liaison, Exhibit_Setup)

# Loop: iterative validation rounds before final consensus - model as a loop:
# Because the description says "The process requires iterative validation rounds and consensus building among experts before final certification is granted."
# We model the expert evaluation and consensus as loop body with a decision to exit or repeat

# Loop body: the expert evaluation including Historical Compare, ..., Consensus
# loop redo brings us back from Consensus Meeting to Provenance Check to redo evaluation parts

# To do this cleanly, isolate loop body as:
# body: PO including Provenance -> Hist_Compare, Material -> Dig_Imaging, ... to Consensus
# redo: activities before loop: Initial Review and the partial order to Provenance etc

# But Initial Review happens just once; iterative rounds apply to expert eval & provenance/material/context checks

# We create loop children:

# Loop body: starts at Provenance, Material, Context up to Consensus
loop_body_nodes = [
    Provenance,
    Material,
    Context,

    Hist_Compare, Expert_Cons,
    Chem_Test, Radio_Date,
    Dig_Imaging, Fing_Match, Forg_Detect,
    Consensus
]

loop_body = StrictPartialOrder(nodes=loop_body_nodes)
# Edges inside loop_body as before (only those related to these nodes):
loop_body.order.add_edge(Provenance, Hist_Compare)
loop_body.order.add_edge(Material, Dig_Imaging)
loop_body.order.add_edge(Context, Chem_Test)
loop_body.order.add_edge(Context, Radio_Date)

loop_body.order.add_edge(Hist_Compare, Expert_Cons)
loop_body.order.add_edge(Expert_Cons, Consensus)
loop_body.order.add_edge(Chem_Test, Consensus)
loop_body.order.add_edge(Radio_Date, Consensus)
loop_body.order.add_edge(Dig_Imaging, Fing_Match)
loop_body.order.add_edge(Fing_Match, Forg_Detect)
loop_body.order.add_edge(Forg_Detect, Consensus)

# Loop redo: a SilentTransition (skip/exit) to exit loop or skip to Certification Prep

redo = SilentTransition()

loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, redo])

# The full model starts with Initial Review, then the loop, then final steps:

final_PO = StrictPartialOrder(
    nodes=[Initial_Review, loop, Certification_Prep, Documentation, Archive_Storage, Insurance_Liaison, Exhibit_Setup]
)

final_PO.order.add_edge(Initial_Review, loop)
final_PO.order.add_edge(loop, Certification_Prep)
final_PO.order.add_edge(Certification_Prep, Documentation)
final_PO.order.add_edge(Documentation, Archive_Storage)
final_PO.order.add_edge(Documentation, Insurance_Liaison)
final_PO.order.add_edge(Archive_Storage, Exhibit_Setup)
final_PO.order.add_edge(Insurance_Liaison, Exhibit_Setup)

root = final_PO