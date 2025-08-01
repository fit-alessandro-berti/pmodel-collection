# Generated from: 2d3301d6-889c-43f6-839d-0eec2b0c5b95.json
# Description: This process describes the complex and multifaceted steps involved in establishing an urban vertical farm in a densely populated city. It begins with site analysis and zoning approval, followed by modular structure design and climate system integration. The process continues with nutrient solution preparation, automated seeding, and lighting calibration. Maintenance routines include pest monitoring and system diagnostics, while data analytics optimize growth cycles. Finally, the harvest scheduling and distribution logistics ensure fresh produce delivery within tight urban supply chains, balancing sustainability with commercial viability in constrained spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the activities
site_analysis      = Transition(label='Site Analysis')
zoning_review      = Transition(label='Zoning Review')
modular_design     = Transition(label='Modular Design')
climate_setup      = Transition(label='Climate Setup')
nutrient_mix       = Transition(label='Nutrient Mix')
seed_automation    = Transition(label='Seed Automation')
lighting_calibrate = Transition(label='Lighting Calibrate')
pest_monitor       = Transition(label='Pest Monitor')
system_diagnostics = Transition(label='System Diagnostics')
growth_analytics   = Transition(label='Growth Analytics')
harvest_schedule   = Transition(label='Harvest Schedule')
supply_logistics   = Transition(label='Supply Logistics')
waste_recycling    = Transition(label='Waste Recycling')
energy_audit       = Transition(label='Energy Audit')
quality_testing    = Transition(label='Quality Testing')

# Build the strict partial order
root = StrictPartialOrder(nodes=[
    site_analysis, zoning_review, modular_design, climate_setup,
    nutrient_mix, seed_automation, lighting_calibrate,
    pest_monitor, system_diagnostics, growth_analytics,
    harvest_schedule, supply_logistics,
    waste_recycling, energy_audit, quality_testing
])

# Define the sequential flow up to maintenance & analytics
root.order.add_edge(site_analysis, zoning_review)
root.order.add_edge(zoning_review, modular_design)
root.order.add_edge(modular_design, climate_setup)
root.order.add_edge(climate_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, seed_automation)
root.order.add_edge(seed_automation, lighting_calibrate)

# Maintenance routines (pest monitor → system diagnostics → growth analytics)
root.order.add_edge(lighting_calibrate, pest_monitor)
root.order.add_edge(pest_monitor, system_diagnostics)
root.order.add_edge(system_diagnostics, growth_analytics)

# Harvest and distribution
root.order.add_edge(growth_analytics, harvest_schedule)
root.order.add_edge(harvest_schedule, supply_logistics)

# After supply, two concurrent tasks: waste recycling & energy audit
root.order.add_edge(supply_logistics, waste_recycling)
root.order.add_edge(supply_logistics, energy_audit)

# Quality testing after both recycling and audit
root.order.add_edge(waste_recycling, quality_testing)
root.order.add_edge(energy_audit,    quality_testing)