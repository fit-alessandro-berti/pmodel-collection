# Generated from: 2050f95a-e6af-403d-8f9a-eff7409dee28.json
# Description: This process outlines the steps required to establish an urban rooftop farm on a commercial building, integrating sustainable agriculture techniques with city infrastructure constraints. It involves initial site assessment, structural analysis, soil and water testing, system design for irrigation and crop placement, procurement of materials, installation of modular planters, setup of automated climate control, seed selection and planting, daily maintenance scheduling, pest monitoring using IoT sensors, periodic yield evaluation, community engagement for education, and final reporting to stakeholders. This atypical process requires coordination between agricultural experts, civil engineers, and urban planners to ensure a productive and environmentally friendly rooftop farm that enhances urban green space while complying with safety regulations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
site_assess = Transition(label='Site Assess')
structural_check = Transition(label='Structural Check')
soil_testing = Transition(label='Soil Testing')
water_quality = Transition(label='Water Quality')
system_design = Transition(label='System Design')
material_buy = Transition(label='Material Buy')
planter_setup = Transition(label='Planter Setup')
climate_setup = Transition(label='Climate Setup')
seed_planting = Transition(label='Seed Planting')
irrigation_start = Transition(label='Irrigation Start')
pest_monitor = Transition(label='Pest Monitor')
yield_measure = Transition(label='Yield Measure')
maintenance_plan = Transition(label='Maintenance Plan')
community_meet = Transition(label='Community Meet')
final_report = Transition(label='Final Report')

# First stage: Site Assess --> Structural Check
first_stage = StrictPartialOrder(nodes=[site_assess, structural_check])
first_stage.order.add_edge(site_assess, structural_check)

# Soil Testing and Water Quality can be done concurrently after Structural Check
soil_water = StrictPartialOrder(nodes=[soil_testing, water_quality])

# Stage after first: Structural Check --> Parallel soil and water tests
second_stage = StrictPartialOrder(nodes=[first_stage, soil_water])
second_stage.order.add_edge(first_stage, soil_water)

# System Design after soil and water tests
third_stage = StrictPartialOrder(nodes=[second_stage, system_design])
third_stage.order.add_edge(second_stage, system_design)

# Material Buy after System Design
fourth_stage = StrictPartialOrder(nodes=[third_stage, material_buy])
fourth_stage.order.add_edge(third_stage, material_buy)

# Planter Setup and Climate Setup can be done in parallel after Material Buy
setup_parallel = StrictPartialOrder(nodes=[planter_setup, climate_setup])

fifth_stage = StrictPartialOrder(nodes=[fourth_stage, setup_parallel])
fifth_stage.order.add_edge(fourth_stage, setup_parallel)

# Seed Planting after Planter Setup (presumably before irrigation)
seed_and_irrigation = StrictPartialOrder(nodes=[seed_planting, irrigation_start])
seed_and_irrigation.order.add_edge(seed_planting, irrigation_start)

sixth_stage = StrictPartialOrder(nodes=[fifth_stage, seed_and_irrigation])
sixth_stage.order.add_edge(fifth_stage, seed_and_irrigation)

# Maintenance Plan and Pest Monitor in parallel after irrigation start
maintain_pest = StrictPartialOrder(nodes=[maintenance_plan, pest_monitor])

seventh_stage = StrictPartialOrder(nodes=[sixth_stage, maintain_pest])
seventh_stage.order.add_edge(sixth_stage, maintain_pest)

# Yield Measure happens after maintenance and pest monitor
eighth_stage = StrictPartialOrder(nodes=[seventh_stage, yield_measure])
eighth_stage.order.add_edge(seventh_stage, yield_measure)

# Community Meet after yield measure
ninth_stage = StrictPartialOrder(nodes=[eighth_stage, community_meet])
ninth_stage.order.add_edge(eighth_stage, community_meet)

# Final Report after community meeting
root = StrictPartialOrder(nodes=[ninth_stage, final_report])
root.order.add_edge(ninth_stage, final_report)