# Generated from: dfb4fa37-3aac-43b8-b58d-6210ececf076.json
# Description: This process outlines the complex steps required to establish a vertical farm within an urban environment. It includes site analysis, securing permits, designing modular grow units, sourcing specialized LED lighting, integrating hydroponic systems, recruiting agritech specialists, pilot crop cultivation, data-driven growth optimization, developing waste recycling loops, establishing local distribution channels, creating customer subscription models, implementing IoT monitoring, conducting sustainability audits, and continuous improvement cycles to ensure high yield and minimal environmental impact in a densely populated area.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
site_analysis = Transition(label='Site Analysis')
permit_securing = Transition(label='Permit Securing')
unit_designing = Transition(label='Unit Designing')
led_sourcing = Transition(label='LED Sourcing')
hydroponic_setup = Transition(label='Hydroponic Setup')
staff_hiring = Transition(label='Staff Hiring')
pilot_cultivation = Transition(label='Pilot Cultivation')
data_integration = Transition(label='Data Integration')
waste_recycling = Transition(label='Waste Recycling')
local_distribution = Transition(label='Local Distribution')
subscription_setup = Transition(label='Subscription Setup')
iot_deployment = Transition(label='IoT Deployment')
sustainability_audit = Transition(label='Sustainability Audit')
market_testing = Transition(label='Market Testing')
process_refinement = Transition(label='Process Refinement')

# Build partial orders for initial sequential steps:
# Site Analysis --> Permit Securing --> Unit Designing
initial_po = StrictPartialOrder(nodes=[site_analysis, permit_securing, unit_designing])
initial_po.order.add_edge(site_analysis, permit_securing)
initial_po.order.add_edge(permit_securing, unit_designing)

# After Unit Designing, parallel sourcing LED and Hydroponic setup, both lead to Staff Hiring
parallel_source = StrictPartialOrder(nodes=[led_sourcing, hydroponic_setup, staff_hiring])
parallel_source.order.add_edge(led_sourcing, staff_hiring)
parallel_source.order.add_edge(hydroponic_setup, staff_hiring)

# Link from initial_po to parallel_source
# Unit Designing --> led_sourcing AND hydroponic_setup (concurrent)
# We encode concurrency by no order between led_sourcing and hydroponic_setup, edges from unit_designing to both:
parallel_start = StrictPartialOrder(
    nodes=[unit_designing, led_sourcing, hydroponic_setup]
)
parallel_start.order.add_edge(unit_designing, led_sourcing)
parallel_start.order.add_edge(unit_designing, hydroponic_setup)

# Let's modularize this: initial_po ends at unit_designing;
# combine with partial order that has unit_designing --> led_sourcing & hydroponic_setup --> staff_hiring
first_part = StrictPartialOrder(
    nodes=[site_analysis, permit_securing, unit_designing, led_sourcing, hydroponic_setup, staff_hiring]
)
first_part.order.add_edge(site_analysis, permit_securing)
first_part.order.add_edge(permit_securing, unit_designing)
first_part.order.add_edge(unit_designing, led_sourcing)
first_part.order.add_edge(unit_designing, hydroponic_setup)
first_part.order.add_edge(led_sourcing, staff_hiring)
first_part.order.add_edge(hydroponic_setup, staff_hiring)

# After staff_hiring: Pilot Cultivation --> Data Integration
cultivation_po = StrictPartialOrder(nodes=[pilot_cultivation, data_integration])
cultivation_po.order.add_edge(pilot_cultivation, data_integration)

# After Data Integration: two parallel branches:
# 1) Waste Recycling --> Local Distribution --> Subscription Setup
wr_branch = StrictPartialOrder(nodes=[waste_recycling, local_distribution, subscription_setup])
wr_branch.order.add_edge(waste_recycling, local_distribution)
wr_branch.order.add_edge(local_distribution, subscription_setup)

# 2) IoT Deployment --> Sustainability Audit
iot_branch = StrictPartialOrder(nodes=[iot_deployment, sustainability_audit])
iot_branch.order.add_edge(iot_deployment, sustainability_audit)

# These two branches occur concurrently after Data Integration
concurrent_after_di = StrictPartialOrder(
    nodes=[data_integration, waste_recycling, local_distribution, subscription_setup, iot_deployment, sustainability_audit]
)
concurrent_after_di.order.add_edge(data_integration, waste_recycling)
concurrent_after_di.order.add_edge(data_integration, iot_deployment)
concurrent_after_di.order.add_edge(waste_recycling, local_distribution)
concurrent_after_di.order.add_edge(local_distribution, subscription_setup)
concurrent_after_di.order.add_edge(iot_deployment, sustainability_audit)

# After those branches finish: choice between Market Testing or go directly to Process Refinement
choice_mt_pr = OperatorPOWL(operator=Operator.XOR, children=[market_testing, process_refinement])

# Market Testing must be followed by Process Refinement (sequentially)
mt_to_pr = StrictPartialOrder(nodes=[market_testing, process_refinement])
mt_to_pr.order.add_edge(market_testing, process_refinement)

# We model Market Testing --> Process Refinement as a sequence,
# and choice between that sequence and just Process Refinement:
choice_mt_pr = OperatorPOWL(operator=Operator.XOR, children=[mt_to_pr, process_refinement])

# Now, model the loop: The process refinement cycle:
# Implement loop: loop = *(initial_body, refinement)
# where initial_body = everything before Market Testing/Process Refinement
# refinement = choice_mt_pr

# initial_body includes all steps up to the start of the loop body
initial_body = StrictPartialOrder(
    nodes=[site_analysis, permit_securing, unit_designing,
           led_sourcing, hydroponic_setup, staff_hiring,
           pilot_cultivation, data_integration,
           waste_recycling, local_distribution, subscription_setup,
           iot_deployment, sustainability_audit],
)
# edges as in prior composed partial orders
initial_body.order.add_edge(site_analysis, permit_securing)
initial_body.order.add_edge(permit_securing, unit_designing)
initial_body.order.add_edge(unit_designing, led_sourcing)
initial_body.order.add_edge(unit_designing, hydroponic_setup)
initial_body.order.add_edge(led_sourcing, staff_hiring)
initial_body.order.add_edge(hydroponic_setup, staff_hiring)
initial_body.order.add_edge(staff_hiring, pilot_cultivation)
initial_body.order.add_edge(pilot_cultivation, data_integration)
initial_body.order.add_edge(data_integration, waste_recycling)
initial_body.order.add_edge(data_integration, iot_deployment)
initial_body.order.add_edge(waste_recycling, local_distribution)
initial_body.order.add_edge(local_distribution, subscription_setup)
initial_body.order.add_edge(iot_deployment, sustainability_audit)

loop = OperatorPOWL(operator=Operator.LOOP, children=[initial_body, choice_mt_pr])

root = loop