# Generated from: c49e6501-52c0-4fb0-b040-3b221c891a0a.json
# Description: This process involves the end-to-end assembly, testing, customization, and deployment of specialized drones for niche industrial applications. Starting from raw component inspection, parts are selected based on client specifications, then assembled with precision. Following mechanical assembly, firmware is loaded and calibrated through iterative testing cycles. Environmental stress tests simulate real-world conditions to ensure durability and performance. Parallel to hardware preparation, software modules are customized to client needs, including navigation algorithms and communication protocols. Once the drone passes all validations, a secure data link is established, and the drone is deployed on-site. Post-deployment includes live monitoring, adaptive firmware updates, and eventual recovery or maintenance scheduling to ensure sustained operational efficacy in challenging environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities as transitions
component_check = Transition(label='Component Check')
spec_review = Transition(label='Spec Review')
parts_sorting = Transition(label='Parts Sorting')
mechanical_fit = Transition(label='Mechanical Fit')

firmware_load = Transition(label='Firmware Load')
calibration_run = Transition(label='Calibration Run')
stress_test = Transition(label='Stress Test')

software_patch = Transition(label='Software Patch')
algorithm_tune = Transition(label='Algorithm Tune')
comms_setup = Transition(label='Comms Setup')

validation_pass = Transition(label='Validation Pass')
data_link = Transition(label='Data Link')
onsite_deploy = Transition(label='Onsite Deploy')

live_monitor = Transition(label='Live Monitor')
update_push = Transition(label='Update Push')
recovery_plan = Transition(label='Recovery Plan')
maintenance_log = Transition(label='Maintenance Log')

# Loop for iterative testing cycles: calibration_run followed by stress_test repeatedly until exit
# The LOOP semantics are: execute first child, then choice to exit or second child + first child again
iterative_testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[calibration_run, stress_test])

# Firmware loading and testing cycle: firmware_load -> iterative_testing_loop
fw_and_testing = StrictPartialOrder(nodes=[firmware_load, iterative_testing_loop])
fw_and_testing.order.add_edge(firmware_load, iterative_testing_loop)

# Hardware preparation sequence: component_check -> spec_review -> parts_sorting -> mechanical_fit -> fw_and_testing
hardware_prep = StrictPartialOrder(nodes=[component_check, spec_review, parts_sorting, mechanical_fit, fw_and_testing])

hardware_prep.order.add_edge(component_check, spec_review)
hardware_prep.order.add_edge(spec_review, parts_sorting)
hardware_prep.order.add_edge(parts_sorting, mechanical_fit)
hardware_prep.order.add_edge(mechanical_fit, fw_and_testing)

# Software customization parallel tasks: software_patch, algorithm_tune, comms_setup concurrent (partial order with no edges)
software_customization = StrictPartialOrder(nodes=[software_patch, algorithm_tune, comms_setup])

# Validation sequence: validation_pass -> data_link -> onsite_deploy
validation_and_deploy = StrictPartialOrder(nodes=[validation_pass, data_link, onsite_deploy])
validation_and_deploy.order.add_edge(validation_pass, data_link)
validation_and_deploy.order.add_edge(data_link, onsite_deploy)

# Post-deployment parallel tasks (concurrent):
# live_monitor runs in parallel with a sequence of update_push -> (choice of recovery_plan or maintenance_log)

# Choice between recovery_plan and maintenance_log
recovery_or_maintenance = OperatorPOWL(operator=Operator.XOR, children=[recovery_plan, maintenance_log])

# Sequence: update_push -> recovery_or_maintenance
update_and_recovery = StrictPartialOrder(nodes=[update_push, recovery_or_maintenance])
update_and_recovery.order.add_edge(update_push, recovery_or_maintenance)

# Post-deployment concurrency: live_monitor || (update_push->(recovery_plan XOR maintenance_log))
post_deployment = StrictPartialOrder(nodes=[live_monitor, update_and_recovery])
# No order edges: concurrent execution

# Combine hardware_prep and software_customization in parallel (concurrent)
prep_parallel = StrictPartialOrder(nodes=[hardware_prep, software_customization])
# No edges - they can run concurrently

# After preparation and customization, proceed to validation_and_deploy
prep_to_validation = StrictPartialOrder(nodes=[prep_parallel, validation_and_deploy])
prep_to_validation.order.add_edge(prep_parallel, validation_and_deploy)

# Final root: sequence of prep_to_validation followed by post_deployment
root = StrictPartialOrder(nodes=[prep_to_validation, post_deployment])
root.order.add_edge(prep_to_validation, post_deployment)