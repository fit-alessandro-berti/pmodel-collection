# Generated from: 442aa379-9694-48f2-b2a0-b8a82f52ba02.json
# Description: This process outlines the complex orchestration required to establish a bespoke urban farming system tailored to specific environmental constraints and client preferences. It begins with site analysis and soil testing, followed by modular design iterations and resource allocation. The process integrates IoT sensor calibration, automated irrigation programming, and nutrient cycle optimization. Throughout, regulatory compliance and sustainability assessments are conducted to ensure ecological impact is minimized. Finally, staff training and digital monitoring setup finalize the system, enabling scalable urban agriculture with precise environmental controls and remote management capabilities.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey        = Transition(label="Site Survey")
soil_testing       = Transition(label="Soil Testing")
design_draft       = Transition(label="Design Draft")
resource_plan      = Transition(label="Resource Plan")
permits_check      = Transition(label="Permits Check")
module_build       = Transition(label="Module Build")
sensor_setup       = Transition(label="Sensor Setup")
irrigation_config  = Transition(label="Irrigation Config")
nutrient_mix       = Transition(label="Nutrient Mix")
compliance_audit   = Transition(label="Compliance Audit")
sustainability_eval= Transition(label="Sustainability Eval")
staff_training     = Transition(label="Staff Training")
system_install     = Transition(label="System Install")
data_sync          = Transition(label="Data Sync")
remote_enable      = Transition(label="Remote Enable")
performance_review = Transition(label="Performance Review")

# Loop for modular design iterations: start with Design Draft, then optionally Resource Plan before another Draft
design_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[design_draft, resource_plan]
)

# Construct the root partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    soil_testing,
    design_loop,
    permits_check,
    module_build,
    sensor_setup,
    irrigation_config,
    nutrient_mix,
    compliance_audit,
    sustainability_eval,
    staff_training,
    system_install,
    data_sync,
    remote_enable,
    performance_review
])

# 1) Site survey -> Soil testing -> Design loop -> Permits check -> Module build
root.order.add_edge(site_survey, soil_testing)
root.order.add_edge(soil_testing, design_loop)
root.order.add_edge(design_loop, permits_check)
root.order.add_edge(permits_check, module_build)

# 2) After module build, run sensor setup, irrigation config, nutrient mix,
#    compliance audit and sustainability eval in parallel (no edges between them)
for nxt in [sensor_setup, irrigation_config, nutrient_mix, compliance_audit, sustainability_eval]:
    root.order.add_edge(module_build, nxt)

# 3) Once those five are done, start staff training and system install (they can run in parallel)
for prev in [sensor_setup, irrigation_config, nutrient_mix, compliance_audit, sustainability_eval]:
    root.order.add_edge(prev, staff_training)
    root.order.add_edge(prev, system_install)

# 4) Digital monitoring setup sequence: System Install -> Data Sync -> Remote Enable
root.order.add_edge(system_install, data_sync)
root.order.add_edge(data_sync, remote_enable)

# 5) Final performance review after both Staff Training and Remote Enable
root.order.add_edge(staff_training, performance_review)
root.order.add_edge(remote_enable, performance_review)