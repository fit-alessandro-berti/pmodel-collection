# Generated from: 4d56b709-1a70-44d2-8156-7bb24688b43e.json
# Description: This process outlines the complex and meticulous steps involved in restoring ancient artifacts recovered from underwater archaeological sites. It begins with initial assessment and documentation followed by desalination to remove salt deposits. Specialized cleaning removes encrustations without damaging the artifact's surface. Structural stabilization is applied to fragile components. Chemical treatments prevent further corrosion. Digital 3D scanning captures precise details for virtual reconstruction. Conservation experts then perform material consolidation to strengthen weakened areas. Environmental simulation tests durability under various conditions. Finally, the artifact undergoes aesthetic retouching and protective coating application before being prepared for exhibition or storage. Throughout the process, multidisciplinary collaboration ensures historical accuracy and preservation integrity while minimizing invasive procedures.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
Initial_Assess = Transition(label='Initial Assess')
Documentation = Transition(label='Documentation')
Salt_Removal = Transition(label='Salt Removal')
Surface_Clean = Transition(label='Surface Clean')
Fragile_Stabilize = Transition(label='Fragile Stabilize')
Corrosion_Treat = Transition(label='Corrosion Treat')
Scanning_3D = Transition(label='3D Scanning')
Material_Strengthen = Transition(label='Material Strengthen')
Enviro_Simulate = Transition(label='Enviro Simulate')
Virtual_Rebuild = Transition(label='Virtual Rebuild')
Aesthetic_Retouch = Transition(label='Aesthetic Retouch')
Coating_Apply = Transition(label='Coating Apply')
Expert_Review = Transition(label='Expert Review')
Condition_Monitor = Transition(label='Condition Monitor')
Final_Prep = Transition(label='Final Prep')

# Multidisciplinary collaboration loop cycle: Expert Review -> Condition Monitor -> Expert Review ...
collab_loop = OperatorPOWL(operator=Operator.LOOP, children=[Expert_Review, Condition_Monitor])

# Partial order reflecting the main sequence (some steps can be concurrent)
# The main workflow is:
# Initial Assess and Documentation (concurrent)
# then Salt Removal
# then Surface Clean
# then Fragile Stabilize
# then Corrosion Treat
# then 3D Scanning
# then Material Strengthen
# then Environmental Simulate and Virtual Rebuild (concurrent)
# then Aesthetic Retouch and Coating Apply (concurrent)
# then Final Prep
# Throughout, the collaboration loop can happen (model as sequence after initial tasks)

root = StrictPartialOrder(
    nodes=[
        Initial_Assess,
        Documentation,
        Salt_Removal,
        Surface_Clean,
        Fragile_Stabilize,
        Corrosion_Treat,
        Scanning_3D,
        Material_Strengthen,
        Enviro_Simulate,
        Virtual_Rebuild,
        Aesthetic_Retouch,
        Coating_Apply,
        collab_loop,
        Final_Prep
    ]
)

# Add edges to define the partial order

# Initial assess and documentation concurrent (no order between)
# But both must precede Salt Removal
root.order.add_edge(Initial_Assess, Salt_Removal)
root.order.add_edge(Documentation, Salt_Removal)

root.order.add_edge(Salt_Removal, Surface_Clean)
root.order.add_edge(Surface_Clean, Fragile_Stabilize)
root.order.add_edge(Fragile_Stabilize, Corrosion_Treat)
root.order.add_edge(Corrosion_Treat, Scanning_3D)
root.order.add_edge(Scanning_3D, Material_Strengthen)
root.order.add_edge(Material_Strengthen, Enviro_Simulate)
root.order.add_edge(Material_Strengthen, Virtual_Rebuild)

# Enviro Simulate and Virtual Rebuild are concurrent, both must precede next phase (Aesthetic and Coating)
root.order.add_edge(Enviro_Simulate, Aesthetic_Retouch)
root.order.add_edge(Virtual_Rebuild, Aesthetic_Retouch)
root.order.add_edge(Enviro_Simulate, Coating_Apply)
root.order.add_edge(Virtual_Rebuild, Coating_Apply)

# Aesthetic Retouch and Coating Apply concurrent, both must precede Final Prep
root.order.add_edge(Aesthetic_Retouch, Final_Prep)
root.order.add_edge(Coating_Apply, Final_Prep)

# The collaboration loop happens after initial tasks and before final prep
# Model as Salt Removal precedes collaboration loop, and collaboration loop precedes Material Strengthen to acknowledge its monitoring role
root.order.add_edge(Salt_Removal, collab_loop)
root.order.add_edge(collab_loop, Material_Strengthen)

# This models periodic review and monitoring that influences strengthening and subsequent steps

# The collaboration loop internal order is:
# Expert Review -> Condition Monitor -> choose exit or loop again (handled by OperatorLOOP)

# Return root as per instruction