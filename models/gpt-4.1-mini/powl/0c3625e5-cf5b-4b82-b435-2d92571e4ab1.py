# Generated from: 0c3625e5-cf5b-4b82-b435-2d92571e4ab1.json
# Description: This process outlines the intricate steps involved in launching an urban vertical farming startup that integrates advanced hydroponics, IoT monitoring, and community engagement. The journey begins with site scouting and feasibility analysis, followed by securing permits and designing modular farm units. Procurement of specialized equipment and nutrient solutions is coordinated with technology setup for climate control and automated irrigation. Concurrently, partnerships with local markets and restaurants are negotiated to ensure distribution channels. Workforce training focuses on both agricultural practices and data analytics to optimize yield. Marketing campaigns leverage social media and urban sustainability narratives to attract early adopters. Throughout, data collection and iterative process optimization ensure continuous improvement, while compliance with health and safety regulations is strictly maintained.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Site_Scouting = Transition(label='Site Scouting')
Feasibility_Study = Transition(label='Feasibility Study')
Permit_Securing = Transition(label='Permit Securing')
Unit_Designing = Transition(label='Unit Designing')
Equipment_Buying = Transition(label='Equipment Buying')
Nutrient_Mixing = Transition(label='Nutrient Mixing')
Tech_Setup = Transition(label='Tech Setup')
Climate_Control = Transition(label='Climate Control')
Irrigation_Setup = Transition(label='Irrigation Setup')
Partner_Outreach = Transition(label='Partner Outreach')
Staff_Training = Transition(label='Staff Training')
Market_Launch = Transition(label='Market Launch')
Data_Logging = Transition(label='Data Logging')
Process_Review = Transition(label='Process Review')
Safety_Audit = Transition(label='Safety Audit')
Customer_Feedback = Transition(label='Customer Feedback')

# First partial order: site scouting --> feasibility study --> permits --> unit designing
first_stage = StrictPartialOrder(
    nodes=[Site_Scouting, Feasibility_Study, Permit_Securing, Unit_Designing]
)
first_stage.order.add_edge(Site_Scouting, Feasibility_Study)
first_stage.order.add_edge(Feasibility_Study, Permit_Securing)
first_stage.order.add_edge(Permit_Securing, Unit_Designing)

# Next partial order: procurement (equipment buying + nutrient mixing) concurrently with tech setup (climate control + irrigation)
procurement = StrictPartialOrder(
    nodes=[Equipment_Buying, Nutrient_Mixing]
)
# no order edges between these two, concurrent

tech_sub = StrictPartialOrder(
    nodes=[Climate_Control, Irrigation_Setup]
)
tech_sub.order.add_edge(Climate_Control, Irrigation_Setup)

tech_setup = StrictPartialOrder(
    nodes=[Tech_Setup, tech_sub]
)
tech_setup.order.add_edge(Tech_Setup, tech_sub)

# Combine procurement and tech setup concurrently (unordered)
procurement_tech = StrictPartialOrder(
    nodes=[procurement, tech_setup]
)
# no edges between procurement and tech_setup => concurrent

# Partnership negotiation (partner outreach)
partner_outreach = Partner_Outreach

# Workforce training (staff training)
staff_training = Staff_Training

# Marketing campaign (market launch)
market_launch = Market_Launch

# These three run concurrently: partner outreach, staff training, market launch
concurrent_marketing_training_outreach = StrictPartialOrder(
    nodes=[partner_outreach, staff_training, market_launch]
)
# no order edges, concurrent

# Data collection and iterative process optimization as a loop:
# Loop over Data Logging and Process Review
data_logging = Data_Logging
process_review = Process_Review
data_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_logging, process_review])

# Safety audit (strictly maintained compliance)
safety_audit = Safety_Audit

# Customer feedback
customer_feedback = Customer_Feedback

# Putting together final partial order:
# first_stage --> (procurement_tech) --> concurrent_marketing_training_outreach --> data_loop --> safety_audit --> customer_feedback

root = StrictPartialOrder(
    nodes=[
        first_stage,
        procurement_tech,
        concurrent_marketing_training_outreach,
        data_loop,
        safety_audit,
        customer_feedback,
    ]
)
root.order.add_edge(first_stage, procurement_tech)
root.order.add_edge(procurement_tech, concurrent_marketing_training_outreach)
root.order.add_edge(concurrent_marketing_training_outreach, data_loop)
root.order.add_edge(data_loop, safety_audit)
root.order.add_edge(safety_audit, customer_feedback)