# Generated from: dfb4fa37-3aac-43b8-b58d-6210ececf076.json
# Description: This process outlines the complex steps required to establish a vertical farm within an urban environment. It includes site analysis, securing permits, designing modular grow units, sourcing specialized LED lighting, integrating hydroponic systems, recruiting agritech specialists, pilot crop cultivation, data-driven growth optimization, developing waste recycling loops, establishing local distribution channels, creating customer subscription models, implementing IoT monitoring, conducting sustainability audits, and continuous improvement cycles to ensure high yield and minimal environmental impact in a densely populated area.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_analysis        = Transition(label='Site Analysis')
permit_securing      = Transition(label='Permit Securing')
unit_designing       = Transition(label='Unit Designing')
led_sourcing         = Transition(label='LED Sourcing')
hydroponic_setup     = Transition(label='Hydroponic Setup')
staff_hiring         = Transition(label='Staff Hiring')
pilot_cultivation    = Transition(label='Pilot Cultivation')
data_integration     = Transition(label='Data Integration')
waste_recycling      = Transition(label='Waste Recycling')
local_distribution   = Transition(label='Local Distribution')
subscription_setup   = Transition(label='Subscription Setup')
iot_deployment       = Transition(label='IoT Deployment')
sustainability_audit = Transition(label='Sustainability Audit')
market_testing       = Transition(label='Market Testing')
process_refinement   = Transition(label='Process Refinement')

# Build the loop body (A): operation cycle from pilot to market testing
body = StrictPartialOrder(nodes=[
    pilot_cultivation,
    data_integration,
    waste_recycling,
    local_distribution,
    subscription_setup,
    iot_deployment,
    sustainability_audit,
    market_testing
])
body.order.add_edge(pilot_cultivation, data_integration)
body.order.add_edge(data_integration, waste_recycling)
body.order.add_edge(waste_recycling, local_distribution)
body.order.add_edge(local_distribution, subscription_setup)
body.order.add_edge(subscription_setup, iot_deployment)
body.order.add_edge(iot_deployment, sustainability_audit)
body.order.add_edge(sustainability_audit, market_testing)

# Build the loop redo-part (B): process refinement
redo = StrictPartialOrder(nodes=[process_refinement])
# no internal edges in a single-node PO

# Assemble the LOOP operator
operation_loop = OperatorPOWL(operator=Operator.LOOP, children=[body, redo])

# Build the root partial order: initial setup steps followed by the improvement loop
root = StrictPartialOrder(nodes=[
    site_analysis,
    permit_securing,
    unit_designing,
    led_sourcing,
    hydroponic_setup,
    staff_hiring,
    operation_loop
])
root.order.add_edge(site_analysis, permit_securing)
root.order.add_edge(permit_securing, unit_designing)
root.order.add_edge(unit_designing, led_sourcing)
root.order.add_edge(led_sourcing, hydroponic_setup)
root.order.add_edge(hydroponic_setup, staff_hiring)
root.order.add_edge(staff_hiring, operation_loop)