# Generated from: 4c3d0c53-61ce-42f1-b90a-61639764b8c7.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farming system within a metropolitan environment. It includes site assessment, modular farm design tailored to building constraints, sourcing sustainable materials, integrating IoT sensors for climate control, hydroponic system installation, nutrient solution calibration, crop selection based on urban demand, automated lighting setup, pest management using biological controls, data-driven growth monitoring, scheduled crop harvesting, waste recycling protocols, distribution logistics for local markets, customer feedback incorporation, and continuous system optimization to maximize yield and sustainability in a space-limited urban context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# Define all activities as labeled transitions
site_assess = Transition(label='Site Assess')
design_farm = Transition(label='Design Farm')
material_source = Transition(label='Material Source')
install_sensors = Transition(label='Install Sensors')
setup_hydroponics = Transition(label='Setup Hydroponics')
calibrate_nutrients = Transition(label='Calibrate Nutrients')
select_crops = Transition(label='Select Crops')
configure_lighting = Transition(label='Configure Lighting')
manage_pests = Transition(label='Manage Pests')
monitor_growth = Transition(label='Monitor Growth')
harvest_crops = Transition(label='Harvest Crops')
recycle_waste = Transition(label='Recycle Waste')
plan_distribution = Transition(label='Plan Distribution')
gather_feedback = Transition(label='Gather Feedback')
optimize_system = Transition(label='Optimize System')

# Create a strict partial order with all activities as nodes
root = StrictPartialOrder(nodes=[
    site_assess,
    design_farm,
    material_source,
    install_sensors,
    setup_hydroponics,
    calibrate_nutrients,
    select_crops,
    configure_lighting,
    manage_pests,
    monitor_growth,
    harvest_crops,
    recycle_waste,
    plan_distribution,
    gather_feedback,
    optimize_system
])

# Add edges reflecting the described sequential/concurrent dependencies

# Initial site assessment before design and material sourcing
root.order.add_edge(site_assess, design_farm)
root.order.add_edge(site_assess, material_source)

# Design depends on site assessment
# Material sourcing can proceed in parallel once site assessment is done

# Installation prep activities depend on design and material source
root.order.add_edge(design_farm, install_sensors)
root.order.add_edge(design_farm, setup_hydroponics)
root.order.add_edge(material_source, install_sensors)
root.order.add_edge(material_source, setup_hydroponics)

# Calibrate nutrients depends on hydroponics setup
root.order.add_edge(setup_hydroponics, calibrate_nutrients)

# Crop selection depends on design farm and perhaps also calibrate nutrients (plan)
root.order.add_edge(design_farm, select_crops)
root.order.add_edge(calibrate_nutrients, select_crops)

# Configure lighting after sensor installation and crop selection
root.order.add_edge(install_sensors, configure_lighting)
root.order.add_edge(select_crops, configure_lighting)

# Manage pests can be done after crop selection
root.order.add_edge(select_crops, manage_pests)

# Monitor growth after lighting configured and pest management ongoing
root.order.add_edge(configure_lighting, monitor_growth)
root.order.add_edge(manage_pests, monitor_growth)

# Harvest crops after monitoring growth
root.order.add_edge(monitor_growth, harvest_crops)

# Recycle waste comes after harvest
root.order.add_edge(harvest_crops, recycle_waste)

# Planning distribution depends on harvest and recycle waste done
root.order.add_edge(harvest_crops, plan_distribution)
root.order.add_edge(recycle_waste, plan_distribution)

# Gather feedback depends on distribution planning
root.order.add_edge(plan_distribution, gather_feedback)

# Optimize system after feedback gathered
root.order.add_edge(gather_feedback, optimize_system)