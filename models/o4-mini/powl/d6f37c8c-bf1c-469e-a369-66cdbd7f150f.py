# Generated from: d6f37c8c-bf1c-469e-a369-66cdbd7f150f.json
# Description: This process involves the bespoke design and assembly of high-performance drones tailored for specialized industrial applications. Starting from client consultation to understand unique requirements, the workflow includes component sourcing, firmware customization, precision assembly, multi-stage testing, and regulatory compliance verification. The integration of AI modules and advanced sensors is followed by environmental stress testing and final quality assurance before packaging and logistics coordination to ensure timely delivery. This atypical process demands cross-functional collaboration among designers, engineers, and logistics specialists to meet strict performance and safety standards in an evolving market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define transitions for each activity
client_brief      = Transition(label='Client Brief')
design_draft      = Transition(label='Design Draft')
component_order   = Transition(label='Component Order')
firmware_build    = Transition(label='Firmware Build')
pcb_assembly      = Transition(label='PCB Assembly')
sensor_install    = Transition(label='Sensor Install')
motor_mount       = Transition(label='Motor Mount')
ai_module         = Transition(label='AI Module')
system_integrate  = Transition(label='System Integrate')
battery_test      = Transition(label='Battery Test')
flight_simulate   = Transition(label='Flight Simulate')
stress_test       = Transition(label='Stress Test')
compliance_check  = Transition(label='Compliance Check')
quality_audit     = Transition(label='Quality Audit')
package_drone     = Transition(label='Package Drone')
delivery_plan     = Transition(label='Delivery Plan')

# Build the partial order
root = StrictPartialOrder(nodes=[
    client_brief,
    design_draft,
    component_order,
    firmware_build,
    pcb_assembly,
    sensor_install,
    motor_mount,
    ai_module,
    system_integrate,
    battery_test,
    flight_simulate,
    stress_test,
    compliance_check,
    quality_audit,
    package_drone,
    delivery_plan
])

# Define the control-flow dependencies
root.order.add_edge(client_brief,     design_draft)
root.order.add_edge(design_draft,     component_order)
root.order.add_edge(component_order,  firmware_build)
root.order.add_edge(component_order,  pcb_assembly)
root.order.add_edge(pcb_assembly,     sensor_install)
root.order.add_edge(sensor_install,   motor_mount)
root.order.add_edge(motor_mount,      ai_module)
root.order.add_edge(firmware_build,   system_integrate)
root.order.add_edge(ai_module,        system_integrate)
root.order.add_edge(system_integrate, battery_test)
root.order.add_edge(battery_test,     flight_simulate)
root.order.add_edge(flight_simulate,  stress_test)
root.order.add_edge(stress_test,      compliance_check)
root.order.add_edge(compliance_check, quality_audit)
root.order.add_edge(quality_audit,    package_drone)
root.order.add_edge(package_drone,    delivery_plan)