# Generated from: 1f38da92-320b-49c2-9a4d-1b7c5ba7e5f2.json
# Description: This process outlines the complex steps involved in managing an urban beekeeping operation within a densely populated city environment. It begins with hive site scouting and regulatory compliance, followed by hive installation and colony acclimation. Regular health inspections and disease monitoring are performed to ensure colony vitality. Seasonal nectar flow assessments guide supplemental feeding schedules. Honey extraction involves specialized urban-safe methods to minimize disruption. Post-harvest, honey is filtered, quality tested, and packaged in eco-friendly materials. Community outreach and educational workshops promote urban pollination awareness. Finally, data logging and hive performance analysis support continuous improvement and sustainable urban apiary management.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Activities as transitions
site_scouting = Transition(label='Site Scouting')
permit_check = Transition(label='Permit Check')
hive_setup = Transition(label='Hive Setup')
colony_acclimate = Transition(label='Colony Acclimate')

health_inspect = Transition(label='Health Inspect')
disease_screen = Transition(label='Disease Screen')

nectar_assess = Transition(label='Nectar Assess')
feed_schedule = Transition(label='Feed Schedule')

honey_extract = Transition(label='Honey Extract')
honey_filter = Transition(label='Honey Filter')
quality_test = Transition(label='Quality Test')
eco_package = Transition(label='Eco Package')

community_talk = Transition(label='Community Talk')

data_log = Transition(label='Data Log')
performance_review = Transition(label='Performance Review')

waste_manage = Transition(label='Waste Manage')

# Partial Order 1: preliminary setup
prelim = StrictPartialOrder(nodes=[site_scouting, permit_check])
prelim.order.add_edge(site_scouting, permit_check)

# Partial Order 2: hive installation/acclimation (sequential)
hive_stage = StrictPartialOrder(nodes=[hive_setup, colony_acclimate])
hive_stage.order.add_edge(hive_setup, colony_acclimate)

# Partial Order 3: health inspections and disease screening (concurrent)
health_stage = StrictPartialOrder(nodes=[health_inspect, disease_screen])
# no order edges, concurrent

# Partial Order 4: nectar assess and feeding schedule (sequential)
feed_stage = StrictPartialOrder(nodes=[nectar_assess, feed_schedule])
feed_stage.order.add_edge(nectar_assess, feed_schedule)

# Partial Order 5: honey processing sequence
honey_proc = StrictPartialOrder(
    nodes=[honey_extract, honey_filter, quality_test, eco_package]
)
honey_proc.order.add_edge(honey_extract, honey_filter)
honey_proc.order.add_edge(honey_filter, quality_test)
honey_proc.order.add_edge(quality_test, eco_package)

# Community outreach - single activity
community = StrictPartialOrder(nodes=[community_talk])

# Data log and performance review sequence
analysis = StrictPartialOrder(nodes=[data_log, performance_review])
analysis.order.add_edge(data_log, performance_review)

# Waste management (last)
waste = StrictPartialOrder(nodes=[waste_manage])

# Compose into a partial order following the described flow:
# prelim --> hive_stage --> health_stage --> feed_stage --> honey_proc --> community --> analysis --> waste

root = StrictPartialOrder(
    nodes=[
        prelim, hive_stage, health_stage, feed_stage, honey_proc, community, analysis, waste
    ]
)
root.order.add_edge(prelim, hive_stage)
root.order.add_edge(hive_stage, health_stage)
root.order.add_edge(health_stage, feed_stage)
root.order.add_edge(feed_stage, honey_proc)
root.order.add_edge(honey_proc, community)
root.order.add_edge(community, analysis)
root.order.add_edge(analysis, waste)