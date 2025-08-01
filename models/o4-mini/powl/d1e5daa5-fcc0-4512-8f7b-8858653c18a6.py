# Generated from: d1e5daa5-fcc0-4512-8f7b-8858653c18a6.json
# Description: This process outlines the complex and multifaceted steps required to establish an urban vertical farming facility. It involves site assessment, regulatory compliance checks, modular system design, installation of hydroponic units, integration of IoT sensors, nutrient solution calibration, climate control programming, crop selection based on microclimate data, lighting optimization, staff training on automated systems, harvesting schedule development, waste recycling protocols, market demand analysis, distribution logistics planning, and ongoing system performance monitoring to ensure sustainable and efficient crop production within constrained urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
site_survey          = Transition(label='Site Survey')
regulation_check     = Transition(label='Regulation Check')
design_modules       = Transition(label='Design Modules')
install_hydroponics  = Transition(label='Install Hydroponics')
integrate_sensors    = Transition(label='Integrate Sensors')
calibrate_nutrients  = Transition(label='Calibrate Nutrients')
program_climate      = Transition(label='Program Climate')
select_crops         = Transition(label='Select Crops')
optimize_lighting    = Transition(label='Optimize Lighting')
train_staff          = Transition(label='Train Staff')
plan_harvest         = Transition(label='Plan Harvest')
recycle_waste        = Transition(label='Recycle Waste')
analyze_demand       = Transition(label='Analyze Demand')
plan_logistics       = Transition(label='Plan Logistics')
monitor_systems      = Transition(label='Monitor Systems')

# Build a strict partial order (sequential workflow)
root = StrictPartialOrder(nodes=[
    site_survey,
    regulation_check,
    design_modules,
    install_hydroponics,
    integrate_sensors,
    calibrate_nutrients,
    program_climate,
    select_crops,
    optimize_lighting,
    train_staff,
    plan_harvest,
    recycle_waste,
    analyze_demand,
    plan_logistics,
    monitor_systems
])

# Add the sequential dependencies
root.order.add_edge(site_survey,      regulation_check)
root.order.add_edge(regulation_check, design_modules)
root.order.add_edge(design_modules,   install_hydroponics)
root.order.add_edge(install_hydroponics, integrate_sensors)
root.order.add_edge(integrate_sensors,   calibrate_nutrients)
root.order.add_edge(calibrate_nutrients,   program_climate)
root.order.add_edge(program_climate,     select_crops)
root.order.add_edge(select_crops,        optimize_lighting)
root.order.add_edge(optimize_lighting,   train_staff)
root.order.add_edge(train_staff,         plan_harvest)
root.order.add_edge(plan_harvest,        recycle_waste)
root.order.add_edge(recycle_waste,       analyze_demand)
root.order.add_edge(analyze_demand,      plan_logistics)
root.order.add_edge(plan_logistics,      monitor_systems)