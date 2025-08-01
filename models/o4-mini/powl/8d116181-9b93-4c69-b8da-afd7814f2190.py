# Generated from: 8d116181-9b93-4c69-b8da-afd7814f2190.json
# Description: This process outlines the setup and operational workflow for an adaptive urban farming system that integrates IoT sensors, AI-driven crop optimization, and community engagement. It begins with site analysis and environmental scanning, followed by modular farm design tailored to spatial constraints. Subsequent steps include sensor deployment for real-time monitoring, nutrient cycling management, and dynamic planting schedules based on AI predictions. The process also incorporates waste-to-compost conversion, stakeholder coordination meetings, and ongoing data analytics for yield improvement. Community workshops and feedback loops ensure adaptability and sustainability, while periodic system audits maintain regulatory compliance and resource efficiency throughout the farm lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_analysis = Transition(label='Site Analysis')
env_scanning = Transition(label='Env Scanning')
modular_design = Transition(label='Modular Design')
sensor_deploy = Transition(label='Sensor Deploy')
nutrient_cycle = Transition(label='Nutrient Cycle')
ai_scheduling = Transition(label='AI Scheduling')
waste_compost = Transition(label='Waste Compost')
stakeholder_meet = Transition(label='Stakeholder Meet')

data_analytics = Transition(label='Data Analytics')
yield_review = Transition(label='Yield Review')
community_workshop = Transition(label='Community Workshop')
feedback_loop = Transition(label='Feedback Loop')

system_audit = Transition(label='System Audit')
regulatory_check = Transition(label='Regulatory Check')
resource_adjust = Transition(label='Resource Adjust')

# Initial sequential part
initial = StrictPartialOrder(nodes=[
    site_analysis,
    env_scanning,
    modular_design,
    sensor_deploy,
    nutrient_cycle,
    ai_scheduling,
    waste_compost,
    stakeholder_meet
])
initial.order.add_edge(site_analysis, env_scanning)
initial.order.add_edge(env_scanning, modular_design)
initial.order.add_edge(modular_design, sensor_deploy)
initial.order.add_edge(sensor_deploy, nutrient_cycle)
initial.order.add_edge(nutrient_cycle, ai_scheduling)
initial.order.add_edge(ai_scheduling, waste_compost)
initial.order.add_edge(waste_compost, stakeholder_meet)

# Loop body for ongoing analytics and feedback
body = StrictPartialOrder(nodes=[
    data_analytics,
    yield_review,
    community_workshop,
    feedback_loop
])
body.order.add_edge(data_analytics, yield_review)
body.order.add_edge(yield_review, community_workshop)
body.order.add_edge(community_workshop, feedback_loop)

# Loop operator: do 'initial' once, then repeatedly do 'body'
loop = OperatorPOWL(operator=Operator.LOOP, children=[initial, body])

# Final sequential part for audits and adjustments
final = StrictPartialOrder(nodes=[
    system_audit,
    regulatory_check,
    resource_adjust
])
final.order.add_edge(system_audit, regulatory_check)
final.order.add_edge(regulatory_check, resource_adjust)

# Root model combining the loop and the final checkpoint
root = StrictPartialOrder(nodes=[loop, final])
root.order.add_edge(loop, final)