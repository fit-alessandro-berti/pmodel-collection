# Generated from: 84d46e56-77fd-4064-b0eb-60335faa0c28.json
# Description: This process outlines the complex setup of an urban vertical farming system within a repurposed commercial building. It includes site analysis, structural reinforcement, environmental controls installation, automated irrigation programming, and crop selection optimization. Integration of renewable energy sources and real-time monitoring systems ensures sustainable, high-yield crop production. Post-installation training and community engagement complete the process, supporting urban agriculture innovation and local food security.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey        = Transition(label='Site Survey')
structural_check   = Transition(label='Structural Check')
permitting         = Transition(label='Permitting')
climate_setup      = Transition(label='Climate Setup')
lighting_install   = Transition(label='Lighting Install')
irrigation_config  = Transition(label='Irrigation Config')
automation_program = Transition(label='Automation Program')
energy_audit       = Transition(label='Energy Audit')
renewables_setup   = Transition(label='Renewables Setup')
sensor_deploy      = Transition(label='Sensor Deploy')
data_cal_monitor   = Transition(label='Data Calibration')
crop_selection     = Transition(label='Crop Selection')
trial_growth       = Transition(label='Trial Growth')
data_cal_loop      = Transition(label='Data Calibration')  # separate node for the loop
staff_training     = Transition(label='Staff Training')
community_outreach = Transition(label='Community Outreach')

# Phase 1: Site survey → Structural check → Permitting
phase1 = StrictPartialOrder(nodes=[site_survey, structural_check, permitting])
phase1.order.add_edge(site_survey, structural_check)
phase1.order.add_edge(structural_check, permitting)

# Parallel branch A: Environmental controls setup
phase_env = StrictPartialOrder(
    nodes=[climate_setup, lighting_install, irrigation_config, automation_program]
)
phase_env.order.add_edge(climate_setup, lighting_install)
phase_env.order.add_edge(lighting_install, irrigation_config)
phase_env.order.add_edge(irrigation_config, automation_program)

# Parallel branch B: Renewable energy integration
phase_energy = StrictPartialOrder(nodes=[energy_audit, renewables_setup])
phase_energy.order.add_edge(energy_audit, renewables_setup)

# Parallel branch C: Monitoring deployment
phase_monitor = StrictPartialOrder(nodes=[sensor_deploy, data_cal_monitor])
phase_monitor.order.add_edge(sensor_deploy, data_cal_monitor)

# Combine the three branches in parallel
parallel_branches = StrictPartialOrder(
    nodes=[phase_env, phase_energy, phase_monitor]
)

# Crop trial loop: Trial Growth with repeated calibration
# LOOP children: [A, B] means run A, then either exit or run B → A again
loop_trial = OperatorPOWL(
    operator=Operator.LOOP,
    children=[trial_growth, data_cal_loop]
)

# Build the overall workflow as a strict partial order
root = StrictPartialOrder(
    nodes=[
        phase1,
        parallel_branches,
        crop_selection,
        loop_trial,
        staff_training,
        community_outreach
    ]
)
root.order.add_edge(phase1, parallel_branches)
root.order.add_edge(parallel_branches, crop_selection)
root.order.add_edge(crop_selection, loop_trial)
root.order.add_edge(loop_trial, staff_training)
root.order.add_edge(staff_training, community_outreach)