# Generated from: dd408735-77a2-4013-9e4a-7117df116f3a.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban rooftop farm on a commercial building. Activities include site assessment, structural analysis, soil testing, microclimate evaluation, and obtaining permits. The process also involves designing modular planting systems, sourcing organic seeds, setting up automated irrigation and nutrient delivery, integrating pest control using biological agents, installing solar-powered climate sensors, training staff on urban farming techniques, and establishing distribution channels for fresh produce. Continuous monitoring and adaptive maintenance ensure crop health and yield optimization under variable urban conditions, making this process atypical yet practical for modern urban agriculture initiatives.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transition instances
site_assess = Transition(label='Site Assess')
structure_check = Transition(label='Structure Check')
soil_test = Transition(label='Soil Test')
climate_eval = Transition(label='Climate Eval')
permit_obtain = Transition(label='Permit Obtain')
design_layout = Transition(label='Design Layout')
seed_sourcing = Transition(label='Seed Sourcing')
irrigation_set = Transition(label='Irrigation Set')
nutrient_mix = Transition(label='Nutrient Mix')
pest_control = Transition(label='Pest Control')
sensor_install = Transition(label='Sensor Install')
staff_train = Transition(label='Staff Train')
crop_planting = Transition(label='Crop Planting')
yield_monitor = Transition(label='Yield Monitor')
market_setup = Transition(label='Market Setup')
maintenance = Transition(label='Maintenance')
waste_manage = Transition(label='Waste Manage')

# Phase 1: Initial assessment and permits (partially ordered, soil & climate evaluations concurrent)
assessment = StrictPartialOrder(
    nodes=[site_assess, structure_check, soil_test, climate_eval, permit_obtain]
)
assessment.order.add_edge(site_assess, structure_check)
assessment.order.add_edge(structure_check, permit_obtain)
assessment.order.add_edge(site_assess, soil_test)
assessment.order.add_edge(site_assess, climate_eval)
assessment.order.add_edge(soil_test, permit_obtain)
assessment.order.add_edge(climate_eval, permit_obtain)
# soil_test and climate_eval concurrent, both before permit_obtain

# Phase 2: Design and sourcing (design before sourcing seeds)
design_and_source = StrictPartialOrder(
    nodes=[design_layout, seed_sourcing]
)
design_and_source.order.add_edge(design_layout, seed_sourcing)

# Phase 3: Setup of infrastructure (irrigation, nutrient mix, pest control, sensor install, staff train)
# These can be partially concurrent with only irrigation_set before nutrient_mix
setup_infra = StrictPartialOrder(
    nodes=[irrigation_set, nutrient_mix, pest_control, sensor_install, staff_train]
)
setup_infra.order.add_edge(irrigation_set, nutrient_mix)
# other nodes concurrent

# Phase 4: Planting and production start (crop planting)
planting = crop_planting

# Phase 5: Monitoring and maintenance loop
monitor_and_maintain = StrictPartialOrder(
    nodes=[yield_monitor, maintenance, waste_manage]
)
monitor_and_maintain.order.add_edge(yield_monitor, maintenance)
monitor_and_maintain.order.add_edge(maintenance, waste_manage)

# Model monitoring and maintenance as a LOOP where:
# A = yield_monitor (monitor)
# B = maintenance (adaptive maintenance)
# loop repeats monitoring and maintenance until exit (modeled with LOOP operator)
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[yield_monitor, maintenance]
)
# we will consider waste_manage follows the monitor_loop as cleanup after loop ends

# Phase 6: Market setup (after initial planting)
market = market_setup

# Combine phases in a global partial order:
root = StrictPartialOrder(
    nodes=[assessment, design_and_source, setup_infra, planting, monitor_loop, waste_manage, market]
)

# Ordering edges between phases:
root.order.add_edge(assessment, design_and_source)      # after permits design & sourcing
root.order.add_edge(design_and_source, setup_infra)    # before infrastructure setup
root.order.add_edge(setup_infra, planting)              # infrastructure before planting
root.order.add_edge(planting, monitor_loop)             # planting before monitoring loop
root.order.add_edge(monitor_loop, waste_manage)         # loop finishes then waste management
root.order.add_edge(planting, market)                   # can start setting up markets after planting
root.order.add_edge(market, waste_manage)               # market setup before waste manage (cleanup/distribution)

# This models concurrency: e.g. market setup can run concurrently with monitoring loop
# but waste_manage is after both
