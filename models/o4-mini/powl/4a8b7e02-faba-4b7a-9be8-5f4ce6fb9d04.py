# Generated from: 4a8b7e02-faba-4b7a-9be8-5f4ce6fb9d04.json
# Description: This process involves the integration of vertical farming systems within urban infrastructure to optimize space and resource utilization. It encompasses site assessment, modular farm design, automated nutrient delivery, environmental monitoring, community engagement, crop rotation planning, waste recycling, pest management using AI, energy consumption optimization, and logistics coordination for local distribution. The process ensures sustainable food production by combining advanced technology, ecological practices, and urban planning, ultimately contributing to food security and reduced carbon footprint in densely populated areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_assess       = Transition(label='Site Assess')
design_modules    = Transition(label='Design Modules')
install_systems   = Transition(label='Install Systems')
calibrate_sensors = Transition(label='Calibrate Sensors')
set_nutrients     = Transition(label='Set Nutrients')
monitor_env       = Transition(label='Monitor Environment')
recycle_waste     = Transition(label='Recycle Waste')
manage_pests      = Transition(label='Manage Pests')
optimize_energy   = Transition(label='Optimize Energy')
plan_rotation     = Transition(label='Plan Rotation')
schedule_harvest  = Transition(label='Schedule Harvest')
coordinate_logistics = Transition(label='Coordinate Logistics')
train_staff       = Transition(label='Train Staff')
engage_community  = Transition(label='Engage Community')
report_metrics    = Transition(label='Report Metrics')

# Silent transition for loop continuation
tau = SilentTransition()

# Define the body of the operational loop (can be repeated)
body_ops = StrictPartialOrder(nodes=[
    monitor_env,
    recycle_waste,
    manage_pests,
    optimize_energy
])
# A LOOP node: execute the body, then either exit or do a silent step then repeat the body
operational_loop = OperatorPOWL(operator=Operator.LOOP, children=[body_ops, tau])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    site_assess,
    design_modules,
    install_systems,
    calibrate_sensors,
    set_nutrients,
    operational_loop,
    plan_rotation,
    schedule_harvest,
    coordinate_logistics,
    train_staff,
    engage_community,
    report_metrics
])

# Add the control‐flow edges
root.order.add_edge(site_assess,       design_modules)
root.order.add_edge(design_modules,    install_systems)
root.order.add_edge(install_systems,   calibrate_sensors)
root.order.add_edge(calibrate_sensors, set_nutrients)
root.order.add_edge(set_nutrients,     operational_loop)
root.order.add_edge(operational_loop,  plan_rotation)
root.order.add_edge(plan_rotation,     schedule_harvest)
root.order.add_edge(schedule_harvest,  coordinate_logistics)
root.order.add_edge(coordinate_logistics, train_staff)
root.order.add_edge(train_staff,       engage_community)
root.order.add_edge(engage_community,  report_metrics)