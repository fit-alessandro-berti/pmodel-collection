# Generated from: 930f55c3-dace-4443-a44e-8c50138b1cdd.json
# Description: This process outlines the complex and multidisciplinary steps involved in establishing an urban vertical farm within a densely populated city environment. It covers site analysis, structural integration into existing buildings, advanced hydroponic system design, automated climate control setup, energy optimization using renewable sources, crop selection based on urban demand, regulatory compliance for food safety, waste recycling methods, and distribution logistics tailored for limited urban space. The process requires coordination of architecture, agriculture, technology, and supply chain domains to create a sustainable, high-yield vertical farming operation that minimizes environmental impact while maximizing fresh produce availability in urban centers.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
structural_design = Transition(label='Structural Design')
hydro_setup = Transition(label='Hydro Setup')
climate_control = Transition(label='Climate Control')
energy_audit = Transition(label='Energy Audit')
crop_selection = Transition(label='Crop Selection')
seed_sowing = Transition(label='Seed Sowing')
nutrient_mix = Transition(label='Nutrient Mix')
lighting_setup = Transition(label='Lighting Setup')
pest_control = Transition(label='Pest Control')
waste_recycle = Transition(label='Waste Recycle')
quality_check = Transition(label='Quality Check')
compliance_review = Transition(label='Compliance Review')
harvest_plan = Transition(label='Harvest Plan')
distribution = Transition(label='Distribution')

# Architectural and structural setup partial order
arch_partial = StrictPartialOrder(nodes=[site_survey, structural_design, hydro_setup])
arch_partial.order.add_edge(site_survey, structural_design)
arch_partial.order.add_edge(structural_design, hydro_setup)

# Technology systems partial order: climate, energy, lighting, nutrient, pest
tech_nodes = [climate_control, energy_audit, lighting_setup, nutrient_mix, pest_control]
tech_partial = StrictPartialOrder(nodes=tech_nodes)
# No explicit ordering among them, so all concurrent

# Agriculture partial order: crop selection -> seed sowing
agri_partial = StrictPartialOrder(nodes=[crop_selection, seed_sowing])
agri_partial.order.add_edge(crop_selection, seed_sowing)

# Waste recycle and quality checks partial order: waste recycle, quality check, compliance review
waste_quality = StrictPartialOrder(nodes=[waste_recycle, quality_check, compliance_review])
# Quality Check and Compliance Review depend on waste recycle (waste recycled first)
waste_quality.order.add_edge(waste_recycle, quality_check)
waste_quality.order.add_edge(waste_recycle, compliance_review)

# Harvest and distribution partial order
harvest_dist = StrictPartialOrder(nodes=[harvest_plan, distribution])
harvest_dist.order.add_edge(harvest_plan, distribution)

# Combine all major groups in partial order

# First, combine arch_partial and tech_partial: tech after hydro setup
arch_tech = StrictPartialOrder(nodes=[arch_partial, tech_partial])
arch_tech.order.add_edge(arch_partial, tech_partial)
# However, arch_partial and tech_partial are StrictPartialOrder objects themselves.
# But nodes in StrictPartialOrder are supposed to be transitions or OperatorPOWL,
# not other StrictPartialOrders. So we need to flatten the nodes.

# Flatten nodes for all and construct one StrictPartialOrder for the root

# We'll combine all nodes at root level:
# Nodes: all individual transitions plus no nesting of StrictPartialOrders
all_nodes = [
    site_survey, structural_design, hydro_setup,
    climate_control, energy_audit, lighting_setup, nutrient_mix, pest_control,
    crop_selection, seed_sowing,
    waste_recycle, quality_check, compliance_review,
    harvest_plan, distribution,
]

root = StrictPartialOrder(nodes=all_nodes)

# Add order edges according to described partial orders:

# Architecture and structure
root.order.add_edge(site_survey, structural_design)
root.order.add_edge(structural_design, hydro_setup)

# Tech system all concurrent, but they start after hydro_setup
root.order.add_edge(hydro_setup, climate_control)
root.order.add_edge(hydro_setup, energy_audit)
root.order.add_edge(hydro_setup, lighting_setup)
root.order.add_edge(hydro_setup, nutrient_mix)
root.order.add_edge(hydro_setup, pest_control)

# Agriculture after tech systems complete: crop selection after all tech nodes.
# For concurrency, we approximate by adding edges from each tech node to crop selection.
root.order.add_edge(climate_control, crop_selection)
root.order.add_edge(energy_audit, crop_selection)
root.order.add_edge(lighting_setup, crop_selection)
root.order.add_edge(nutrient_mix, crop_selection)
root.order.add_edge(pest_control, crop_selection)

root.order.add_edge(crop_selection, seed_sowing)

# Waste recycle and quality checks after agriculture seed sowing
root.order.add_edge(seed_sowing, waste_recycle)

# Quality check and compliance review after waste recycle
root.order.add_edge(waste_recycle, quality_check)
root.order.add_edge(waste_recycle, compliance_review)

# Harvest plan can only start after quality check and compliance review
root.order.add_edge(quality_check, harvest_plan)
root.order.add_edge(compliance_review, harvest_plan)

# Distribution after harvest plan
root.order.add_edge(harvest_plan, distribution)