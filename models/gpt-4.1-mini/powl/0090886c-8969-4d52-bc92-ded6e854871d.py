# Generated from: 0090886c-8969-4d52-bc92-ded6e854871d.json
# Description: This process involves establishing a vertical farming system within an urban environment, integrating advanced hydroponic and aeroponic technologies. It begins with site assessment and structural retrofitting, followed by environmental control installation, nutrient cycling design, and seed selection tailored to urban microclimates. The process includes IoT sensor deployment for real-time monitoring, automated irrigation calibration, pest management via integrated biological controls, and workforce training for operational maintenance. Finally, it covers yield forecasting using AI analytics and establishing supply chain logistics focused on rapid distribution to local markets, ensuring sustainability and minimal carbon footprint throughout the lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
site_assessment = Transition(label='Site Assessment')
structure_retrofit = Transition(label='Structure Retrofit')
env_control = Transition(label='Env Control')
nutrient_design = Transition(label='Nutrient Design')
seed_selection = Transition(label='Seed Selection')
sensor_deploy = Transition(label='Sensor Deploy')
irrigation_setup = Transition(label='Irrigation Setup')
pest_control = Transition(label='Pest Control')
workforce_train = Transition(label='Workforce Train')
system_calibration = Transition(label='System Calibration')
growth_monitoring = Transition(label='Growth Monitoring')
data_analytics = Transition(label='Data Analytics')
yield_forecast = Transition(label='Yield Forecast')
logistics_plan = Transition(label='Logistics Plan')
market_launch = Transition(label='Market Launch')

# Partial order construction based on the described sequence and dependencies:
# 1) Site Assessment --> Structure Retrofit
# 2) Structure Retrofit --> Env Control --> Nutrient Design --> Seed Selection
# 3) IoT Sensor Deploy and Automated Irrigation Calibration and Pest Control and Workforce Training
#    can run concurrently after Seed Selection finishes
#    However, note: "System Calibration" and "Growth Monitoring" likely follow Sensor Deploy and Irrigation Setup
#    "System Calibration" and "Growth Monitoring" follow Pest Control and Workforce Train as well, 
#    but based on description, "System Calibration" likely depends on Sensor Deploy and Irrigation Setup
#    We'll create appropriate partial ordering
# 4) Data Analytics depends on Growth Monitoring
# 5) Yield Forecast depends on Data Analytics
# 6) Logistics Plan depends on Yield Forecast
# 7) Market Launch depends on Logistics Plan

# Build partial order nodes
nodes = [
    site_assessment,
    structure_retrofit,
    env_control,
    nutrient_design,
    seed_selection,
    sensor_deploy,
    irrigation_setup,
    pest_control,
    workforce_train,
    system_calibration,
    growth_monitoring,
    data_analytics,
    yield_forecast,
    logistics_plan,
    market_launch
]

root = StrictPartialOrder(nodes=nodes)

# Define order edges in accordance with the process description:

# Initial sequential dependencies
root.order.add_edge(site_assessment, structure_retrofit)
root.order.add_edge(structure_retrofit, env_control)
root.order.add_edge(env_control, nutrient_design)
root.order.add_edge(nutrient_design, seed_selection)

# After seed_selection, four activities start concurrently:
# sensor_deploy, irrigation_setup, pest_control, workforce_train

root.order.add_edge(seed_selection, sensor_deploy)
root.order.add_edge(seed_selection, irrigation_setup)
root.order.add_edge(seed_selection, pest_control)
root.order.add_edge(seed_selection, workforce_train)

# system_calibration depends on sensor_deploy and irrigation_setup (integration/calibration)
root.order.add_edge(sensor_deploy, system_calibration)
root.order.add_edge(irrigation_setup, system_calibration)

# growth_monitoring depends on system_calibration and also probably on pest_control and workforce_train
# The description groups growth monitoring after system calibration and pest management/workforce train
# To model partial order, let's require growth_monitoring after system_calibration, pest_control and workforce_train

root.order.add_edge(system_calibration, growth_monitoring)
root.order.add_edge(pest_control, growth_monitoring)
root.order.add_edge(workforce_train, growth_monitoring)

# data_analytics depends on growth_monitoring
root.order.add_edge(growth_monitoring, data_analytics)

# yield_forecast depends on data_analytics
root.order.add_edge(data_analytics, yield_forecast)

# logistics_plan depends on yield_forecast
root.order.add_edge(yield_forecast, logistics_plan)

# market_launch depends on logistics_plan
root.order.add_edge(logistics_plan, market_launch)