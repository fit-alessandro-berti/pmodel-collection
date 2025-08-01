# Generated from: 287d9d16-74c6-4664-ac93-7d9ec2db2f22.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farming facility within a repurposed industrial building. It involves initial site assessment for structural integrity and sunlight exposure, followed by modular system design tailored to crop types. Activities include sourcing sustainable materials, installing hydroponic and aeroponic systems, integrating IoT sensors for climate and nutrient monitoring, implementing automated lighting and irrigation controls, staff training on crop management, and establishing supply chain logistics for fresh produce distribution to local markets. The process concludes with continuous system optimization based on data analytics to maximize yield and resource efficiency while minimizing environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_assess    = Transition(label='Site Assess')
design_layout  = Transition(label='Design Layout')
material_src   = Transition(label='Material Sourcing')
system_setup   = Transition(label='System Setup')
install_hydro  = Transition(label='Install Hydroponics')
install_aero   = Transition(label='Install Aeroponics')
sensor_int     = Transition(label='Sensor Integrate')
lighting_set   = Transition(label='Lighting Setup')
irrigation_set = Transition(label='Irrigation Setup')
staff_train    = Transition(label='Staff Training')
crop_seed      = Transition(label='Crop Seeding')
climate_ctrl   = Transition(label='Climate Control')
data_mon       = Transition(label='Data Monitoring')
supply_plan    = Transition(label='Supply Planning')
market_deliv   = Transition(label='Market Delivery')
yield_review   = Transition(label='Yield Review')
system_opt     = Transition(label='System Optimize')

# Define the loop's redo-part: Yield Review -> System Optimize
redo_part = StrictPartialOrder(
    nodes=[yield_review, system_opt]
)
redo_part.order.add_edge(yield_review, system_opt)

# Define the loop: first do Data Monitoring, then either exit or do (Yield Review -> System Optimize) and repeat
monitoring_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[data_mon, redo_part]
)

# Assemble the overall partial order
root = StrictPartialOrder(
    nodes=[
        site_assess, design_layout, material_src, system_setup,
        install_hydro, install_aero,
        sensor_int, lighting_set, irrigation_set,
        staff_train, crop_seed, climate_ctrl,
        supply_plan, market_deliv,
        monitoring_loop
    ]
)

# Define control-flow edges
root.order.add_edge(site_assess, design_layout)
root.order.add_edge(design_layout, material_src)
root.order.add_edge(material_src, system_setup)

root.order.add_edge(system_setup, install_hydro)
root.order.add_edge(system_setup, install_aero)

root.order.add_edge(install_hydro, sensor_int)
root.order.add_edge(install_aero, sensor_int)

root.order.add_edge(sensor_int, lighting_set)
root.order.add_edge(sensor_int, irrigation_set)

root.order.add_edge(lighting_set, staff_train)
root.order.add_edge(irrigation_set, staff_train)

root.order.add_edge(staff_train, crop_seed)
root.order.add_edge(crop_seed, climate_ctrl)

root.order.add_edge(climate_ctrl, supply_plan)
root.order.add_edge(supply_plan, market_deliv)

# After initial delivery, enter the continuous monitoring & optimization loop
root.order.add_edge(market_deliv, monitoring_loop)