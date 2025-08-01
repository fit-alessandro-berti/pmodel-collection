# Generated from: 44df5368-6ead-49d4-bc26-ed5ea41b14ae.json
# Description: This process outlines the establishment of a fully automated urban vertical farming facility integrating IoT sensors, AI-driven climate control, and hydroponic systems. Activities include site selection based on solar exposure and urban zoning laws, modular rack installation, nutrient solution formulation, AI model training for crop yield prediction, pest control via biocontrol agents, continuous environmental monitoring, adaptive lighting scheduling, and integration with local distribution networks. The process also incorporates community engagement programs and sustainability reporting to ensure minimal environmental impact and maximum social benefit. This atypical yet realistic process blends agriculture, technology, and urban planning to create efficient food production in dense city environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
zoning_check = Transition(label='Zoning Check')
rack_setup = Transition(label='Rack Setup')
sensor_install = Transition(label='Sensor Install')
solution_mix = Transition(label='Solution Mix')
ai_training = Transition(label='AI Training')
pest_control = Transition(label='Pest Control')
env_monitor = Transition(label='Env Monitor')
lighting_plan = Transition(label='Lighting Plan')
water_recirc = Transition(label='Water Recirc')
yield_assess = Transition(label='Yield Assess')
data_sync = Transition(label='Data Sync')
network_link = Transition(label='Network Link')
community_meet = Transition(label='Community Meet')
sustain_report = Transition(label='Sustain Report')

# First phase: Site Survey and Zoning Check in parallel (independent)
# Then Rack Setup after both done (Rack Setup depends on both)
# Sensor Install depends on Rack Setup
# Solution Mix independent and can run concurrently with AI Training
# AI Training depends on Sensor Install
# Pest Control depends on AI Training
# Env Monitor depends on Sensor Install (runs concurrently with Pest Control)
# Lighting Plan depends on Env Monitor
# Water Recirc depends on Lighting Plan
# Yield Assess depends on Pest Control and Water Recirc
# Data Sync depends on Yield Assess
# Network Link depends on Data Sync
# Community Meet and Sustain Report independent after Network Link

# Build partial orders stepwise
# Phase 1 partial order: Site Survey and Zoning Check (parallel), then Rack Setup
phase1 = StrictPartialOrder(nodes=[site_survey, zoning_check, rack_setup])
phase1.order.add_edge(site_survey, rack_setup)
phase1.order.add_edge(zoning_check, rack_setup)

# Phase 2 partial order: Sensor Install after Rack Setup
phase2 = StrictPartialOrder(nodes=[sensor_install])
# Sensor Install depends on Rack Setup => add edge later in combined PO

# Phase 3 partial order: Solution Mix and AI Training
# Solution Mix independent, AI Training depends on Sensor Install
solution_ai = StrictPartialOrder(nodes=[solution_mix, ai_training])
# dependencies added later

# Pest Control after AI Training
pest = StrictPartialOrder(nodes=[pest_control])

# Env Monitor depends on Sensor Install (concurrent with Pest Control)
env = StrictPartialOrder(nodes=[env_monitor])

# Lighting Plan after Env Monitor
lighting = StrictPartialOrder(nodes=[lighting_plan])
# Edge added later

# Water Recirc after Lighting Plan
water = StrictPartialOrder(nodes=[water_recirc])
# Edge added later

# Yield Assess depends on Pest Control and Water Recirc
yield_assess_po = StrictPartialOrder(nodes=[yield_assess])
# Edges added later

# Data Sync after Yield Assess
data_sync_po = StrictPartialOrder(nodes=[data_sync])
# Edge added later

# Network Link after Data Sync
network_link_po = StrictPartialOrder(nodes=[network_link])
# Edge added later

# Final community and sustain reports (parallel)
community_sustain = StrictPartialOrder(nodes=[community_meet, sustain_report])
# Edge from Network Link to both

# Combine all nodes
nodes = [
    site_survey, zoning_check, rack_setup, sensor_install, solution_mix, ai_training,
    pest_control, env_monitor, lighting_plan, water_recirc, yield_assess,
    data_sync, network_link, community_meet, sustain_report
]

root = StrictPartialOrder(nodes=nodes)

# Add edges as per dependencies

# Phase 1
root.order.add_edge(site_survey, rack_setup)
root.order.add_edge(zoning_check, rack_setup)

# Phase 2
root.order.add_edge(rack_setup, sensor_install)

# Phase 3
# AI Training depends on Sensor Install
root.order.add_edge(sensor_install, ai_training)
# Solution Mix independent (no edges)

# Pest Control after AI Training
root.order.add_edge(ai_training, pest_control)

# Env Monitor after Sensor Install (runs concurrently with Pest Control)
root.order.add_edge(sensor_install, env_monitor)

# Lighting Plan after Env Monitor
root.order.add_edge(env_monitor, lighting_plan)

# Water Recirc after Lighting Plan
root.order.add_edge(lighting_plan, water_recirc)

# Yield Assess after Pest Control and Water Recirc
root.order.add_edge(pest_control, yield_assess)
root.order.add_edge(water_recirc, yield_assess)

# Data Sync after Yield Assess
root.order.add_edge(yield_assess, data_sync)

# Network Link after Data Sync
root.order.add_edge(data_sync, network_link)

# Community Meet and Sustain Report after Network Link (both in parallel)
root.order.add_edge(network_link, community_meet)
root.order.add_edge(network_link, sustain_report)