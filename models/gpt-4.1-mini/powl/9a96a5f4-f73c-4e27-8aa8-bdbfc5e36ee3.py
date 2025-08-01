# Generated from: 9a96a5f4-f73c-4e27-8aa8-bdbfc5e36ee3.json
# Description: This process outlines the comprehensive steps involved in setting up an urban vertical farming system within a repurposed industrial building. It includes site evaluation, modular rack assembly, climate control integration, automated irrigation programming, nutrient solution formulation, crop selection based on local demand, seedling germination, pest monitoring using AI sensors, harvest scheduling, quality control, waste recycling, energy consumption optimization, distribution logistics planning, and continuous system feedback analysis to maximize yield and sustainability in an urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey = Transition(label='Site Survey')
rack_assembly = Transition(label='Rack Assembly')
climate_setup = Transition(label='Climate Setup')
irrigation_config = Transition(label='Irrigation Config')
nutrient_mix = Transition(label='Nutrient Mix')
crop_selection = Transition(label='Crop Selection')
seed_germination = Transition(label='Seed Germination')
pest_monitoring = Transition(label='Pest Monitoring')
harvest_plan = Transition(label='Harvest Plan')
quality_check = Transition(label='Quality Check')
waste_recycling = Transition(label='Waste Recycling')
energy_audit = Transition(label='Energy Audit')
logistics_plan = Transition(label='Logistics Plan')
data_analysis = Transition(label='Data Analysis')
system_feedback = Transition(label='System Feedback')

# Create partial order with dependencies describing the flow:
root = StrictPartialOrder(nodes=[
    site_survey,
    rack_assembly,
    climate_setup,
    irrigation_config,
    nutrient_mix,
    crop_selection,
    seed_germination,
    pest_monitoring,
    harvest_plan,
    quality_check,
    waste_recycling,
    energy_audit,
    logistics_plan,
    data_analysis,
    system_feedback
])

# Define the order according to natural process logic:

# Initial equipment and environment setup
root.order.add_edge(site_survey, rack_assembly)
root.order.add_edge(rack_assembly, climate_setup)
root.order.add_edge(climate_setup, irrigation_config)
root.order.add_edge(irrigation_config, nutrient_mix)

# Crop preparation depends on nutrient and irrigation
root.order.add_edge(nutrient_mix, crop_selection)

# Seed germination depends on crop selection
root.order.add_edge(crop_selection, seed_germination)

# Pest monitoring runs after seed germination
root.order.add_edge(seed_germination, pest_monitoring)

# Harvest planning depends on pest monitoring being active
root.order.add_edge(pest_monitoring, harvest_plan)

# Quality check happens after harvest planning
root.order.add_edge(harvest_plan, quality_check)

# Waste recycling and energy audit can run concurrently after quality check
root.order.add_edge(quality_check, waste_recycling)
root.order.add_edge(quality_check, energy_audit)

# Logistics planning depends on harvest plan and energy audit (assumed here after quality check)
root.order.add_edge(harvest_plan, logistics_plan)
root.order.add_edge(energy_audit, logistics_plan)

# Data analysis depends on logistics planning, waste recycling, energy audit (consolidation)
root.order.add_edge(logistics_plan, data_analysis)
root.order.add_edge(waste_recycling, data_analysis)
root.order.add_edge(energy_audit, data_analysis)

# System feedback closes the loop, after data analysis
root.order.add_edge(data_analysis, system_feedback)