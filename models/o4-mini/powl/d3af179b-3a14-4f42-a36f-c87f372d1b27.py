# Generated from: d3af179b-3a14-4f42-a36f-c87f372d1b27.json
# Description: This process outlines the establishment of a vertical farming operation within an urban environment, focusing on integrating sustainable agriculture with smart technology. It involves site analysis, modular unit design, climate control optimization, nutrient solution formulation, LED spectrum tuning, automated seeding, growth monitoring via IoT sensors, pest management using biological agents, data-driven yield prediction, energy consumption assessment, waste recycling systems, community engagement programs, regulatory compliance audits, and final crop distribution logistics. The workflow ensures maximized space efficiency and minimized environmental impact while delivering fresh produce locally.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define transitions for each activity
site_survey      = Transition(label='Site Survey')
design_modules   = Transition(label='Design Modules')
climate_setup    = Transition(label='Climate Setup')
nutrient_mix     = Transition(label='Nutrient Mix')
led_tuning       = Transition(label='LED Tuning')
seed_automation  = Transition(label='Seed Automation')
growth_monitor   = Transition(label='Growth Monitor')
pest_control     = Transition(label='Pest Control')
yield_forecast   = Transition(label='Yield Forecast')
energy_audit     = Transition(label='Energy Audit')
waste_system     = Transition(label='Waste System')
community_meet   = Transition(label='Community Meet')
compliance_check = Transition(label='Compliance Check')
crop_packing     = Transition(label='Crop Packing')
logistics_plan   = Transition(label='Logistics Plan')

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_modules,
    climate_setup,
    nutrient_mix,
    led_tuning,
    seed_automation,
    growth_monitor,
    pest_control,
    yield_forecast,
    energy_audit,
    waste_system,
    community_meet,
    compliance_check,
    crop_packing,
    logistics_plan
])

# Sequential setup up to seeding
root.order.add_edge(site_survey, design_modules)
root.order.add_edge(design_modules, climate_setup)
root.order.add_edge(climate_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, led_tuning)
root.order.add_edge(led_tuning, seed_automation)

# Concurrent growth-phase activities
root.order.add_edge(seed_automation, growth_monitor)
root.order.add_edge(seed_automation, pest_control)
root.order.add_edge(growth_monitor, yield_forecast)
root.order.add_edge(pest_control, yield_forecast)

# Parallel post-growth evaluations before packing
root.order.add_edge(yield_forecast, energy_audit)
root.order.add_edge(yield_forecast, waste_system)
root.order.add_edge(yield_forecast, community_meet)
root.order.add_edge(yield_forecast, compliance_check)

# Join into packing and final logistics
root.order.add_edge(energy_audit, crop_packing)
root.order.add_edge(waste_system, crop_packing)
root.order.add_edge(community_meet, crop_packing)
root.order.add_edge(compliance_check, crop_packing)
root.order.add_edge(crop_packing, logistics_plan)