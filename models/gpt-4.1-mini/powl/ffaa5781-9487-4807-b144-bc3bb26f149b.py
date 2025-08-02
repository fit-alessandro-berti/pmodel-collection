# Generated from: ffaa5781-9487-4807-b144-bc3bb26f149b.json
# Description: This process involves the comprehensive verification and authentication of historical artifacts prior to acquisition or display in a museum. It begins with initial provenance research followed by multidisciplinary scientific analysis including radiocarbon dating, material composition tests, and microscopic examination. Concurrently, expert consultations with historians and archaeologists are conducted to validate contextual accuracy. Legal ownership and export documentation are scrutinized to ensure compliance with international cultural heritage laws. The workflow also incorporates digital imaging and 3D modeling for record-keeping and virtual exhibition purposes. Final approval requires a consensus meeting among curators, legal advisors, and scientific analysts before formal acquisition and cataloging into the museum's database.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Provenance_Check = Transition(label='Provenance Check')

Radiocarbon_Test = Transition(label='Radiocarbon Test')
Material_Analysis = Transition(label='Material Analysis')
Microscopic_Scan = Transition(label='Microscopic Scan')

Expert_Review = Transition(label='Expert Review')
Context_Validation = Transition(label='Context Validation')

Legal_Audit = Transition(label='Legal Audit')
Export_Verify = Transition(label='Export Verify')

Digital_Imaging = Transition(label='Digital Imaging')
ThreeD_Modeling = Transition(label='3D Modeling')

Consensus_Meeting = Transition(label='Consensus Meeting')
Final_Approval = Transition(label='Final Approval')

Catalog_Entry = Transition(label='Catalog Entry')
Virtual_Setup = Transition(label='Virtual Setup')
Archival_Backup = Transition(label='Archival Backup')

# Multidisciplinary scientific analysis partial order
scientific_analysis = StrictPartialOrder(nodes=[Radiocarbon_Test, Material_Analysis, Microscopic_Scan])
# no edges -> concurrent

# Expert consultations partial order
expert_consultations = StrictPartialOrder(nodes=[Expert_Review, Context_Validation])
# no edges -> concurrent

# Legal scrutiny partial order
legal_scrutiny = StrictPartialOrder(nodes=[Legal_Audit, Export_Verify])
# no edges -> concurrent

# Digital record-keeping partial order
digital_record = StrictPartialOrder(nodes=[Digital_Imaging, ThreeD_Modeling])
# no edges -> concurrent

# Final approval sequence (consensus meeting -> final approval)
final_approval_seq = StrictPartialOrder(nodes=[Consensus_Meeting, Final_Approval])
final_approval_seq.order.add_edge(Consensus_Meeting, Final_Approval)

# Final cataloging partial order (concurrent activities)
cataloging_concurrent = StrictPartialOrder(
    nodes=[Catalog_Entry, Virtual_Setup, Archival_Backup])
# no edges -> concurrent

# Initial provenance research then scientific analysis and expert consultations and legal scrutiny and digital record-keeping
# Scientific analysis, expert consultations, legal scrutiny, and digital record are done concurrently after Provenance Check

# Combine all concurrent branches after Provenance_Check
post_provenance = StrictPartialOrder(
    nodes=[scientific_analysis, expert_consultations, legal_scrutiny, digital_record])
# no edges to keep concurrency

# Create root partial order with nodes: Provenance_Check and the four concurrent groups above and final approval sequence and cataloging
root = StrictPartialOrder(
    nodes=[Provenance_Check,
           scientific_analysis,
           expert_consultations,
           legal_scrutiny,
           digital_record,
           final_approval_seq,
           cataloging_concurrent])

# Order edges:
# Provenance_Check precedes scientific_analysis, expert_consultations, legal_scrutiny, digital_record
root.order.add_edge(Provenance_Check, scientific_analysis)
root.order.add_edge(Provenance_Check, expert_consultations)
root.order.add_edge(Provenance_Check, legal_scrutiny)
root.order.add_edge(Provenance_Check, digital_record)

# After all above complete, the consensus meeting (final_approval_seq) can start
# We assume final approval requires consensus meeting, legal advisors, and scientific analysts (implied)
#
# The "final approval requires consensus meeting among curators, legal advisors, and scientific analysts"
# We model that final_approval_seq happens after expert_consultations, legal_scrutiny, scientific_analysis
root.order.add_edge(scientific_analysis, final_approval_seq)
root.order.add_edge(expert_consultations, final_approval_seq)
root.order.add_edge(legal_scrutiny, final_approval_seq)

# Then after final approval, cataloging and setups happen concurrently
root.order.add_edge(final_approval_seq, cataloging_concurrent)