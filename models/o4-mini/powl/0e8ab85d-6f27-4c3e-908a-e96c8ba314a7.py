# Generated from: 0e8ab85d-6f27-4c3e-908a-e96c8ba314a7.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farming facility in a repurposed warehouse. It includes site analysis, environmental control calibration, modular system installation, nutrient cycling optimization, and continuous crop monitoring. The process integrates IoT sensor deployment for real-time data, automated irrigation scheduling, and adaptive lighting adjustments based on crop growth phases. Additionally, it involves waste recycling protocols, staff training on precision agriculture technologies, and market readiness assessments to ensure sustainable production and profitable yield cycles within a compact urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_survey        = Transition(label='Site Survey')
design_layout      = Transition(label='Design Layout')
structure_retrofit = Transition(label='Structure Retrofit')
system_install     = Transition(label='System Install')
sensor_setup       = Transition(label='Sensor Setup')
enviro_calibrate   = Transition(label='Enviro Calibrate')
irrigation_init    = Transition(label='Irrigation Plan')
nutrient_init      = Transition(label='Nutrient Mix')
lighting_init      = Transition(label='Lighting Adjust')
staff_training     = Transition(label='Staff Training')
crop_planting      = Transition(label='Crop Planting')
market_review      = Transition(label='Market Review')
yield_forecast     = Transition(label='Yield Forecast')

# Define the loop‐body activities
growth_monitor     = Transition(label='Growth Monitor')
data_analysis      = Transition(label='Data Analysis')
irrigation_loop    = Transition(label='Irrigation Plan')
lighting_loop      = Transition(label='Lighting Adjust')
nutrient_loop      = Transition(label='Nutrient Mix')
waste_recycle      = Transition(label='Waste Recycle')

# Build the loop body as a partial order B
loop_body = StrictPartialOrder(nodes=[data_analysis,
                                      irrigation_loop,
                                      lighting_loop,
                                      nutrient_loop,
                                      waste_recycle])
loop_body.order.add_edge(data_analysis, irrigation_loop)
loop_body.order.add_edge(data_analysis, lighting_loop)
loop_body.order.add_edge(data_analysis, nutrient_loop)
loop_body.order.add_edge(data_analysis, waste_recycle)

# Build the LOOP operator: first growth_monitor, then B, looping until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, loop_body])

# Build the top‐level strict partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    structure_retrofit,
    system_install,
    sensor_setup,
    enviro_calibrate,
    irrigation_init,
    nutrient_init,
    lighting_init,
    staff_training,
    crop_planting,
    loop,
    market_review,
    yield_forecast
])

# Add the control‐flow edges
root.order.add_edge(site_survey,      design_layout)
root.order.add_edge(design_layout,    structure_retrofit)
root.order.add_edge(structure_retrofit, system_install)
root.order.add_edge(system_install,   sensor_setup)
root.order.add_edge(sensor_setup,     enviro_calibrate)
root.order.add_edge(enviro_calibrate, irrigation_init)
root.order.add_edge(irrigation_init,  nutrient_init)
root.order.add_edge(nutrient_init,    lighting_init)
root.order.add_edge(lighting_init,    staff_training)
root.order.add_edge(staff_training,   crop_planting)
root.order.add_edge(crop_planting,    loop)
root.order.add_edge(loop,             market_review)
root.order.add_edge(market_review,    yield_forecast)