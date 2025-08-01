# Generated from: 5eeb4440-3958-43b1-945f-8de92f3d7534.json
# Description: This process involves establishing an urban vertical farming system within a repurposed commercial building. It begins with site evaluation and environmental assessment, followed by modular design planning tailored for space optimization. The process includes procurement of hydroponic equipment, installation of LED grow lights, and integration of automated nutrient delivery systems. Subsequent activities cover seeding, climate control calibration, and continuous monitoring using IoT sensors. Crop rotation schedules are developed alongside pest management strategies that emphasize biological controls. Harvesting is coordinated with urban distribution logistics, including cold storage and last-mile delivery to local markets. The process concludes with data analysis for yield optimization and sustainability reporting to stakeholders.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
site_eval = Transition(label='Site Eval')
env_assessment = Transition(label='Env Assessment')
modular_design = Transition(label='Modular Design')
equip_procure = Transition(label='Equip Procure')
light_install = Transition(label='Light Install')
nutrient_setup = Transition(label='Nutrient Setup')
seed_planting = Transition(label='Seed Planting')
climate_calibrate = Transition(label='Climate Calibrate')
sensor_install = Transition(label='Sensor Install')
crop_rotation = Transition(label='Crop Rotation')
pest_control = Transition(label='Pest Control')
harvest_crop = Transition(label='Harvest Crop')
cold_storage = Transition(label='Cold Storage')
delivery_plan = Transition(label='Delivery Plan')
data_analyze = Transition(label='Data Analyze')
report_generate = Transition(label='Report Generate')

# Create a partial order for the main linear flow
root = StrictPartialOrder(nodes=[
    site_eval, env_assessment, modular_design, 
    equip_procure, light_install, nutrient_setup,
    seed_planting, climate_calibrate, sensor_install,
    crop_rotation, pest_control,
    harvest_crop, cold_storage, delivery_plan,
    data_analyze, report_generate
])

# Add edges for the sequential flow
root.order.add_edge(site_eval, env_assessment)
root.order.add_edge(env_assessment, modular_design)
root.order.add_edge(modular_design, equip_procure)
root.order.add_edge(equip_procure, light_install)
root.order.add_edge(light_install, nutrient_setup)

root.order.add_edge(nutrient_setup, seed_planting)
root.order.add_edge(seed_planting, climate_calibrate)
root.order.add_edge(climate_calibrate, sensor_install)

root.order.add_edge(sensor_install, crop_rotation)
root.order.add_edge(sensor_install, pest_control)
# crop_rotation and pest_control are concurrent after sensor_install
# no order edge between crop_rotation and pest_control

root.order.add_edge(crop_rotation, harvest_crop)
root.order.add_edge(pest_control, harvest_crop)

root.order.add_edge(harvest_crop, cold_storage)
root.order.add_edge(cold_storage, delivery_plan)
root.order.add_edge(delivery_plan, data_analyze)
root.order.add_edge(data_analyze, report_generate)