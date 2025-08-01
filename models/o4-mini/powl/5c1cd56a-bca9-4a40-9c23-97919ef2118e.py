# Generated from: 5c1cd56a-bca9-4a40-9c23-97919ef2118e.json
# Description: This process outlines the complex workflow involved in leasing customized drones for industrial inspection purposes. It includes client consultation to determine specific requirements, drone design adjustments, regulatory compliance checks, prototype testing, contract negotiation, insurance setup, pilot training scheduling, deployment planning, real-time monitoring, maintenance scheduling, data analytics delivery, feedback collection, renewal assessment, and end-of-lease asset recovery. Each step requires coordination between engineering, legal, operations, and customer service teams to ensure tailored solutions meet safety standards and client expectations while optimizing operational efficiency and minimizing downtime.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all atomic activities
client       = Transition(label='Client Consult')
design       = Transition(label='Design Adjust')
compliance   = Transition(label='Compliance Check')
prototype    = Transition(label='Prototype Test')
contract     = Transition(label='Contract Sign')
insurance    = Transition(label='Insurance Setup')
train        = Transition(label='Pilot Train')
deploy       = Transition(label='Deploy Plan')
monitor      = Transition(label='Real-time Monitor')
maintenance  = Transition(label='Schedule Maintenance')
analytics    = Transition(label='Data Analytics')
feedback     = Transition(label='Collect Feedback')
renewal      = Transition(label='Renewal Assess')
asset        = Transition(label='Asset Recover')
invoice      = Transition(label='Invoice Process')

# Build the leasing‐cycle partial order (one contract round through feedback)
cycle = StrictPartialOrder(nodes=[
    contract, insurance, train, deploy, monitor, maintenance, analytics, feedback
])
cycle.order.add_edge(contract,   insurance)
cycle.order.add_edge(insurance,  train)
cycle.order.add_edge(train,      deploy)
cycle.order.add_edge(deploy,     monitor)
cycle.order.add_edge(monitor,    maintenance)
cycle.order.add_edge(maintenance, analytics)
cycle.order.add_edge(analytics,  feedback)

# Build the loop: after each feedback, assess renewal; if renew, do another cycle
lease_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[renewal, cycle]
)

# Assemble the full process: consultation → design → compliance → prototype →
#   lease‐loop → asset recovery → invoicing
root = StrictPartialOrder(nodes=[
    client, design, compliance, prototype, lease_loop, asset, invoice
])
root.order.add_edge(client,    design)
root.order.add_edge(design,    compliance)
root.order.add_edge(compliance, prototype)
root.order.add_edge(prototype, lease_loop)
root.order.add_edge(lease_loop, asset)
root.order.add_edge(asset,     invoice)