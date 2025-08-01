# Generated from: ce370660-2e0d-48a2-b656-f42125ba06a3.json
# Description: This process outlines the establishment of a sustainable urban rooftop farm on a commercial building. It involves initial structural assessments to ensure load capacity, followed by modular soil bed installation adapted for limited space. Specialized irrigation systems are integrated to optimize water usage, alongside solar-powered sensors for real-time monitoring of crop health. The process also includes obtaining necessary permits, community engagement for local support, and coordinated logistics for seed and nutrient delivery. Finally, staff training on hydroponic techniques and ongoing maintenance schedules ensure the farm’s productivity and environmental benefits are maximized throughout the year.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Structural_Check = Transition(label='Structural Check')
Permit_Apply = Transition(label='Permit Apply')
Design_Layout = Transition(label='Design Layout')
Soil_Prep = Transition(label='Soil Prep')
Bed_Install = Transition(label='Bed Install')
Irrigation_Setup = Transition(label='Irrigation Setup')
Sensor_Mount = Transition(label='Sensor Mount')
Solar_Connect = Transition(label='Solar Connect')
Seed_Order = Transition(label='Seed Order')
Nutrient_Mix = Transition(label='Nutrient Mix')
Community_Meet = Transition(label='Community Meet')
Staff_Train = Transition(label='Staff Train')
Plant_Crop = Transition(label='Plant Crop')
Maintenance_Plan = Transition(label='Maintenance Plan')
Harvest_Schedule = Transition(label='Harvest Schedule')
Waste_Manage = Transition(label='Waste Manage')

# Structural assessments then design layout
struct_assess = StrictPartialOrder(nodes=[Structural_Check, Design_Layout])
struct_assess.order.add_edge(Structural_Check, Design_Layout)

# Soil bed installation modular steps: Soil Prep then Bed Install
soil_bed = StrictPartialOrder(nodes=[Soil_Prep, Bed_Install])
soil_bed.order.add_edge(Soil_Prep, Bed_Install)

# Specialized irrigation and sensors setup partially concurrent:
# Irrigation Setup then Sensor Mount and Solar Connect can be concurrent
# Model Sensor Mount and Solar Connect as a PO without order (concurrent)
sensor_setup = StrictPartialOrder(nodes=[Sensor_Mount, Solar_Connect])

irrigation_and_sensor = StrictPartialOrder(nodes=[Irrigation_Setup, sensor_setup])
irrigation_and_sensor.order.add_edge(Irrigation_Setup, sensor_setup)

# Permits and community engagement can be concurrent but both before logistics
# Logistics includes Seed Order and Nutrient Mix that can be concurrent
seed_nutrient = StrictPartialOrder(nodes=[Seed_Order, Nutrient_Mix])

perm_comm = StrictPartialOrder(nodes=[Permit_Apply, Community_Meet])  # concurrent

# Staff training then plant crop
staff_plant = StrictPartialOrder(nodes=[Staff_Train, Plant_Crop])
staff_plant.order.add_edge(Staff_Train, Plant_Crop)

# Maintenance Plan and Harvest Schedule concurrent (ongoing schedules)
maintenance_harvest = StrictPartialOrder(nodes=[Maintenance_Plan, Harvest_Schedule])

# Waste management can happen after harvest schedule
maint_harvest_waste = StrictPartialOrder(nodes=[maintenance_harvest, Waste_Manage])
maint_harvest_waste.order.add_edge(maintenance_harvest, Waste_Manage)

# Organize the whole flow:
# 1) Structural assessment and design
# 2) Soil bed installation
# 3) Irrigation and sensors setup
# 4) Permits and community meeting
# 5) Logistics (Seed Order and Nutrient Mix)
# 6) Staff training and planting
# 7) Maintenance and harvest with waste management

# Compose logistics after permits & community
perm_comm_logistics = StrictPartialOrder(nodes=[perm_comm, seed_nutrient])
perm_comm_logistics.order.add_edge(perm_comm, seed_nutrient)

# Compose after soil bed
soil_irrig_sensor = StrictPartialOrder(nodes=[soil_bed, irrigation_and_sensor])
soil_irrig_sensor.order.add_edge(soil_bed, irrigation_and_sensor)

# Compose whole first part: structural/design -> soil/bed -> irrigation/sensor
preparation = StrictPartialOrder(nodes=[struct_assess, soil_irrig_sensor])
preparation.order.add_edge(struct_assess, soil_irrig_sensor)

# Compose preparation -> permits+community+logistics
prep_perms_comm = StrictPartialOrder(nodes=[preparation, perm_comm_logistics])
prep_perms_comm.order.add_edge(preparation, perm_comm_logistics)

# Compose next staff training and planting after permits/logistics
pre_plant = StrictPartialOrder(nodes=[prep_perms_comm, staff_plant])
pre_plant.order.add_edge(prep_perms_comm, staff_plant)

# Compose final maintenance and waste after planting
final_phase = StrictPartialOrder(nodes=[pre_plant, maint_harvest_waste])
final_phase.order.add_edge(pre_plant, maint_harvest_waste)

root = final_phase