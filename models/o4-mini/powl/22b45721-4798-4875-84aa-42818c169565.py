# Generated from: 22b45721-4798-4875-84aa-42818c169565.json
# Description: This process outlines the detailed steps involved in restoring antique furniture and artifacts to their original condition while preserving historical value. Beginning with initial assessment and documentation, the workflow includes material analysis, gentle cleaning, structural repairs, paint and finish evaluation, and controlled environmental testing. Specialized techniques such as micro-sanding, resin infill, and patina recreation are applied selectively. The process concludes with quality verification, client consultation, and archival recording to ensure both aesthetic integrity and provenance are maintained. Each step requires precise coordination among conservators, material scientists, and historians to balance restoration with preservation ethics.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
initial_survey  = Transition(label="Initial Survey")
photo_capture   = Transition(label="Photo Capture")
material_test   = Transition(label="Material Test")
dust_removal    = Transition(label="Dust Removal")
structural_check= Transition(label="Structural Check")
joint_repair    = Transition(label="Joint Repair")
finish_assess   = Transition(label="Finish Assess")
surface_coat    = Transition(label="Surface Coat")
uv_test         = Transition(label="UV Test")
humidity_set    = Transition(label="Humidity Set")
client_review   = Transition(label="Client Review")
archival_log    = Transition(label="Archival Log")
final_approval  = Transition(label="Final Approval")

# Silent transition for the loop
skip = SilentTransition()

# Specialized techniques choice: micro‐sanding, resin infill, patina match
micro_sand   = Transition(label="Micro Sand")
resin_fill   = Transition(label="Resin Fill")
patina_match = Transition(label="Patina Match")
specialized_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[micro_sand, resin_fill, patina_match]
)

# Loop: zero or more specialized techniques
# children = [body, redo]; semantics: body, then exit or redo + body again
# Here body = skip (allows zero), redo = specialized_choice
special_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[skip, specialized_choice]
)

# Build the main partial order
root = StrictPartialOrder(nodes=[
    initial_survey,
    photo_capture,
    material_test,
    dust_removal,
    structural_check,
    joint_repair,
    special_loop,
    finish_assess,
    surface_coat,
    uv_test,
    humidity_set,
    client_review,
    archival_log,
    final_approval
])

# Define the control‐flow / causal edges
root.order.add_edge(initial_survey,  photo_capture)
root.order.add_edge(photo_capture,   material_test)
root.order.add_edge(material_test,   dust_removal)
root.order.add_edge(dust_removal,    structural_check)
root.order.add_edge(structural_check,joint_repair)
root.order.add_edge(joint_repair,    special_loop)
root.order.add_edge(special_loop,    finish_assess)
root.order.add_edge(finish_assess,   surface_coat)
# Surface coat must precede both tests (they are concurrent)
root.order.add_edge(surface_coat,    uv_test)
root.order.add_edge(surface_coat,    humidity_set)
# Both tests must finish before client review
root.order.add_edge(uv_test,         client_review)
root.order.add_edge(humidity_set,    client_review)
root.order.add_edge(client_review,   archival_log)
root.order.add_edge(archival_log,    final_approval)