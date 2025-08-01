# Generated from: 5c15a05b-6d22-48da-8b74-9ec3c265b675.json
# Description: This process outlines the establishment of a fully automated urban vertical farm within a repurposed industrial building. It involves initial site analysis, environmental impact assessments, integration of IoT sensors for microclimate control, modular hydroponic rack installation, nutrient solution calibration, AI-driven crop scheduling, automated seeding and harvesting, waste recycling loops, and sustainability reporting. The procedure ensures optimized space utilization, energy efficiency, and maximized crop yield while adhering to local regulations and community engagement protocols, making it a complex yet innovative approach to urban agriculture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site        = Transition(label='Site Survey')
impact      = Transition(label='Impact Study')
iot         = Transition(label='IoT Setup')
rack        = Transition(label='Rack Install')
nutrient    = Transition(label='Nutrient Mix')
schedule    = Transition(label='Crop Schedule')
seed        = Transition(label='Seed Automation')
harvest     = Transition(label='Harvest Cycle')
waste       = Transition(label='Waste Process')
audit       = Transition(label='Energy Audit')
sync        = Transition(label='Data Sync')
quality     = Transition(label='Quality Check')
regulation  = Transition(label='Regulation Review')
community   = Transition(label='Community Meet')
report      = Transition(label='Report Generate')

# Build the repeat‐loop for the core cultivation cycle:
#   A = Crop Schedule
#   B = (Seed Automation -> Harvest Cycle -> Waste Process)
cycle_body = StrictPartialOrder(nodes=[seed, harvest, waste])
cycle_body.order.add_edge(seed, harvest)
cycle_body.order.add_edge(harvest, waste)

loop = OperatorPOWL(operator=Operator.LOOP, children=[schedule, cycle_body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site, impact, iot, rack,
    regulation, community,
    nutrient, loop,
    audit, sync, quality,
    report
])

# Initial linear setup
root.order.add_edge(site, impact)
root.order.add_edge(impact, iot)
root.order.add_edge(iot, rack)

# Concurrent compliance and community steps after rack install
root.order.add_edge(rack, regulation)
root.order.add_edge(rack, community)

# Both regulation review and community meeting must complete before nutrient mix
root.order.add_edge(regulation, nutrient)
root.order.add_edge(community, nutrient)

# Nutrient mix precedes the cultivation loop
root.order.add_edge(nutrient, loop)

# After exiting the loop, perform audit, sync, quality check and generate report
root.order.add_edge(loop, audit)
root.order.add_edge(audit, sync)
root.order.add_edge(sync, quality)
root.order.add_edge(quality, report)