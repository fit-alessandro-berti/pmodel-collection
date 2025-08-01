# Generated from: 83d511ed-17fc-4955-a646-66f1dd316a12.json
# Description: This process outlines the detailed steps involved in establishing an urban vertical farm within a repurposed commercial building. It includes activities such as site analysis, structural retrofitting, environmental control installation, crop selection, hydroponic system design, nutrient formulation, automated monitoring setup, pest management planning, labor training, and market integration. Each phase is critical to ensure sustainable production, optimize yield, and minimize environmental impact while addressing urban food security challenges through innovative farming techniques and technology integration.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
site_survey = Transition(label='Site Survey')
structural_check = Transition(label='Structural Check')
retrofitting = Transition(label='Retrofitting')
env_control = Transition(label='Env Control')
crop_research = Transition(label='Crop Research')
system_design = Transition(label='System Design')
nutrient_mix = Transition(label='Nutrient Mix')
sensor_setup = Transition(label='Sensor Setup')
irrigation_plan = Transition(label='Irrigation Plan')
pest_control = Transition(label='Pest Control')
staff_training = Transition(label='Staff Training')
energy_audit = Transition(label='Energy Audit')
waste_recycle = Transition(label='Waste Recycle')
market_study = Transition(label='Market Study')
launch_prep = Transition(label='Launch Prep')
yield_monitor = Transition(label='Yield Monitor')

# From the description, the likely ordering:
# 1) Site Survey
# 2) Structural Check
# 3) Retrofitting
# 4) Env Control
# 5) Crop Research
# 6) System Design
# 7) Nutrient Mix
# 8) Sensor Setup
# 9) Irrigation Plan
# 10) Pest Control
# 11) Staff Training
# Parallel activities: Energy Audit and Waste Recycle can be parallel to others (likely around installation)
# 12) Market Study
# 13) Launch Prep
# 14) Yield Monitor (final step - ongoing monitoring)

# Construct StrictPartialOrder nodes
nodes = [
    site_survey,
    structural_check,
    retrofitting,
    env_control,
    crop_research,
    system_design,
    nutrient_mix,
    sensor_setup,
    irrigation_plan,
    pest_control,
    staff_training,
    energy_audit,
    waste_recycle,
    market_study,
    launch_prep,
    yield_monitor
]

root = StrictPartialOrder(nodes=nodes)

# Define dependencies/order according to logical flow

# Initial build sequence
root.order.add_edge(site_survey, structural_check)
root.order.add_edge(structural_check, retrofitting)
root.order.add_edge(retrofitting, env_control)

# Parallel after Env Control: Crop Research and Energy Audit & Waste Recycle can start in parallel
root.order.add_edge(env_control, crop_research)
root.order.add_edge(env_control, energy_audit)
root.order.add_edge(env_control, waste_recycle)

# Crop research followed by system design and nutrient mix
root.order.add_edge(crop_research, system_design)
root.order.add_edge(system_design, nutrient_mix)

# Nutrient mix enables sensor setup and irrigation plan (parallel)
root.order.add_edge(nutrient_mix, sensor_setup)
root.order.add_edge(nutrient_mix, irrigation_plan)

# Sensor setup and irrigation plan enable pest control
# Pest control after both sensor setup and irrigation plan: add edges from both to pest control
root.order.add_edge(sensor_setup, pest_control)
root.order.add_edge(irrigation_plan, pest_control)

# Pest control then enables staff training
root.order.add_edge(pest_control, staff_training)

# Energy audit and waste recycle should complete before market study
root.order.add_edge(energy_audit, market_study)
root.order.add_edge(waste_recycle, market_study)

# Staff training must finish before market study and launch prep
root.order.add_edge(staff_training, market_study)
root.order.add_edge(staff_training, launch_prep)

# Market study enables launch prep
root.order.add_edge(market_study, launch_prep)

# Launch prep enables yield monitor (final step)
root.order.add_edge(launch_prep, yield_monitor)