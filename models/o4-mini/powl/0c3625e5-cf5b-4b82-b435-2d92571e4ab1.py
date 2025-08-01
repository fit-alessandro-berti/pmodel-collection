# Generated from: 0c3625e5-cf5b-4b82-b435-2d92571e4ab1.json
# Description: This process outlines the intricate steps involved in launching an urban vertical farming startup that integrates advanced hydroponics, IoT monitoring, and community engagement. The journey begins with site scouting and feasibility analysis, followed by securing permits and designing modular farm units. Procurement of specialized equipment and nutrient solutions is coordinated with technology setup for climate control and automated irrigation. Concurrently, partnerships with local markets and restaurants are negotiated to ensure distribution channels. Workforce training focuses on both agricultural practices and data analytics to optimize yield. Marketing campaigns leverage social media and urban sustainability narratives to attract early adopters. Throughout, data collection and iterative process optimization ensure continuous improvement, while compliance with health and safety regulations is strictly maintained.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_scouting   = Transition(label='Site Scouting')
feasibility     = Transition(label='Feasibility Study')
permit_sec      = Transition(label='Permit Securing')
unit_design     = Transition(label='Unit Designing')
equip_buy       = Transition(label='Equipment Buying')
nutrient_mix    = Transition(label='Nutrient Mixing')
tech_setup      = Transition(label='Tech Setup')
climate_ctrl    = Transition(label='Climate Control')
irrigation_set  = Transition(label='Irrigation Setup')
partner_out     = Transition(label='Partner Outreach')
staff_training  = Transition(label='Staff Training')
market_launch   = Transition(label='Market Launch')

# Loop children: data logging + iterative review/audit/feedback
data_logging    = Transition(label='Data Logging')
process_review  = Transition(label='Process Review')
safety_audit    = Transition(label='Safety Audit')
cust_feedback   = Transition(label='Customer Feedback')

# Build the inner PO for review -> audit -> feedback
review_cycle = StrictPartialOrder(nodes=[process_review, safety_audit, cust_feedback])
review_cycle.order.add_edge(process_review, safety_audit)
review_cycle.order.add_edge(safety_audit, cust_feedback)

# Define the loop: do data logging, then repeat review_cycle and data logging until exit
improvement_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[data_logging, review_cycle]
)

# Build the main partial order
root = StrictPartialOrder(nodes=[
    site_scouting, feasibility, permit_sec, unit_design,
    equip_buy, nutrient_mix, tech_setup, climate_ctrl, irrigation_set,
    partner_out, staff_training, market_launch,
    improvement_loop
])

# Sequence: site scouting -> feasibility -> permit -> design
root.order.add_edge(site_scouting, feasibility)
root.order.add_edge(feasibility, permit_sec)
root.order.add_edge(permit_sec, unit_design)

# After design, start procurement, tech setup, and partner outreach in parallel
root.order.add_edge(unit_design, equip_buy)
root.order.add_edge(unit_design, tech_setup)
root.order.add_edge(unit_design, partner_out)

# Procurement and tech setup internal orders
root.order.add_edge(equip_buy, nutrient_mix)
root.order.add_edge(tech_setup, climate_ctrl)
root.order.add_edge(tech_setup, irrigation_set)

# After procurement & tech, train staff
root.order.add_edge(nutrient_mix, staff_training)
root.order.add_edge(climate_ctrl, staff_training)
root.order.add_edge(irrigation_set, staff_training)

# Market launch after staff training and partner outreach
root.order.add_edge(staff_training, market_launch)
root.order.add_edge(partner_out, market_launch)

# After launch, enter the improvement loop
root.order.add_edge(market_launch, improvement_loop)