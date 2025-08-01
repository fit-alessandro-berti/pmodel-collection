# Generated from: 10543713-2ad4-4575-bb41-868f3691219e.json
# Description: This process involves the meticulous restoration of ancient artifacts that require a blend of scientific analysis and artistic skill. It begins with initial condition assessment and documentation, followed by material identification through spectroscopy and microscopic examination. Conservation treatments are then planned, including stabilization, cleaning, and structural repair using reversible materials. Throughout the restoration, environmental controls and ethical considerations are strictly maintained to preserve authenticity. After treatment, the artifact undergoes final quality checks, digital archiving, and preparation for exhibition or storage, ensuring both historical integrity and future research accessibility.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
cond_check       = Transition(label='Condition Check')
photo_capture    = Transition(label='Photo Capture')
material_scan    = Transition(label='Material Scan')
microscope_rev   = Transition(label='Microscope Review')
damage_mapping   = Transition(label='Damage Mapping')
treatment_plan   = Transition(label='Treatment Plan')
clean_surface    = Transition(label='Clean Surface')
stabilize_struct = Transition(label='Stabilize Structure')
apply_adhesive   = Transition(label='Apply Adhesive')
fill_gaps        = Transition(label='Fill Gaps')
color_match      = Transition(label='Color Match')
protect_coating  = Transition(label='Protect Coating')
quality_inspect  = Transition(label='Quality Inspect')
digital_archive  = Transition(label='Digital Archive')
exhibit_prep     = Transition(label='Exhibit Prep')
storage_setup    = Transition(label='Storage Setup')

# Define the XOR choice between Exhibition and Storage
end_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[exhibit_prep, storage_setup]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    cond_check, photo_capture,
    material_scan, microscope_rev,
    damage_mapping, treatment_plan,
    clean_surface, stabilize_struct,
    apply_adhesive, fill_gaps,
    color_match, protect_coating,
    quality_inspect, digital_archive,
    end_choice
])

# Initial assessment and documentation
root.order.add_edge(cond_check, photo_capture)

# Material identification (parallel spectroscopy & microscopy)
root.order.add_edge(photo_capture, material_scan)
root.order.add_edge(photo_capture, microscope_rev)

# Damage mapping after both scans
root.order.add_edge(material_scan, damage_mapping)
root.order.add_edge(microscope_rev, damage_mapping)

# Treatment planning
root.order.add_edge(damage_mapping, treatment_plan)

# Conservation treatments: cleaning & stabilization in parallel
root.order.add_edge(treatment_plan, clean_surface)
root.order.add_edge(treatment_plan, stabilize_struct)

# Structural repair steps after both cleaning & stabilization
root.order.add_edge(clean_surface, apply_adhesive)
root.order.add_edge(stabilize_struct, apply_adhesive)
root.order.add_edge(clean_surface, fill_gaps)
root.order.add_edge(stabilize_struct, fill_gaps)

# Finishing treatments
root.order.add_edge(apply_adhesive, color_match)
root.order.add_edge(fill_gaps, color_match)
root.order.add_edge(color_match, protect_coating)

# Post‐treatment checks & archiving
root.order.add_edge(protect_coating, quality_inspect)
root.order.add_edge(quality_inspect, digital_archive)

# Final exclusive choice: exhibit or storage
root.order.add_edge(digital_archive, end_choice)