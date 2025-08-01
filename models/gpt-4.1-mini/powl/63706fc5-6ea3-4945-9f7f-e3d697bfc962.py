# Generated from: 63706fc5-6ea3-4945-9f7f-e3d697bfc962.json
# Description: This process outlines the intricate steps involved in restoring antique artifacts, combining historical research, material analysis, and specialized craftsmanship. It begins with artifact assessment and provenance verification, followed by condition documentation and damage mapping. The process includes sourcing period-appropriate materials, stabilizing fragile components, and performing delicate cleaning using chemical and mechanical methods. Restoration artisans then reconstruct missing parts using traditional techniques while ensuring minimal intervention. A final quality review ensures historical accuracy and structural integrity before packaging and archival recording for future reference and provenance tracking.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
artifact_assess = Transition(label='Artifact Assess')
provenance_check = Transition(label='Provenance Check')

condition_scan = Transition(label='Condition Scan')
damage_mapping = Transition(label='Damage Mapping')

material_source = Transition(label='Material Source')
fragility_test = Transition(label='Fragility Test')

chemical_clean = Transition(label='Chemical Clean')
mechanical_clean = Transition(label='Mechanical Clean')

stabilize_structure = Transition(label='Stabilize Structure')
surface_treatment = Transition(label='Surface Treatment')

part_reconstruction = Transition(label='Part Reconstruction')

quality_review = Transition(label='Quality Review')
historical_audit = Transition(label='Historical Audit')

packaging_prep = Transition(label='Packaging Prep')
archival_record = Transition(label='Archival Record')

# Choice between Chemical Clean or Mechanical Clean (cleaning methods)
cleaning_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[chemical_clean, mechanical_clean]
)

# Partial order for cleaning process: Stabilize → cleaning_choice → Surface Treatment
cleaning_process = StrictPartialOrder(
    nodes=[stabilize_structure, cleaning_choice, surface_treatment]
)
cleaning_process.order.add_edge(stabilize_structure, cleaning_choice)
cleaning_process.order.add_edge(cleaning_choice, surface_treatment)

# Partial order for initial assessment and condition documentation
assessment = StrictPartialOrder(
    nodes=[artifact_assess, provenance_check]
)
assessment.order.add_edge(artifact_assess, provenance_check)

condition_document = StrictPartialOrder(
    nodes=[condition_scan, damage_mapping]
)
condition_document.order.add_edge(condition_scan, damage_mapping)

# Partial order for the initial phase: assessment → condition_document
initial_phase = StrictPartialOrder(
    nodes=[assessment, condition_document]
)
initial_phase.order.add_edge(assessment, condition_document)

# Partial order for sourcing materials and fragility test (concurrent could be possible, 
# but fragility test is likely after sourcing, so order added)
materials_phase = StrictPartialOrder(
    nodes=[material_source, fragility_test]
)
materials_phase.order.add_edge(material_source, fragility_test)

# Partial order for reconstruction: part reconstruction alone (depends on cleaning process)
reconstruction_phase = part_reconstruction

# Partial order for final quality and historical audit (concurrent)
final_quality = StrictPartialOrder(
    nodes=[quality_review, historical_audit]
)

# Partial order for packaging and archival recording (concurrent)
final_packaging = StrictPartialOrder(
    nodes=[packaging_prep, archival_record]
)

# Build the overall process order:

# Phase 1: initial_phase → materials_phase → cleaning_process → part_reconstruction → final_quality → final_packaging

root = StrictPartialOrder(
    nodes=[
        initial_phase,
        materials_phase,
        cleaning_process,
        reconstruction_phase,
        final_quality,
        final_packaging
    ]
)

# Add edges for strict partial order
root.order.add_edge(initial_phase, materials_phase)
root.order.add_edge(materials_phase, cleaning_process)
root.order.add_edge(cleaning_process, reconstruction_phase)
root.order.add_edge(reconstruction_phase, final_quality)
root.order.add_edge(final_quality, final_packaging)