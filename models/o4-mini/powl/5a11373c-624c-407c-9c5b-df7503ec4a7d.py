# Generated from: 5a11373c-624c-407c-9c5b-df7503ec4a7d.json
# Description: This complex urban beekeeping process involves site evaluation, hive preparation, and colony acquisition tailored to city environments. It includes environmental monitoring, pollen mapping, and urban pest management to ensure colony health. Regular hive inspections, honey extraction, and quality testing follow, alongside community engagement through workshops and local market distribution. The workflow integrates data logging and seasonal adaptation strategies to optimize yield and sustainability in densely populated areas, addressing unique challenges like pollution and limited forage availability while promoting urban biodiversity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define basic transitions
site = Transition(label='Site Survey')
setup = Transition(label='Hive Setup')
purchase = Transition(label='Colony Purchase')

poll_map = Transition(label='Pollination Map')
pest = Transition(label='Pest Control')
env = Transition(label='Enviro Monitor')
forage = Transition(label='Forage Scout')
health = Transition(label='Bee Health')

inspect = Transition(label='Hive Inspect')
extract = Transition(label='Honey Extract')
test = Transition(label='Quality Test')
log = Transition(label='Data Logging')
season_adjust = Transition(label='Season Adjust')

workshop = Transition(label='Workshop Host')
engage = Transition(label='Community Engage')
market = Transition(label='Market Deliver')

# Monitoring phase (concurrent)
monitoring = StrictPartialOrder(nodes=[poll_map, pest, env, forage, health])

# Inspection loop body (sequential)
body = StrictPartialOrder(nodes=[inspect, extract, test, log])
body.order.add_edge(inspect, extract)
body.order.add_edge(extract, test)
body.order.add_edge(test, log)

# Loop: regular inspections & seasonal adjustment
loop = OperatorPOWL(operator=Operator.LOOP, children=[body, season_adjust])

# Community engagement phase (sequential)
community = StrictPartialOrder(nodes=[workshop, engage, market])
community.order.add_edge(workshop, engage)
community.order.add_edge(engage, market)

# Root partial order
root = StrictPartialOrder(nodes=[site, setup, purchase, monitoring, loop, community])
root.order.add_edge(site, setup)
root.order.add_edge(setup, purchase)
root.order.add_edge(purchase, monitoring)
root.order.add_edge(monitoring, loop)
root.order.add_edge(loop, community)