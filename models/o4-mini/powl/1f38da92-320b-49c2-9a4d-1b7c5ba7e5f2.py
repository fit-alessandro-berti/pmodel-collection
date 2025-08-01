# Generated from: 1f38da92-320b-49c2-9a4d-1b7c5ba7e5f2.json
# Description: This process outlines the complex steps involved in managing an urban beekeeping operation within a densely populated city environment. It begins with hive site scouting and regulatory compliance, followed by hive installation and colony acclimation. Regular health inspections and disease monitoring are performed to ensure colony vitality. Seasonal nectar flow assessments guide supplemental feeding schedules. Honey extraction involves specialized urban-safe methods to minimize disruption. Post-harvest, honey is filtered, quality tested, and packaged in eco-friendly materials. Community outreach and educational workshops promote urban pollination awareness. Finally, data logging and hive performance analysis support continuous improvement and sustainable urban apiary management.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Atomic activities
site = Transition(label='Site Scouting')
permit = Transition(label='Permit Check')
hive_setup = Transition(label='Hive Setup')
colony = Transition(label='Colony Acclimate')
health_inspect = Transition(label='Health Inspect')
disease_screen = Transition(label='Disease Screen')
nectar_assess = Transition(label='Nectar Assess')
feed_schedule = Transition(label='Feed Schedule')
honey_extract = Transition(label='Honey Extract')
honey_filter = Transition(label='Honey Filter')
quality_test = Transition(label='Quality Test')
eco_package = Transition(label='Eco Package')
waste_manage = Transition(label='Waste Manage')
community_talk = Transition(label='Community Talk')
data_log = Transition(label='Data Log')
performance_review = Transition(label='Performance Review')

# Loop for regular health inspections and disease monitoring
# First perform Health Inspect -> Disease Screen, then optionally repeat
inspection_seq = StrictPartialOrder(nodes=[health_inspect, disease_screen])
inspection_seq.order.add_edge(health_inspect, disease_screen)
skip = SilentTransition()
inspection_loop = OperatorPOWL(operator=Operator.LOOP, children=[inspection_seq, skip])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site, permit, hive_setup, colony,
    inspection_loop,
    nectar_assess, feed_schedule,
    honey_extract, honey_filter, quality_test,
    eco_package, waste_manage,
    community_talk, data_log, performance_review
])

# Define the control-flow order
root.order.add_edge(site, permit)
root.order.add_edge(permit, hive_setup)
root.order.add_edge(hive_setup, colony)
root.order.add_edge(colony, inspection_loop)
root.order.add_edge(inspection_loop, nectar_assess)
root.order.add_edge(nectar_assess, feed_schedule)
root.order.add_edge(feed_schedule, honey_extract)
root.order.add_edge(honey_extract, honey_filter)
root.order.add_edge(honey_filter, quality_test)
root.order.add_edge(quality_test, eco_package)
root.order.add_edge(eco_package, waste_manage)
root.order.add_edge(waste_manage, community_talk)
root.order.add_edge(community_talk, data_log)
root.order.add_edge(data_log, performance_review)