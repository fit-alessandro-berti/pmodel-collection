# Generated from: 5575ecda-8f3b-4802-b3fc-595c6d24ea31.json
# Description: This process outlines the establishment of a fully operational urban vertical farm within a city environment. It involves site assessment, modular structure assembly, climate system integration, automated nutrient delivery setup, crop selection based on local demand, AI-driven growth monitoring, pest management using bio-controls, waste recycling, energy optimization, workforce training, compliance verification, marketing launch, and continuous process improvement to ensure sustainable high-yield production while minimizing environmental impact in an atypical urban agricultural setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_assess        = Transition(label='Site Assess')
design_layout      = Transition(label='Design Layout')
module_build       = Transition(label='Module Build')
install_climate    = Transition(label='Install Climate')
setup_nutrients    = Transition(label='Setup Nutrients')
select_crops       = Transition(label='Select Crops')
deploy_sensors     = Transition(label='Deploy Sensors')
calibrate_ai       = Transition(label='Calibrate AI')
bio_pestcontrol    = Transition(label='Bio Pestcontrol')
recycle_waste      = Transition(label='Recycle Waste')
optimize_energy    = Transition(label='Optimize Energy')
train_staff        = Transition(label='Train Staff')
verify_compliance  = Transition(label='Verify Compliance')
launch_marketing   = Transition(label='Launch Marketing')
process_review     = Transition(label='Process Review')

# Build the main linear sequence (A) up to "Launch Marketing"
seq_nodes = [
    site_assess, design_layout, module_build, install_climate,
    setup_nutrients, select_crops, deploy_sensors, calibrate_ai,
    bio_pestcontrol, recycle_waste, optimize_energy, train_staff,
    verify_compliance, launch_marketing
]
A = StrictPartialOrder(nodes=seq_nodes)
for i in range(len(seq_nodes) - 1):
    A.order.add_edge(seq_nodes[i], seq_nodes[i+1])

# Wrap the core sequence in a loop for continuous process improvement
# * (A, Process Review) – do A, then either exit or do Process Review and repeat
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[A, process_review]
)