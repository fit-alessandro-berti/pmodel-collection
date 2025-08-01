# Generated from: aea6db33-cff4-4b22-8d81-db4ce6f249d7.json
# Description: This process outlines the complex establishment of an urban vertical farm designed to optimize crop yields within limited city spaces. It involves site analysis, modular system design, environmental control calibration, hydroponic nutrient management, automation integration, and continuous monitoring. The workflow incorporates multi-disciplinary coordination between agronomists, engineers, and IT specialists to ensure sustainability, energy efficiency, and scalability. Additionally, it addresses regulatory compliance, waste recycling, and community engagement to create a self-sustaining urban agriculture model that can adapt to varying climatic and urban constraints while maximizing resource use efficiency and crop diversity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
system_design = Transition(label='System Design')
permit_apply = Transition(label='Permit Apply')
structural_build = Transition(label='Structural Build')
lighting_setup = Transition(label='Lighting Setup')
irrigation_install = Transition(label='Irrigation Install')
nutrient_mix = Transition(label='Nutrient Mix')
sensor_deploy = Transition(label='Sensor Deploy')
automation_config = Transition(label='Automation Config')
climate_adjust = Transition(label='Climate Adjust')
crop_planting = Transition(label='Crop Planting')
growth_monitor = Transition(label='Growth Monitor')
pest_control = Transition(label='Pest Control')
waste_cycle = Transition(label='Waste Cycle')
data_analyze = Transition(label='Data Analyze')
community_meet = Transition(label='Community Meet')

# High-level phases modeled as partial orders or sequences (some concurrency)
# Phase 1: Site survey -> System design -> Permit apply
phase1 = StrictPartialOrder(nodes=[site_survey, system_design, permit_apply])
phase1.order.add_edge(site_survey, system_design)
phase1.order.add_edge(system_design, permit_apply)

# Phase 2: Structural build after permit
phase2 = StrictPartialOrder(nodes=[structural_build])
# No inner order - just a single activity, but constrained to start after permit apply

# Phase 3: Installations—lighting, irrigation, nutrient mix, sensor deploy can be partially concurrent after structural build
installations = StrictPartialOrder(nodes=[lighting_setup, irrigation_install, nutrient_mix, sensor_deploy])
# No order edges = fully concurrent installation activities

# Phase 4: Automation config and climate adjustment after installations
automation_and_climate = StrictPartialOrder(nodes=[automation_config, climate_adjust])
# concurrent config and climate after installations

# Phase 5: Crop planting after automation/climate
planting = StrictPartialOrder(nodes=[crop_planting])

# Phase 6: Growth monitoring, pest control, waste cycle in parallel (long-term operations)
long_term_ops = StrictPartialOrder(nodes=[growth_monitor, pest_control, waste_cycle])

# Phase 7: Data analysis and community meeting can be done concurrently after long-term ops
final_phase = StrictPartialOrder(nodes=[data_analyze, community_meet])

# Linking phases with order dependencies:
# phase1 -> phase2 -> installations -> automation/climate -> planting -> long_term_ops -> final_phase
root = StrictPartialOrder(
    nodes=[phase1, phase2, installations, automation_and_climate, planting, long_term_ops, final_phase]
)
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, installations)
root.order.add_edge(installations, automation_and_climate)
root.order.add_edge(automation_and_climate, planting)
root.order.add_edge(planting, long_term_ops)
root.order.add_edge(long_term_ops, final_phase)