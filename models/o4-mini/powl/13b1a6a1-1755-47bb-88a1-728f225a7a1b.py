# Generated from: 13b1a6a1-1755-47bb-88a1-728f225a7a1b.json
# Description: This process outlines the intricate steps involved in the assembly and configuration of customized drones tailored for specialized industrial applications. It begins with component sourcing based on client specifications, followed by precision frame construction and modular subsystem integration. Each drone undergoes advanced firmware installation, sensor calibration, and environmental resilience testing. The process also involves iterative flight simulations and real-world trial deployments to ensure compliance with safety and performance standards. Post-deployment, the system captures operational data for continuous improvement and client feedback integration, culminating in bespoke maintenance scheduling and upgrade path planning to extend drone lifecycle and optimize mission effectiveness.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define basic activities
component_sourcing    = Transition(label='Component Sourcing')
frame_build           = Transition(label='Frame Build')
subsystem_fit         = Transition(label='Subsystem Fit')
firmware_load         = Transition(label='Firmware Load')
sensor_calibrate      = Transition(label='Sensor Calibrate')
env_test              = Transition(label='Env Test')
flight_simulate       = Transition(label='Flight Simulate')
trial_deploy          = Transition(label='Trial Deploy')
compliance_check      = Transition(label='Compliance Check')
data_capture          = Transition(label='Data Capture')
client_review         = Transition(label='Client Review')
feedback_integrate    = Transition(label='Feedback Integrate')
maintenance_plan      = Transition(label='Maintenance Plan')
upgrade_design        = Transition(label='Upgrade Design')
final_approval        = Transition(label='Final Approval')

# Build the iterative flight‐trial‐compliance cycle
cycle = StrictPartialOrder(
    nodes=[flight_simulate, trial_deploy, compliance_check]
)
cycle.order.add_edge(flight_simulate, trial_deploy)
cycle.order.add_edge(trial_deploy, compliance_check)

# Wrap the cycle into a loop: execute cycle at least once, then either exit or repeat
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[cycle, cycle]
)

# Assemble the full process as a partial order
root = StrictPartialOrder(
    nodes=[
        component_sourcing,
        frame_build,
        subsystem_fit,
        firmware_load,
        sensor_calibrate,
        env_test,
        loop,
        data_capture,
        client_review,
        feedback_integrate,
        maintenance_plan,
        upgrade_design,
        final_approval
    ]
)
root.order.add_edge(component_sourcing, frame_build)
root.order.add_edge(frame_build, subsystem_fit)
root.order.add_edge(subsystem_fit, firmware_load)
root.order.add_edge(firmware_load, sensor_calibrate)
root.order.add_edge(sensor_calibrate, env_test)
root.order.add_edge(env_test, loop)
root.order.add_edge(loop, data_capture)
root.order.add_edge(data_capture, client_review)
root.order.add_edge(client_review, feedback_integrate)
root.order.add_edge(feedback_integrate, maintenance_plan)
root.order.add_edge(maintenance_plan, upgrade_design)
root.order.add_edge(upgrade_design, final_approval)