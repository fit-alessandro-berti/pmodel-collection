# Generated from: 9f54782e-e362-455f-bee2-670fa4f31379.json
# Description: This process involves the comprehensive management of urban beekeeping operations, integrating environmental monitoring, hive maintenance, community engagement, and product distribution. Activities include site selection based on flora density, real-time hive health diagnostics via IoT sensors, seasonal swarm control measures, disease prevention through organic treatments, and data-driven honey yield forecasting. Additionally, the process encompasses regulatory compliance checks, educational workshops for local residents, and coordinating with urban agriculture initiatives to optimize pollination impact within city ecosystems. The approach ensures sustainable apiary practices while balancing ecological benefits and urban development constraints.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Flora_Mapping = Transition(label='Flora Mapping')
Hive_Setup = Transition(label='Hive Setup')
Sensor_Install = Transition(label='Sensor Install')
Health_Check = Transition(label='Health Check')
Swarm_Control = Transition(label='Swarm Control')
Pest_Treatment = Transition(label='Pest Treatment')
Data_Logging = Transition(label='Data Logging')
Yield_Forecast = Transition(label='Yield Forecast')
Compliance_Audit = Transition(label='Compliance Audit')
Workshop_Plan = Transition(label='Workshop Plan')
Community_Meet = Transition(label='Community Meet')
Pollination_Map = Transition(label='Pollination Map')
Harvest_Honey = Transition(label='Harvest Honey')
Product_Label = Transition(label='Product Label')
Market_Ship = Transition(label='Market Ship')

# Environmental monitoring: Site Survey and Flora Mapping run in sequence
env_monitoring = StrictPartialOrder(nodes=[Site_Survey, Flora_Mapping])
env_monitoring.order.add_edge(Site_Survey, Flora_Mapping)

# Hive Setup and Sensor Install run concurrently after env_monitoring
hive_setup_and_sensor = StrictPartialOrder(nodes=[Hive_Setup, Sensor_Install])
# no order between Hive_Setup and Sensor_Install (concurrent)

env_to_hive_sensor = StrictPartialOrder(nodes=[env_monitoring, hive_setup_and_sensor])
env_to_hive_sensor.order.add_edge(env_monitoring, hive_setup_and_sensor)

# Hive maintenance partial order:
# Health Check -> Swarm Control -> Pest Treatment (sequence)
hive_maintenance = StrictPartialOrder(nodes=[Health_Check, Swarm_Control, Pest_Treatment])
hive_maintenance.order.add_edge(Health_Check, Swarm_Control)
hive_maintenance.order.add_edge(Swarm_Control, Pest_Treatment)

# Data operations and forecasting partial order:
# Data Logging -> Yield Forecast (sequence)
data_ops = StrictPartialOrder(nodes=[Data_Logging, Yield_Forecast])
data_ops.order.add_edge(Data_Logging, Yield_Forecast)

# Regulatory compliance partial order:
# Compliance Audit (single activity)
reg_compliance = Compliance_Audit

# Community engagement partial order:
# Workshop Plan -> Community Meet (sequence)
community_engagement = StrictPartialOrder(nodes=[Workshop_Plan, Community_Meet])
community_engagement.order.add_edge(Workshop_Plan, Community_Meet)

# Urban agriculture initiatives partial order:
# Pollination Map alone (single activity)
urban_agri = Pollination_Map

# Product distribution partial order:
# Harvest Honey -> Product Label -> Market Ship (sequence)
product_dist = StrictPartialOrder(nodes=[Harvest_Honey, Product_Label, Market_Ship])
product_dist.order.add_edge(Harvest_Honey, Product_Label)
product_dist.order.add_edge(Product_Label, Market_Ship)

# Compose maintenance, data ops, compliance, community, urban agri and product dist concurrently
middle_part = StrictPartialOrder(
    nodes=[hive_maintenance, data_ops, reg_compliance, community_engagement, urban_agri, product_dist]
)
# no order between these major parts => maximal concurrency

# Finally, full process:
# env_to_hive_sensor ==> middle_part
root = StrictPartialOrder(nodes=[env_to_hive_sensor, middle_part])
root.order.add_edge(env_to_hive_sensor, middle_part)