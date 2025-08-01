# Generated from: 65cd00ff-08f7-4739-823f-cc40fa8e4833.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farm designed to maximize crop yield in limited city spaces. It includes site analysis, modular infrastructure assembly, climate control calibration, nutrient solution preparation, automated planting, growth monitoring through IoT sensors, pest management with integrated biocontrol, adaptive lighting adjustment, harvesting automation, post-harvest processing, packaging, and distribution logistics. The process also involves continuous data analysis for yield optimization and sustainability reporting to comply with local regulations and environmental standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
site_survey      = Transition(label='Site Survey')
design_layout    = Transition(label='Design Layout')
module_setup     = Transition(label='Module Setup')
climate_calibrate= Transition(label='Climate Calibrate')
nutrient_mix     = Transition(label='Nutrient Mix')
plant_seeding    = Transition(label='Plant Seeding')
sensor_install   = Transition(label='Sensor Install')
growth_monitor   = Transition(label='Growth Monitor')
pest_control     = Transition(label='Pest Control')
light_adjust     = Transition(label='Light Adjust')
harvest_crop     = Transition(label='Harvest Crop')
process_sorting  = Transition(label='Process Sorting')
pack_goods       = Transition(label='Pack Goods')
logistics_plan   = Transition(label='Logistics Plan')
data_analysis    = Transition(label='Data Analysis')
sustain_report   = Transition(label='Sustain Report')

# Create a strict partial order and add the activities in sequence
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    module_setup,
    climate_calibrate,
    nutrient_mix,
    plant_seeding,
    sensor_install,
    growth_monitor,
    pest_control,
    light_adjust,
    harvest_crop,
    process_sorting,
    pack_goods,
    logistics_plan,
    data_analysis,
    sustain_report
])

# Add the sequential ordering edges
sequence = [
    site_survey, design_layout, module_setup, climate_calibrate, nutrient_mix,
    plant_seeding, sensor_install, growth_monitor, pest_control, light_adjust,
    harvest_crop, process_sorting, pack_goods, logistics_plan, data_analysis,
    sustain_report
]
for src, tgt in zip(sequence, sequence[1:]):
    root.order.add_edge(src, tgt)