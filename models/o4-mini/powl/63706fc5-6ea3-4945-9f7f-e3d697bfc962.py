# Generated from: 63706fc5-6ea3-4945-9f7f-e3d697bfc962.json
# Description: This process outlines the intricate steps involved in restoring antique artifacts, combining historical research, material analysis, and specialized craftsmanship. It begins with artifact assessment and provenance verification, followed by condition documentation and damage mapping. The process includes sourcing period-appropriate materials, stabilizing fragile components, and performing delicate cleaning using chemical and mechanical methods. Restoration artisans then reconstruct missing parts using traditional techniques while ensuring minimal intervention. A final quality review ensures historical accuracy and structural integrity before packaging and archival recording for future reference and provenance tracking.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
artifact_assess    = Transition(label="Artifact Assess")
provenance_check   = Transition(label="Provenance Check")
condition_scan     = Transition(label="Condition Scan")
damage_mapping     = Transition(label="Damage Mapping")
material_source    = Transition(label="Material Source")
fragility_test     = Transition(label="Fragility Test")
stabilize_structure= Transition(label="Stabilize Structure")
chemical_clean     = Transition(label="Chemical Clean")
mechanical_clean   = Transition(label="Mechanical Clean")
part_reconstruction= Transition(label="Part Reconstruction")
surface_treatment  = Transition(label="Surface Treatment")
quality_review     = Transition(label="Quality Review")
historical_audit   = Transition(label="Historical Audit")
packaging_prep     = Transition(label="Packaging Prep")
archival_record    = Transition(label="Archival Record")

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    artifact_assess,
    provenance_check,
    condition_scan,
    damage_mapping,
    material_source,
    fragility_test,
    stabilize_structure,
    chemical_clean,
    mechanical_clean,
    part_reconstruction,
    surface_treatment,
    quality_review,
    historical_audit,
    packaging_prep,
    archival_record
])

# Define control‐flow dependencies
# 1. Start: Artifact Assess & Provenance Check
root.order.add_edge(artifact_assess, condition_scan)
root.order.add_edge(provenance_check, condition_scan)

# 2. Condition documentation then damage mapping
root.order.add_edge(condition_scan, damage_mapping)

# 3. After mapping: material sourcing & fragility testing
root.order.add_edge(damage_mapping, material_source)
root.order.add_edge(damage_mapping, fragility_test)

# 4. Stabilize after testing
root.order.add_edge(fragility_test, stabilize_structure)

# 5. Cleaning (chemical & mechanical) after sourcing & stabilization
root.order.add_edge(material_source, chemical_clean)
root.order.add_edge(stabilize_structure, chemical_clean)
root.order.add_edge(material_source, mechanical_clean)
root.order.add_edge(stabilize_structure, mechanical_clean)

# 6. Part reconstruction after both cleans
root.order.add_edge(chemical_clean, part_reconstruction)
root.order.add_edge(mechanical_clean, part_reconstruction)

# 7. Surface treatment → reviews
root.order.add_edge(part_reconstruction, surface_treatment)
root.order.add_edge(surface_treatment, quality_review)
root.order.add_edge(surface_treatment, historical_audit)

# 8. Packaging prep after both reviews
root.order.add_edge(quality_review, packaging_prep)
root.order.add_edge(historical_audit, packaging_prep)

# 9. Final archival recording
root.order.add_edge(packaging_prep, archival_record)