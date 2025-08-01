# Generated from: 1f4b255d-e4d4-4e23-8303-6eac7be6b396.json
# Description: This process outlines the establishment of a vertical farming system within an urban environment, integrating advanced hydroponic techniques, automated climate control, and sustainable energy sources. It involves site analysis, modular structure assembly, nutrient solution preparation, sensor calibration, crop selection, growth monitoring, pest management using bio-controls, and yield optimization. The process ensures minimal water usage and maximizes space efficiency while adhering to local regulations and community engagement for urban agriculture promotion. Continuous data analysis and iterative improvements maintain crop health and operational sustainability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
site_survey      = Transition(label='Site Survey')
permit_check     = Transition(label='Permit Check')
design_layout    = Transition(label='Design Layout')
structure_build  = Transition(label='Structure Build')
install_lighting = Transition(label='Install Lighting')
setup_hydroponics= Transition(label='Setup Hydroponics')
prepare_nutrients= Transition(label='Prepare Nutrients')
calibrate_sensors= Transition(label='Calibrate Sensors')
select_crops     = Transition(label='Select Crops')
plant_seeding    = Transition(label='Plant Seeding')
climate_adjust   = Transition(label='Climate Adjust')
monitor_growth   = Transition(label='Monitor Growth')
pest_control     = Transition(label='Pest Control')
data_logging     = Transition(label='Data Logging')
harvest_cycle    = Transition(label='Harvest Cycle')
waste_manage     = Transition(label='Waste Manage')
community_outreach = Transition(label='Community Outreach')

# Build the loop body for the growth-monitoring cycle
growth_block = StrictPartialOrder(nodes=[
    monitor_growth, data_logging, pest_control, climate_adjust
])
growth_block.order.add_edge(monitor_growth, data_logging)
growth_block.order.add_edge(monitor_growth, pest_control)
growth_block.order.add_edge(data_logging, climate_adjust)
growth_block.order.add_edge(pest_control, climate_adjust)

# Loop operator to model iterative improvements / continuous cycle
# children[0] = initial block, children[1] = redo block (repeat same steps)
growth_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_block, growth_block]
)

# Assemble the overall process as a partial order
root = StrictPartialOrder(nodes=[
    site_survey, permit_check, design_layout,
    structure_build, install_lighting, setup_hydroponics,
    prepare_nutrients, calibrate_sensors, select_crops,
    plant_seeding, growth_loop, harvest_cycle,
    waste_manage, community_outreach
])

# Define control-flow dependencies
root.order.add_edge(site_survey,      permit_check)
root.order.add_edge(permit_check,     design_layout)
root.order.add_edge(design_layout,    structure_build)
root.order.add_edge(structure_build,  install_lighting)
root.order.add_edge(structure_build,  setup_hydroponics)
root.order.add_edge(install_lighting, prepare_nutrients)
root.order.add_edge(setup_hydroponics,prepare_nutrients)
root.order.add_edge(prepare_nutrients,calibrate_sensors)
root.order.add_edge(calibrate_sensors,select_crops)
root.order.add_edge(select_crops,     plant_seeding)
root.order.add_edge(plant_seeding,    growth_loop)
root.order.add_edge(growth_loop,      harvest_cycle)
root.order.add_edge(harvest_cycle,    waste_manage)

# Community outreach can run in parallel once permits are checked
root.order.add_edge(permit_check,     community_outreach)