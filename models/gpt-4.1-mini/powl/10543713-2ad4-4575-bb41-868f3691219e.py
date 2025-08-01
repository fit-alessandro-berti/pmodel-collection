# Generated from: 10543713-2ad4-4575-bb41-868f3691219e.json
# Description: This process involves the meticulous restoration of ancient artifacts that require a blend of scientific analysis and artistic skill. It begins with initial condition assessment and documentation, followed by material identification through spectroscopy and microscopic examination. Conservation treatments are then planned, including stabilization, cleaning, and structural repair using reversible materials. Throughout the restoration, environmental controls and ethical considerations are strictly maintained to preserve authenticity. After treatment, the artifact undergoes final quality checks, digital archiving, and preparation for exhibition or storage, ensuring both historical integrity and future research accessibility.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
Condition_Check = Transition(label='Condition Check')
Photo_Capture = Transition(label='Photo Capture')
Material_Scan = Transition(label='Material Scan')
Microscope_Review = Transition(label='Microscope Review')
Damage_Mapping = Transition(label='Damage Mapping')
Treatment_Plan = Transition(label='Treatment Plan')
Clean_Surface = Transition(label='Clean Surface')
Stabilize_Structure = Transition(label='Stabilize Structure')
Apply_Adhesive = Transition(label='Apply Adhesive')
Fill_Gaps = Transition(label='Fill Gaps')
Color_Match = Transition(label='Color Match')
Protect_Coating = Transition(label='Protect Coating')
Quality_Inspect = Transition(label='Quality Inspect')
Digital_Archive = Transition(label='Digital Archive')
Exhibit_Prep = Transition(label='Exhibit Prep')
Storage_Setup = Transition(label='Storage Setup')

# Step 1: Initial condition assessment and documentation (Condition Check -> Photo Capture)
initial_PO = StrictPartialOrder(nodes=[Condition_Check, Photo_Capture])
initial_PO.order.add_edge(Condition_Check, Photo_Capture)

# Step 2: Material identification through spectroscopy and microscopic examination (Material Scan and Microscope Review in parallel)
material_PO = StrictPartialOrder(nodes=[Material_Scan, Microscope_Review])
# parallel means no order edges between these two

# Step 3: Damage mapping after material identification
damage_PO = StrictPartialOrder(nodes=[Damage_Mapping])
# damage mapping follows after both material scans complete, so edges from material_PO's nodes to Damage_Mapping

# Step 4: Conservation treatments planned (Treatment Plan)
treatment_plan_PO = StrictPartialOrder(nodes=[Treatment_Plan])
# after damage mapping

# Step 5: Treatments include:
# stabilization, cleaning, structural repair using reversible materials
# Stabilize Structure and Clean Surface can be parallel before adhesive and filling
# Then apply adhesive and fill gaps are sequential
# Color Match and Protect Coating are sequential afterward

# Create partial order for stabilization and cleaning in parallel
stabilize_clean_PO = StrictPartialOrder(nodes=[Stabilize_Structure, Clean_Surface])
# parallel: no edges between these two

# Then applying adhesive and filling gaps sequentially: Apply Adhesive -> Fill Gaps
adhesive_fill_PO = StrictPartialOrder(nodes=[Apply_Adhesive, Fill_Gaps])
adhesive_fill_PO.order.add_edge(Apply_Adhesive, Fill_Gaps)

# Then color match and protect coating sequentially: Color Match -> Protect Coating
color_protect_PO = StrictPartialOrder(nodes=[Color_Match, Protect_Coating])
color_protect_PO.order.add_edge(Color_Match, Protect_Coating)

# Combine all treatments in a partial order
# Order:
# Treatment Plan -> stabilize_clean_PO (both nodes)
# stabilize_clean_PO nodes -> adhesive_fill_PO nodes
# adhesive_fill_PO nodes -> color_protect_PO nodes

treatments_nodes = [
    Treatment_Plan,
    Stabilize_Structure,
    Clean_Surface,
    Apply_Adhesive,
    Fill_Gaps,
    Color_Match,
    Protect_Coating
]

treatments_PO = StrictPartialOrder(nodes=treatments_nodes)

# Add order edges
treatments_PO.order.add_edge(Treatment_Plan, Stabilize_Structure)
treatments_PO.order.add_edge(Treatment_Plan, Clean_Surface)

treatments_PO.order.add_edge(Stabilize_Structure, Apply_Adhesive)
treatments_PO.order.add_edge(Clean_Surface, Apply_Adhesive)

treatments_PO.order.add_edge(Apply_Adhesive, Fill_Gaps)
treatments_PO.order.add_edge(Fill_Gaps, Color_Match)
treatments_PO.order.add_edge(Color_Match, Protect_Coating)

# Step 6: Throughout restoration, environmental controls and ethical considerations maintained
# These are not explicit activities, so we consider this as a silent transition concurrent with treatments? 
# We can use a silent transition (skip) to represent this concurrency with the main sequences
skip = SilentTransition()

# Parallel of treatments_PO with skip (to represent environmental & ethical controls ongoing)
# So we create a partial order with nodes = treatments_PO + skip, no order edges between skip and treatments_PO nodes to keep concurrency
env_ethics_PO = StrictPartialOrder(nodes=treatments_nodes + [skip])

# Step 7: After treatment, final quality checks, digital archiving, preparation for exhibition or storage
# Quality Inspect -> Digital Archive -> (XOR: Exhibit Prep or Storage Setup)

final_PO_nodes = [
    Quality_Inspect,
    Digital_Archive,
]

# Create XOR for Exhibit Prep and Storage Setup
final_choice = OperatorPOWL(operator=Operator.XOR, children=[Exhibit_Prep, Storage_Setup])

final_PO = StrictPartialOrder(nodes=final_PO_nodes + [final_choice])

final_PO.order.add_edge(Quality_Inspect, Digital_Archive)
final_PO.order.add_edge(Digital_Archive, final_choice)

# Now connect all parts:

# initial_PO (Condition Check -> Photo Capture)
# then material_PO (Material Scan || Microscope Review)
# then Damage Mapping after material_PO
# then Treatment Plan after Damage Mapping
# then treatments_PO + skip (environmental controls)
# then final_PO (quality inspect etc.)

root_nodes = [
    initial_PO,
    material_PO,
    Damage_Mapping,
    env_ethics_PO,
    final_PO
]

root = StrictPartialOrder(nodes=root_nodes)

# Define order edges between these submodels accordingly:

# After Photo Capture, start Material Scan and Microscope Review in parallel
root.order.add_edge(initial_PO, material_PO)

# After material_PO nodes done, Damage Mapping
root.order.add_edge(material_PO, Damage_Mapping)

# After Damage Mapping, start environmental + treatment activities (env_ethics_PO)
root.order.add_edge(Damage_Mapping, env_ethics_PO)

# After env_ethics_PO done, start final_PO
root.order.add_edge(env_ethics_PO, final_PO)