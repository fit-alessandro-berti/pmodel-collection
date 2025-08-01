# Generated from: 336c547d-e5a9-41fe-b168-750046caf413.json
# Description: This process outlines the complex and interdisciplinary steps required to establish a sustainable urban rooftop farm in a dense city environment. It involves initial site assessment, structural integrity analysis, microclimate evaluation, soil substrate preparation, irrigation system design, plant species selection optimized for urban conditions, installation of renewable energy sources, pest control planning with eco-friendly methods, community engagement and education programs, real-time environmental monitoring setup, harvest scheduling, waste composting integration, and finally, distribution logistics tailored to local markets and restaurants. Each activity requires careful coordination between architects, agronomists, engineers, and community stakeholders to ensure the project’s viability and long-term impact on urban food security and green space enhancement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey     = Transition(label='Site Survey')
load_testing    = Transition(label='Load Testing')
climate_study   = Transition(label='Climate Study')
soil_mix        = Transition(label='Soil Mix')
irrigation_plan = Transition(label='Irrigation Plan')
crop_choice     = Transition(label='Crop Choice')
energy_install  = Transition(label='Energy Install')
sensor_setup    = Transition(label='Sensor Setup')
pest_monitor    = Transition(label='Pest Monitor')
community_meet  = Transition(label='Community Meet')
training_day    = Transition(label='Training Day')
harvest_plan    = Transition(label='Harvest Plan')
waste_cycle     = Transition(label='Waste Cycle')
market_link     = Transition(label='Market Link')
report_review   = Transition(label='Report Review')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_survey, load_testing, climate_study,
    soil_mix, irrigation_plan, crop_choice,
    energy_install, sensor_setup, pest_monitor,
    community_meet, training_day,
    harvest_plan, waste_cycle, market_link, report_review
])

# Define the control‐flow dependencies
root.order.add_edge(site_survey, load_testing)
root.order.add_edge(load_testing, climate_study)

# Parallel preparation tasks after climate study
root.order.add_edge(climate_study, soil_mix)
root.order.add_edge(climate_study, irrigation_plan)
root.order.add_edge(climate_study, crop_choice)

# Energy installation depends on structural integrity
root.order.add_edge(load_testing, energy_install)

# Sensor setup and pest monitoring after energy install
root.order.add_edge(energy_install, sensor_setup)
root.order.add_edge(sensor_setup, pest_monitor)

# Community engagement and training
root.order.add_edge(pest_monitor, community_meet)
root.order.add_edge(community_meet, training_day)

# Harvest planning relies on sensor data and pest monitoring
root.order.add_edge(sensor_setup, harvest_plan)
root.order.add_edge(pest_monitor, harvest_plan)

# Post‐harvest tasks
root.order.add_edge(harvest_plan, waste_cycle)
root.order.add_edge(harvest_plan, market_link)

# Final review after all branches complete
root.order.add_edge(waste_cycle, report_review)
root.order.add_edge(market_link, report_review)
root.order.add_edge(training_day, report_review)