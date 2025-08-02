# Generated from: 67b6bc49-7d25-485d-b414-132e5919e2e3.json
# Description: This process involves the careful evaluation, documentation, and restoration of antique artifacts to preserve their historical integrity while enhancing their aesthetic appeal. It includes detailed condition assessments, sourcing of period-accurate materials, delicate cleaning procedures, and expert craftsmanship to repair damages without compromising originality. Continuous consultation with historians and material scientists ensures authenticity. The process concludes with final quality checks, certification, and preparation for display or sale, balancing conservation ethics with market demands.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Artifact_Intake = Transition(label='Artifact Intake')
Historical_Research = Transition(label='Historical Research')
Condition_Survey = Transition(label='Condition Survey')
Material_Sourcing = Transition(label='Material Sourcing')
Cleaning_Prep = Transition(label='Cleaning Prep')
Surface_Cleaning = Transition(label='Surface Cleaning')
Structural_Repair = Transition(label='Structural Repair')
Finish_Restoration = Transition(label='Finish Restoration')
Expert_Consultation = Transition(label='Expert Consultation')
Documentation = Transition(label='Documentation')
Quality_Review = Transition(label='Quality Review')
Certification = Transition(label='Certification')
Packaging = Transition(label='Packaging')
Display_Setup = Transition(label='Display Setup')
Client_Handover = Transition(label='Client Handover')

# Partial order 1: Initial evaluation and preparation:
# Artifact Intake then parallel Historical Research and Condition Survey
initial_eval = StrictPartialOrder(nodes=[Artifact_Intake, Historical_Research, Condition_Survey])
initial_eval.order.add_edge(Artifact_Intake, Historical_Research)
initial_eval.order.add_edge(Artifact_Intake, Condition_Survey)

# Partial order 2: Material sourcing after Condition Survey
material_sourcing = StrictPartialOrder(nodes=[Condition_Survey, Material_Sourcing])
material_sourcing.order.add_edge(Condition_Survey, Material_Sourcing)

# Partial order 3: Cleaning sequence after Material Sourcing
cleaning_seq = StrictPartialOrder(
    nodes=[Material_Sourcing, Cleaning_Prep, Surface_Cleaning])
cleaning_seq.order.add_edge(Material_Sourcing, Cleaning_Prep)
cleaning_seq.order.add_edge(Cleaning_Prep, Surface_Cleaning)

# Partial order 4: Repair and restoration after cleaning
repair_and_restore = StrictPartialOrder(
    nodes=[Surface_Cleaning, Structural_Repair, Finish_Restoration])
repair_and_restore.order.add_edge(Surface_Cleaning, Structural_Repair)
repair_and_restore.order.add_edge(Structural_Repair, Finish_Restoration)

# Partial order 5: Expert Consultation overlaps with Documentation
# Expert Consultation occurs after Historical Research and Condition Survey
expert_consult = StrictPartialOrder(
    nodes=[Historical_Research, Condition_Survey, Expert_Consultation])
expert_consult.order.add_edge(Historical_Research, Expert_Consultation)
expert_consult.order.add_edge(Condition_Survey, Expert_Consultation)

# Documentation after Expert Consultation and Finish Restoration
documentation_po = StrictPartialOrder(
    nodes=[Expert_Consultation, Finish_Restoration, Documentation])
documentation_po.order.add_edge(Expert_Consultation, Documentation)
documentation_po.order.add_edge(Finish_Restoration, Documentation)

# Partial order 6: Final quality checks and certification after documentation
final_checks = StrictPartialOrder(
    nodes=[Documentation, Quality_Review, Certification])
final_checks.order.add_edge(Documentation, Quality_Review)
final_checks.order.add_edge(Quality_Review, Certification)

# Partial order 7: Packaging, Display Setup after Certification
final_prep = StrictPartialOrder(
    nodes=[Certification, Packaging, Display_Setup])
final_prep.order.add_edge(Certification, Packaging)
final_prep.order.add_edge(Certification, Display_Setup)

# Client Handover last, after packaging and display setup
handover_po = StrictPartialOrder(
    nodes=[Packaging, Display_Setup, Client_Handover])
handover_po.order.add_edge(Packaging, Client_Handover)
handover_po.order.add_edge(Display_Setup, Client_Handover)

# Build the full model by combining partial orders with proper dependencies
# We can represent the flow as a partial order connecting these partial orders

# The nodes of the root PO are the activities themselves (all 15)
all_nodes = [
    Artifact_Intake,
    Historical_Research,
    Condition_Survey,
    Material_Sourcing,
    Cleaning_Prep,
    Surface_Cleaning,
    Structural_Repair,
    Finish_Restoration,
    Expert_Consultation,
    Documentation,
    Quality_Review,
    Certification,
    Packaging,
    Display_Setup,
    Client_Handover
]

root = StrictPartialOrder(nodes=all_nodes)

# Add order edges according to all partial orders above

# initial_eval edges
root.order.add_edge(Artifact_Intake, Historical_Research)
root.order.add_edge(Artifact_Intake, Condition_Survey)

# material_sourcing edge
root.order.add_edge(Condition_Survey, Material_Sourcing)

# cleaning_seq edges
root.order.add_edge(Material_Sourcing, Cleaning_Prep)
root.order.add_edge(Cleaning_Prep, Surface_Cleaning)

# repair_and_restore edges
root.order.add_edge(Surface_Cleaning, Structural_Repair)
root.order.add_edge(Structural_Repair, Finish_Restoration)

# expert_consult edges
root.order.add_edge(Historical_Research, Expert_Consultation)
root.order.add_edge(Condition_Survey, Expert_Consultation)

# documentation_po edges
root.order.add_edge(Expert_Consultation, Documentation)
root.order.add_edge(Finish_Restoration, Documentation)

# final_checks edges
root.order.add_edge(Documentation, Quality_Review)
root.order.add_edge(Quality_Review, Certification)

# final_prep edges
root.order.add_edge(Certification, Packaging)
root.order.add_edge(Certification, Display_Setup)

# handover_po edges
root.order.add_edge(Packaging, Client_Handover)
root.order.add_edge(Display_Setup, Client_Handover)