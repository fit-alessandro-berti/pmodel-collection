# Generated from: 19e34b23-3f55-4dd7-b5e2-e8f83a83dbb9.json
# Description: This process outlines the comprehensive setup of an urban vertical farm, integrating advanced hydroponics, AI-controlled environment systems, and modular construction techniques. It begins with site analysis and zoning approval, followed by designing multi-layer growth platforms and selecting crop varieties suited for vertical farming. Procurement involves sourcing sustainable materials and specialized equipment. Installation covers lighting, irrigation, and climate control systems. AI calibration ensures optimal growth conditions through sensor data integration. Staff training is conducted on system operation and maintenance. Post-installation, a trial cultivation phase verifies system efficiency. Finally, marketing strategies are deployed targeting local retailers and consumers to establish supply chains and promote farm-to-table initiatives.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
site_analysis = Transition(label='Site Analysis')
zoning_approval = Transition(label='Zoning Approval')
platform_design = Transition(label='Platform Design')
crop_selection = Transition(label='Crop Selection')
material_sourcing = Transition(label='Material Sourcing')
equipment_order = Transition(label='Equipment Order')
system_install = Transition(label='System Install')
lighting_setup = Transition(label='Lighting Setup')
irrigation_setup = Transition(label='Irrigation Setup')
climate_control = Transition(label='Climate Control')
ai_calibration = Transition(label='AI Calibration')
staff_training = Transition(label='Staff Training')
trial_cultivation = Transition(label='Trial Cultivation')
data_monitoring = Transition(label='Data Monitoring')
market_launch = Transition(label='Market Launch')

# Create partial orders for groups of activities that are concurrent or sequential

# Site Analysis --> Zoning Approval
step1 = StrictPartialOrder(nodes=[site_analysis, zoning_approval])
step1.order.add_edge(site_analysis, zoning_approval)

# Platform Design and Crop Selection are concurrent after Zoning Approval
step2 = StrictPartialOrder(nodes=[platform_design, crop_selection])
# No order edges means concurrent

# Material Sourcing --> Equipment Order in procurement
procurement = StrictPartialOrder(nodes=[material_sourcing, equipment_order])
procurement.order.add_edge(material_sourcing, equipment_order)

# Lighting Setup, Irrigation Setup, Climate Control all concurrent after System Install
installation_substeps = StrictPartialOrder(nodes=[lighting_setup, irrigation_setup, climate_control])
# concurrent, no edges

# System Install after procurement
installation = StrictPartialOrder(nodes=[system_install, installation_substeps])
installation.order.add_edge(system_install, installation_substeps)

# AI Calibration --> Staff Training
calibration_training = StrictPartialOrder(nodes=[ai_calibration, staff_training])
calibration_training.order.add_edge(ai_calibration, staff_training)

# Trial Cultivation and Data Monitoring concurrent after Staff Training
post_install = StrictPartialOrder(nodes=[trial_cultivation, data_monitoring])
# concurrent, no edges

# Market Launch after Trial Cultivation and Data Monitoring
market = StrictPartialOrder(nodes=[post_install, market_launch])
market.order.add_edge(post_install, market_launch)

# Combine smaller steps into larger partial orders with their dependencies

# Step1 --> Step2 (Zoning Approval --> Platform Design and Crop Selection)
step1_2 = StrictPartialOrder(nodes=[step1, step2])
step1_2.order.add_edge(step1, step2)

# Step2 --> Procurement
step2_procurement = StrictPartialOrder(nodes=[step2, procurement])
step2_procurement.order.add_edge(step2, procurement)

# Procurement --> Installation
procurement_installation = StrictPartialOrder(nodes=[procurement, installation])
procurement_installation.order.add_edge(procurement, installation)

# Installation --> AI Calibration & Staff Training
install_caltrain = StrictPartialOrder(nodes=[installation, calibration_training])
install_caltrain.order.add_edge(installation, calibration_training)

# CalibrationTraining --> Post Installation (Trial Cultivation, Data Monitoring)
caltrain_post = StrictPartialOrder(nodes=[calibration_training, post_install])
caltrain_post.order.add_edge(calibration_training, post_install)

# Post Installation --> Market Launch
post_market = StrictPartialOrder(nodes=[post_install, market_launch])
post_market.order.add_edge(post_install, market_launch)

# Combine entire process respecting all dependencies
root = StrictPartialOrder(
    nodes=[
        site_analysis,
        zoning_approval,
        platform_design,
        crop_selection,
        material_sourcing,
        equipment_order,
        system_install,
        lighting_setup,
        irrigation_setup,
        climate_control,
        ai_calibration,
        staff_training,
        trial_cultivation,
        data_monitoring,
        market_launch,
    ]
)

# Add edges that encode the defined sequential dependencies:

# Site Analysis --> Zoning Approval
root.order.add_edge(site_analysis, zoning_approval)

# Zoning Approval --> Platform Design and Crop Selection (both concurrent)
root.order.add_edge(zoning_approval, platform_design)
root.order.add_edge(zoning_approval, crop_selection)

# Platform Design and Crop Selection finish before procurement starts
root.order.add_edge(platform_design, material_sourcing)
root.order.add_edge(crop_selection, material_sourcing)

# Material Sourcing --> Equipment Order
root.order.add_edge(material_sourcing, equipment_order)

# Equipment Order finishes before System Install
root.order.add_edge(equipment_order, system_install)

# System Install --> Lighting Setup, Irrigation Setup, Climate Control (all concurrent)
root.order.add_edge(system_install, lighting_setup)
root.order.add_edge(system_install, irrigation_setup)
root.order.add_edge(system_install, climate_control)

# After installation substeps complete, AI Calibration starts
root.order.add_edge(lighting_setup, ai_calibration)
root.order.add_edge(irrigation_setup, ai_calibration)
root.order.add_edge(climate_control, ai_calibration)

# AI Calibration --> Staff Training
root.order.add_edge(ai_calibration, staff_training)

# Staff Training --> Trial Cultivation and Data Monitoring (concurrent)
root.order.add_edge(staff_training, trial_cultivation)
root.order.add_edge(staff_training, data_monitoring)

# Trial Cultivation and Data Monitoring finish before Market Launch
root.order.add_edge(trial_cultivation, market_launch)
root.order.add_edge(data_monitoring, market_launch)