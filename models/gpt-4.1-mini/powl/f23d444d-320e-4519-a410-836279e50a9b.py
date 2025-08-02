# Generated from: f23d444d-320e-4519-a410-836279e50a9b.json
# Description: This process outlines the complex and atypical steps involved in establishing an urban vertical farm within a densely populated city environment. It covers site evaluation, modular system design, nutrient cycling optimization, automated environmental control integration, multi-layer crop scheduling, waste repurposing, and community engagement strategies to ensure sustainability and scalability. The process also includes adaptive pest management protocols, real-time data analytics deployment for yield prediction, and compliance with urban agricultural regulations, making it a multifaceted approach to innovative food production in constrained urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey = Transition(label='Site Survey')
system_design = Transition(label='System Design')
module_build = Transition(label='Module Build')
nutrient_mix = Transition(label='Nutrient Mix')
seed_selection = Transition(label='Seed Selection')
planting_plan = Transition(label='Planting Plan')
irrigation_setup = Transition(label='Irrigation Setup')
climate_control = Transition(label='Climate Control')
lighting_adjust = Transition(label='Lighting Adjust')
pest_monitor = Transition(label='Pest Monitor')
waste_cycle = Transition(label='Waste Cycle')
data_capture = Transition(label='Data Capture')
yield_forecast = Transition(label='Yield Forecast')
regulation_check = Transition(label='Regulation Check')
community_meet = Transition(label='Community Meet')
harvest_prep = Transition(label='Harvest Prep')
market_link = Transition(label='Market Link')

# Build loops for Pest Monitor (adaptive pest management)
# loop: execute pest_monitor, then choose exit or loop more
pest_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_monitor, SilentTransition()])

# Set real-time data analytics deployment: after data_capture -> yield_forecast (forecast depends on data)
data_forecast_po = StrictPartialOrder(nodes=[data_capture, yield_forecast])
data_forecast_po.order.add_edge(data_capture, yield_forecast)

# Build choice for community engagement or regulation check (both optional, run one or the other or none)
community_or_regulation = OperatorPOWL(operator=Operator.XOR, children=[community_meet, regulation_check, SilentTransition()])

# Assemble the root partial order reflecting main process flow:

# Phase 1: Site survey and system design to module build
phase1 = StrictPartialOrder(nodes=[site_survey, system_design, module_build])
phase1.order.add_edge(site_survey, system_design)
phase1.order.add_edge(system_design, module_build)

# Phase 2: Nutrient mix and planting plan can be concurrent after module build
# And irrigation setup, climate control, lighting adjust are concurrent as well, all after module build
phase2 = StrictPartialOrder(nodes=[nutrient_mix, seed_selection, planting_plan,
                                  irrigation_setup, climate_control, lighting_adjust])
# define no order edges: everything concurrent

# Phase 3: Pest monitor loop and waste cycle concurrent
# Pest monitor loop defined above, waste_cycle separate
phase3 = StrictPartialOrder(nodes=[pest_monitor_loop, waste_cycle])

# Phase 4: Data capture and yield forecast done sequentially (already grouped above in data_forecast_po)

# Phase 5: Harvest prep and market link sequential
harvest_market = StrictPartialOrder(nodes=[harvest_prep, market_link])
harvest_market.order.add_edge(harvest_prep, market_link)

# Combine phases partial orders with proper order edges to reflect flow

root = StrictPartialOrder(nodes=[phase1, phase2, phase3, data_forecast_po, community_or_regulation, harvest_market])

# Define order edges between major phases:

# phase1 --> phase2 (after module build complete)
root.order.add_edge(phase1, phase2)

# phase2 --> phase3 (after planting and setups)
root.order.add_edge(phase2, phase3)

# phase3 --> data_forecast_po (waste cycle and pest monitoring -> data capture)
root.order.add_edge(phase3, data_forecast_po)

# data_forecast_po --> community_or_regulation (yield forecast leads to engagement/regulation steps)
root.order.add_edge(data_forecast_po, community_or_regulation)

# community_or_regulation --> harvest_market (lastly harvest and market)
root.order.add_edge(community_or_regulation, harvest_market)