# Generated from: 1ed2da76-699d-4de0-98ac-7d18a0cc576b.json
# Description: This process outlines the complex setup and operational workflow for establishing an urban vertical farm that integrates hydroponics, renewable energy, and IoT sensor networks. It involves site assessment, modular structure assembly, nutrient solution formulation, environmental calibration, automated planting, real-time growth monitoring, pest detection via AI, adaptive lighting control, water recycling, harvest scheduling, quality analysis, packaging automation, and distribution logistics, ensuring sustainable and efficient fresh produce supply in metropolitan areas. Each step requires cross-disciplinary coordination among agronomists, engineers, and data scientists to optimize yield and minimize resource consumption.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
site_survey    = Transition(label='Site Survey')
design_plan    = Transition(label='Design Plan')
permit_acquire = Transition(label='Permit Acquire')
structure_build= Transition(label='Structure Build')
sensor_install = Transition(label='Sensor Install')
nutrient_mix   = Transition(label='Nutrient Mix')
plant_setup    = Transition(label='Plant Setup')
env_calibrate  = Transition(label='Env Calibrate')
growth_monitor = Transition(label='Growth Monitor')
pest_detect    = Transition(label='Pest Detect')
light_control  = Transition(label='Light Control')
water_cycle    = Transition(label='Water Cycle')
harvest_plan   = Transition(label='Harvest Plan')
quality_test   = Transition(label='Quality Test')
pack_goods     = Transition(label='Pack Goods')
logistics_arrange = Transition(label='Logistics Arrange')

# Define a silent transition for controlling the loop
skip = SilentTransition()

# Define the concurrent monitoring cycle: growth monitoring, pest detection,
# adaptive lighting, and water recycling can happen in any order
monitoring_cycle = StrictPartialOrder(
    nodes=[growth_monitor, pest_detect, light_control, water_cycle]
)
# no edges => all four tasks are concurrent within one cycle

# Define a loop over the monitoring cycle: execute it at least once, then
# optionally repeat
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitoring_cycle, skip]
)

# Build the root partial order, sequencing the setup, calibration, monitoring loop,
# and the post-monitoring tasks (harvest planning, quality test, packaging, logistics)
root = StrictPartialOrder(
    nodes=[
        site_survey,
        design_plan,
        permit_acquire,
        structure_build,
        sensor_install,
        nutrient_mix,
        plant_setup,
        env_calibrate,
        monitor_loop,
        harvest_plan,
        quality_test,
        pack_goods,
        logistics_arrange
    ]
)

# Sequence the setup and calibration steps
root.order.add_edge(site_survey,     design_plan)
root.order.add_edge(design_plan,     permit_acquire)
root.order.add_edge(permit_acquire,  structure_build)
root.order.add_edge(structure_build, sensor_install)
root.order.add_edge(sensor_install,  nutrient_mix)
root.order.add_edge(nutrient_mix,    plant_setup)
root.order.add_edge(plant_setup,     env_calibrate)

# Then enter the monitoring loop
root.order.add_edge(env_calibrate,   monitor_loop)

# After finishing the monitoring loop, proceed to harvest planning and beyond
root.order.add_edge(monitor_loop,    harvest_plan)
root.order.add_edge(harvest_plan,    quality_test)
root.order.add_edge(quality_test,    pack_goods)
root.order.add_edge(pack_goods,      logistics_arrange)