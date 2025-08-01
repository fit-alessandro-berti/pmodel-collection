# Generated from: da034b24-c3d4-43e2-bc72-8817c673186f.json
# Description: This process describes the complex coordination required to establish and maintain an urban beekeeping network across multiple city locations. It involves site assessments for hive placement, regulatory compliance checks, community engagement activities, hive monitoring, honey harvesting coordination, pest control scheduling, data logging for environmental impact, educational workshops planning, supply chain management for beekeeping materials, and collaboration with local agricultural authorities. The process ensures sustainable urban apiaries while promoting biodiversity and urban agriculture education, balancing ecological concerns with city regulations and public safety.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey     = Transition(label='Site Survey')
permit_check    = Transition(label='Permit Check')
hive_setup      = Transition(label='Hive Setup')
community_meet  = Transition(label='Community Meet')
workshop_plan   = Transition(label='Workshop Plan')
volunteer_coord = Transition(label='Volunteer Coord')
hive_monitor    = Transition(label='Hive Monitor')
pest_control    = Transition(label='Pest Control')
honey_harvest   = Transition(label='Honey Harvest')
data_logging    = Transition(label='Data Logging')
waste_manage    = Transition(label='Waste Manage')
feedback_gather = Transition(label='Feedback Gather')
supply_order    = Transition(label='Supply Order')
reg_review      = Transition(label='Regulation Review')
poll_map        = Transition(label='Pollination Map')
apiary_audit    = Transition(label='Apiary Audit')

# Silent transition to be used in the loop construct
skip = SilentTransition()

# Define the maintenance cycle as a partial order:
#   Hive Monitor -> Data Logging -> {Pest Control, Honey Harvest} -> Waste Manage -> Feedback Gather -> Supply Order
maintain_cycle = StrictPartialOrder(nodes=[
    hive_monitor, data_logging,
    pest_control, honey_harvest,
    waste_manage, feedback_gather,
    supply_order
])
maintain_cycle.order.add_edge(hive_monitor, data_logging)
maintain_cycle.order.add_edge(data_logging, pest_control)
maintain_cycle.order.add_edge(data_logging, honey_harvest)
maintain_cycle.order.add_edge(pest_control, waste_manage)
maintain_cycle.order.add_edge(honey_harvest, waste_manage)
maintain_cycle.order.add_edge(waste_manage, feedback_gather)
maintain_cycle.order.add_edge(feedback_gather, supply_order)

# Wrap the maintenance cycle in a LOOP: repeat the cycle until exit
maintenance_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[maintain_cycle, skip]
)

# Build the root partial order:
# 1) Site setup sequence: Site Survey -> Permit Check -> Hive Setup -> Community Meet -> Workshop Plan -> Volunteer Coord
# 2) After Hive Setup, start in parallel:
#    - the maintenance loop
#    - regulatory review
#    - pollination mapping
#    - apiary auditing
root = StrictPartialOrder(nodes=[
    site_survey, permit_check, hive_setup,
    community_meet, workshop_plan, volunteer_coord,
    maintenance_loop,
    reg_review, poll_map, apiary_audit
])

# Ordering dependencies for the initial setup and community branch
root.order.add_edge(site_survey, permit_check)
root.order.add_edge(permit_check, hive_setup)
root.order.add_edge(hive_setup, community_meet)
root.order.add_edge(community_meet, workshop_plan)
root.order.add_edge(workshop_plan, volunteer_coord)

# After hive is set up, all maintenance and periodic tasks may start concurrently
root.order.add_edge(hive_setup, maintenance_loop)
root.order.add_edge(hive_setup, reg_review)
root.order.add_edge(hive_setup, poll_map)
root.order.add_edge(hive_setup, apiary_audit)