# Generated from: b7f71da5-b9b3-4442-8a2b-009656285059.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farm within a repurposed industrial building. It involves site assessment, environmental analysis, infrastructure retrofitting, hydroponic system installation, crop selection, nutrient calibration, lighting optimization, climate control setup, labor training, and compliance verification. The process ensures sustainable food production in dense urban areas, integrating technology and agriculture to maximize yield while minimizing resource consumption and environmental impact. Continuous monitoring and adaptation phases guarantee long-term operational efficiency and product quality.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
risk_audit       = Transition(label='Risk Audit')
design_layout    = Transition(label='Design Layout')
system_retrofit  = Transition(label='System Retrofit')
install_hydroponics = Transition(label='Install Hydroponics')
select_crops     = Transition(label='Select Crops')
calibrate_nutrients = Transition(label='Calibrate Nutrients')
setup_lighting   = Transition(label='Setup Lighting')
control_climate  = Transition(label='Control Climate')
train_staff      = Transition(label='Train Staff')
compliance_check = Transition(label='Compliance Check')
launch_pilot     = Transition(label='Launch Pilot')
monitor_growth   = Transition(label='Monitor Growth')
adjust_parameters= Transition(label='Adjust Parameters')
quality_test     = Transition(label='Quality Test')
harvest_cycle    = Transition(label='Harvest Cycle')

# Build the loop body: adjust_parameters -> quality_test
loop_body = StrictPartialOrder(nodes=[adjust_parameters, quality_test])
loop_body.order.add_edge(adjust_parameters, quality_test)

# Define the monitoring & adaptation loop: always do monitor_growth, then either exit or do (adjust->test) then monitor again
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_growth, loop_body])

# Assemble the overall workflow as a partial order
root = StrictPartialOrder(nodes=[
    site_survey, risk_audit, design_layout, system_retrofit,
    install_hydroponics, select_crops, calibrate_nutrients,
    setup_lighting, control_climate, train_staff,
    compliance_check, launch_pilot, monitor_loop, harvest_cycle
])

# Define the strict sequence of activities
seq = [
    site_survey, risk_audit, design_layout, system_retrofit,
    install_hydroponics, select_crops, calibrate_nutrients,
    setup_lighting, control_climate, train_staff,
    compliance_check, launch_pilot, monitor_loop, harvest_cycle
]
for src, tgt in zip(seq, seq[1:]):
    root.order.add_edge(src, tgt)