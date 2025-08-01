# Generated from: aea6db33-cff4-4b22-8d81-db4ce6f249d7.json
# Description: This process outlines the complex establishment of an urban vertical farm designed to optimize crop yields within limited city spaces. It involves site analysis, modular system design, environmental control calibration, hydroponic nutrient management, automation integration, and continuous monitoring. The workflow incorporates multi-disciplinary coordination between agronomists, engineers, and IT specialists to ensure sustainability, energy efficiency, and scalability. Additionally, it addresses regulatory compliance, waste recycling, and community engagement to create a self-sustaining urban agriculture model that can adapt to varying climatic and urban constraints while maximizing resource use efficiency and crop diversity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey       = Transition(label='Site Survey')
permit_apply      = Transition(label='Permit Apply')
system_design     = Transition(label='System Design')
structural_build  = Transition(label='Structural Build')
lighting_setup    = Transition(label='Lighting Setup')
irrigation_install= Transition(label='Irrigation Install')
nutrient_mix      = Transition(label='Nutrient Mix')
sensor_deploy     = Transition(label='Sensor Deploy')
automation_config = Transition(label='Automation Config')
climate_adjust    = Transition(label='Climate Adjust')
crop_planting     = Transition(label='Crop Planting')
growth_monitor    = Transition(label='Growth Monitor')
data_analyze      = Transition(label='Data Analyze')
pest_control      = Transition(label='Pest Control')
waste_cycle       = Transition(label='Waste Cycle')
community_meet    = Transition(label='Community Meet')

# Parallel setup after structural build
parallel_setup = StrictPartialOrder(nodes=[
    lighting_setup,
    irrigation_install,
    nutrient_mix,
    sensor_deploy,
    automation_config,
    climate_adjust
])
# No edges => fully concurrent

# Body of the monitoring loop (concurrent data analysis, pest control, waste recycling)
monitor_body = StrictPartialOrder(nodes=[
    data_analyze,
    pest_control,
    waste_cycle
])
# No edges => fully concurrent

# Loop: perform growth monitoring, then either exit or do the body and repeat
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitor, monitor_body]
)

# Assemble the overall workflow as a partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    permit_apply,
    system_design,
    structural_build,
    parallel_setup,
    crop_planting,
    monitor_loop,
    community_meet
])

# Define the sequencing order
root.order.add_edge(site_survey,       permit_apply)
root.order.add_edge(permit_apply,      system_design)
root.order.add_edge(system_design,     structural_build)
root.order.add_edge(structural_build,  parallel_setup)
root.order.add_edge(parallel_setup,    crop_planting)
root.order.add_edge(crop_planting,     monitor_loop)
root.order.add_edge(monitor_loop,      community_meet)