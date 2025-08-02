# Generated from: 728d126e-02cc-4d82-a4f8-9bbdecb935ca.json
# Description: This process involves the detailed authentication and provenance verification of historical artifacts before acquisition or exhibition. It begins with initial artifact intake and visual inspection, followed by material composition analysis using advanced spectroscopy techniques. Next, provenance research is conducted through archival records and expert interviews. Radiocarbon dating and microscopic wear pattern analysis are performed to ascertain age and usage. Concurrently, digital 3D scanning captures precise artifact morphology for virtual reconstruction. A multidisciplinary panel reviews the compiled data to confirm authenticity. Finally, secure cataloging and condition reporting conclude the workflow, ensuring that only verified artifacts proceed to display or sale, minimizing fraud and preserving cultural heritage integrity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Artifact_Intake = Transition(label='Artifact Intake')
Visual_Inspect = Transition(label='Visual Inspect')
Material_Scan = Transition(label='Material Scan')

Provenance_Check = Transition(label='Provenance Check')
Archive_Research = Transition(label='Archive Research')
Expert_Consult = Transition(label='Expert Consult')

Radiocarbon_Test = Transition(label='Radiocarbon Test')
Wear_Analysis = Transition(label='Wear Analysis')

Scan_3D = Transition(label='3D Scanning')

Data_Compilation = Transition(label='Data Compilation')
Panel_Review = Transition(label='Panel Review')
Authenticity_Confirm = Transition(label='Authenticity Confirm')

Secure_Catalog = Transition(label='Secure Catalog')
Condition_Report = Transition(label='Condition Report')

Final_Approval = Transition(label='Final Approval')

# Provenance research subworkflow: choice (XOR) between Archive Research and Expert Consult, both as children of Provenance_Check
# According to description, Provenance Check is conducted through Archive Research and Expert Interviews,
# so this likely means these two act concurrently or as a partial order under Provenance_Check.
# However, the description explicitly says: "Provenance research is conducted through archival records and expert interviews".
# They should be performed both, so concurrency or partial order.
# We model Provenance_Check as a strict partial order of Archive_Research and Expert_Consult, then Provenance_Check is a parent node?
# Actually, description suggests Provenance_Check encompassing these two activities, so we treat Provenance_Check as a label of the overall provenance research
# OR remove Provenance_Check and just use Archive_Research and Expert_Consult concurrently.
# The activities list includes Provenance_Check explicitly.
# So we might do Provenance_Check as a silent transition or node that precedes Archive_Research and Expert_Consult in parallel.
# But considering as a single activity "Provenance Check" plus Archive_Research and Expert_Consult underneath as sub-activities is complex here.
# Instead, interpret Provenance_Check as the phase header; then Archive_Research and Expert_Consult are performed in parallel
# So model Provenance_Check as a node followed by concurrency of Archive_Research and Expert_Consult.
# Alternatively, Provenance_Check can be skipped, since Archive_Research and Expert_Consult are the actual tasks.
# To follow the prompt strictly, all activities must be used.

# Choose to model Provenance_Check as a silent transition connecting to both Archive_Research and Expert_Consult concurrently.

# Define a silent transition for Provenance_Check start to split concurrency
Provenance_Start = SilentTransition()

# Construct the model accordingly

# Partial order of Provenance Research: Provenance_Start triggers both Archive_Research and Expert_Consult concurrently
# Partial order of Radiocarbon Test and Wear Analysis is sequential or concurrent?
# "Radiocarbon dating and microscopic wear pattern analysis are performed", likely concurrently.

# Also, 3D Scanning happens concurrently alongside Radiocarbon_Test and Wear_Analysis.

# Data Compilation happens after Radiocarbon_Test, Wear_Analysis, and 3D Scanning complete.

# Then Panel Review, then Authenticity Confirm sequentially.

# Finally, Secure Catalog and Condition Report concurrently, then Final Approval

# Build partial orders and concurrency accordingly.

# Begin:

