# Generated from: 9aea699d-7ff7-4c19-b39d-3b5a0915817d.json
# Description: This process outlines the comprehensive steps involved in establishing an urban rooftop farming operation on a commercial building. It begins with structural assessments to ensure load capacity, followed by microclimate analysis to optimize plant selection and layout. Procurement of sustainable materials and soil substrates occurs next, alongside installation of automated irrigation systems and solar-powered lighting. Continuous integration of sensor networks allows real-time monitoring of moisture, temperature, and nutrient levels. Staff training in urban agriculture techniques and safety protocols ensures efficient daily operations. Finally, the process includes marketing strategies targeting local restaurants and community programs to promote farm-to-table initiatives, ensuring economic viability and social impact within urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as POWL transitions
load_check     = Transition(label="Load Check")
climate_scan   = Transition(label="Climate Scan")
material_buy   = Transition(label="Material Buy")
soil_prep      = Transition(label="Soil Prep")
irrigation_fit = Transition(label="Irrigation Fit")
lighting_setup = Transition(label="Lighting Setup")
sensor_install = Transition(label="Sensor Install")
data_sync      = Transition(label="Data Sync")
crop_select    = Transition(label="Crop Select")
staff_train    = Transition(label="Staff Train")
safety_drill   = Transition(label="Safety Drill")
harvest_plan   = Transition(label="Harvest Plan")
market_out     = Transition(label="Market Outreach")
community_eng  = Transition(label="Community Engage")
waste_manage   = Transition(label="Waste Manage")
energy_audit   = Transition(label="Energy Audit")
yield_assess   = Transition(label="Yield Assess")

# Build the partial order
root = StrictPartialOrder(nodes=[
    load_check, climate_scan,
    material_buy, soil_prep, irrigation_fit, lighting_setup,
    sensor_install, data_sync, crop_select,
    staff_train, safety_drill,
    harvest_plan, market_out, community_eng,
    waste_manage, energy_audit, yield_assess
])

# Structural assessment then climate scan
root.order.add_edge(load_check, climate_scan)

# After climate scan, procurement and installations run in parallel
for nxt in [material_buy, soil_prep, irrigation_fit, lighting_setup]:
    root.order.add_edge(climate_scan, nxt)

# Once procurement & installations are done, install sensors
for prev in [material_buy, soil_prep, irrigation_fit, lighting_setup]:
    root.order.add_edge(prev, sensor_install)

# Sensor install -> data sync -> crop selection
root.order.add_edge(sensor_install, data_sync)
root.order.add_edge(data_sync, crop_select)

# Crop selection -> staff training -> safety drill
root.order.add_edge(crop_select, staff_train)
root.order.add_edge(staff_train, safety_drill)

# After safety, plan the harvest
root.order.add_edge(safety_drill, harvest_plan)

# Harvest plan leads to marketing & community engagement in parallel
root.order.add_edge(harvest_plan, market_out)
root.order.add_edge(harvest_plan, community_eng)

# Join marketing & community into waste management
root.order.add_edge(market_out, waste_manage)
root.order.add_edge(community_eng, waste_manage)

# Final evaluation steps
root.order.add_edge(waste_manage, energy_audit)
root.order.add_edge(energy_audit, yield_assess)