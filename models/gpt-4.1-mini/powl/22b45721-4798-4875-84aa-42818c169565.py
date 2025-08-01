# Generated from: 22b45721-4798-4875-84aa-42818c169565.json
# Description: This process outlines the detailed steps involved in restoring antique furniture and artifacts to their original condition while preserving historical value. Beginning with initial assessment and documentation, the workflow includes material analysis, gentle cleaning, structural repairs, paint and finish evaluation, and controlled environmental testing. Specialized techniques such as micro-sanding, resin infill, and patina recreation are applied selectively. The process concludes with quality verification, client consultation, and archival recording to ensure both aesthetic integrity and provenance are maintained. Each step requires precise coordination among conservators, material scientists, and historians to balance restoration with preservation ethics.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Initial_Survey = Transition(label='Initial Survey')
Photo_Capture = Transition(label='Photo Capture')
Material_Test = Transition(label='Material Test')
Dust_Removal = Transition(label='Dust Removal')
Structural_Check = Transition(label='Structural Check')
Joint_Repair = Transition(label='Joint Repair')
Micro_Sand = Transition(label='Micro Sand')
Resin_Fill = Transition(label='Resin Fill')
Finish_Assess = Transition(label='Finish Assess')
Patina_Match = Transition(label='Patina Match')
Surface_Coat = Transition(label='Surface Coat')
UV_Test = Transition(label='UV Test')
Humidity_Set = Transition(label='Humidity Set')
Client_Review = Transition(label='Client Review')
Archival_Log = Transition(label='Archival Log')
Final_Approval = Transition(label='Final Approval')

# Partial orders for sequences

# 1. Initial assessment & documentation
# Initial Survey --> Photo Capture
initial_doc = StrictPartialOrder(nodes=[Initial_Survey, Photo_Capture])
initial_doc.order.add_edge(Initial_Survey, Photo_Capture)

# 2. Material analysis and gentle cleaning
# Material Test --> Dust Removal
mat_and_clean = StrictPartialOrder(nodes=[Material_Test, Dust_Removal])
mat_and_clean.order.add_edge(Material_Test, Dust_Removal)

# 3. Structural repairs
# Structural Check --> Joint Repair
struct_repairs = StrictPartialOrder(nodes=[Structural_Check, Joint_Repair])
struct_repairs.order.add_edge(Structural_Check, Joint_Repair)

# 4. Specialized techniques (micro-sanding, resin infill, patina recreation)
# These three can run concurrently after structural repairs
specialized = StrictPartialOrder(nodes=[Micro_Sand, Resin_Fill, Patina_Match])
# no edges -> concurrent

# 5. Paint and finish evaluation
# Finish Assess --> Surface Coat
finish_eval = StrictPartialOrder(nodes=[Finish_Assess, Surface_Coat])
finish_eval.order.add_edge(Finish_Assess, Surface_Coat)

# 6. Controlled environmental testing
# UV Test and Humidity Set can be concurrent
env_testing = StrictPartialOrder(nodes=[UV_Test, Humidity_Set])
# no edges -> concurrent

# 7. Quality verification, client consultation, archival recording in sequence
# Client Review --> Archival Log --> Final Approval
final_sequence = StrictPartialOrder(nodes=[Client_Review, Archival_Log, Final_Approval])
final_sequence.order.add_edge(Client_Review, Archival_Log)
final_sequence.order.add_edge(Archival_Log, Final_Approval)

# Now, assemble the overall workflow partial order respecting dependencies:

# Initial phase sequence:
# initial_doc --> mat_and_clean --> struct_repairs --> specialized techniques --> finish_eval --> env_testing --> final_sequence

nodes = [initial_doc, mat_and_clean, struct_repairs, specialized, finish_eval, env_testing, final_sequence]

root = StrictPartialOrder(nodes=nodes)
root.order.add_edge(initial_doc, mat_and_clean)
root.order.add_edge(mat_and_clean, struct_repairs)
root.order.add_edge(struct_repairs, specialized)
root.order.add_edge(specialized, finish_eval)
root.order.add_edge(finish_eval, env_testing)
root.order.add_edge(env_testing, final_sequence)