# Generated from: 6e51aa90-f787-4e68-9955-a5fb0939a6ce.json
# Description: This process outlines the establishment of an urban rooftop farm integrating advanced hydroponic systems and renewable energy sources. It begins with site evaluation for structural integrity and sunlight exposure, followed by design planning incorporating modular growing units and water recycling mechanisms. Procurement of specialized materials such as nutrient solutions, grow lights, and sensors is coordinated with local vendors. Installation involves structural reinforcement, system assembly, and sensor calibration. Crop selection is optimized for urban climates and market demands. Continuous monitoring ensures optimal growth through data analysis and automated adjustments. Community engagement activities include workshops and local produce distribution. The process concludes with performance review and scalability assessment for other rooftops in the city.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_survey = Transition(label='Site Survey')
structural_test = Transition(label='Structural Test')
sunlight_map = Transition(label='Sunlight Map')
design_plan = Transition(label='Design Plan')
vendor_coordination = Transition(label='Vendor Coordination')
material_order = Transition(label='Material Order')
reinforce_roof = Transition(label='Reinforce Roof')
install_systems = Transition(label='Install Systems')
calibrate_sensors = Transition(label='Calibrate Sensors')
select_crops = Transition(label='Select Crops')
setup_hydroponics = Transition(label='Setup Hydroponics')
configure_lighting = Transition(label='Configure Lighting')
water_recycling = Transition(label='Water Recycling')
monitor_growth = Transition(label='Monitor Growth')
data_analysis = Transition(label='Data Analysis')
automate_controls = Transition(label='Automate Controls')
community_workshop = Transition(label='Community Workshop')
local_distribution = Transition(label='Local Distribution')
performance_review = Transition(label='Performance Review')
scale_assessment = Transition(label='Scale Assessment')

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, structural_test, sunlight_map,
    design_plan, vendor_coordination, material_order,
    reinforce_roof, install_systems, calibrate_sensors,
    select_crops, setup_hydroponics, configure_lighting,
    water_recycling, monitor_growth, data_analysis,
    automate_controls, community_workshop, local_distribution,
    performance_review, scale_assessment
])

# Site evaluation -> design planning
root.order.add_edge(site_survey, design_plan)
root.order.add_edge(structural_test, design_plan)
root.order.add_edge(sunlight_map, design_plan)

# Design plan -> procurement & crop selection
root.order.add_edge(design_plan, vendor_coordination)
root.order.add_edge(vendor_coordination, material_order)
root.order.add_edge(design_plan, select_crops)

# Procurement -> installation start
root.order.add_edge(material_order, reinforce_roof)

# Installation sequence
root.order.add_edge(reinforce_roof, install_systems)
root.order.add_edge(install_systems, calibrate_sensors)

# After calibration + crops chosen -> system setup
root.order.add_edge(calibrate_sensors, setup_hydroponics)
root.order.add_edge(select_crops, setup_hydroponics)

# Setup modules
root.order.add_edge(setup_hydroponics, configure_lighting)
root.order.add_edge(setup_hydroponics, water_recycling)

# Once systems are in place -> start monitoring
root.order.add_edge(configure_lighting, monitor_growth)
root.order.add_edge(water_recycling, monitor_growth)

# Monitoring -> analysis -> automation
root.order.add_edge(monitor_growth, data_analysis)
root.order.add_edge(data_analysis, automate_controls)

# After automation -> community engagement
root.order.add_edge(automate_controls, community_workshop)
root.order.add_edge(automate_controls, local_distribution)

# Engagement & automation feed into review
root.order.add_edge(community_workshop, performance_review)
root.order.add_edge(local_distribution, performance_review)
root.order.add_edge(automate_controls, performance_review)

# Final scalability assessment
root.order.add_edge(performance_review, scale_assessment)