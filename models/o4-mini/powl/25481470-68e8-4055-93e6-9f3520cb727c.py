# Generated from: 25481470-68e8-4055-93e6-9f3520cb727c.json
# Description: This process outlines the complex and multi-disciplinary steps involved in establishing an urban rooftop farm. It includes site analysis, environmental impact assessment, structural integrity checks, soil and water testing, sourcing sustainable materials, installation of hydroponic systems, seed selection, pest management planning, community engagement, and continuous monitoring for crop optimization. The process demands coordination between architects, agronomists, environmental scientists, and local authorities to ensure compliance with regulations and maximize productivity while maintaining urban ecological balance.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey       = Transition(label='Site Survey')
impact_review     = Transition(label='Impact Review')
regulation_review = Transition(label='Regulation Review')
structure_check   = Transition(label='Structure Check')
soil_testing      = Transition(label='Soil Testing')
water_analysis    = Transition(label='Water Analysis')
material_sourcing = Transition(label='Material Sourcing')
system_install    = Transition(label='System Install')
irrigation_setup  = Transition(label='Irrigation Setup')
crop_planting     = Transition(label='Crop Planting')
seed_selection    = Transition(label='Seed Selection')
pest_planning     = Transition(label='Pest Planning')
community_meet    = Transition(label='Community Meet')

# Monitoring cycle activities
growth_monitor  = Transition(label='Growth Monitor')
yield_assess    = Transition(label='Yield Assess')
waste_manage    = Transition(label='Waste Manage')
energy_audit    = Transition(label='Energy Audit')

# Silent transition for loop continuation
skip = SilentTransition()

# Build the monitoring loop: execute the monitoring sequence, then either exit or skip->monitor again
monitor_cycle = StrictPartialOrder(nodes=[growth_monitor, yield_assess, waste_manage, energy_audit])
monitor_cycle.order.add_edge(growth_monitor, yield_assess)
monitor_cycle.order.add_edge(yield_assess, waste_manage)
monitor_cycle.order.add_edge(waste_manage, energy_audit)

monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_cycle, skip])

# Build the main workflow partial order
root = StrictPartialOrder(nodes=[
    site_survey, impact_review, regulation_review, structure_check,
    soil_testing, water_analysis,
    material_sourcing, system_install, irrigation_setup, crop_planting,
    seed_selection, pest_planning, community_meet,
    monitor_loop
])

# Define the sequencing constraints
root.order.add_edge(site_survey, impact_review)
root.order.add_edge(impact_review, regulation_review)
root.order.add_edge(regulation_review, structure_check)

# Soil and water tests can run in parallel after structure check
root.order.add_edge(structure_check, soil_testing)
root.order.add_edge(structure_check, water_analysis)
# Both tests must finish before sourcing materials
root.order.add_edge(soil_testing, material_sourcing)
root.order.add_edge(water_analysis, material_sourcing)

# Community engagement after impact review
root.order.add_edge(impact_review, community_meet)
# Compliance review also gates community meeting
root.order.add_edge(regulation_review, community_meet)

# Material sourcing -> system install -> irrigation -> planting
root.order.add_edge(material_sourcing, system_install)
root.order.add_edge(system_install, irrigation_setup)
root.order.add_edge(irrigation_setup, crop_planting)

# Seed selection and pest planning must complete before planting
root.order.add_edge(seed_selection, crop_planting)
root.order.add_edge(pest_planning, crop_planting)
# Community meet also feeds into planting
root.order.add_edge(community_meet, crop_planting)

# After planting, enter the monitoring loop
root.order.add_edge(crop_planting, monitor_loop)