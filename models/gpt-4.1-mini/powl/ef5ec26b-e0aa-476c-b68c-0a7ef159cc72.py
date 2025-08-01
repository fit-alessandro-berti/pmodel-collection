# Generated from: ef5ec26b-e0aa-476c-b68c-0a7ef159cc72.json
# Description: This process outlines the complex coordination required to establish and maintain a collaborative urban farming initiative involving multiple stakeholders such as local governments, community groups, and technology providers. It includes site selection, soil testing, resource allocation, crop planning, volunteer recruitment, real-time monitoring, and yield optimization using IoT devices and data analytics. The process also integrates conflict resolution mechanisms, educational workshops, seasonal market planning, and sustainability assessments to ensure long-term viability and community engagement. Each activity is designed to balance technological integration with social dynamics to create a resilient urban agriculture ecosystem in dense metropolitan areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activity transitions
Site_Survey = Transition(label='Site Survey')
Soil_Testing = Transition(label='Soil Testing')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Resource_Plan = Transition(label='Resource Plan')
Crop_Selection = Transition(label='Crop Selection')
Volunteer_Signup = Transition(label='Volunteer Sign-up')
Tech_Setup = Transition(label='Tech Setup')
Irrigation_Check = Transition(label='Irrigation Check')
Data_Collection = Transition(label='Data Collection')
Growth_Monitoring = Transition(label='Growth Monitoring')
Conflict_Mediate = Transition(label='Conflict Mediate')
Workshop_Prep = Transition(label='Workshop Prep')
Market_Forecast = Transition(label='Market Forecast')
Yield_Analysis = Transition(label='Yield Analysis')
Sustainability_Audit = Transition(label='Sustainability Audit')
Community_Feedback = Transition(label='Community Feedback')
Equipment_Maintain = Transition(label='Equipment Maintain')
Waste_Manage = Transition(label='Waste Manage')

# 1) Initial Preparations partial order:
# Site Survey --> Soil Testing --> Stakeholder Meet --> Resource Plan
prep_po = StrictPartialOrder(nodes=[Site_Survey, Soil_Testing, Stakeholder_Meet, Resource_Plan])
prep_po.order.add_edge(Site_Survey, Soil_Testing)
prep_po.order.add_edge(Soil_Testing, Stakeholder_Meet)
prep_po.order.add_edge(Stakeholder_Meet, Resource_Plan)

# 2) Crop planning and volunteer recruitment can proceed concurrently after Resource Plan:
# Crop Selection and Volunteer Sign-up concurrent, but both after Resource Plan
crop_volunteer_po = StrictPartialOrder(nodes=[Crop_Selection, Volunteer_Signup])
# They are concurrent, but must come after Resource Plan — modeled in main PO edges

# 3) Technological setup and checks after volunteer signup and crop selection:
# Tech Setup --> Irrigation Check (seq)
tech_check_po = StrictPartialOrder(nodes=[Tech_Setup, Irrigation_Check])
tech_check_po.order.add_edge(Tech_Setup, Irrigation_Check)

# 4) Monitoring loop: Data Collection -> Growth Monitoring repeated
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Data_Collection, Growth_Monitoring]
)

# 5) Conflict resolution and workshops can be choices after Stakeholder Meet and during process
# Model as XOR choice between Conflict Mediate and Workshop Prep (plus silent skip to allow skipping)
skip = SilentTransition()
conflict_workshop_xor = OperatorPOWL(
    operator=Operator.XOR,
    children=[Conflict_Mediate, Workshop_Prep, skip]
)

# 6) Seasonal market and yield analysis after monitoring loop
market_yield_po = StrictPartialOrder(nodes=[Market_Forecast, Yield_Analysis])
market_yield_po.order.add_edge(Market_Forecast, Yield_Analysis)

# 7) Sustainability and community feedback concurrent after yield analysis
sustain_feedback_po = StrictPartialOrder(
    nodes=[Sustainability_Audit, Community_Feedback]
)  # Concurrent with no edges

# 8) Equipment maintenance and waste management concurrent at any time after Resource Plan
equip_waste_po = StrictPartialOrder(
    nodes=[Equipment_Maintain, Waste_Manage]
)  # Concurrent with no edges

# Compose the full process
# main PO nodes include:
# - prep_po (initial preparations)
# - crop_volunteer_po (crop select & volunteer signup)
# - tech_check_po (tech setup & irrigation check)
# - conflict_workshop_xor (conflicts or workshops optional)
# - monitor_loop (monitoring loop)
# - market_yield_po (market & yield)
# - sustain_feedback_po (sustain & feedback)
# - equip_waste_po (equip & waste)

nodes_all = [
    prep_po,
    crop_volunteer_po,
    tech_check_po,
    conflict_workshop_xor,
    monitor_loop,
    market_yield_po,
    sustain_feedback_po,
    equip_waste_po
]

root = StrictPartialOrder(nodes=nodes_all)

# Define ordering dependencies that reflect logical process flow:
# Initial preparations before crop & volunteer
root.order.add_edge(prep_po, crop_volunteer_po)
# Crop & volunteer before tech setup stage
root.order.add_edge(crop_volunteer_po, tech_check_po)
# Stakeholder meet is part of prep_po, conflict/workshop after Stakeholder Meet (in prep_po),
# so we set prep_po before conflict_workshop_xor:
root.order.add_edge(prep_po, conflict_workshop_xor)
# tech_check before monitoring loop
root.order.add_edge(tech_check_po, monitor_loop)
# monitoring loop before market and yield
root.order.add_edge(monitor_loop, market_yield_po)
# market & yield before sustain & feedback
root.order.add_edge(market_yield_po, sustain_feedback_po)

# Equipment and waste can be concurrent after Resource Plan (which is part of prep_po),
# so set prep_po before equip_waste_po but no other edges to keep concurrency
root.order.add_edge(prep_po, equip_waste_po)

# No other edges to keep concurrency between conflict_workshop_xor and tech_check_po, 
# and between equipment/waste and monitoring etc.

# The model reflects the complex collaboration with concurrency and loops
