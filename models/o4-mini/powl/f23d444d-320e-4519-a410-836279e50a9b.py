# Generated from: f23d444d-320e-4519-a410-836279e50a9b.json
# Description: This process outlines the complex and atypical steps involved in establishing an urban vertical farm within a densely populated city environment. It covers site evaluation, modular system design, nutrient cycling optimization, automated environmental control integration, multi-layer crop scheduling, waste repurposing, and community engagement strategies to ensure sustainability and scalability. The process also includes adaptive pest management protocols, real-time data analytics deployment for yield prediction, and compliance with urban agricultural regulations, making it a multifaceted approach to innovative food production in constrained urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activity transitions
site_survey    = Transition(label='Site Survey')
system_design  = Transition(label='System Design')
module_build   = Transition(label='Module Build')
nutrient_mix   = Transition(label='Nutrient Mix')
seed_selection = Transition(label='Seed Selection')
planting_plan  = Transition(label='Planting Plan')
irrigation     = Transition(label='Irrigation Setup')
climate_ctrl   = Transition(label='Climate Control')
lighting_adj   = Transition(label='Lighting Adjust')
pest_monitor   = Transition(label='Pest Monitor')
waste_cycle    = Transition(label='Waste Cycle')
data_capture   = Transition(label='Data Capture')
yield_forecast = Transition(label='Yield Forecast')
reg_check      = Transition(label='Regulation Check')
community_meet = Transition(label='Community Meet')
harvest_prep   = Transition(label='Harvest Prep')
market_link    = Transition(label='Market Link')

# Silent transition for optional regulation check
skip = SilentTransition()

# Exclusive choice: either perform regulation check or skip
regulation_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[reg_check, skip]
)

# Loop body A: pest monitoring, data capture, forecasting, then optional regulation check
loop_body = StrictPartialOrder(
    nodes=[pest_monitor, data_capture, yield_forecast, regulation_choice]
)
loop_body.order.add_edge(pest_monitor, data_capture)
loop_body.order.add_edge(data_capture, yield_forecast)
loop_body.order.add_edge(yield_forecast, regulation_choice)

# B part of the loop: waste repurposing
loop_node = OperatorPOWL(
    operator=Operator.LOOP,
    children=[loop_body, waste_cycle]
)

# Build the top‐level partial order
root = StrictPartialOrder(
    nodes=[
        site_survey,
        system_design,
        module_build,
        nutrient_mix,
        seed_selection,
        planting_plan,
        irrigation,
        climate_ctrl,
        lighting_adj,
        loop_node,
        community_meet,
        harvest_prep,
        market_link
    ]
)

# Sequence: site survey → system design → module build → nutrient mix → seed selection → planting plan
root.order.add_edge(site_survey,   system_design)
root.order.add_edge(system_design, module_build)
root.order.add_edge(module_build,  nutrient_mix)
root.order.add_edge(nutrient_mix,  seed_selection)
root.order.add_edge(seed_selection, planting_plan)

# From planting plan to environmental control setup (concurrent)
root.order.add_edge(planting_plan, irrigation)
root.order.add_edge(planting_plan, climate_ctrl)
root.order.add_edge(planting_plan, lighting_adj)

# After all controls are in place, start the monitoring‐repurposing loop
root.order.add_edge(irrigation,  loop_node)
root.order.add_edge(climate_ctrl, loop_node)
root.order.add_edge(lighting_adj, loop_node)

# After the loop, engage the community and proceed to harvest and market linkage
root.order.add_edge(loop_node,    community_meet)
root.order.add_edge(community_meet, harvest_prep)
root.order.add_edge(harvest_prep,  market_link)