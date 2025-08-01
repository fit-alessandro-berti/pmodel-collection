# Generated from: 96686db1-0a80-44e0-9978-d3231dba3c8e.json
# Description: This process describes the complex establishment of an urban vertical farm within a repurposed multi-story building. It involves integrating advanced hydroponic systems, optimizing artificial lighting, and implementing automated nutrient delivery tailored to diverse plant species. The process ensures sustainable water recycling, climate control, and pest management without chemicals. Coordination with local authorities for zoning and energy compliance is required. Post-installation, continuous monitoring through IoT sensors enables adaptive growth adjustments. The integration of AI-driven analytics supports yield forecasting and resource optimization, ensuring economic viability within urban agriculture constraints.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the elementary activities
site_survey      = Transition(label="Site Survey")
zoning           = Transition(label="Zoning Approval")
struct_audit     = Transition(label="Structural Audit")
hydro_design     = Transition(label="Hydroponic Design")
lighting_setup   = Transition(label="Lighting Setup")
nutrient_plan    = Transition(label="Nutrient Plan")
water_recycling  = Transition(label="Water Recycling")
climate_control  = Transition(label="Climate Control")
pest_monitoring  = Transition(label="Pest Monitoring")
sensor_install   = Transition(label="Sensor Install")
iot_network      = Transition(label="IoT Network")
ai_integration   = Transition(label="AI Integration")
staff_training   = Transition(label="Staff Training")
growth_testing   = Transition(label="Growth Testing")
yield_forecast   = Transition(label="Yield Forecast")

# Build the monitoring/adjustment loop:
# A = perform growth testing then yield forecasting
A = StrictPartialOrder(nodes=[growth_testing, yield_forecast])
A.order.add_edge(growth_testing, yield_forecast)

# B = adjust nutrient plan and climate control in parallel
B = StrictPartialOrder(nodes=[nutrient_plan, climate_control])
# no edge => they are concurrent adjustments

loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Assemble the full process as a partial order
root = StrictPartialOrder(
    nodes=[
        site_survey, zoning, struct_audit,
        hydro_design, lighting_setup, nutrient_plan,
        water_recycling, climate_control, pest_monitoring,
        sensor_install, iot_network, ai_integration,
        staff_training, loop
    ]
)

# Define the control‐flow dependencies
root.order.add_edge(site_survey,     zoning)
root.order.add_edge(zoning,          struct_audit)
root.order.add_edge(struct_audit,    hydro_design)
root.order.add_edge(hydro_design,    lighting_setup)
root.order.add_edge(lighting_setup,  nutrient_plan)
root.order.add_edge(nutrient_plan,   water_recycling)
root.order.add_edge(nutrient_plan,   climate_control)
root.order.add_edge(water_recycling, pest_monitoring)
root.order.add_edge(climate_control, pest_monitoring)
root.order.add_edge(pest_monitoring, sensor_install)
root.order.add_edge(sensor_install,  iot_network)
root.order.add_edge(iot_network,     ai_integration)
root.order.add_edge(ai_integration,  staff_training)
root.order.add_edge(staff_training,  loop)