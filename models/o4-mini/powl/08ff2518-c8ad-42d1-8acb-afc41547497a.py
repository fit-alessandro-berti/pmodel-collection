# Generated from: 08ff2518-c8ad-42d1-8acb-afc41547497a.json
# Description: This process outlines the intricate steps involved in establishing an urban vertical farm within a densely populated city environment. It includes site analysis, regulatory compliance, modular system design, climate control calibration, nutrient cycling optimization, and community integration. The process requires coordination among agronomists, engineers, local authorities, and marketing teams to ensure sustainability, crop yield maximization, and economic viability while minimizing environmental impact in constrained urban spaces. It culminates in continuous monitoring and adaptive management to respond to urban challenges such as pollution, limited sunlight, and water reuse.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site       = Transition(label='Site Survey')
permit     = Transition(label='Permit Filing')
module     = Transition(label='Module Design')
sensor     = Transition(label='Sensor Setup')
climate    = Transition(label='Climate Adjust')
water      = Transition(label='Water Cycle')
nutrient   = Transition(label='Nutrient Prep')
seed       = Transition(label='Seed Sowing')
growth     = Transition(label='Growth Monitor')
pest       = Transition(label='Pest Control')
harvest    = Transition(label='Harvest Plan')
market     = Transition(label='Market Study')
community  = Transition(label='Community Meet')
waste      = Transition(label='Waste Reuse')
data       = Transition(label='Data Review')
audit      = Transition(label='Yield Audit')
feedback   = Transition(label='Feedback Loop')

# Build the loop body: after a growth monitoring iteration,
# perform pest control, data review, yield audit, waste reuse, then feedback
loop_body = StrictPartialOrder(nodes=[pest, data, audit, waste, feedback])
loop_body.order.add_edge(pest, data)
loop_body.order.add_edge(data, audit)
loop_body.order.add_edge(audit, waste)
loop_body.order.add_edge(waste, feedback)

# Define the monitoring & adaptive management loop:
# A = growth monitor, B = loop_body
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth, loop_body])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    site, permit, module, sensor, climate,
    water, nutrient,
    seed,
    market, community,
    harvest,
    monitor_loop
])

# Site analysis and permitting
root.order.add_edge(site, permit)
# Design and system setup
root.order.add_edge(permit, module)
root.order.add_edge(module, sensor)
root.order.add_edge(sensor, climate)
# Calibration feeds into water cycle & nutrient prep (concurrent)
root.order.add_edge(climate, water)
root.order.add_edge(climate, nutrient)
# Then seed sowing
root.order.add_edge(water, seed)
root.order.add_edge(nutrient, seed)
# Pre‐harvest studies (market & community in parallel), then planning
root.order.add_edge(seed, market)
root.order.add_edge(seed, community)
root.order.add_edge(market, harvest)
root.order.add_edge(community, harvest)
# Harvest plan precedes continuous monitoring loop
root.order.add_edge(harvest, monitor_loop)