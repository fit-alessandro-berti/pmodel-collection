# Generated from: 766e4357-8030-4747-9c04-6327337299fd.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farm within a repurposed industrial building. It involves site analysis, modular system design, climate control optimization, hydroponic nutrient calibration, automation integration, crop scheduling, pest management, yield forecasting, and community engagement. The process ensures sustainable food production in dense city environments by leveraging IoT sensors, renewable energy sources, and real-time data analytics. It also addresses regulatory compliance, waste recycling, and post-harvest logistics to maximize efficiency and environmental impact. The coordination between multidisciplinary teams, from architects to agronomists, is critical for success.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey = Transition(label='Site Survey')
design_modules = Transition(label='Design Modules')
climate_setup = Transition(label='Climate Setup')
nutrient_mix = Transition(label='Nutrient Mix')
sensor_install = Transition(label='Sensor Install')
automation_sync = Transition(label='Automation Sync')
crop_plan = Transition(label='Crop Plan')
pest_control = Transition(label='Pest Control')
yield_model = Transition(label='Yield Model')
energy_audit = Transition(label='Energy Audit')
compliance_check = Transition(label='Compliance Check')
waste_setup = Transition(label='Waste Setup')
harvest_prep = Transition(label='Harvest Prep')
data_monitor = Transition(label='Data Monitor')
community_meet = Transition(label='Community Meet')

# Coordination between multidisciplinary teams is implied by concurrency of foundational steps:
# Step 1: Site Survey --> Design Modules
# Step 2: Parallel branches after Design Modules:
#    - Climate Setup --> Nutrient Mix
#    - Sensor Install --> Automation Sync
# Parallel branches indicate concurrency, so partial order will model this as concurrent nodes.

# After Climate Setup and Nutrient Mix, Crop Plan follows.
# After Sensor Install and Automation Sync, Pest Control follows.

# Crop Plan and Pest Control precede Yield Model.
# Energy Audit, Compliance Check, and Waste Setup happen concurrently and precede Harvest Prep.
# Harvest Prep precedes Data Monitor.
# Data Monitor precedes Community Meet.

# Construct partial order nodes and edges according to dependencies:
nodes = [
    site_survey,
    design_modules,
    climate_setup,
    nutrient_mix,
    sensor_install,
    automation_sync,
    crop_plan,
    pest_control,
    yield_model,
    energy_audit,
    compliance_check,
    waste_setup,
    harvest_prep,
    data_monitor,
    community_meet
]

root = StrictPartialOrder(nodes=nodes)

# Add edges reflecting dependencies:

# Site Survey -> Design Modules
root.order.add_edge(site_survey, design_modules)

# Design Modules -> Climate Setup and Sensor Install (concurrent)
root.order.add_edge(design_modules, climate_setup)
root.order.add_edge(design_modules, sensor_install)

# Climate Setup -> Nutrient Mix
root.order.add_edge(climate_setup, nutrient_mix)

# Nutrient Mix -> Crop Plan
root.order.add_edge(nutrient_mix, crop_plan)

# Sensor Install -> Automation Sync
root.order.add_edge(sensor_install, automation_sync)

# Automation Sync -> Pest Control
root.order.add_edge(automation_sync, pest_control)

# Crop Plan and Pest Control both precede Yield Model
root.order.add_edge(crop_plan, yield_model)
root.order.add_edge(pest_control, yield_model)

# Yield Model -> Energy Audit, Compliance Check, Waste Setup (concurrent)
root.order.add_edge(yield_model, energy_audit)
root.order.add_edge(yield_model, compliance_check)
root.order.add_edge(yield_model, waste_setup)

# Energy Audit, Compliance Check, Waste Setup all precede Harvest Prep
root.order.add_edge(energy_audit, harvest_prep)
root.order.add_edge(compliance_check, harvest_prep)
root.order.add_edge(waste_setup, harvest_prep)

# Harvest Prep -> Data Monitor
root.order.add_edge(harvest_prep, data_monitor)

# Data Monitor -> Community Meet
root.order.add_edge(data_monitor, community_meet)