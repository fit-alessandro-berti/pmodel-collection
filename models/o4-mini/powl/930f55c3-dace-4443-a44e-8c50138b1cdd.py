# Generated from: 930f55c3-dace-4443-a44e-8c50138b1cdd.json
# Description: This process outlines the complex and multidisciplinary steps involved in establishing an urban vertical farm within a densely populated city environment. It covers site analysis, structural integration into existing buildings, advanced hydroponic system design, automated climate control setup, energy optimization using renewable sources, crop selection based on urban demand, regulatory compliance for food safety, waste recycling methods, and distribution logistics tailored for limited urban space. The process requires coordination of architecture, agriculture, technology, and supply chain domains to create a sustainable, high-yield vertical farming operation that minimizes environmental impact while maximizing fresh produce availability in urban centers.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_survey      = Transition(label='Site Survey')
structural_design= Transition(label='Structural Design')
hydro_setup      = Transition(label='Hydro Setup')
climate_control  = Transition(label='Climate Control')
lighting_setup   = Transition(label='Lighting Setup')
energy_audit     = Transition(label='Energy Audit')
crop_selection   = Transition(label='Crop Selection')
seed_sowing      = Transition(label='Seed Sowing')
nutrient_mix     = Transition(label='Nutrient Mix')
pest_control     = Transition(label='Pest Control')
waste_recycle    = Transition(label='Waste Recycle')
quality_check    = Transition(label='Quality Check')
compliance_review= Transition(label='Compliance Review')
harvest_plan     = Transition(label='Harvest Plan')
distribution     = Transition(label='Distribution')

# Create the partial order model
root = StrictPartialOrder(nodes=[
    site_survey, structural_design, hydro_setup,
    climate_control, lighting_setup, energy_audit,
    crop_selection, seed_sowing, nutrient_mix,
    pest_control, waste_recycle, quality_check,
    compliance_review, harvest_plan, distribution
])

# Add precedence relations
root.order.add_edge(site_survey,       structural_design)
root.order.add_edge(structural_design, hydro_setup)

# After hydro setup, three branches run in parallel
root.order.add_edge(hydro_setup, climate_control)
root.order.add_edge(hydro_setup, lighting_setup)
root.order.add_edge(hydro_setup, energy_audit)

# Crop selection needs all three environmental setups
root.order.add_edge(climate_control, crop_selection)
root.order.add_edge(lighting_setup,  crop_selection)
root.order.add_edge(energy_audit,    crop_selection)

# Seeding and initial treatments
root.order.add_edge(crop_selection, seed_sowing)
root.order.add_edge(seed_sowing,     nutrient_mix)
root.order.add_edge(seed_sowing,     pest_control)
root.order.add_edge(climate_control, pest_control)

# Waste recycling depends on both nutrient use and pest control
root.order.add_edge(nutrient_mix,  waste_recycle)
root.order.add_edge(pest_control,  waste_recycle)

# Quality check after all operational tasks
root.order.add_edge(nutrient_mix,  quality_check)
root.order.add_edge(pest_control,  quality_check)
root.order.add_edge(waste_recycle, quality_check)

# Final approvals and logistics
root.order.add_edge(quality_check,    compliance_review)
root.order.add_edge(compliance_review, harvest_plan)
root.order.add_edge(harvest_plan,     distribution)