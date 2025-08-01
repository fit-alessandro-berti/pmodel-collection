# Generated from: a4299542-9b53-499a-b845-638e130cc69e.json
# Description: This process involves the detailed restoration of antique items, combining historical research, material analysis, delicate cleaning, and precise reconstruction to preserve authenticity while enhancing durability. It begins with provenance verification and condition assessment, followed by specialized treatment planning. Each step demands careful documentation and iterative quality checks to ensure that the restored artifact retains its original character. Collaborative input from historians, chemists, and artisans is integrated throughout. The process culminates in final preservation and detailed reporting for archival purposes, enabling museums or collectors to maintain cultural heritage effectively.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Provenance_Check = Transition(label='Provenance Check')
Condition_Scan = Transition(label='Condition Scan')

Material_Test = Transition(label='Material Test')
Damage_Map = Transition(label='Damage Map')

Cleaning_Prep = Transition(label='Cleaning Prep')
Surface_Clean = Transition(label='Surface Clean')

Structural_Fix = Transition(label='Structural Fix')
Paint_Match = Transition(label='Paint Match')
Color_Touch = Transition(label='Color Touch')

Finish_Seal = Transition(label='Finish Seal')
Humidity_Control = Transition(label='Humidity Control')

Documentation = Transition(label='Documentation')
Expert_Review = Transition(label='Expert Review')
Quality_Audit = Transition(label='Quality Audit')

Final_Report = Transition(label='Final Report')

# Step 1: Provenance Check and Condition Scan happen in sequence
step1 = StrictPartialOrder(nodes=[Provenance_Check, Condition_Scan])
step1.order.add_edge(Provenance_Check, Condition_Scan)

# Step 2: Specialized treatment planning consisting of Material Test and Damage Map (concurrent)
step2 = StrictPartialOrder(nodes=[Material_Test, Damage_Map])  # concurrent, no edges

# Step 3: Cleaning steps sequential: Cleaning Prep --> Surface Clean
cleaning = StrictPartialOrder(nodes=[Cleaning_Prep, Surface_Clean])
cleaning.order.add_edge(Cleaning_Prep, Surface_Clean)

# Step 4: Reconstruction steps: Structural Fix --> Paint Match --> Color Touch sequentially
reconstruction = StrictPartialOrder(nodes=[Structural_Fix, Paint_Match, Color_Touch])
reconstruction.order.add_edge(Structural_Fix, Paint_Match)
reconstruction.order.add_edge(Paint_Match, Color_Touch)

# Step 5: Finish Seal and Humidity Control concurrent (both preservation enhancements)
preservation = StrictPartialOrder(nodes=[Finish_Seal, Humidity_Control])  # concurrent, no edges

# Step 6: Documentation, Expert Review, Quality Audit:
# These steps are iterative quality checks, modeled as a loop:
# Loop body: Documentation --> Expert Review --> Quality Audit
quality_checks = StrictPartialOrder(nodes=[Documentation, Expert_Review, Quality_Audit])
quality_checks.order.add_edge(Documentation, Expert_Review)
quality_checks.order.add_edge(Expert_Review, Quality_Audit)

# Loop: execute quality_checks, then decide to exit or repeat
loop_quality = OperatorPOWL(operator=Operator.LOOP, children=[quality_checks, SilentTransition()])

# Finally: Final Report

# Compose the entire process partial order:

# Ordering:
# step1 --> step2 --> cleaning --> reconstruction --> preservation --> loop_quality --> Final_Report

root = StrictPartialOrder(nodes=[
    step1,
    step2,
    cleaning,
    reconstruction,
    preservation,
    loop_quality,
    Final_Report
])

root.order.add_edge(step1, step2)
root.order.add_edge(step2, cleaning)
root.order.add_edge(cleaning, reconstruction)
root.order.add_edge(reconstruction, preservation)
root.order.add_edge(preservation, loop_quality)
root.order.add_edge(loop_quality, Final_Report)