# Generated from: fa8c0802-8b9d-4a67-9d07-38b28904557a.json
# Description: This process involves dynamically adjusting supply chain parameters in response to real-time environmental, economic, and social data inputs. It begins with continuous sensor data aggregation followed by anomaly detection, supplier risk assessment, and predictive demand modeling. The process incorporates stakeholder feedback loops and automated negotiation protocols with suppliers to optimize inventory levels. Risk mitigation strategies are deployed through contingency resource allocation. Final calibration includes sustainability impact scoring and compliance verification before executing adaptive distribution scheduling to ensure resilience and efficiency under fluctuating global conditions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
data_agg       = Transition(label='Data Aggregation')
anomaly        = Transition(label='Anomaly Detect')
risk           = Transition(label='Risk Assess')
demand         = Transition(label='Demand Model')
stakeholder    = Transition(label='Stakeholder Sync')
feedback       = Transition(label='Feedback Loop')
negotiation    = Transition(label='Auto Negotiate')
inventory      = Transition(label='Inventory Optimize')
contingency    = Transition(label='Contingency Plan')
resource       = Transition(label='Resource Allocate')
sustainability = Transition(label='Sustainability Check')
impact         = Transition(label='Impact Score')
compliance     = Transition(label='Compliance Verify')
distribution   = Transition(label='Distribution Plan')
schedule       = Transition(label='Schedule Execute')
audit          = Transition(label='Performance Audit')

# Build the stakeholder‐negotiation‐inventory loop body
body_loop = StrictPartialOrder(
    nodes=[stakeholder, feedback, negotiation, inventory]
)
body_loop.order.add_edge(stakeholder, feedback)
body_loop.order.add_edge(feedback, negotiation)
body_loop.order.add_edge(negotiation, inventory)

# Create a LOOP operator: execute the body once, then repeat (body) until exit
loop_node = OperatorPOWL(
    operator=Operator.LOOP,
    children=[body_loop, body_loop]
)

# Build the root partial order for the overall process
root = StrictPartialOrder(
    nodes=[
        data_agg,
        anomaly,
        risk,
        demand,
        loop_node,
        contingency,
        resource,
        sustainability,
        impact,
        compliance,
        distribution,
        schedule,
        audit
    ]
)

# Define the main sequence dependencies
root.order.add_edge(data_agg,       anomaly)
root.order.add_edge(anomaly,        risk)
root.order.add_edge(risk,           demand)
root.order.add_edge(demand,         loop_node)
root.order.add_edge(loop_node,      contingency)
root.order.add_edge(contingency,    resource)
root.order.add_edge(resource,       sustainability)
root.order.add_edge(sustainability, impact)
root.order.add_edge(impact,         compliance)
root.order.add_edge(compliance,     distribution)
root.order.add_edge(distribution,   schedule)
root.order.add_edge(schedule,       audit)