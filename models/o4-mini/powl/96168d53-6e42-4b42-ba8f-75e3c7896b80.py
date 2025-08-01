# Generated from: 96168d53-6e42-4b42-ba8f-75e3c7896b80.json
# Description: This process outlines the comprehensive steps involved in restoring ancient artifacts that exhibit unpredictable degradation patterns due to environmental exposure and prior restoration attempts. It integrates multidisciplinary analysis including chemical composition assessment, digital reconstruction, and adaptive preservation techniques. The workflow requires iterative testing phases, collaboration between conservators and data scientists, and decision points based on evolving artifact conditions. This atypical approach ensures the artifact's longevity while preserving its historical authenticity and minimizing invasive procedures, making it suitable for highly sensitive and unique cultural heritage objects.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
initial_survey        = Transition(label='Initial Survey')
material_sampling     = Transition(label='Material Sampling')
damage_mapping        = Transition(label='Damage Mapping')
chemical_analysis     = Transition(label='Chemical Analysis')
digital_scanning      = Transition(label='Digital Scanning')
condition_reporting   = Transition(label='Condition Reporting')
restoration_planning  = Transition(label='Restoration Planning')
test_application      = Transition(label='Test Application')
quality_review        = Transition(label='Quality Review')
structural_reinforce  = Transition(label='Structural Reinforce')
surface_cleaning      = Transition(label='Surface Cleaning')
micro_repair          = Transition(label='Micro Repair')
color_matching        = Transition(label='Color Matching')
preservation_coating  = Transition(label='Preservation Coating')
environmental_setup   = Transition(label='Environmental Setup')
final_documentation   = Transition(label='Final Documentation')
long_term_monitor     = Transition(label='Long-term Monitor')

# Iterative testing loop: apply test, then review, repeat until satisfied
test_loop = OperatorPOWL(operator=Operator.LOOP, children=[test_application, quality_review])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    initial_survey,
    material_sampling,
    damage_mapping,
    chemical_analysis,
    digital_scanning,
    condition_reporting,
    restoration_planning,
    test_loop,
    structural_reinforce,
    surface_cleaning,
    micro_repair,
    color_matching,
    preservation_coating,
    environmental_setup,
    final_documentation,
    long_term_monitor
])

# Define ordering dependencies
root.order.add_edge(initial_survey,       material_sampling)
root.order.add_edge(material_sampling,    damage_mapping)
# Parallel analysis tasks
root.order.add_edge(damage_mapping,       chemical_analysis)
root.order.add_edge(damage_mapping,       digital_scanning)
# Join before reporting
root.order.add_edge(chemical_analysis,    condition_reporting)
root.order.add_edge(digital_scanning,     condition_reporting)
root.order.add_edge(condition_reporting,  restoration_planning)
# After planning, enter test loop
root.order.add_edge(restoration_planning, test_loop)
# After tests pass, perform restoration steps
root.order.add_edge(test_loop,            structural_reinforce)
root.order.add_edge(structural_reinforce, surface_cleaning)
root.order.add_edge(surface_cleaning,     micro_repair)
root.order.add_edge(micro_repair,         color_matching)
root.order.add_edge(color_matching,       preservation_coating)
# Final wrapping up
root.order.add_edge(preservation_coating, environmental_setup)
root.order.add_edge(environmental_setup,  final_documentation)
root.order.add_edge(final_documentation,  long_term_monitor)