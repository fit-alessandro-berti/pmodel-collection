# Generated from: 5eb2e3f6-4b85-44be-9267-5e2d2f64bf64.json
# Description: This process involves the end-to-end deployment of an urban vertical farming system in dense metropolitan areas. It begins with site analysis and regulatory compliance checks, followed by modular farm design tailored to the building structure. Procurement of specialized hydroponic equipment and nutrient solutions is critical, alongside the integration of IoT sensors for climate control. Installation includes assembling grow racks, lighting, and irrigation systems. Post-installation, calibration of environmental controls ensures optimal plant growth. Staff training on maintenance and data monitoring is conducted before initiating the crop seeding phase. Continuous monitoring, pest management, and yield optimization are performed throughout the growth cycle. Finally, harvested produce is packaged and distributed locally, completing the sustainable urban agriculture supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_analysis    = Transition(label='Site Analysis')
permits_check    = Transition(label='Permits Check')
farm_design      = Transition(label='Farm Design')
equipment_buy    = Transition(label='Equipment Buy')
nutrient_prep    = Transition(label='Nutrient Prep')
sensor_setup     = Transition(label='Sensor Setup')
rack_install     = Transition(label='Rack Install')
light_config     = Transition(label='Light Config')
irrigation_fit   = Transition(label='Irrigation Fit')
enviro_calib     = Transition(label='Enviro Calibrate')
staff_training   = Transition(label='Staff Training')
crop_seeding     = Transition(label='Crop Seeding')
growth_monitor   = Transition(label='Growth Monitor')
pest_control     = Transition(label='Pest Control')
yield_optimize   = Transition(label='Yield Optimize')
harvest_pack     = Transition(label='Harvest Pack')
local_deliver    = Transition(label='Local Deliver')

# Parallel procurement: Equipment Buy, Nutrient Prep, Sensor Setup
parallel_procure = StrictPartialOrder(nodes=[equipment_buy,
                                             nutrient_prep,
                                             sensor_setup])
# Parallel installation: Rack Install, Light Config, Irrigation Fit
parallel_install = StrictPartialOrder(nodes=[rack_install,
                                             light_config,
                                             irrigation_fit])

# Loop for continuous monitoring, pest control, yield optimization
# A = growth_monitor, B = (pest_control || yield_optimize)
loop_body = StrictPartialOrder(nodes=[pest_control, yield_optimize])
monitor_loop = OperatorPOWL(operator=Operator.LOOP,
                            children=[growth_monitor, loop_body])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    site_analysis,
    permits_check,
    farm_design,
    parallel_procure,
    parallel_install,
    enviro_calib,
    staff_training,
    crop_seeding,
    monitor_loop,
    harvest_pack,
    local_deliver
])

# Define the control‐flow edges
root.order.add_edge(site_analysis,    permits_check)
root.order.add_edge(permits_check,    farm_design)
root.order.add_edge(farm_design,      parallel_procure)
root.order.add_edge(parallel_procure, parallel_install)
root.order.add_edge(parallel_install, enviro_calib)
root.order.add_edge(enviro_calib,     staff_training)
root.order.add_edge(staff_training,   crop_seeding)
root.order.add_edge(crop_seeding,     monitor_loop)
root.order.add_edge(monitor_loop,     harvest_pack)
root.order.add_edge(harvest_pack,     local_deliver)