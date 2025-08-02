# Generated from: e307a4e0-16b7-4ac0-b3db-6db1b2536966.json
# Description: This process involves the careful restoration and preservation of antique artifacts, ensuring historical accuracy while enhancing structural integrity. It starts with initial assessment and documentation, followed by controlled cleaning and material analysis. Conservation techniques are applied selectively to preserve originality, including stabilization, repair, and protective coating. Throughout the process, ethical considerations and provenance validation are maintained. Final steps include detailed reporting, client review, and archival storage, ensuring the artifact's longevity and historical value for future generations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Initial_Assess = Transition(label='Initial Assess')
Artifact_Scan = Transition(label='Artifact Scan')
Condition_Map = Transition(label='Condition Map')
Material_Test = Transition(label='Material Test')
Cleaning_Phase = Transition(label='Cleaning Phase')
Stability_Check = Transition(label='Stability Check')
Minor_Repair = Transition(label='Minor Repair')
Structural_Reinforce = Transition(label='Structural Reinforce')
Surface_Restore = Transition(label='Surface Restore')
Coating_Apply = Transition(label='Coating Apply')
Ethics_Review = Transition(label='Ethics Review')
Provenance_Verify = Transition(label='Provenance Verify')
Client_Update = Transition(label='Client Update')
Final_Report = Transition(label='Final Report')
Archive_Store = Transition(label='Archive Store')

# Initial assessment and documentation (Initial Assess, Artifact Scan, Condition Map)
initial_PO = StrictPartialOrder(nodes=[Initial_Assess, Artifact_Scan, Condition_Map])
initial_PO.order.add_edge(Initial_Assess, Artifact_Scan)
initial_PO.order.add_edge(Initial_Assess, Condition_Map)
initial_PO.order.add_edge(Artifact_Scan, Condition_Map)

# Controlled cleaning and material analysis (Cleaning Phase and Material Test) run concurrently but after initial_PO
clean_material_PO = StrictPartialOrder(nodes=[Cleaning_Phase, Material_Test])

# Conservation techniques selectively applied - modeled as XOR choice of combos:
# We create choices for the three main conservation techniques:
# 1) Stability Check leading possibly to Minor Repair
# 2) Structural Reinforce
# 3) Surface Restore and Coating Apply
#
# Because these steps should preserve originality selectively, it's reasonable they can be applied in any order or concurrently.
# To model concurrency among these three technique groups, we keep a PO with the three branches unconnected:
#
# However, inside the first group: Stability Check -> Minor Repair (minor repair optional after stability check, so XOR with tau)
# Second and third groups are single activities or sequences.

# Minor Repair is selective after Stability Check, so:
skip = Transition(label='')  # tau, silent transition
# but pm4py uses SilentTransition() for tau:
from pm4py.objects.powl.obj import SilentTransition
skip = SilentTransition()

stab_minor_choice = OperatorPOWL(operator=Operator.XOR, children=[Minor_Repair, skip])
stab_branch = StrictPartialOrder(nodes=[Stability_Check, stab_minor_choice])
stab_branch.order.add_edge(Stability_Check, stab_minor_choice)

# Third group: Surface Restore -> Coating Apply sequentially
surface_coat_PO = StrictPartialOrder(nodes=[Surface_Restore, Coating_Apply])
surface_coat_PO.order.add_edge(Surface_Restore, Coating_Apply)

# Technique groups nodes (Stability branch, Structural Reinforce, Surface/Coating)
technique_PO = StrictPartialOrder(nodes=[stab_branch, Structural_Reinforce, surface_coat_PO])
# no order edges => concurrent among technique groups

# Ethical considerations and provenance validation maintained throughout
# We model Ethics Review and Provenance Verify as concurrent nodes that happen after initial_PO and before final steps
ethics_prov_PO = StrictPartialOrder(nodes=[Ethics_Review, Provenance_Verify])
# concurrent - no order edges between them

# Final steps: Final Report -> Client Update -> Archive Store sequential
final_PO = StrictPartialOrder(nodes=[Final_Report, Client_Update, Archive_Store])
final_PO.order.add_edge(Final_Report, Client_Update)
final_PO.order.add_edge(Client_Update, Archive_Store)

# Build the whole PO combined in order:
#
# initial_PO -> clean_material_PO -> technique_PO -> ethics_prov_PO -> final_PO
#
# We add edges to enforce this order:

root = StrictPartialOrder(
    nodes=[initial_PO, clean_material_PO, technique_PO, ethics_prov_PO, final_PO]
)
root.order.add_edge(initial_PO, clean_material_PO)
root.order.add_edge(clean_material_PO, technique_PO)
root.order.add_edge(technique_PO, ethics_prov_PO)
root.order.add_edge(ethics_prov_PO, final_PO)