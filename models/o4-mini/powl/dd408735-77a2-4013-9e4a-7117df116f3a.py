# Generated from: dd408735-77a2-4013-9e4a-7117df116f3a.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban rooftop farm on a commercial building. Activities include site assessment, structural analysis, soil testing, microclimate evaluation, and obtaining permits. The process also involves designing modular planting systems, sourcing organic seeds, setting up automated irrigation and nutrient delivery, integrating pest control using biological agents, installing solar-powered climate sensors, training staff on urban farming techniques, and establishing distribution channels for fresh produce. Continuous monitoring and adaptive maintenance ensure crop health and yield optimization under variable urban conditions, making this process atypical yet practical for modern urban agriculture initiatives.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_assess     = Transition(label='Site Assess')
structure_check = Transition(label='Structure Check')
soil_test       = Transition(label='Soil Test')
climate_eval    = Transition(label='Climate Eval')
permit_obtain   = Transition(label='Permit Obtain')
design_layout   = Transition(label='Design Layout')
seed_sourcing   = Transition(label='Seed Sourcing')
irrigation_set  = Transition(label='Irrigation Set')
nutrient_mix    = Transition(label='Nutrient Mix')
pest_control    = Transition(label='Pest Control')
sensor_install  = Transition(label='Sensor Install')
staff_train     = Transition(label='Staff Train')
crop_planting   = Transition(label='Crop Planting')
yield_monitor   = Transition(label='Yield Monitor')
maintenance     = Transition(label='Maintenance')
waste_manage    = Transition(label='Waste Manage')
market_setup    = Transition(label='Market Setup')

# Define the monitoring-maintenance loop body
monitor_cycle = StrictPartialOrder(nodes=[yield_monitor, maintenance, waste_manage])
monitor_cycle.order.add_edge(yield_monitor, maintenance)
monitor_cycle.order.add_edge(maintenance, waste_manage)

# Silent transition for loop tail
skip = SilentTransition()

# Loop: repeatedly do monitor_cycle or exit
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_cycle, skip])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_assess, structure_check, soil_test, climate_eval, permit_obtain,
    design_layout, seed_sourcing, irrigation_set, nutrient_mix, pest_control,
    sensor_install, staff_train, crop_planting, market_setup, monitor_loop
])

# Add the linear sequence up to planting
root.order.add_edge(site_assess, structure_check)
root.order.add_edge(structure_check, soil_test)
root.order.add_edge(soil_test, climate_eval)
root.order.add_edge(climate_eval, permit_obtain)
root.order.add_edge(permit_obtain, design_layout)
root.order.add_edge(design_layout, seed_sourcing)
root.order.add_edge(seed_sourcing, irrigation_set)
root.order.add_edge(irrigation_set, nutrient_mix)
root.order.add_edge(nutrient_mix, pest_control)
root.order.add_edge(pest_control, sensor_install)
root.order.add_edge(sensor_install, staff_train)
root.order.add_edge(staff_train, crop_planting)

# After planting, start monitoring loop and optionally set up market concurrently
root.order.add_edge(crop_planting, monitor_loop)
root.order.add_edge(crop_planting, market_setup)