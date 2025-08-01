# Generated from: 9a96a5f4-f73c-4e27-8aa8-bdbfc5e36ee3.json
# Description: This process outlines the comprehensive steps involved in setting up an urban vertical farming system within a repurposed industrial building. It includes site evaluation, modular rack assembly, climate control integration, automated irrigation programming, nutrient solution formulation, crop selection based on local demand, seedling germination, pest monitoring using AI sensors, harvest scheduling, quality control, waste recycling, energy consumption optimization, distribution logistics planning, and continuous system feedback analysis to maximize yield and sustainability in an urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities as POWL transitions
site_survey      = Transition(label="Site Survey")
rack_assembly    = Transition(label="Rack Assembly")
climate_setup    = Transition(label="Climate Setup")
irrigation_cfg   = Transition(label="Irrigation Config")
nutrient_mix     = Transition(label="Nutrient Mix")
crop_selection   = Transition(label="Crop Selection")
seed_germination = Transition(label="Seed Germination")
pest_monitoring  = Transition(label="Pest Monitoring")
harvest_plan     = Transition(label="Harvest Plan")
quality_check    = Transition(label="Quality Check")
waste_recycling  = Transition(label="Waste Recycling")
energy_audit     = Transition(label="Energy Audit")
logistics_plan   = Transition(label="Logistics Plan")
data_analysis    = Transition(label="Data Analysis")
system_feedback  = Transition(label="System Feedback")

# Build a strict partial order for the main sequence (Site Survey → ... → Data Analysis)
sequence = StrictPartialOrder(nodes=[
    site_survey,
    rack_assembly,
    climate_setup,
    irrigation_cfg,
    nutrient_mix,
    crop_selection,
    seed_germination,
    pest_monitoring,
    harvest_plan,
    quality_check,
    waste_recycling,
    energy_audit,
    logistics_plan,
    data_analysis
])

# Add the ordering edges to enforce a linear sequence
sequence.order.add_edge(site_survey,      rack_assembly)
sequence.order.add_edge(rack_assembly,    climate_setup)
sequence.order.add_edge(climate_setup,    irrigation_cfg)
sequence.order.add_edge(irrigation_cfg,   nutrient_mix)
sequence.order.add_edge(nutrient_mix,     crop_selection)
sequence.order.add_edge(crop_selection,   seed_germination)
sequence.order.add_edge(seed_germination, pest_monitoring)
sequence.order.add_edge(pest_monitoring,  harvest_plan)
sequence.order.add_edge(harvest_plan,     quality_check)
sequence.order.add_edge(quality_check,    waste_recycling)
sequence.order.add_edge(waste_recycling,  energy_audit)
sequence.order.add_edge(energy_audit,     logistics_plan)
sequence.order.add_edge(logistics_plan,   data_analysis)

# Wrap the sequence in a LOOP: after Data Analysis, perform System Feedback
# and then repeat the main sequence (continuous improvement cycle)
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[sequence, system_feedback]
)