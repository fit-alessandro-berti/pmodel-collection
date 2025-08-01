# Generated from: 8f64dec3-bd14-4b00-b538-919d01552122.json
# Description: This process involves the careful restoration of antique artifacts, combining historical research, material analysis, and precision craftsmanship to preserve original features while ensuring structural integrity. The workflow begins with artifact assessment and documentation, followed by controlled cleaning, selective material consolidation, and surface stabilization. Specialized activities include micro-crack repair, color matching, and period-accurate repainting. Throughout the process, environmental controls are maintained to prevent further degradation. Final steps include quality inspection, provenance updating, and preparing detailed restoration reports for archival purposes. This atypical process ensures antiques retain both their aesthetic and historical values through a multidisciplinary approach.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Artifact_Assess = Transition(label='Artifact Assess')
Historical_Check = Transition(label='Historical Check')
Material_Test = Transition(label='Material Test')
Condition_Map = Transition(label='Condition Map')
Surface_Clean = Transition(label='Surface Clean')
Consolidate_Fragile = Transition(label='Consolidate Fragile')
Structural_Fix = Transition(label='Structural Fix')
Micro_Crack = Transition(label='Micro Crack')
Color_Match = Transition(label='Color Match')
Repaint_Period = Transition(label='Repaint Period')
Environmental_Set = Transition(label='Environmental Set')
Quality_Inspect = Transition(label='Quality Inspect')
Documentation = Transition(label='Documentation')
Provenance_Update = Transition(label='Provenance Update')
Report_Prep = Transition(label='Report Prep')
Archive_Store = Transition(label='Archive Store')

# Environmental_Set maintained throughout after initial phase, so add it in concurrency with subsequent steps.

# Initial assessment phase: Artifact Assess, Historical Check, Material Test, Condition Map in strict order
initial_assessment = StrictPartialOrder(
    nodes=[Artifact_Assess, Historical_Check, Material_Test, Condition_Map]
)
initial_assessment.order.add_edge(Artifact_Assess, Historical_Check)
initial_assessment.order.add_edge(Historical_Check, Material_Test)
initial_assessment.order.add_edge(Material_Test, Condition_Map)

# Cleaning and consolidation in sequence: Surface Clean -> Consolidate Fragile -> Structural Fix
cleaning_consolidation = StrictPartialOrder(
    nodes=[Surface_Clean, Consolidate_Fragile, Structural_Fix]
)
cleaning_consolidation.order.add_edge(Surface_Clean, Consolidate_Fragile)
cleaning_consolidation.order.add_edge(Consolidate_Fragile, Structural_Fix)

# Specialized crafts in partial order (concurrent where possible)
# Micro Crack repair, Color Match and Repaint Period may be partially concurrent but Repaint likely after Color Match
specialized_crafts = StrictPartialOrder(
    nodes=[Micro_Crack, Color_Match, Repaint_Period]
)
specialized_crafts.order.add_edge(Color_Match, Repaint_Period)
# Micro Crack independent, concurrent with Color Match/Repaint

# Environmental Set must be set before specialized crafts and maintained throughout, modeled as first step in concurrency.
# So Environmental_Set precedes specialized crafts.

env_and_crafts = StrictPartialOrder(
    nodes=[Environmental_Set, specialized_crafts]
)
env_and_crafts.order.add_edge(Environmental_Set, specialized_crafts)

# Final steps strictly ordered: Quality Inspect -> Provenance Update -> Documentation -> Report Prep -> Archive Store
final_steps = StrictPartialOrder(
    nodes=[Quality_Inspect, Provenance_Update, Documentation, Report_Prep, Archive_Store]
)
final_steps.order.add_edge(Quality_Inspect, Provenance_Update)
final_steps.order.add_edge(Provenance_Update, Documentation)
final_steps.order.add_edge(Documentation, Report_Prep)
final_steps.order.add_edge(Report_Prep, Archive_Store)

# Combine all major phases in sequence:
# initial_assessment -> cleaning_consolidation -> env_and_crafts -> final_steps

root = StrictPartialOrder(
    nodes=[initial_assessment, cleaning_consolidation, env_and_crafts, final_steps]
)
root.order.add_edge(initial_assessment, cleaning_consolidation)
root.order.add_edge(cleaning_consolidation, env_and_crafts)
root.order.add_edge(env_and_crafts, final_steps)