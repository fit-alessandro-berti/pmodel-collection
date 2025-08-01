# Generated from: f63e07f2-1586-4bb2-982a-bef568aedf02.json
# Description: This process outlines the intricate steps involved in authenticating rare historical artifacts for a private museum collection. It begins with initial artifact intake, followed by provenance verification through archival research and expert interviews. Subsequently, advanced material analysis using spectroscopy and radiocarbon dating is conducted to determine the artifact's age and composition. Concurrently, digital imaging and 3D modeling capture detailed visual data. A collaborative review meeting with historians, scientists, and curators evaluates all collected data to reach a consensus on authenticity. If authenticated, the artifact undergoes conservation assessment and customized preservation planning. Finally, detailed documentation is archived and a public exhibition strategy is developed, ensuring the artifact's historical integrity is maintained while maximizing educational impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as labeled transitions
Artifact_Intake = Transition(label='Artifact Intake')

Provenance_Check = Transition(label='Provenance Check')
Archive_Research = Transition(label='Archive Research')
Expert_Interview = Transition(label='Expert Interview')

Material_Analysis = Transition(label='Material Analysis')
Spectroscopy_Test = Transition(label='Spectroscopy Test')
Carbon_Dating = Transition(label='Carbon Dating')

Digital_Imaging = Transition(label='Digital Imaging')
ThreeD_Modeling = Transition(label='3D Modeling')

Data_Review = Transition(label='Data Review')
Consensus_Meeting = Transition(label='Consensus Meeting')

Conservation_Plan = Transition(label='Conservation Plan')
Preservation_Setup = Transition(label='Preservation Setup')

Documentation = Transition(label='Documentation')
Exhibition_Prep = Transition(label='Exhibition Prep')

# Build provenance verification partial order: Provenance Check --> (Archive Research & Expert Interview concurrent)
provenance_PO = StrictPartialOrder(nodes=[Provenance_Check, Archive_Research, Expert_Interview])
provenance_PO.order.add_edge(Provenance_Check, Archive_Research)
provenance_PO.order.add_edge(Provenance_Check, Expert_Interview)
# Archive Research and Expert Interview are concurrent (no edge between them)

# Build material analysis partial order: Material Analysis --> Spectroscopy Test and Carbon Dating concurrent
material_analysis_PO = StrictPartialOrder(nodes=[Material_Analysis, Spectroscopy_Test, Carbon_Dating])
material_analysis_PO.order.add_edge(Material_Analysis, Spectroscopy_Test)
material_analysis_PO.order.add_edge(Material_Analysis, Carbon_Dating)
# Spectroscopy Test and Carbon Dating concurrent

# Build imaging partial order: Digital Imaging and 3D Modeling concurrent
imaging_PO = StrictPartialOrder(nodes=[Digital_Imaging, ThreeD_Modeling])
# no edges, fully concurrent

# Build concurrent partial order of material_analysis_PO and imaging_PO
# This means all 5 nodes: Spectroscopy_Test, Carbon_Dating, Material_Analysis, Digital_Imaging, ThreeD_Modeling together:
# with edges from Material_Analysis to Spectroscopy_Test and Carbon_Dating;
# Digital_Imaging and ThreeD_Modeling are concurrent with all others (no edges)
material_imaging_PO = StrictPartialOrder(
    nodes=[Material_Analysis, Spectroscopy_Test, Carbon_Dating, Digital_Imaging, ThreeD_Modeling]
)
material_imaging_PO.order.add_edge(Material_Analysis, Spectroscopy_Test)
material_imaging_PO.order.add_edge(Material_Analysis, Carbon_Dating)
# no edges for concurrent with digital imaging and 3D modeling

# Build review part: Data Review --> Consensus Meeting
review_PO = StrictPartialOrder(nodes=[Data_Review, Consensus_Meeting])
review_PO.order.add_edge(Data_Review, Consensus_Meeting)

# After consensus:
# Conservation Plan --> Preservation Setup
conservation_PO = StrictPartialOrder(nodes=[Conservation_Plan, Preservation_Setup])
conservation_PO.order.add_edge(Conservation_Plan, Preservation_Setup)

# Documentation and Exhibition Prep concurrent
doc_exh_PO = StrictPartialOrder(nodes=[Documentation, Exhibition_Prep])
# no edges between them means concurrent

# Build the main flow order step by step

# Step 1: Artifact Intake
# Step 2: Provenance verification partial order
# Step 3: Material analysis and imaging concurrent partial order
# Step 4: Data Review and Consensus Meeting in order
# Step 5: If authenticated (assumed deterministic here, so straight), conservation_PO
# Step 6: doc_exh_PO concurrent
# Merge these steps in a big partial order with edges defining order

nodes_main = [
    Artifact_Intake,
    provenance_PO,
    material_imaging_PO,
    review_PO,
    conservation_PO,
    doc_exh_PO
]

root = StrictPartialOrder(nodes=nodes_main)
# Artifact Intake --> Provenance Check partial order
root.order.add_edge(Artifact_Intake, provenance_PO)
# Provenance partial order --> material + imaging partial order
root.order.add_edge(provenance_PO, material_imaging_PO)
# material + imaging partial order --> review partial order
root.order.add_edge(material_imaging_PO, review_PO)
# review --> conservation partial order
root.order.add_edge(review_PO, conservation_PO)
# conservation --> doc + exhibition partial order
root.order.add_edge(conservation_PO, doc_exh_PO)