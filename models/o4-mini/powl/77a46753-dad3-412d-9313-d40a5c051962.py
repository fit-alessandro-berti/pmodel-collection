# Generated from: 77a46753-dad3-412d-9313-d40a5c051962.json
# Description: This process outlines the end-to-end cycle of managing a vertical urban farming supply chain, starting from crop selection and seed procurement through controlled environment cultivation, automated nutrient delivery, real-time growth monitoring, harvesting, post-harvest processing, quality assurance, packaging, and distribution to local markets. It integrates IoT sensor data analytics with manual inspection to optimize yield and sustainability in densely populated areas. The process also includes waste recycling, energy consumption tracking, and customer feedback integration to continuously improve the urban farming ecosystem while minimizing environmental impact and maximizing freshness and nutritional value for consumers.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
seed_sourcing      = Transition(label='Seed Sourcing')
crop_planning      = Transition(label='Crop Planning')
environment_setup  = Transition(label='Environment Setup')
nutrient_mixing    = Transition(label='Nutrient Mixing')
automated_feeding  = Transition(label='Automated Feeding')
growth_monitoring  = Transition(label='Growth Monitoring')
data_analysis      = Transition(label='Data Analysis')
manual_inspection  = Transition(label='Manual Inspection')
harvest_scheduling = Transition(label='Harvest Scheduling')
crop_harvesting    = Transition(label='Crop Harvesting')
post_harvest       = Transition(label='Post-Harvest')
quality_testing    = Transition(label='Quality Testing')
packaging_prep     = Transition(label='Packaging Prep')
distribution_plan  = Transition(label='Distribution Plan')

waste_recycling    = Transition(label='Waste Recycling')
energy_tracking    = Transition(label='Energy Tracking')
customer_feedback  = Transition(label='Customer Feedback')

# Main linear/concurrent workflow before improvement loop
main_process = StrictPartialOrder(nodes=[
    seed_sourcing,
    crop_planning,
    environment_setup,
    nutrient_mixing,
    automated_feeding,
    growth_monitoring,
    data_analysis,
    manual_inspection,
    harvest_scheduling,
    crop_harvesting,
    post_harvest,
    quality_testing,
    packaging_prep,
    distribution_plan
])
# Sequence edges
main_process.order.add_edge(seed_sourcing,      crop_planning)
main_process.order.add_edge(crop_planning,      environment_setup)
main_process.order.add_edge(environment_setup,  nutrient_mixing)
main_process.order.add_edge(nutrient_mixing,    automated_feeding)
main_process.order.add_edge(automated_feeding,  growth_monitoring)
# Fork to analysis and inspection
main_process.order.add_edge(growth_monitoring,  data_analysis)
main_process.order.add_edge(growth_monitoring,  manual_inspection)
# Join before scheduling
main_process.order.add_edge(data_analysis,      harvest_scheduling)
main_process.order.add_edge(manual_inspection,  harvest_scheduling)
# Continue sequence
main_process.order.add_edge(harvest_scheduling, crop_harvesting)
main_process.order.add_edge(crop_harvesting,    post_harvest)
main_process.order.add_edge(post_harvest,       quality_testing)
main_process.order.add_edge(quality_testing,    packaging_prep)
main_process.order.add_edge(packaging_prep,     distribution_plan)

# Improvement activities to feed the next cycle
improvement_cycle = StrictPartialOrder(nodes=[
    waste_recycling,
    energy_tracking,
    customer_feedback
])
# No edges => activities are concurrent

# Loop: do main_process, then optionally do improvements, then repeat or exit
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[main_process, improvement_cycle]
)