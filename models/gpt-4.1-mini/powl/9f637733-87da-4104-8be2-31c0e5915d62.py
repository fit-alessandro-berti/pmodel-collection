# Generated from: 9f637733-87da-4104-8be2-31c0e5915d62.json
# Description: This process outlines the intricate steps involved in restoring vintage musical instruments to playable and collectible condition. It begins with initial assessment, followed by detailed documentation of damage and provenance verification. Specialized cleaning techniques are applied to remove years of grime without harming original finishes. Structural repairs require precise woodworking or metalwork to preserve authenticity. Acoustic tuning is performed to balance sound quality. Custom replacement parts are fabricated when originals are unavailable, ensuring historical accuracy. Final polishing enhances aesthetic appeal, while quality control verifies functionality. The process concludes with archival recording of restoration details and client handover, maintaining a comprehensive history for collectors and musicians alike.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
Initial_Assess = Transition(label='Initial Assess')
Provenance_Check = Transition(label='Provenance Check')
Damage_Document = Transition(label='Damage Document')
Surface_Clean = Transition(label='Surface Clean')
Finish_Protect = Transition(label='Finish Protect')
Structural_Repair = Transition(label='Structural Repair')
Woodwork_Fix = Transition(label='Woodwork Fix')
Metalwork_Fix = Transition(label='Metalwork Fix')
Part_Fabricate = Transition(label='Part Fabricate')
Acoustic_Tune = Transition(label='Acoustic Tune')
Sound_Test = Transition(label='Sound Test')
Polish_Finish = Transition(label='Polish Finish')
Quality_Inspect = Transition(label='Quality Inspect')
Archive_Record = Transition(label='Archive Record')
Client_Handover = Transition(label='Client Handover')

# Model the repair sub-steps (Woodwork Fix and Metalwork Fix) as choice inside Structural Repair
# Structural Repair consists of Woodwork Fix or Metalwork Fix executed exclusively
repair_choice = OperatorPOWL(operator=Operator.XOR, children=[Woodwork_Fix, Metalwork_Fix])

# Structural Repair is a partial order of Structural_Repair activity that includes the choice inside 
# However, from description, Structural Repair "requires precise woodworking or metalwork"
# We interpret "Structural Repair" as encompassing the choice between these two fixes.
# To keep clarity, let's consider Structural_Repair as label, and children the choice (repair).
# We can model Structural_Repair as a PO with two nodes: Structural_Repair and the choice between woodworking and metalwork.
structural_repair_po = StrictPartialOrder(nodes=[Structural_Repair, repair_choice])
structural_repair_po.order.add_edge(Structural_Repair, repair_choice)

# The top-level partial order of the process:
# Stepwise order:
# Initial Assess --> Damage Document & Provenance Check (both after Initial Assess and concurrent)
# Then Surface Clean
# Then Finish Protect
# Then Structural Repair (with sub choice)
# Then Part Fabricate
# Then Acoustic Tune --> Sound Test
# Then Polish Finish
# Then Quality Inspect
# Then Archive Record
# Then Client Handover

# Note that Damage Document and Provenance Check can run in parallel after Initial Assess

po_nodes = [
    Initial_Assess,
    Damage_Document,
    Provenance_Check,
    Surface_Clean,
    Finish_Protect,
    structural_repair_po,
    Part_Fabricate,
    Acoustic_Tune,
    Sound_Test,
    Polish_Finish,
    Quality_Inspect,
    Archive_Record,
    Client_Handover,
]

root = StrictPartialOrder(nodes=po_nodes)

# Edges reflecting described dependencies

# Initial Assess precedes Damage Document and Provenance Check
root.order.add_edge(Initial_Assess, Damage_Document)
root.order.add_edge(Initial_Assess, Provenance_Check)

# Damage Document and Provenance Check complete before Surface Clean (both needed before cleaning)
root.order.add_edge(Damage_Document, Surface_Clean)
root.order.add_edge(Provenance_Check, Surface_Clean)

# Surface Clean before Finish Protect
root.order.add_edge(Surface_Clean, Finish_Protect)

# Finish Protect before Structural Repair
root.order.add_edge(Finish_Protect, structural_repair_po)

# Structural Repair before Part Fabricate
root.order.add_edge(structural_repair_po, Part_Fabricate)

# Part Fabricate before Acoustic Tune
root.order.add_edge(Part_Fabricate, Acoustic_Tune)

# Acoustic Tune before Sound Test
root.order.add_edge(Acoustic_Tune, Sound_Test)

# Sound Test before Polish Finish
root.order.add_edge(Sound_Test, Polish_Finish)

# Polish Finish before Quality Inspect
root.order.add_edge(Polish_Finish, Quality_Inspect)

# Quality Inspect before Archive Record
root.order.add_edge(Quality_Inspect, Archive_Record)

# Archive Record before Client Handover
root.order.add_edge(Archive_Record, Client_Handover)