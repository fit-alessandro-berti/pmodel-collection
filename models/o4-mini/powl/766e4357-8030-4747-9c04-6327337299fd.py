# Generated from: 766e4357-8030-4747-9c04-6327337299fd.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farm within a repurposed industrial building. It involves site analysis, modular system design, climate control optimization, hydroponic nutrient calibration, automation integration, crop scheduling, pest management, yield forecasting, and community engagement. The process ensures sustainable food production in dense city environments by leveraging IoT sensors, renewable energy sources, and real-time data analytics. It also addresses regulatory compliance, waste recycling, and post-harvest logistics to maximize efficiency and environmental impact. The coordination between multidisciplinary teams, from architects to agronomists, is critical for success.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the activities
site_survey      = Transition(label='Site Survey')
design_modules   = Transition(label='Design Modules')
climate_setup    = Transition(label='Climate Setup')
nutrient_mix     = Transition(label='Nutrient Mix')
sensor_install   = Transition(label='Sensor Install')
automation_sync  = Transition(label='Automation Sync')
crop_plan        = Transition(label='Crop Plan')
pest_control     = Transition(label='Pest Control')
yield_model      = Transition(label='Yield Model')
energy_audit     = Transition(label='Energy Audit')
compliance_check = Transition(label='Compliance Check')
waste_setup      = Transition(label='Waste Setup')
harvest_prep     = Transition(label='Harvest Prep')
data_monitor     = Transition(label='Data Monitor')
community_meet   = Transition(label='Community Meet')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_survey, design_modules, climate_setup, nutrient_mix,
    sensor_install, automation_sync, crop_plan, pest_control,
    yield_model, energy_audit, compliance_check, waste_setup,
    harvest_prep, data_monitor, community_meet
])

# Sequential core workflow
root.order.add_edge(site_survey, design_modules)
root.order.add_edge(design_modules, climate_setup)
root.order.add_edge(climate_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, sensor_install)
root.order.add_edge(sensor_install, automation_sync)
root.order.add_edge(automation_sync, crop_plan)
root.order.add_edge(crop_plan, pest_control)
root.order.add_edge(pest_control, yield_model)

# After yield forecasting, conduct audits and setup in parallel
root.order.add_edge(yield_model, energy_audit)
root.order.add_edge(yield_model, compliance_check)
root.order.add_edge(yield_model, waste_setup)

# All three must complete before harvesting prep
root.order.add_edge(energy_audit, harvest_prep)
root.order.add_edge(compliance_check, harvest_prep)
root.order.add_edge(waste_setup, harvest_prep)

# Real-time monitoring begins after automation sync
root.order.add_edge(automation_sync, data_monitor)

# Harvest prep completes before final community engagement
root.order.add_edge(harvest_prep, community_meet)
# And data analytics informs the community as well
root.order.add_edge(data_monitor, community_meet)