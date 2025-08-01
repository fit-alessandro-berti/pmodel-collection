# Generated from: 25bca7e9-a9d7-47ba-b3a5-b42aaa9385f1.json
# Description: This process outlines the complex assembly and configuration of custom drones tailored for specialized industrial applications. It involves initial client specification gathering, component sourcing from multiple suppliers with quality verification, precision assembly under controlled environmental conditions, firmware customization based on mission parameters, multi-stage testing including flight simulation and stress analysis, iterative adjustments for performance optimization, regulatory compliance checks, packaging with anti-static measures, and final shipment coordination with logistics partners. Each activity ensures the drone meets strict client requirements and industry standards before deployment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
cspecs    = Transition(label='Client Specs')
sourcing  = Transition(label='Component Sourcing')
qc        = Transition(label='Quality Check')
assembly  = Transition(label='Frame Assembly')
wiring    = Transition(label='Wiring Setup')
firmware  = Transition(label='Firmware Load')

calibration = Transition(label='Calibration Run')
flightsim   = Transition(label='Flight Sim')
stresstest  = Transition(label='Stress Test')
adjust      = Transition(label='Adjust Settings')

audit     = Transition(label='Compliance Audit')
packprep  = Transition(label='Packaging Prep')
static    = Transition(label='Static Shield')
logplan   = Transition(label='Logistics Plan')
dispatch  = Transition(label='Final Dispatch')

# Build the testing sub-workflow: calibration -> {flight sim, stress test} in parallel
po_tests = StrictPartialOrder(nodes=[calibration, flightsim, stresstest])
po_tests.order.add_edge(calibration, flightsim)
po_tests.order.add_edge(calibration, stresstest)

# Loop for iterative adjustments: do tests (A), then optionally adjust (B), then repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[po_tests, adjust])

# Assemble the top‐level partial order
root = StrictPartialOrder(nodes=[
    cspecs, sourcing, qc,
    assembly, wiring, firmware,
    loop,
    audit, packprep, static,
    logplan, dispatch
])

# Define the control‐flow dependencies
root.order.add_edge(cspecs, sourcing)
root.order.add_edge(sourcing, qc)
root.order.add_edge(qc, assembly)
root.order.add_edge(assembly, wiring)
root.order.add_edge(wiring, firmware)
root.order.add_edge(firmware, loop)
root.order.add_edge(loop, audit)
root.order.add_edge(audit, packprep)
root.order.add_edge(packprep, static)
root.order.add_edge(static, logplan)
root.order.add_edge(logplan, dispatch)