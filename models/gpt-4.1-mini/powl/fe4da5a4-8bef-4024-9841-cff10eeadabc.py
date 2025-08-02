# Generated from: fe4da5a4-8bef-4024-9841-cff10eeadabc.json
# Description: This process describes the complex and atypical business workflow for establishing an urban rooftop farm on commercial buildings. It includes securing permits, structural assessments, soil and water testing, sourcing sustainable materials, installing modular planters, integrating IoT sensors for environmental monitoring, setting up automated irrigation systems, coordinating with local vendors for organic seeds, training staff on urban agriculture practices, implementing pest control measures, marketing fresh produce to local restaurants, managing seasonal crop rotation, ensuring compliance with city health regulations, and establishing waste composting protocols to maintain environmental sustainability and maximize yield within limited urban space.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Permit_Securing = Transition(label='Permit Securing')
Structure_Check = Transition(label='Structure Check')
Soil_Testing = Transition(label='Soil Testing')
Water_Analysis = Transition(label='Water Analysis')
Material_Sourcing = Transition(label='Material Sourcing')
Planter_Setup = Transition(label='Planter Setup')
Sensor_Install = Transition(label='Sensor Install')
Irrigation_Setup = Transition(label='Irrigation Setup')
Vendor_Liaison = Transition(label='Vendor Liaison')
Staff_Training = Transition(label='Staff Training')
Pest_Control = Transition(label='Pest Control')
Produce_Marketing = Transition(label='Produce Marketing')
Crop_Rotation = Transition(label='Crop Rotation')
Health_Audit = Transition(label='Health Audit')
Waste_Composting = Transition(label='Waste Composting')

# Model partial order based on described logical dependencies
# Logical flow assumptions (typical/business logic):
# 1) Permits before any structural or soil/water analysis
# 2) Structure check before planters setup
# 3) Soil and water testing may be concurrent after permit, before planter/material setup
# 4) Material sourcing before planter setup
# 5) Sensor install and irrigation setup after planter setup
# 6) Vendor liaison & staff training can be concurrent after irrigation and sensor setup
# 7) Pest control after staff training
# 8) Produce marketing after pest control
# 9) Crop rotation after produce marketing (seasonal)
# 10) Health audit after crop rotation
# 11) Waste composting after health audit

root = StrictPartialOrder(nodes=[
    Permit_Securing,
    Structure_Check,
    Soil_Testing,
    Water_Analysis,
    Material_Sourcing,
    Planter_Setup,
    Sensor_Install,
    Irrigation_Setup,
    Vendor_Liaison,
    Staff_Training,
    Pest_Control,
    Produce_Marketing,
    Crop_Rotation,
    Health_Audit,
    Waste_Composting,
])

# Permit Securing before Structure Check, Soil Testing and Water Analysis and Material Sourcing
root.order.add_edge(Permit_Securing, Structure_Check)
root.order.add_edge(Permit_Securing, Soil_Testing)
root.order.add_edge(Permit_Securing, Water_Analysis)
root.order.add_edge(Permit_Securing, Material_Sourcing)

# Structure Check before Planter Setup
root.order.add_edge(Structure_Check, Planter_Setup)
# Soil Testing before Planter Setup (must be done before planters installed)
root.order.add_edge(Soil_Testing, Planter_Setup)
# Water Analysis before Planter Setup
root.order.add_edge(Water_Analysis, Planter_Setup)
# Material Sourcing before Planter Setup
root.order.add_edge(Material_Sourcing, Planter_Setup)

# Planter Setup before Sensor Install and Irrigation Setup
root.order.add_edge(Planter_Setup, Sensor_Install)
root.order.add_edge(Planter_Setup, Irrigation_Setup)

# Sensor Install and Irrigation Setup before Vendor Liaison and Staff Training
root.order.add_edge(Sensor_Install, Vendor_Liaison)
root.order.add_edge(Sensor_Install, Staff_Training)
root.order.add_edge(Irrigation_Setup, Vendor_Liaison)
root.order.add_edge(Irrigation_Setup, Staff_Training)

# Vendor Liaison and Staff Training unordered (concurrent)
# Staff Training before Pest Control
root.order.add_edge(Staff_Training, Pest_Control)

# Pest Control before Produce Marketing
root.order.add_edge(Pest_Control, Produce_Marketing)

# Produce Marketing before Crop Rotation
root.order.add_edge(Produce_Marketing, Crop_Rotation)

# Crop Rotation before Health Audit
root.order.add_edge(Crop_Rotation, Health_Audit)

# Health Audit before Waste Composting
root.order.add_edge(Health_Audit, Waste_Composting)