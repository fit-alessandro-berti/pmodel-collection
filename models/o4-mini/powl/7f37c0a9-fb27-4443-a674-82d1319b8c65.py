# Generated from: 7f37c0a9-fb27-4443-a674-82d1319b8c65.json
# Description: This process details the comprehensive steps required to establish a sustainable urban rooftop farm on a commercial building. It involves initial site assessment, structural analysis, microclimate evaluation, soil-less media selection, modular bed construction, automated irrigation installation, crop selection based on local demand, integration of renewable energy sources, pest management planning, community engagement for education, regular monitoring of plant health, data-driven yield optimization, nutrient cycling strategies, waste composting, and final certification for organic produce sales. Each step ensures that the farm is both ecologically responsible and economically viable, blending advanced agritech with urban infrastructure constraints to create a robust urban agriculture solution.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the 15 activities as POWL transitions
site_assess        = Transition(label='Site Assess')
structure_test     = Transition(label='Structure Test')
climate_scan       = Transition(label='Climate Scan')
media_select       = Transition(label='Media Select')
bed_construct      = Transition(label='Bed Construct')
irrigation_setup   = Transition(label='Irrigation Setup')
crop_choose        = Transition(label='Crop Choose')
energy_integrate   = Transition(label='Energy Integrate')
pest_plan          = Transition(label='Pest Plan')
community_engage   = Transition(label='Community Engage')
health_monitor     = Transition(label='Health Monitor')
yield_optimize     = Transition(label='Yield Optimize')
nutrient_cycle     = Transition(label='Nutrient Cycle')
waste_compost      = Transition(label='Waste Compost')
organic_certify    = Transition(label='Organic Certify')

# Build a strict partial order with all activities in sequence
root = StrictPartialOrder(nodes=[
    site_assess,
    structure_test,
    climate_scan,
    media_select,
    bed_construct,
    irrigation_setup,
    crop_choose,
    energy_integrate,
    pest_plan,
    community_engage,
    health_monitor,
    yield_optimize,
    nutrient_cycle,
    waste_compost,
    organic_certify
])

# Add the ordering edges to enforce the described workflow sequence
root.order.add_edge(site_assess,      structure_test)
root.order.add_edge(structure_test,   climate_scan)
root.order.add_edge(climate_scan,     media_select)
root.order.add_edge(media_select,     bed_construct)
root.order.add_edge(bed_construct,    irrigation_setup)
root.order.add_edge(irrigation_setup, crop_choose)
root.order.add_edge(crop_choose,      energy_integrate)
root.order.add_edge(energy_integrate, pest_plan)
root.order.add_edge(pest_plan,        community_engage)
root.order.add_edge(community_engage, health_monitor)
root.order.add_edge(health_monitor,   yield_optimize)
root.order.add_edge(yield_optimize,   nutrient_cycle)
root.order.add_edge(nutrient_cycle,   waste_compost)
root.order.add_edge(waste_compost,    organic_certify)