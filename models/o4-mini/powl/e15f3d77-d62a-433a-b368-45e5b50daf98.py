# Generated from: e15f3d77-d62a-433a-b368-45e5b50daf98.json
# Description: This process details the end-to-end assembly of customized drones tailored to specific client requirements. It begins with requirements gathering and design adaptation, followed by specialized component sourcing from multiple vendors. The components undergo individual testing before precision assembly, firmware installation, and calibration. Post-assembly, drones are subjected to environmental stress testing and flight simulation to ensure operational reliability. Final quality checks include battery endurance and sensor accuracy validation. After successful validation, drones are packaged with customized manuals and shipped with tracking integration. Customer feedback is collected post-delivery to inform continuous improvement cycles.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic transitions
gather        = Transition(label='Gather Specs')
adapt         = Transition(label='Adapt Design')
source        = Transition(label='Source Parts')
component_test= Transition(label='Component Test')
assemble      = Transition(label='Assemble Frame')
install_fw    = Transition(label='Install Firmware')
calibrate     = Transition(label='Calibrate Sensors')
stress_test   = Transition(label='Stress Test')
simulate      = Transition(label='Flight Simulate')
validate_batt = Transition(label='Validate Battery')
check_acc     = Transition(label='Check Accuracy')
package_units = Transition(label='Package Units')
create_manuals= Transition(label='Create Manuals')
ship          = Transition(label='Ship Drones')
feedback      = Transition(label='Collect Feedback')

# Build the loop body as a partial order
body = StrictPartialOrder(nodes=[
    source, component_test, assemble, install_fw, calibrate,
    stress_test, simulate,
    validate_batt, check_acc,
    package_units, create_manuals,
    ship, feedback
])

# Sequential dependencies
body.order.add_edge(source, component_test)
body.order.add_edge(component_test, assemble)
body.order.add_edge(assemble, install_fw)
body.order.add_edge(install_fw, calibrate)
body.order.add_edge(calibrate, stress_test)
body.order.add_edge(stress_test, simulate)

# After simulation, two parallel quality checks
body.order.add_edge(simulate, validate_batt)
body.order.add_edge(simulate, check_acc)

# After both checks complete, packaging and manual creation may happen in parallel,
# but shipping must wait for both package and manuals
body.order.add_edge(validate_batt, package_units)
body.order.add_edge(check_acc, package_units)
# Create manuals is independent, so no edges into it

body.order.add_edge(package_units, ship)
body.order.add_edge(create_manuals, ship)

# After shipping, collect feedback
body.order.add_edge(ship, feedback)

# Build the loop: adapt → (body) → adapt … until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[adapt, body])

# Root PO: gather specs must happen before entering the loop
root = StrictPartialOrder(nodes=[gather, loop])
root.order.add_edge(gather, loop)