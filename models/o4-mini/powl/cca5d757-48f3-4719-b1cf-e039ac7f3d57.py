# Generated from: cca5d757-48f3-4719-b1cf-e039ac7f3d57.json
# Description: This process outlines the complex and multifaceted approach to establishing a sustainable urban rooftop farm in a densely populated cityscape. It involves site assessment for structural integrity, microclimate analysis, soil-less medium preparation, modular bed installation, automated irrigation setup, crop selection based on seasonal and local demand, pest management using integrated natural methods, community engagement for educational workshops, digital monitoring system deployment, waste recycling integration, seasonal yield forecasting, and finally distribution channel establishment through local markets and restaurants. This atypical yet realistic process requires cross-disciplinary coordination between architects, agronomists, technologists, and community organizers to ensure a productive, eco-friendly, and economically viable rooftop farming venture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
site_assess     = Transition(label='Site Assess')
load_testing    = Transition(label='Load Testing')
climate_study   = Transition(label='Climate Study')
medium_prep     = Transition(label='Medium Prep')
bed_install     = Transition(label='Bed Install')
irrigation_setup= Transition(label='Irrigation Setup')
crop_select     = Transition(label='Crop Select')
pest_control    = Transition(label='Pest Control')
community_meet  = Transition(label='Community Meet')
workshop_plan   = Transition(label='Workshop Plan')
monitor_deploy  = Transition(label='Monitor Deploy')
tech_integrate  = Transition(label='Tech Integrate')
waste_cycle     = Transition(label='Waste Cycle')
yield_forecast  = Transition(label='Yield Forecast')
market_link     = Transition(label='Market Link')

# Create the partial‐order root model with all nodes
root = StrictPartialOrder(nodes=[
    site_assess, load_testing, climate_study, medium_prep, bed_install,
    irrigation_setup, crop_select, pest_control, community_meet,
    workshop_plan, monitor_deploy, tech_integrate, waste_cycle,
    yield_forecast, market_link
])

# Define control‐flow dependencies
# 1. Site assessment leads to structural load testing and climate study (in parallel)
root.order.add_edge(site_assess, load_testing)
root.order.add_edge(site_assess, climate_study)

# 2. Both load testing and climate study must complete before medium preparation
root.order.add_edge(load_testing, medium_prep)
root.order.add_edge(climate_study, medium_prep)

# 3. Sequential setup: medium prep → bed install → irrigation setup
root.order.add_edge(medium_prep, bed_install)
root.order.add_edge(bed_install, irrigation_setup)

# 4. Crop selection after irrigation setup, then pest control
root.order.add_edge(irrigation_setup, crop_select)
root.order.add_edge(crop_select, pest_control)

# 5. After pest control, two branches in parallel:
#    (a) community engagement → workshop planning
#    (b) monitoring deployment → tech integration → waste cycle → yield forecasting → market linkage
root.order.add_edge(pest_control, community_meet)
root.order.add_edge(pest_control, monitor_deploy)

root.order.add_edge(community_meet, workshop_plan)

root.order.add_edge(monitor_deploy, tech_integrate)
root.order.add_edge(tech_integrate, waste_cycle)
root.order.add_edge(waste_cycle, yield_forecast)
root.order.add_edge(yield_forecast, market_link)