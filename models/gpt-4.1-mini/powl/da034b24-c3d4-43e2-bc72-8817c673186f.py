# Generated from: da034b24-c3d4-43e2-bc72-8817c673186f.json
# Description: This process describes the complex coordination required to establish and maintain an urban beekeeping network across multiple city locations. It involves site assessments for hive placement, regulatory compliance checks, community engagement activities, hive monitoring, honey harvesting coordination, pest control scheduling, data logging for environmental impact, educational workshops planning, supply chain management for beekeeping materials, and collaboration with local agricultural authorities. The process ensures sustainable urban apiaries while promoting biodiversity and urban agriculture education, balancing ecological concerns with city regulations and public safety.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Survey = Transition(label='Site Survey')
Permit_Check = Transition(label='Permit Check')
Hive_Setup = Transition(label='Hive Setup')
Community_Meet = Transition(label='Community Meet')
Hive_Monitor = Transition(label='Hive Monitor')
Pest_Control = Transition(label='Pest Control')
Honey_Harvest = Transition(label='Honey Harvest')
Data_Logging = Transition(label='Data Logging')
Workshop_Plan = Transition(label='Workshop Plan')
Supply_Order = Transition(label='Supply Order')
Volunteer_Coord = Transition(label='Volunteer Coord')
Regulation_Review = Transition(label='Regulation Review')
Pollination_Map = Transition(label='Pollination Map')
Apiary_Audit = Transition(label='Apiary Audit')
Feedback_Gather = Transition(label='Feedback Gather')
Waste_Manage = Transition(label='Waste Manage')

# Core sequence: Site Survey --> Permit Check --> Hive Setup
setup_PO = StrictPartialOrder(nodes=[Site_Survey, Permit_Check, Hive_Setup])
setup_PO.order.add_edge(Site_Survey, Permit_Check)
setup_PO.order.add_edge(Permit_Check, Hive_Setup)

# Post-setup regulatory steps are related to Regulation Review
reg_review_PO = StrictPartialOrder(nodes=[Regulation_Review, Apiary_Audit])
reg_review_PO.order.add_edge(Regulation_Review, Apiary_Audit)

# Pollination Map occurs after Audit
audit_to_pollination_PO = StrictPartialOrder(nodes=[Apiary_Audit, Pollination_Map])
audit_to_pollination_PO.order.add_edge(Apiary_Audit, Pollination_Map)

# Data Logging runs with Pollination Map after Audit
data_and_pollination_PO = StrictPartialOrder(nodes=[Pollination_Map, Data_Logging])
# Concurrent, no order edges

# Community Meet and Volunteer Coord can be concurrent and unrelated to hive maintenance activities
community_PO = StrictPartialOrder(nodes=[Community_Meet, Volunteer_Coord])
# concurrent no order edges

# Hive monitoring loop with pest control and honey harvest (monitoring ongoing with periodic pest control and harvest)
# Model continuous hive monitoring with a loop: Run Hive Monitor, then choose whether to do Pest Control or Honey Harvest, then back to Hive Monitor again
# Using loop: (* (Hive_Monitor, X(Pest_Control, Honey_Harvest)))

monitor_choice = OperatorPOWL(operator=Operator.XOR, children=[Pest_Control, Honey_Harvest])
hive_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[Hive_Monitor, monitor_choice])

# Supply order and waste management run concurrently during the process
supp_waste_PO = StrictPartialOrder(nodes=[Supply_Order, Waste_Manage])
# concurrent no order edges

# Workshop Plan and Feedback Gather (education related), Feedback Gather depends on Workshop Plan finishing
edu_PO = StrictPartialOrder(nodes=[Workshop_Plan, Feedback_Gather])
edu_PO.order.add_edge(Workshop_Plan, Feedback_Gather)

# Now assemble partial orders reflecting their logical connections:

# After Hive Setup, Reg Review starts, which then leads to audit then pollination mapping + data logging in parallel
post_setup_PO = StrictPartialOrder(
    nodes=[reg_review_PO, audit_to_pollination_PO, data_and_pollination_PO]
)
post_setup_PO.order.add_edge(reg_review_PO, audit_to_pollination_PO)
post_setup_PO.order.add_edge(audit_to_pollination_PO, data_and_pollination_PO)

# Combine the higher level phases concurrently: 
# (setup_PO) --> (post_setup_PO) --> concurrent activities: 
#   hive_monitor_loop, community_PO, supp_waste_PO, edu_PO

# But hive monitor loop and community and supplies etc can start after hive setup and basic regulatory steps
level1_PO = StrictPartialOrder(
    nodes=[setup_PO, post_setup_PO]
)
level1_PO.order.add_edge(setup_PO, post_setup_PO)

# Concurrent at next level
concurrent_activities = StrictPartialOrder(
    nodes=[hive_monitor_loop, community_PO, supp_waste_PO, edu_PO]
)
# concurrent no order edges among them

# Final root partial order combining all
#level1_PO --> concurrent activities (all start after level1_PO)
root = StrictPartialOrder(
    nodes=[level1_PO, concurrent_activities]
)
root.order.add_edge(level1_PO, concurrent_activities)