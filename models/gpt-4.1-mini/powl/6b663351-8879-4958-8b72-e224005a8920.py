# Generated from: 6b663351-8879-4958-8b72-e224005a8920.json
# Description: This process involves the meticulous restoration of historical artifacts that have been damaged or deteriorated over time. It begins with an initial assessment to evaluate the artifact's condition and material composition, followed by detailed documentation and imaging. After analysis, a tailored conservation plan is developed, incorporating both traditional craftsmanship and modern scientific techniques. The artifact then undergoes careful cleaning, structural stabilization, and surface treatment to halt further decay. Specialized repairs are performed using compatible materials, and any missing components are recreated with precision. Throughout the restoration, ongoing monitoring ensures environmental conditions remain optimal. Finally, a comprehensive report is generated, and the artifact is prepared for display or storage under controlled conditions, preserving cultural heritage for future generations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Initial_Assess = Transition(label='Initial Assess')
Material_Test = Transition(label='Material Test')
Condition_Map = Transition(label='Condition Map')
Imaging_Scan = Transition(label='Imaging Scan')
Plan_Draft = Transition(label='Plan Draft')

Tool_Setup = Transition(label='Tool Setup')
Surface_Clean = Transition(label='Surface Clean')
Structural_Fix = Transition(label='Structural Fix')

Component_Mold = Transition(label='Component Mold')
Material_Match = Transition(label='Material Match')
Repair_Apply = Transition(label='Repair Apply')

Stabilize_Env = Transition(label='Stabilize Env')
Quality_Check = Transition(label='Quality Check')
Report_Write = Transition(label='Report Write')
Artifact_Pack = Transition(label='Artifact Pack')

# First phase: initial assessment, documentation, imaging in partial order
# "Initial Assess" before "Material Test" and "Condition Map" and "Imaging Scan"
# "Material Test", "Condition Map" and "Imaging Scan" can be concurrent
phase1_nodes = [Material_Test, Condition_Map, Imaging_Scan]
phase1 = StrictPartialOrder(nodes=[Initial_Assess] + phase1_nodes)
phase1.order.add_edge(Initial_Assess, Material_Test)
phase1.order.add_edge(Initial_Assess, Condition_Map)
phase1.order.add_edge(Initial_Assess, Imaging_Scan)

# Second phase: Plan Draft after phase1
phase2 = Plan_Draft

# Third phase: Cleaning, Structural Stabilization, Surface Treatment
# Tool Setup before Surface Clean and Structural Fix; Surface Clean and Structural Fix concurrent after Tool Setup
phase3_nodes = [Surface_Clean, Structural_Fix]
phase3 = StrictPartialOrder(nodes=[Tool_Setup] + phase3_nodes)
phase3.order.add_edge(Tool_Setup, Surface_Clean)
phase3.order.add_edge(Tool_Setup, Structural_Fix)

# Fourth phase: Specialized repairs
# Component Mold and Material Match concurrent
# Repair Apply after both Component Mold and Material Match
phase4 = StrictPartialOrder(nodes=[Component_Mold, Material_Match, Repair_Apply])
phase4.order.add_edge(Component_Mold, Repair_Apply)
phase4.order.add_edge(Material_Match, Repair_Apply)

# Fifth phase: Monitoring and quality check
# Stabilize Env before Quality Check
phase5 = StrictPartialOrder(nodes=[Stabilize_Env, Quality_Check])
phase5.order.add_edge(Stabilize_Env, Quality_Check)

# Sixth phase: Final report and packing
# Report Write before Artifact Pack
phase6 = StrictPartialOrder(nodes=[Report_Write, Artifact_Pack])
phase6.order.add_edge(Report_Write, Artifact_Pack)

# Now combine phases incrementally in order:
# phase1 --> phase2 --> phase3 --> phase4 --> phase5 --> phase6

root = StrictPartialOrder(
    nodes=[phase1, phase2, phase3, phase4, phase5, phase6]
)
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, phase3)
root.order.add_edge(phase3, phase4)
root.order.add_edge(phase4, phase5)
root.order.add_edge(phase5, phase6)