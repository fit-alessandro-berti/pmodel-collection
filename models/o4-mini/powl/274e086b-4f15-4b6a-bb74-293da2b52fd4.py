# Generated from: 274e086b-4f15-4b6a-bb74-293da2b52fd4.json
# Description: This process involves the planning, installation, and operationalization of a vertical farming system within an urban environment. It includes site analysis, modular structure assembly, automated irrigation configuration, crop selection tailored for vertical growth, integration of IoT sensors for monitoring microclimate conditions, nutrient solution preparation, and the deployment of AI-driven growth optimization software. The process also covers staff training on maintenance protocols, pest management using biocontrol agents, and establishing distribution channels for fresh produce. Continuous data collection and system calibration ensure sustainable yield and energy efficiency, adapting to urban constraints and regulatory compliance.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey      = Transition(label='Site Survey')
design_layout    = Transition(label='Design Layout')
structure_build  = Transition(label='Structure Build')
irrigation_setup = Transition(label='Irrigation Setup')
crop_select      = Transition(label='Crop Select')
sensor_install   = Transition(label='Sensor Install')
nutrient_mix     = Transition(label='Nutrient Mix')
ai_deploy        = Transition(label='AI Deploy')
staff_train      = Transition(label='Staff Train')
pest_control     = Transition(label='Pest Control')
market_launch    = Transition(label='Market Launch')

data_monitor     = Transition(label='Data Monitor')
yield_analyze    = Transition(label='Yield Analyze')
energy_audit     = Transition(label='Energy Audit')
compliance_check = Transition(label='Compliance Check')
feedback_loop    = Transition(label='Feedback Loop')

# Build the monitoring-and-calibration loop body
monitor_body = StrictPartialOrder(nodes=[
    data_monitor,
    yield_analyze,
    energy_audit,
    compliance_check
])
monitor_body.order.add_edge(data_monitor, yield_analyze)
monitor_body.order.add_edge(yield_analyze, energy_audit)
monitor_body.order.add_edge(energy_audit, compliance_check)

# Define the LOOP: do monitor_body, then optionally do feedback_loop & repeat
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor_body, feedback_loop]
)

# Assemble the main process as a strict partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    structure_build,
    irrigation_setup,
    crop_select,
    sensor_install,
    nutrient_mix,
    ai_deploy,
    staff_train,
    pest_control,
    market_launch,
    loop
])

# Sequence the setup and deployment activities
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, structure_build)
root.order.add_edge(structure_build, irrigation_setup)
root.order.add_edge(irrigation_setup, crop_select)
root.order.add_edge(crop_select, sensor_install)
root.order.add_edge(sensor_install, nutrient_mix)
root.order.add_edge(nutrient_mix, ai_deploy)
root.order.add_edge(ai_deploy, staff_train)
root.order.add_edge(staff_train, pest_control)

# After pest control, branch into market launch and continuous monitoring loop
root.order.add_edge(pest_control, market_launch)
root.order.add_edge(pest_control, loop)