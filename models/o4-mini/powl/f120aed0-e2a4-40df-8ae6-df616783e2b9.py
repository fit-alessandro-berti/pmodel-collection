# Generated from: f120aed0-e2a4-40df-8ae6-df616783e2b9.json
# Description: This process outlines the complex and atypical steps involved in establishing an urban vertical farming enterprise within a repurposed industrial building. It includes site evaluation, modular rack design, hydroponic system installation, climate control calibration, nutrient solution preparation, crop selection based on market demand, seed germination, continuous monitoring using IoT sensors, pest control with integrated biocontrol agents, automated harvesting, post-harvest quality assessment, packaging for urban consumers, data analytics for yield optimization, community engagement for local sourcing, and finally, distribution logistics tailored to minimize carbon footprint in densely populated areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the activities
site_survey       = Transition(label="Site Survey")
rack_design       = Transition(label="Rack Design")
system_setup      = Transition(label="System Setup")
climate_calibrate = Transition(label="Climate Calibrate")
nutrient_prep     = Transition(label="Nutrient Prep")
crop_select       = Transition(label="Crop Select")
seed_germinate    = Transition(label="Seed Germinate")
sensor_deploy     = Transition(label="Sensor Deploy")
pest_control      = Transition(label="Pest Control")
harvest_automate  = Transition(label="Harvest Automate")
quality_check     = Transition(label="Quality Check")
pack_produce      = Transition(label="Pack Produce")
data_analyze      = Transition(label="Data Analyze")
engage_community  = Transition(label="Engage Community")
logistics_plan    = Transition(label="Logistics Plan")

# Assemble them into a strict partial order (sequential)
nodes = [
    site_survey,
    rack_design,
    system_setup,
    climate_calibrate,
    nutrient_prep,
    crop_select,
    seed_germinate,
    sensor_deploy,
    pest_control,
    harvest_automate,
    quality_check,
    pack_produce,
    data_analyze,
    engage_community,
    logistics_plan
]

root = StrictPartialOrder(nodes=nodes)
# Add the sequential dependencies
for i in range(len(nodes) - 1):
    root.order.add_edge(nodes[i], nodes[i + 1])