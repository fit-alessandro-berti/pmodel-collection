# Generated from: 88251bbf-2034-4e8e-86a7-6cfc141060ae.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm within a metropolitan area. It includes site analysis, modular structure design, hydroponic system installation, sensor calibration, crop cycle planning, and integration of renewable energy sources. The process also covers regulatory compliance, community engagement, waste recycling, and real-time data monitoring to optimize yield and sustainability in a constrained urban environment, ensuring both economic viability and environmental responsibility.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey      = Transition(label='Site Survey')
design_layout    = Transition(label='Design Layout')
permits_obtain   = Transition(label='Permits Obtain')
structure_build  = Transition(label='Structure Build')
hydroponic_setup = Transition(label='Hydroponic Setup')
sensor_install   = Transition(label='Sensor Install')
calibrate_sensors= Transition(label='Calibrate Sensors')
energy_integrate = Transition(label='Energy Integrate')
community_meet   = Transition(label='Community Meet')
crop_plan        = Transition(label='Crop Plan')
seed_selection   = Transition(label='Seed Selection')
planting_stage   = Transition(label='Planting Stage')
growth_monitor   = Transition(label='Growth Monitor')
data_analyze     = Transition(label='Data Analyze')
waste_process    = Transition(label='Waste Process')
yield_harvest    = Transition(label='Yield Harvest')
market_launch    = Transition(label='Market Launch')

# Optional community engagement
skip = SilentTransition()
community_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[community_meet, skip]
)

# Sequence for seeding
seed_seq = StrictPartialOrder(nodes=[seed_selection, planting_stage])
seed_seq.order.add_edge(seed_selection, planting_stage)

# Growth cycle body
growth_cycle = StrictPartialOrder(nodes=[growth_monitor, data_analyze, waste_process])
growth_cycle.order.add_edge(growth_monitor, data_analyze)
growth_cycle.order.add_edge(data_analyze, waste_process)

# Loop for crop cycles
crop_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[seed_seq, growth_cycle]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, design_layout, permits_obtain, structure_build,
    hydroponic_setup, community_choice, sensor_install,
    calibrate_sensors, energy_integrate, crop_plan,
    crop_loop, yield_harvest, market_launch
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, permits_obtain)
root.order.add_edge(permits_obtain, structure_build)
root.order.add_edge(structure_build, hydroponic_setup)

# After structure is ready: optional community meet, sensor & energy setup
root.order.add_edge(hydroponic_setup, community_choice)
root.order.add_edge(hydroponic_setup, sensor_install)
root.order.add_edge(hydroponic_setup, energy_integrate)

# Sensor calibration
root.order.add_edge(sensor_install, calibrate_sensors)

# Crop planning after energy integration, sensor calibration, community engagement
root.order.add_edge(calibrate_sensors, crop_plan)
root.order.add_edge(energy_integrate, crop_plan)
root.order.add_edge(community_choice, crop_plan)

# Seed and grow loop
root.order.add_edge(crop_plan, crop_loop)

# Harvest and market
root.order.add_edge(crop_loop, yield_harvest)
root.order.add_edge(yield_harvest, market_launch)