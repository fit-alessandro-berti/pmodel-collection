# Generated from: 96168d53-6e42-4b42-ba8f-75e3c7896b80.json
# Description: This process outlines the comprehensive steps involved in restoring ancient artifacts that exhibit unpredictable degradation patterns due to environmental exposure and prior restoration attempts. It integrates multidisciplinary analysis including chemical composition assessment, digital reconstruction, and adaptive preservation techniques. The workflow requires iterative testing phases, collaboration between conservators and data scientists, and decision points based on evolving artifact conditions. This atypical approach ensures the artifact's longevity while preserving its historical authenticity and minimizing invasive procedures, making it suitable for highly sensitive and unique cultural heritage objects.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Initial_Survey = Transition(label='Initial Survey')
Material_Sampling = Transition(label='Material Sampling')
Damage_Mapping = Transition(label='Damage Mapping')
Chemical_Analysis = Transition(label='Chemical Analysis')
Digital_Scanning = Transition(label='Digital Scanning')
Condition_Reporting = Transition(label='Condition Reporting')
Restoration_Planning = Transition(label='Restoration Planning')
Test_Application = Transition(label='Test Application')
Structural_Reinforce = Transition(label='Structural Reinforce')
Surface_Cleaning = Transition(label='Surface Cleaning')
Micro_Repair = Transition(label='Micro Repair')
Color_Matching = Transition(label='Color Matching')
Preservation_Coating = Transition(label='Preservation Coating')
Environmental_Setup = Transition(label='Environmental Setup')
Quality_Review = Transition(label='Quality Review')
Final_Documentation = Transition(label='Final Documentation')
Long_term_Monitor = Transition(label='Long-term Monitor')

# Iterative testing loop: * (Restoration Planning, Test Application)
iterative_testing = OperatorPOWL(operator=Operator.LOOP, children=[Restoration_Planning, Test_Application])

# Collaborative parallel work after initial survey:
# Material Sampling and Damage Mapping can be concurrent
# Chemical Analysis and Digital Scanning are after those two, also concurrent
first_parallel = StrictPartialOrder(nodes=[Material_Sampling, Damage_Mapping])

second_parallel = StrictPartialOrder(nodes=[Chemical_Analysis, Digital_Scanning])

# Construction of multi-step partial order for analysis phase
analysis_phase = StrictPartialOrder(nodes=[first_parallel, second_parallel])
analysis_phase.order.add_edge(first_parallel, second_parallel)

# Condition Reporting follows analysis phase
# Restoration Planning follows condition reporting
partial1 = StrictPartialOrder(nodes=[analysis_phase, Condition_Reporting])
partial1.order.add_edge(analysis_phase, Condition_Reporting)

partial2 = StrictPartialOrder(nodes=[Condition_Reporting, iterative_testing])
partial2.order.add_edge(Condition_Reporting, iterative_testing)

# Preservation activities after iterative testing loop
preservation_parallel = StrictPartialOrder(nodes=[
    Structural_Reinforce,
    Surface_Cleaning,
    Micro_Repair,
    Color_Matching,
    Preservation_Coating,
    Environmental_Setup
])

# Quality Review follows preservation activities
quality_review_phase = StrictPartialOrder(nodes=[preservation_parallel, Quality_Review])
quality_review_phase.order.add_edge(preservation_parallel, Quality_Review)

# Final Documentation follows Quality Review
final_phase = StrictPartialOrder(nodes=[quality_review_phase, Final_Documentation])
final_phase.order.add_edge(quality_review_phase, Final_Documentation)

# Long-term monitoring is concurrent with final documentation (to represent ongoing monitoring)
end_phase = StrictPartialOrder(nodes=[final_phase, Long_term_Monitor])

# Build full process partial order:
# Initial Survey -> analysis phase -> condition reporting -> iterative testing loop -> preservation -> quality review -> final doc & monitoring
root = StrictPartialOrder(
    nodes=[
        Initial_Survey,
        partial1,
        partial2,
        preservation_parallel,
        quality_review_phase,
        final_phase,
        Long_term_Monitor
    ]
)

root.order.add_edge(Initial_Survey, partial1)
root.order.add_edge(partial1, partial2)
root.order.add_edge(partial2, preservation_parallel)
root.order.add_edge(preservation_parallel, quality_review_phase)
root.order.add_edge(quality_review_phase, final_phase)
# Long_term_Monitor is part of end phase, concurrent with Final Documentation,
# already included as node and no edges added from final_phase to Long_term_Monitor

# To allow concurrency of long term monitoring and final documentation:
# final_phase includes final doc and quality review, already ordered, so Long_term_Monitor concurrent with Final_Documentation in end_phase
# but we included Long_term_Monitor also in root nodes, so we omit ordering edges connecting it to final_phase nodes

# The structure captures iterative testing, multidisciplinary analysis, concurrent preservation steps, and the monitoring phase.
