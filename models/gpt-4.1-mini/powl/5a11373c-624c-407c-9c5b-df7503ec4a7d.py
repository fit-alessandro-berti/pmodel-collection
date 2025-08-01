# Generated from: 5a11373c-624c-407c-9c5b-df7503ec4a7d.json
# Description: This complex urban beekeeping process involves site evaluation, hive preparation, and colony acquisition tailored to city environments. It includes environmental monitoring, pollen mapping, and urban pest management to ensure colony health. Regular hive inspections, honey extraction, and quality testing follow, alongside community engagement through workshops and local market distribution. The workflow integrates data logging and seasonal adaptation strategies to optimize yield and sustainability in densely populated areas, addressing unique challenges like pollution and limited forage availability while promoting urban biodiversity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Survey = Transition(label='Site Survey')
Hive_Setup = Transition(label='Hive Setup')
Colony_Purchase = Transition(label='Colony Purchase')
Pollination_Map = Transition(label='Pollination Map')
Pest_Control = Transition(label='Pest Control')
Enviro_Monitor = Transition(label='Enviro Monitor')
Hive_Inspect = Transition(label='Hive Inspect')
Honey_Extract = Transition(label='Honey Extract')
Quality_Test = Transition(label='Quality Test')
Data_Logging = Transition(label='Data Logging')
Season_Adjust = Transition(label='Season Adjust')
Workshop_Host = Transition(label='Workshop Host')
Market_Deliver = Transition(label='Market Deliver')
Bee_Health = Transition(label='Bee Health')
Forage_Scout = Transition(label='Forage Scout')
Community_Engage = Transition(label='Community Engage')

# Pre-processing phase: site evaluation (Site Survey), hive preparation (Hive Setup), colony acquisition (Colony Purchase)
preparation = StrictPartialOrder(nodes=[Site_Survey, Hive_Setup, Colony_Purchase])
preparation.order.add_edge(Site_Survey, Hive_Setup)
preparation.order.add_edge(Hive_Setup, Colony_Purchase)

# Environmental monitoring block: Pollination Map, Pest Control, Enviro Monitor performed concurrently
environment_monitor = StrictPartialOrder(
    nodes=[Pollination_Map, Pest_Control, Enviro_Monitor]
)
# No order edges: they can happen concurrently

# Ensure colony health: Bee Health depends on Pest Control and Enviro Monitor
# Forage Scout and Bee Health happen after Pest Control and Enviro Monitor, with Forage Scout concurrent with Bee Health
health_check = StrictPartialOrder(nodes=[Pest_Control, Enviro_Monitor, Bee_Health, Forage_Scout])
health_check.order.add_edge(Pest_Control, Bee_Health)
health_check.order.add_edge(Enviro_Monitor, Bee_Health)
health_check.order.add_edge(Pest_Control, Forage_Scout)
health_check.order.add_edge(Enviro_Monitor, Forage_Scout)

# Hive inspection and honey extraction flow
inspection_and_harvest = StrictPartialOrder(nodes=[Hive_Inspect, Honey_Extract, Quality_Test])
inspection_and_harvest.order.add_edge(Hive_Inspect, Honey_Extract)
inspection_and_harvest.order.add_edge(Honey_Extract, Quality_Test)

# Data logging and season adjustment flow (season adaptation strategies), concurrent with inspections
data_and_season = StrictPartialOrder(nodes=[Data_Logging, Season_Adjust])
# No order edges, concurrent activities

# Community engagement: Workshop Host, Community Engage, Market Deliver
# Workshop Host and Community Engage concurrent and both before Market Deliver
community = StrictPartialOrder(nodes=[Workshop_Host, Community_Engage, Market_Deliver])
community.order.add_edge(Workshop_Host, Market_Deliver)
community.order.add_edge(Community_Engage, Market_Deliver)

# Integrate environment_monitor and health_check in sequence: first monitor environment, then health check dependent on that
env_and_health = StrictPartialOrder(nodes=[environment_monitor, health_check])
env_and_health.order.add_edge(environment_monitor, health_check)

# Integrate hive inspection/harvest and data/season concurrently
inspect_and_data = StrictPartialOrder(nodes=[inspection_and_harvest, data_and_season])
# No order edges: concurrent

# Overall final flow order
# preparation -> env_and_health -> inspect_and_data -> community
root = StrictPartialOrder(
    nodes=[preparation, env_and_health, inspect_and_data, community]
)
root.order.add_edge(preparation, env_and_health)
root.order.add_edge(env_and_health, inspect_and_data)
root.order.add_edge(inspect_and_data, community)