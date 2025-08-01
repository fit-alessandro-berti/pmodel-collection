# Generated from: 4d56b709-1a70-44d2-8156-7bb24688b43e.json
# Description: This process outlines the complex and meticulous steps involved in restoring ancient artifacts recovered from underwater archaeological sites. It begins with initial assessment and documentation followed by desalination to remove salt deposits. Specialized cleaning removes encrustations without damaging the artifact's surface. Structural stabilization is applied to fragile components. Chemical treatments prevent further corrosion. Digital 3D scanning captures precise details for virtual reconstruction. Conservation experts then perform material consolidation to strengthen weakened areas. Environmental simulation tests durability under various conditions. Finally, the artifact undergoes aesthetic retouching and protective coating application before being prepared for exhibition or storage. Throughout the process, multidisciplinary collaboration ensures historical accuracy and preservation integrity while minimizing invasive procedures.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
initial_assess      = Transition(label='Initial Assess')
documentation       = Transition(label='Documentation')
salt_removal        = Transition(label='Salt Removal')
surface_clean       = Transition(label='Surface Clean')
fragile_stabilize   = Transition(label='Fragile Stabilize')
corrosion_treat     = Transition(label='Corrosion Treat')
scan                = Transition(label='3D Scanning')
virtual_rebuild     = Transition(label='Virtual Rebuild')
material_strengthen = Transition(label='Material Strengthen')
enviro_simulate     = Transition(label='Enviro Simulate')
aesthetic_retouch   = Transition(label='Aesthetic Retouch')
coating_apply       = Transition(label='Coating Apply')
final_prep          = Transition(label='Final Prep')
expert_review       = Transition(label='Expert Review')
condition_monitor   = Transition(label='Condition Monitor')

# Build the partial order
root = StrictPartialOrder(nodes=[
    initial_assess, documentation,
    salt_removal, surface_clean, fragile_stabilize, corrosion_treat,
    scan, virtual_rebuild, material_strengthen, enviro_simulate,
    aesthetic_retouch, coating_apply, final_prep,
    expert_review, condition_monitor
])

# Initial assessment and documentation must finish before desalination
root.order.add_edge(initial_assess, salt_removal)
root.order.add_edge(documentation, salt_removal)

# Main sequential workflow
root.order.add_edge(salt_removal, surface_clean)
root.order.add_edge(surface_clean, fragile_stabilize)
root.order.add_edge(fragile_stabilize, corrosion_treat)
root.order.add_edge(corrosion_treat, scan)
root.order.add_edge(scan, virtual_rebuild)
root.order.add_edge(virtual_rebuild, material_strengthen)
root.order.add_edge(material_strengthen, enviro_simulate)
root.order.add_edge(enviro_simulate, aesthetic_retouch)
root.order.add_edge(aesthetic_retouch, coating_apply)
root.order.add_edge(coating_apply, final_prep)

# Cross-cutting expert review and condition monitoring
root.order.add_edge(initial_assess, expert_review)
root.order.add_edge(documentation, expert_review)
root.order.add_edge(initial_assess, condition_monitor)
root.order.add_edge(documentation, condition_monitor)
# They must complete before final preparation
root.order.add_edge(expert_review, final_prep)
root.order.add_edge(condition_monitor, final_prep)