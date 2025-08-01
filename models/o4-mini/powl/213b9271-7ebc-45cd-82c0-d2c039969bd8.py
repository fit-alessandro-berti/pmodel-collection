# Generated from: 213b9271-7ebc-45cd-82c0-d2c039969bd8.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban rooftop farm on a commercial building. It includes site assessment for structural integrity and sunlight exposure, soil and water testing, regulatory compliance checks, selection of crop varieties suited for rooftop conditions, installation of hydroponic or soil-based systems, integration of automated irrigation and climate control technologies, recruitment and training of specialized farming staff, ongoing pest and disease management, periodic yield monitoring and data analysis, community engagement for educational purposes, and final evaluation of environmental impact and profitability to ensure long-term viability and scalability of the rooftop farm model.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_assess      = Transition(label='Site Assess')
structural_check = Transition(label='Structural Check')
sunlight_map     = Transition(label='Sunlight Map')
soil_test        = Transition(label='Soil Test')
water_quality    = Transition(label='Water Quality')
permit_review    = Transition(label='Permit Review')
crop_select      = Transition(label='Crop Select')
system_install   = Transition(label='System Install')
irrigation_setup = Transition(label='Irrigation Setup')
climate_control  = Transition(label='Climate Control')
staff_hire       = Transition(label='Staff Hire')
training_run     = Transition(label='Training Run')
pest_monitor     = Transition(label='Pest Monitor')
yield_track      = Transition(label='Yield Track')
data_analyze     = Transition(label='Data Analyze')
community_meet   = Transition(label='Community Meet')
impact_review    = Transition(label='Impact Review')
profit_assess    = Transition(label='Profit Assess')

# Silent transition for loop redo
skip = SilentTransition()

# Define the monitoring sequence: Pest Monitor -> Yield Track -> Data Analyze
monitor_seq = StrictPartialOrder(nodes=[pest_monitor, yield_track, data_analyze])
monitor_seq.order.add_edge(pest_monitor, yield_track)
monitor_seq.order.add_edge(yield_track, data_analyze)

# Loop for periodic monitoring: do monitor_seq, then either exit or redo (skip)
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_seq, skip])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_assess,
    structural_check,
    sunlight_map,
    soil_test,
    water_quality,
    permit_review,
    crop_select,
    system_install,
    irrigation_setup,
    climate_control,
    staff_hire,
    training_run,
    monitor_loop,
    community_meet,
    impact_review,
    profit_assess
])

# Site assessment leads to structural check and sunlight mapping
root.order.add_edge(site_assess, structural_check)
root.order.add_edge(site_assess, sunlight_map)

# After both structural check and sunlight map, do soil and water tests
root.order.add_edge(structural_check, soil_test)
root.order.add_edge(sunlight_map, soil_test)
root.order.add_edge(structural_check, water_quality)
root.order.add_edge(sunlight_map, water_quality)

# Tests feed into permit review
root.order.add_edge(soil_test, permit_review)
root.order.add_edge(water_quality, permit_review)

# Permit review -> crop selection -> system installation
root.order.add_edge(permit_review, crop_select)
root.order.add_edge(crop_select, system_install)

# After system install, set up irrigation and climate control in parallel
root.order.add_edge(system_install, irrigation_setup)
root.order.add_edge(system_install, climate_control)

# Once technology is in place, hire and train staff
root.order.add_edge(irrigation_setup, staff_hire)
root.order.add_edge(climate_control, staff_hire)
root.order.add_edge(staff_hire, training_run)

# After training, start monitoring loop and community engagement in parallel
root.order.add_edge(training_run, monitor_loop)
root.order.add_edge(training_run, community_meet)

# Both monitoring and community meet lead to final evaluation
root.order.add_edge(monitor_loop, impact_review)
root.order.add_edge(community_meet, impact_review)

# Final evaluation sequence
root.order.add_edge(impact_review, profit_assess)