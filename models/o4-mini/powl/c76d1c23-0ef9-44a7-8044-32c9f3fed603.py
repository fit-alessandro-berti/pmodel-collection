# Generated from: c76d1c23-0ef9-44a7-8044-32c9f3fed603.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farm within a densely populated city environment. It begins with site assessment and zoning approvals, followed by modular structure design and procurement of hydroponic systems. After installation, the farm undergoes environmental calibration to optimize light, humidity, and nutrient delivery. Crop selection is tailored to local demand and growth cycles. Continuous monitoring and adaptive pest management ensure sustainable yields. The process concludes with harvest scheduling, packaging, and distribution logistics targeted at local markets, while integrating data analytics for ongoing optimization and scalability of operations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_survey      = Transition(label="Site Survey")
zoning_check     = Transition(label="Zoning Check")
design_layout    = Transition(label="Design Layout")
system_order     = Transition(label="System Order")
structure_build  = Transition(label="Structure Build")
install_hydro    = Transition(label="Install Hydroponics")
calibrate        = Transition(label="Calibrate Sensors")
select_crops     = Transition(label="Select Crops")
plant_seeding    = Transition(label="Plant Seeding")
monitor_growth   = Transition(label="Monitor Growth")
manage_pests     = Transition(label="Manage Pests")
schedule_harvest = Transition(label="Schedule Harvest")
package_produce  = Transition(label="Package Produce")
local_delivery   = Transition(label="Local Delivery")
analyze_data     = Transition(label="Analyze Data")

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, zoning_check, design_layout, system_order,
    structure_build, install_hydro, calibrate, select_crops,
    plant_seeding, monitor_growth, manage_pests, schedule_harvest,
    package_produce, local_delivery, analyze_data
])

# Sequential flow up to installation calibration
root.order.add_edge(site_survey, zoning_check)
root.order.add_edge(zoning_check, design_layout)
root.order.add_edge(design_layout, system_order)
root.order.add_edge(system_order, structure_build)
root.order.add_edge(structure_build, install_hydro)
root.order.add_edge(install_hydro, calibrate)

# After calibration: crop selection and data analysis in parallel
root.order.add_edge(calibrate, select_crops)
root.order.add_edge(calibrate, analyze_data)

# From crop selection to planting
root.order.add_edge(select_crops, plant_seeding)

# Monitoring and pest management start after seeding (can run concurrently)
root.order.add_edge(plant_seeding, monitor_growth)
root.order.add_edge(plant_seeding, manage_pests)

# Harvest scheduling waits for both monitoring and pest management
root.order.add_edge(monitor_growth, schedule_harvest)
root.order.add_edge(manage_pests, schedule_harvest)

# Final logistics
root.order.add_edge(schedule_harvest, package_produce)
root.order.add_edge(package_produce, local_delivery)