# 1) Artifact Intake --> Visual Inspect --> Material Scan --> Provenance_Check --> (Archive Research || Expert Consult) --> Radiocarbon & Wear Analysis & 3D Scanning --> Data Compilation --> Panel Review --> Authenticity Confirm --> Secure Catalog & Condition Report --> Final Approval

# Provenance_Check step: replace by Provenance_Start silent node before two concurrent nodes Archive_Research and Expert_Consult
# So order: Material Scan --> Provenance_Start --> Archive_Research and Expert_Consult concurrent

# Need also to connect Provenance_Start to Provenance_Check activity (explicit activity)

# Possibly model Provenance_Check as a transition that occurs after Archive_Research and Expert_Consult complete?
# But description lists Provenance_Check as an activity.

# So a reasonable model:

# Material Scan --> Provenance_Check --> Provenance_Start (silent) --> Archive_Research and Expert_Consult concurrently

# Alternatively, Provenance_Check is a node between Material Scan and Archive_Research & Expert_Consult concurrency.

# Then Radiocarbon_Test and Wear_Analysis parallel after those, and 3D Scanning concurrent with those.

# So the phase after Provenance research is Radiocarbon_Test, Wear_Analysis, and 3D Scanning in concurrency.

# Then Data Compilation after those three.

# Then Panel Review, Authenticity Confirm sequentially.

# Then Secure Catalog and Condition Report concurrently.

# Then Final Approval.

# Implement step by step.

# Start building the model nodes list and edges:

nodes = [
    Artifact_Intake,
    Visual_Inspect,
    Material_Scan,
    Provenance_Check,
    Provenance_Start,
    Archive_Research,
    Expert_Consult,
    Radiocarbon_Test,
    Wear_Analysis,
    Scan_3D,
    Data_Compilation,
    Panel_Review,
    Authenticity_Confirm,
    Secure_Catalog,
    Condition_Report,
    Final_Approval,
]

root = StrictPartialOrder(nodes=nodes)

# Add edges for sequential flow:
root.order.add_edge(Artifact_Intake, Visual_Inspect)
root.order.add_edge(Visual_Inspect, Material_Scan)
root.order.add_edge(Material_Scan, Provenance_Check)
root.order.add_edge(Provenance_Check, Provenance_Start)

# Provenance_Start splits into concurrent Archive Research and Expert Consult
root.order.add_edge(Provenance_Start, Archive_Research)
root.order.add_edge(Provenance_Start, Expert_Consult)

# Next steps happen after both Archive_Research and Expert_Consult complete:
# So Radiocarbon_Test and Wear_Analysis can only start after both finish.

# Because both should finish before going to next step, so add edges:
root.order.add_edge(Archive_Research, Radiocarbon_Test)
root.order.add_edge(Expert_Consult, Radiocarbon_Test)

root.order.add_edge(Archive_Research, Wear_Analysis)
root.order.add_edge(Expert_Consult, Wear_Analysis)

# Radiocarbon_Test and Wear_Analysis are concurrent
# 3D Scanning runs concurrently with these two, but it is not dependent on them
# So no edges required for concurrency

# After all three complete, Data Compilation
root.order.add_edge(Radiocarbon_Test, Data_Compilation)
root.order.add_edge(Wear_Analysis, Data_Compilation)
root.order.add_edge(Scan_3D, Data_Compilation)

# Data Compilation --> Panel Review --> Authenticity Confirm
root.order.add_edge(Data_Compilation, Panel_Review)
root.order.add_edge(Panel_Review, Authenticity_Confirm)

# Authenticity Confirm --> Secure Catalog and Condition Report concurrent
root.order.add_edge(Authenticity_Confirm, Secure_Catalog)
root.order.add_edge(Authenticity_Confirm, Condition_Report)

# Secure Catalog and Condition Report --> Final Approval
root.order.add_edge(Secure_Catalog, Final_Approval)
root.order.add_edge(Condition_Report, Final_Approval)