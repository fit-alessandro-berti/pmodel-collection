# Generated from: 2b56d3d2-aba1-4ce0-bdbf-f7e2aca123eb.json
# Description: This process outlines the complex steps involved in establishing an urban drone delivery system tailored to high-density metropolitan areas. It includes regulatory compliance checks, airspace mapping, drone fleet customization, dynamic routing algorithms, weather impact analysis, community engagement, and continuous performance monitoring to ensure safety, efficiency, and customer satisfaction. The process integrates multidisciplinary coordination among technology teams, local authorities, logistics partners, and environmental experts to address challenges such as noise pollution, flight path optimization, emergency protocols, and real-time data analytics for adaptive operations in rapidly changing urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
regulation_review = Transition(label='Regulation Review')
airspace_mapping = Transition(label='Airspace Mapping')
fleet_customization = Transition(label='Fleet Customization')
route_planning = Transition(label='Route Planning')
weather_analysis = Transition(label='Weather Analysis')
community_meet = Transition(label='Community Meet')
safety_protocol = Transition(label='Safety Protocol')
pilot_training = Transition(label='Pilot Training')
tech_integration = Transition(label='Tech Integration')
noise_assessment = Transition(label='Noise Assessment')
emergency_prep = Transition(label='Emergency Prep')
data_collection = Transition(label='Data Collection')
performance_audit = Transition(label='Performance Audit')
partner_alignment = Transition(label='Partner Alignment')
feedback_loop = Transition(label='Feedback Loop')
system_scaling = Transition(label='System Scaling')
compliance_audit = Transition(label='Compliance Audit')

# Logical considerations and structure based on the description:
#  - Start with 'Regulation Review' (regulatory compliance checks)
#  - Followed by parallel parts for airspace, fleet, routing, weather, community engagement
#  - Safety and pilot training preparation after regulatory and fleet/route/weather established
#  - Followed by tech integration that coordinates various parties
#  - Noise assessment and emergency prep after tech integrated
#  - Data collection and performance audit form a continuous feedback loop
#  - Partner alignment and system scaling happen later, compliance audit is final
#  
# We'll model these with partial orders and loops where appropriate.

# Subprocess 1: Initial regulatory compliance and mapping
init_po = StrictPartialOrder(nodes=[regulation_review, airspace_mapping])
init_po.order.add_edge(regulation_review, airspace_mapping)

# Subprocess 2: Fleet customization and route planning can be concurrent after airspace mapping
fleet_route_po = StrictPartialOrder(nodes=[fleet_customization, route_planning])
# no order edge - they are concurrent

# Subprocess 3: Weather analysis and community meet can be concurrent after fleet/route
weather_community_po = StrictPartialOrder(nodes=[weather_analysis, community_meet])
# no edges - concurrent

# Order: airspace_mapping --> (fleet_customization, route_planning)
# so link init_po to fleet_route_po by airspace_mapping --> both fleet_customization and route_planning.
# Since fleet_route_po has no inner order edges, add external edges in higher PO.

# Subprocess 4: Safety protocol and pilot training are sequential after weather/community meet
safety_training_po = StrictPartialOrder(nodes=[safety_protocol, pilot_training])
safety_training_po.order.add_edge(safety_protocol, pilot_training)

# Subprocess 5: Tech integration after pilot training
# Subprocess 6: Noise assessment and emergency prep concurrent after tech integration
noise_emergency_po = StrictPartialOrder(nodes=[noise_assessment, emergency_prep])
# concurrent nodes, no edges

# Subprocess 7: Data collection and performance audit with feedback loop (loop)
# We'll model the loop as * (Data Collection, Feedback Loop)
loop_feedback = OperatorPOWL(operator=Operator.LOOP, children=[data_collection, feedback_loop])

# performance audit after data collection and feedback loop
performance_audit_po = StrictPartialOrder(nodes=[performance_audit])
# single node, no edges.

# Subprocess 8: Partner alignment and system scaling concurrent after performance audit
partner_scaling_po = StrictPartialOrder(nodes=[partner_alignment, system_scaling])
# concurrent no edges

# Subprocess 9: Final compliance audit after partner alignment and system scaling
compliance_po = StrictPartialOrder(nodes=[compliance_audit])

# Now compose all these into a big partial order with correct edges:

# Nodes collection:
# We'll include initial partial orders and operator nodes

# Create a top-level partial order:
root = StrictPartialOrder(
    nodes=[
        init_po,                # 0
        fleet_route_po,         # 1
        weather_community_po,   # 2
        safety_training_po,     # 3
        tech_integration,       # 4 - single transition
        noise_emergency_po,     # 5
        loop_feedback,          # 6
        performance_audit_po,   # 7
        partner_scaling_po,     # 8
        compliance_po           # 9
    ]
)

# Add edges for ordering between those subprocesses:

# init_po (Regulation Review --> Airspace Mapping)

# airspace_mapping --> fleet_customization & route_planning
root.order.add_edge(init_po, fleet_route_po)  # partial order edges connect PO nodes

# fleet_route_po --> weather_community_po
root.order.add_edge(fleet_route_po, weather_community_po)

# weather_community_po --> safety_training_po
root.order.add_edge(weather_community_po, safety_training_po)

# safety_training_po --> tech_integration
root.order.add_edge(safety_training_po, tech_integration)

# tech_integration --> noise_emergency_po
root.order.add_edge(tech_integration, noise_emergency_po)

# noise_emergency_po --> loop_feedback (data collection + feedback loop)
root.order.add_edge(noise_emergency_po, loop_feedback)

# loop_feedback --> performance_audit_po
root.order.add_edge(loop_feedback, performance_audit_po)

# performance_audit_po --> partner_scaling_po
root.order.add_edge(performance_audit_po, partner_scaling_po)

# partner_scaling_po --> compliance_po (final)
root.order.add_edge(partner_scaling_po, compliance_po)