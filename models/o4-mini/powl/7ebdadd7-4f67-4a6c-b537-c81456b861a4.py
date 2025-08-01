# Generated from: 7ebdadd7-4f67-4a6c-b537-c81456b861a4.json
# Description: This process outlines the complex series of steps required to establish a fully operational urban vertical farm within a constrained city environment. It involves site selection based on environmental and zoning factors, modular infrastructure design, integration of hydroponic and aeroponic systems, automation setup for climate control and nutrient delivery, and implementation of sustainable energy sources. The process further includes staff training on specialized equipment, regulatory compliance checks, iterative crop trial cycles to optimize yield, and a digital supply chain integration to connect with local markets efficiently. Continuous monitoring and adaptive management ensure peak productivity and resource conservation in an atypical urban agricultural context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey      = Transition(label='Site Survey')
zoning_review    = Transition(label='Zoning Review')
modular_design   = Transition(label='Modular Design')
system_integration = Transition(label='System Integration')
climate_setup    = Transition(label='Climate Setup')
nutrient_mix     = Transition(label='Nutrient Mix')
automation_install = Transition(label='Automation Install')
energy_connect   = Transition(label='Energy Connect')
staff_training   = Transition(label='Staff Training')
compliance_check = Transition(label='Compliance Check')
trial_crops      = Transition(label='Trial Crops')
yield_analysis   = Transition(label='Yield Analysis')
supply_sync      = Transition(label='Supply Sync')
monitoring_setup = Transition(label='Monitoring Setup')
adaptive_control = Transition(label='Adaptive Control')

# Loop for iterative crop trial cycles: Trial Crops -> Yield Analysis, repeated until exit
loop_trials = OperatorPOWL(
    operator=Operator.LOOP,
    children=[trial_crops, yield_analysis]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    zoning_review,
    modular_design,
    system_integration,
    climate_setup,
    nutrient_mix,
    automation_install,
    energy_connect,
    staff_training,
    compliance_check,
    loop_trials,
    supply_sync,
    monitoring_setup,
    adaptive_control
])

# Add sequencing edges
# Site selection phase (concurrent but both precede modular design)
root.order.add_edge(site_survey, modular_design)
root.order.add_edge(zoning_review, modular_design)

# Design and integration
root.order.add_edge(modular_design, system_integration)

# Automation setup: climate & nutrient in parallel, both before installation
root.order.add_edge(system_integration, climate_setup)
root.order.add_edge(system_integration, nutrient_mix)
root.order.add_edge(climate_setup, automation_install)
root.order.add_edge(nutrient_mix, automation_install)

# Energy connection then staff/regulatory preparation
root.order.add_edge(automation_install, energy_connect)
root.order.add_edge(energy_connect, staff_training)
root.order.add_edge(energy_connect, compliance_check)

# After training & compliance, start the trial‐yield loop
root.order.add_edge(staff_training, loop_trials)
root.order.add_edge(compliance_check, loop_trials)

# Once loop exits, move to supply sync, then monitoring & adaptive control in parallel
root.order.add_edge(loop_trials, supply_sync)
root.order.add_edge(supply_sync, monitoring_setup)
root.order.add_edge(supply_sync, adaptive_control)