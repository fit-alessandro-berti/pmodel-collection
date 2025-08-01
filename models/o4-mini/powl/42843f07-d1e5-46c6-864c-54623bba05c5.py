# Generated from: 42843f07-d1e5-46c6-864c-54623bba05c5.json
# Description: This process outlines the comprehensive steps required to establish a fully operational urban vertical farm within a metropolitan environment. It involves site assessment, modular infrastructure design, climate system integration, nutrient cycling optimization, IoT sensor deployment, and automation setup. The process continues with seed selection, germination protocols, growth monitoring, pest control, harvesting schedules, packaging logistics, waste recycling, energy management, and continuous yield analysis. Each phase is critical to ensure sustainable production, minimize environmental impact, and maximize crop output in limited urban spaces while adapting to fluctuating demand and technological advancements.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_survey    = Transition(label="Site Survey")
modular_design = Transition(label="Modular Design")
climate_setup  = Transition(label="Climate Setup")
nutrient_mix   = Transition(label="Nutrient Mix")
sensor_deploy  = Transition(label="Sensor Deploy")
automation_init= Transition(label="Automation Init")
seed_selection = Transition(label="Seed Selection")
germination    = Transition(label="Germination")
growth_check   = Transition(label="Growth Check")
pest_control   = Transition(label="Pest Control")
harvest_plan   = Transition(label="Harvest Plan")
pack_logistics = Transition(label="Pack Logistics")
waste_sorting  = Transition(label="Waste Sorting")
energy_audit   = Transition(label="Energy Audit")
yield_review   = Transition(label="Yield Review")

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, modular_design, climate_setup, nutrient_mix,
    sensor_deploy, automation_init, seed_selection, germination,
    growth_check, pest_control, harvest_plan, pack_logistics,
    waste_sorting, energy_audit, yield_review
])

# Add the sequential dependencies
seq = [
    (site_survey, modular_design),
    (modular_design, climate_setup),
    (climate_setup, nutrient_mix),
    (nutrient_mix, sensor_deploy),
    (sensor_deploy, automation_init),
    (automation_init, seed_selection),
    (seed_selection, germination),
    (germination, growth_check),
    (growth_check, pest_control),
    (pest_control, harvest_plan),
    (harvest_plan, pack_logistics),
    (pack_logistics, waste_sorting),
    (waste_sorting, energy_audit),
    (energy_audit, yield_review)
]

for src, tgt in seq:
    root.order.add_edge(src, tgt)