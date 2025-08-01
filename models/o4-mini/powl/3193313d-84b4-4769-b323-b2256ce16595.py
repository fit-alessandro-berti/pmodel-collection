# Generated from: 3193313d-84b4-4769-b323-b2256ce16595.json
# Description: This process outlines the complex sequence required to establish an urban vertical farm within a metropolitan environment. It involves site selection based on environmental factors, designing multi-level hydroponic systems, sourcing sustainable materials, integrating IoT sensors for climate control, securing permits from local authorities, installing energy-efficient LED lighting, implementing automated nutrient delivery, training staff on plant care and system maintenance, and launching a market outreach campaign focused on local produce. The process also includes establishing partnerships with local restaurants and grocery stores, continuous monitoring of crop health through data analytics, and adapting operations based on seasonal changes and consumer feedback to maximize yield and sustainability in a highly regulated urban setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_assess        = Transition(label='Site Assess')
design_layout      = Transition(label='Design Layout')
material_source    = Transition(label='Material Source')
permit_obtain      = Transition(label='Permit Obtain')
system_install     = Transition(label='System Install')
sensor_setup       = Transition(label='Sensor Setup')
lighting_configure = Transition(label='Lighting Configure')
nutrient_program   = Transition(label='Nutrient Program')
staff_train        = Transition(label='Staff Train')
crop_planting      = Transition(label='Crop Planting')
market_launch      = Transition(label='Market Launch')
partnership_build  = Transition(label='Partnership Build')
data_monitor       = Transition(label='Data Monitor')
feedback_collect   = Transition(label='Feedback Collect')
yield_adjust       = Transition(label='Yield Adjust')

# Build the monitoring+feedback loop: A = monitor → collect, B = adjust yield
monitor_fb = StrictPartialOrder(nodes=[data_monitor, feedback_collect])
monitor_fb.order.add_edge(data_monitor, feedback_collect)
loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_fb, yield_adjust])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    site_assess, design_layout, material_source, permit_obtain,
    system_install, sensor_setup, lighting_configure, nutrient_program,
    staff_train, crop_planting, market_launch, partnership_build, loop
])

# Logical sequencing
root.order.add_edge(site_assess, design_layout)
root.order.add_edge(design_layout, material_source)
root.order.add_edge(design_layout, permit_obtain)
root.order.add_edge(design_layout, system_install)
root.order.add_edge(material_source, system_install)
root.order.add_edge(permit_obtain, system_install)

root.order.add_edge(system_install, sensor_setup)
root.order.add_edge(system_install, lighting_configure)
root.order.add_edge(system_install, nutrient_program)

root.order.add_edge(sensor_setup, staff_train)
root.order.add_edge(lighting_configure, staff_train)
root.order.add_edge(nutrient_program, staff_train)

root.order.add_edge(staff_train, crop_planting)

root.order.add_edge(crop_planting, market_launch)
root.order.add_edge(crop_planting, partnership_build)
root.order.add_edge(crop_planting, loop)