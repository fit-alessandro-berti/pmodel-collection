# Generated from: 0e96de15-8e18-4d32-b81b-4b232af96ab2.json
# Description: This process outlines the complex sequence required to establish an urban vertical farm within a repurposed industrial building. It involves site analysis, environmental assessments, modular system design, procurement of specialized hydroponic equipment, installation of climate control units, integration of IoT sensors for monitoring, seed selection based on urban microclimate data, nutrient solution formulation, staff training on automated systems, regulatory compliance checks, trial crop planting, data-driven growth optimization, pest management using biocontrol agents, harvest scheduling, and final product packaging for local distribution. Each step requires coordination across multiple disciplines including agronomy, engineering, logistics, and regulatory affairs to ensure a sustainable and productive urban agriculture system.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_analysis = Transition(label="Site Analysis")
env_assessment = Transition(label="Env Assessment")
system_design = Transition(label="System Design")
equipment_procure = Transition(label="Equipment Procure")
climate_install = Transition(label="Climate Install")
sensor_integrate = Transition(label="Sensor Integrate")
seed_selection = Transition(label="Seed Selection")
nutrient_mix = Transition(label="Nutrient Mix")
staff_training = Transition(label="Staff Training")
compliance_check = Transition(label="Compliance Check")
trial_planting = Transition(label="Trial Planting")
growth_optimize = Transition(label="Growth Optimize")
pest_control = Transition(label="Pest Control")
harvest_schedule = Transition(label="Harvest Schedule")
packaging_prep = Transition(label="Packaging Prep")

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_analysis,
    env_assessment,
    system_design,
    equipment_procure,
    climate_install,
    sensor_integrate,
    seed_selection,
    nutrient_mix,
    staff_training,
    compliance_check,
    trial_planting,
    growth_optimize,
    pest_control,
    harvest_schedule,
    packaging_prep
])

# Add sequential dependencies
root.order.add_edge(site_analysis, env_assessment)
root.order.add_edge(env_assessment, system_design)
root.order.add_edge(system_design, equipment_procure)
root.order.add_edge(equipment_procure, climate_install)
root.order.add_edge(climate_install, sensor_integrate)
root.order.add_edge(sensor_integrate, seed_selection)
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, staff_training)
root.order.add_edge(staff_training, compliance_check)
root.order.add_edge(compliance_check, trial_planting)
root.order.add_edge(trial_planting, growth_optimize)
root.order.add_edge(growth_optimize, pest_control)
root.order.add_edge(pest_control, harvest_schedule)
root.order.add_edge(harvest_schedule, packaging_prep)