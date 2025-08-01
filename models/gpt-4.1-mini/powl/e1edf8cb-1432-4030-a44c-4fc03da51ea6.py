# Generated from: e1edf8cb-1432-4030-a44c-4fc03da51ea6.json
# Description: This process outlines the setup of an urban vertical farming system within a repurposed industrial building. It involves site analysis, environmental control installation, hydroponic system configuration, crop selection based on urban demand, integration of IoT sensors for monitoring, staff training on automated systems, and establishing supply chain logistics for fresh produce delivery. The process ensures optimal space utilization, sustainability, and year-round crop production despite urban constraints, incorporating waste recycling and energy efficiency measures to reduce operational costs and environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Site_Survey = Transition(label='Site Survey')
Structural_Check = Transition(label='Structural Check')
Env_Control = Transition(label='Env Control')
Hydro_Setup = Transition(label='Hydro Setup')
Crop_Select = Transition(label='Crop Select')
IoT_Install = Transition(label='IoT Install')
Sensor_Calibrate = Transition(label='Sensor Calibrate')
Water_Cycle = Transition(label='Water Cycle')
Nutrient_Mix = Transition(label='Nutrient Mix')
Lighting_Adjust = Transition(label='Lighting Adjust')
Staff_Train = Transition(label='Staff Train')
Waste_Manage = Transition(label='Waste Manage')
Energy_Audit = Transition(label='Energy Audit')
Harvest_Plan = Transition(label='Harvest Plan')
Delivery_Setup = Transition(label='Delivery Setup')
Market_Align = Transition(label='Market Align')

# Partial orders representing concurrent/partially ordered steps

# Initial site analysis steps: Site Survey then Structural Check
site_analysis = StrictPartialOrder(nodes=[Site_Survey, Structural_Check])
site_analysis.order.add_edge(Site_Survey, Structural_Check)

# Environmental control installation: Env Control then Hydro Setup (dependency)
env_install = StrictPartialOrder(nodes=[Env_Control, Hydro_Setup])
env_install.order.add_edge(Env_Control, Hydro_Setup)

# Crop preparation includes Crop Select, then parallel IoT Install and Staff Train (concurrent)
crop_select = Crop_Select

iot_sensor_calib = StrictPartialOrder(nodes=[IoT_Install, Sensor_Calibrate])
iot_sensor_calib.order.add_edge(IoT_Install, Sensor_Calibrate)

# Water cycle, Nutrient Mix, Lighting Adjust are concurrent environmental routines
env_routines = StrictPartialOrder(nodes=[Water_Cycle, Nutrient_Mix, Lighting_Adjust])
# no order edges: fully concurrent

# Waste Manage and Energy Audit are concurrent sustainability measures
sustain_measures = StrictPartialOrder(nodes=[Waste_Manage, Energy_Audit])
# no order edges

# Harvest planning followed by delivery setup and market alignment (delivery setup before market align)
harvest_delivery = StrictPartialOrder(nodes=[Harvest_Plan, Delivery_Setup, Market_Align])
harvest_delivery.order.add_edge(Harvest_Plan, Delivery_Setup)
harvest_delivery.order.add_edge(Delivery_Setup, Market_Align)

# Combine IoT calibration with environmental routines (Sensor Calibrate before concurrent Water Cycle, Nutrient Mix, Lighting Adjust)
iot_and_env_routines = StrictPartialOrder(
    nodes=[iot_sensor_calib, Water_Cycle, Nutrient_Mix, Lighting_Adjust])
iot_and_env_routines.order.add_edge(iot_sensor_calib, Water_Cycle)
iot_and_env_routines.order.add_edge(iot_sensor_calib, Nutrient_Mix)
iot_and_env_routines.order.add_edge(iot_sensor_calib, Lighting_Adjust)

# Staff Train is after Crop Select but can overlap with iot_and_env_routines (assume after crop select)
crop_and_train = StrictPartialOrder(nodes=[Crop_Select, Staff_Train])
crop_and_train.order.add_edge(Crop_Select, Staff_Train)

# Combine crop_and_train and iot_and_env_routines concurrently (no order edges between them)
crop_train_env_parallel = StrictPartialOrder(
    nodes=[crop_and_train, iot_and_env_routines])
# no order edges between these two partial orders => concurrency

# Combine env_install before crop_train_env_parallel
env_before_croptrain = StrictPartialOrder(
    nodes=[env_install, crop_train_env_parallel])
env_before_croptrain.order.add_edge(env_install, crop_train_env_parallel)

# Sustainability measures after env and crop related steps
sust_after_env_crop = StrictPartialOrder(
    nodes=[env_before_croptrain, sustain_measures])
sust_after_env_crop.order.add_edge(env_before_croptrain, sustain_measures)

# Harvest and delivery after sustainability
all_before_harvest = StrictPartialOrder(
    nodes=[sust_after_env_crop, harvest_delivery])
all_before_harvest.order.add_edge(sust_after_env_crop, harvest_delivery)

# Combine with initial site analysis before everything else
root = StrictPartialOrder(
    nodes=[site_analysis, all_before_harvest])
root.order.add_edge(site_analysis, all_before_harvest)