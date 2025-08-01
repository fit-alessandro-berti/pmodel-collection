# Generated from: c49e6501-52c0-4fb0-b040-3b221c891a0a.json
# Description: This process involves the end-to-end assembly, testing, customization, and deployment of specialized drones for niche industrial applications. Starting from raw component inspection, parts are selected based on client specifications, then assembled with precision. Following mechanical assembly, firmware is loaded and calibrated through iterative testing cycles. Environmental stress tests simulate real-world conditions to ensure durability and performance. Parallel to hardware preparation, software modules are customized to client needs, including navigation algorithms and communication protocols. Once the drone passes all validations, a secure data link is established, and the drone is deployed on-site. Post-deployment includes live monitoring, adaptive firmware updates, and eventual recovery or maintenance scheduling to ensure sustained operational efficacy in challenging environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
cc        = Transition(label='Component Check')
spec      = Transition(label='Spec Review')
sort      = Transition(label='Parts Sorting')
mech      = Transition(label='Mechanical Fit')
fw        = Transition(label='Firmware Load')
calib     = Transition(label='Calibration Run')
stress    = Transition(label='Stress Test')
sp        = Transition(label='Software Patch')
atune     = Transition(label='Algorithm Tune')
comms     = Transition(label='Comms Setup')
val       = Transition(label='Validation Pass')
dlink     = Transition(label='Data Link')
onsite    = Transition(label='Onsite Deploy')
live      = Transition(label='Live Monitor')
upd       = Transition(label='Update Push')
recplan   = Transition(label='Recovery Plan')
mlog      = Transition(label='Maintenance Log')

# Loop for iterative testing: calibrate then stress test, repeat until exit
loop_test = OperatorPOWL(operator=Operator.LOOP, children=[calib, stress])

# Build the partial order
root = StrictPartialOrder(nodes=[
    cc, spec, sort, mech,
    fw, loop_test,
    sp, atune, comms,
    val, dlink, onsite,
    live, upd, recplan, mlog
])

# Sequential flow: inspection to assembly
root.order.add_edge(cc, spec)
root.order.add_edge(spec, sort)
root.order.add_edge(sort, mech)

# Fork into hardware testing and software customization
root.order.add_edge(mech, fw)
root.order.add_edge(mech, sp)

# Hardware testing branch
root.order.add_edge(fw, loop_test)

# Software customization branch
root.order.add_edge(sp, atune)
root.order.add_edge(atune, comms)

# Join before deployment: validation after both branches
root.order.add_edge(loop_test, val)
root.order.add_edge(comms, val)

# Deployment sequence
root.order.add_edge(val, dlink)
root.order.add_edge(dlink, onsite)

# Post-deployment parallel activities
root.order.add_edge(onsite, live)
root.order.add_edge(onsite, upd)

# Recovery and maintenance after monitoring and updates
root.order.add_edge(live, recplan)
root.order.add_edge(upd, recplan)
root.order.add_edge(recplan, mlog)