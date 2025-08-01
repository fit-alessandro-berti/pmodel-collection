# Generated from: 418fd8c0-d56e-4260-9475-14aeab6beb62.json
# Description: This process involves the intricate coordination and implementation of a dynamic art installation that reacts to environmental stimuli and audience interaction. It begins with concept validation and sensor calibration, progresses through modular component assembly and real-time data integration, and concludes with adaptive lighting and sound synchronization. The process requires multidisciplinary collaboration between artists, engineers, and software developers to ensure seamless interactivity and immersive experience. Continuous monitoring and iterative adjustments are essential to maintain responsiveness and artistic intent throughout exhibit duration.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
concept_validate = Transition(label='Concept Validate')
sensor_calibrate   = Transition(label='Sensor Calibrate')
module_assemble    = Transition(label='Module Assemble')
power_configure    = Transition(label='Power Configure')
network_setup      = Transition(label='Network Setup')
data_integrate     = Transition(label='Data Integrate')
signal_test        = Transition(label='Signal Test')
software_deploy    = Transition(label='Software Deploy')
interaction_map    = Transition(label='Interaction Map')
lighting_sync      = Transition(label='Lighting Sync')
sound_adjust       = Transition(label='Sound Adjust')
safety_check       = Transition(label='Safety Check')
feedback_collect   = Transition(label='Feedback Collect')
system_monitor     = Transition(label='System Monitor')
visitor_track      = Transition(label='Visitor Track')
performance_tune   = Transition(label='Performance Tune')
content_update     = Transition(label='Content Update')

# Build the monitoring partial order (body of the loop)
monitoring_body = StrictPartialOrder(nodes=[
    feedback_collect,
    system_monitor,
    visitor_track
])
monitoring_body.order.add_edge(feedback_collect, system_monitor)
monitoring_body.order.add_edge(system_monitor, visitor_track)

# Build the adjustment partial order (loop back branch)
adjustment = StrictPartialOrder(nodes=[
    performance_tune,
    content_update
])
adjustment.order.add_edge(performance_tune, content_update)

# Loop operator for continuous monitoring & iterative adjustments
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitoring_body, adjustment]
)

# Root partial order for the overall installation process
root = StrictPartialOrder(nodes=[
    concept_validate,
    sensor_calibrate,
    module_assemble,
    power_configure,
    network_setup,
    data_integrate,
    signal_test,
    software_deploy,
    interaction_map,
    lighting_sync,
    sound_adjust,
    safety_check,
    monitor_loop
])

# Define the control‐flow / partial‐order relations
root.order.add_edge(concept_validate, sensor_calibrate)
root.order.add_edge(sensor_calibrate, module_assemble)
# After assembly, power & network setup can proceed in parallel
root.order.add_edge(module_assemble, power_configure)
root.order.add_edge(module_assemble, network_setup)
# Both converge into data integration
root.order.add_edge(power_configure, data_integrate)
root.order.add_edge(network_setup, data_integrate)
root.order.add_edge(data_integrate, signal_test)
root.order.add_edge(signal_test, software_deploy)
root.order.add_edge(software_deploy, interaction_map)
# Audience interaction mapping drives lighting and sound in parallel
root.order.add_edge(interaction_map, lighting_sync)
root.order.add_edge(interaction_map, sound_adjust)
# Before entering the monitoring loop, ensure safety checks
root.order.add_edge(lighting_sync, safety_check)
root.order.add_edge(sound_adjust, safety_check)
# Safety check precedes the continuous monitoring & adjustment loop
root.order.add_edge(safety_check, monitor_loop)