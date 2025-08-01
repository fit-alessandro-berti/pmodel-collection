# Generated from: 19e34b23-3f55-4dd7-b5e2-e8f83a83dbb9.json
# Description: This process outlines the comprehensive setup of an urban vertical farm, integrating advanced hydroponics, AI-controlled environment systems, and modular construction techniques. It begins with site analysis and zoning approval, followed by designing multi-layer growth platforms and selecting crop varieties suited for vertical farming. Procurement involves sourcing sustainable materials and specialized equipment. Installation covers lighting, irrigation, and climate control systems. AI calibration ensures optimal growth conditions through sensor data integration. Staff training is conducted on system operation and maintenance. Post-installation, a trial cultivation phase verifies system efficiency. Finally, marketing strategies are deployed targeting local retailers and consumers to establish supply chains and promote farm-to-table initiatives.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activity transitions
site_analysis      = Transition(label='Site Analysis')
zoning_approval    = Transition(label='Zoning Approval')
platform_design    = Transition(label='Platform Design')
crop_selection     = Transition(label='Crop Selection')
material_sourcing  = Transition(label='Material Sourcing')
equipment_order    = Transition(label='Equipment Order')
system_install     = Transition(label='System Install')
lighting_setup     = Transition(label='Lighting Setup')
irrigation_setup   = Transition(label='Irrigation Setup')
climate_control    = Transition(label='Climate Control')
ai_calibration     = Transition(label='AI Calibration')
staff_training     = Transition(label='Staff Training')
trial_cultivation  = Transition(label='Trial Cultivation')
data_monitoring    = Transition(label='Data Monitoring')
market_launch      = Transition(label='Market Launch')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_analysis, zoning_approval,
    platform_design, crop_selection,
    material_sourcing, equipment_order,
    system_install,
    lighting_setup, irrigation_setup, climate_control,
    ai_calibration, staff_training,
    trial_cultivation, data_monitoring,
    market_launch
])

# Sequence: Site Analysis -> Zoning Approval
root.order.add_edge(site_analysis, zoning_approval)

# After zoning approval: Platform Design and Crop Selection (in parallel)
root.order.add_edge(zoning_approval, platform_design)
root.order.add_edge(zoning_approval, crop_selection)

# Procurement depends on both design tasks
root.order.add_edge(platform_design, material_sourcing)
root.order.add_edge(crop_selection,   material_sourcing)
root.order.add_edge(platform_design, equipment_order)
root.order.add_edge(crop_selection,   equipment_order)

# Procurement -> System Install
root.order.add_edge(material_sourcing, system_install)
root.order.add_edge(equipment_order,   system_install)

# Installation subtasks in parallel
root.order.add_edge(system_install, lighting_setup)
root.order.add_edge(system_install, irrigation_setup)
root.order.add_edge(system_install, climate_control)

# All install subtasks -> AI Calibration
root.order.add_edge(lighting_setup,   ai_calibration)
root.order.add_edge(irrigation_setup, ai_calibration)
root.order.add_edge(climate_control,  ai_calibration)

# Calibration -> Training -> Trial & Monitoring (in parallel)
root.order.add_edge(ai_calibration,   staff_training)
root.order.add_edge(staff_training,   trial_cultivation)
root.order.add_edge(staff_training,   data_monitoring)

# Both Trial Cultivation and Data Monitoring -> Market Launch
root.order.add_edge(trial_cultivation, market_launch)
root.order.add_edge(data_monitoring,   market_launch)