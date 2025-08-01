# Generated from: 84288aef-d199-4f10-b7be-47b149d16b94.json
# Description: This process outlines the intricate steps involved in restoring vintage musical instruments to their former glory while preserving original materials and craftsmanship. The workflow involves detailed assessment of the instrument's condition, sourcing rare and period-accurate components, careful disassembly, cleaning, structural repairs, refinishing using traditional methods, fine tuning of acoustics, and final aesthetic treatments. Each step requires specialized skills to balance authenticity with functional improvement, ensuring that the restored instrument not only looks as it did originally but also performs at professional standards. Documentation and provenance verification are integral, along with customer consultation and post-restoration maintenance planning, making this restoration process both an art and a science.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
initial_survey     = Transition(label="Initial Survey")
condition_report   = Transition(label="Condition Report")
provenance_check   = Transition(label="Provenance Check")
parts_sourcing     = Transition(label="Parts Sourcing")
component_removal  = Transition(label="Component Removal")
surface_cleaning   = Transition(label="Surface Cleaning")
wood_repair        = Transition(label="Wood Repair")
metalwork_fix      = Transition(label="Metalwork Fix")
finish_stripping   = Transition(label="Finish Stripping")
traditional_stain  = Transition(label="Traditional Stain")
structural_rebuild = Transition(label="Structural Rebuild")
acoustic_tuning    = Transition(label="Acoustic Tuning")
hardware_refit     = Transition(label="Hardware Refit")
final_polish       = Transition(label="Final Polish")
quality_review     = Transition(label="Quality Review")
customer_demo      = Transition(label="Customer Demo")
maintenance_plan   = Transition(label="Maintenance Plan")

# Silent transition for optional paths or loop exits
skip = SilentTransition()

# Choice: optionally source parts or skip if no rare components needed
parts_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[parts_sourcing, skip]
)

# Rework cycle: tune, refit, polish in sequence
rework_cycle = StrictPartialOrder(nodes=[acoustic_tuning, hardware_refit, final_polish])
rework_cycle.order.add_edge(acoustic_tuning, hardware_refit)
rework_cycle.order.add_edge(hardware_refit, final_polish)

# Loop: perform quality review, if needed do rework cycle and review again
review_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[quality_review, rework_cycle]
)

# Build the overall partial‐order workflow
root = StrictPartialOrder(nodes=[
    initial_survey,
    condition_report,
    provenance_check,
    parts_choice,
    component_removal,
    surface_cleaning,
    wood_repair,
    metalwork_fix,
    finish_stripping,
    traditional_stain,
    structural_rebuild,
    review_loop,
    customer_demo,
    maintenance_plan
])

# Define the control‐flow dependencies (partial order)
# 1. Initial assessment
root.order.add_edge(initial_survey, condition_report)
root.order.add_edge(initial_survey, provenance_check)

# 2. After reporting and provenance, decide on sourcing parts
root.order.add_edge(condition_report, parts_choice)
root.order.add_edge(provenance_check, parts_choice)

# 3. Disassembly and cleaning
root.order.add_edge(parts_choice, component_removal)
root.order.add_edge(component_removal, surface_cleaning)

# 4. Repairs can proceed in parallel (wood and metal) but both before stripping
root.order.add_edge(surface_cleaning, wood_repair)
root.order.add_edge(surface_cleaning, metalwork_fix)
root.order.add_edge(wood_repair, finish_stripping)
root.order.add_edge(metalwork_fix, finish_stripping)

# 5. Refinishing steps
root.order.add_edge(finish_stripping, traditional_stain)
root.order.add_edge(traditional_stain, structural_rebuild)

# 6. Structural rebuild leads to review loop
root.order.add_edge(structural_rebuild, review_loop)

# 7. After all reviews and any rework, demo and maintenance plan
root.order.add_edge(review_loop, customer_demo)
root.order.add_edge(customer_demo, maintenance_plan)