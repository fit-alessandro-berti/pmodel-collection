# Generated from: 9f54782e-e362-455f-bee2-670fa4f31379.json
# Description: This process involves the comprehensive management of urban beekeeping operations, integrating environmental monitoring, hive maintenance, community engagement, and product distribution. Activities include site selection based on flora density, real-time hive health diagnostics via IoT sensors, seasonal swarm control measures, disease prevention through organic treatments, and data-driven honey yield forecasting. Additionally, the process encompasses regulatory compliance checks, educational workshops for local residents, and coordinating with urban agriculture initiatives to optimize pollination impact within city ecosystems. The approach ensures sustainable apiary practices while balancing ecological benefits and urban development constraints.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
site_survey      = Transition(label='Site Survey')
flora_mapping    = Transition(label='Flora Mapping')
hive_setup       = Transition(label='Hive Setup')
sensor_install   = Transition(label='Sensor Install')
health_check     = Transition(label='Health Check')
swarm_control    = Transition(label='Swarm Control')
pest_treatment   = Transition(label='Pest Treatment')
data_logging     = Transition(label='Data Logging')
yield_forecast   = Transition(label='Yield Forecast')
compliance_audit = Transition(label='Compliance Audit')
workshop_plan    = Transition(label='Workshop Plan')
community_meet   = Transition(label='Community Meet')
pollination_map  = Transition(label='Pollination Map')
harvest_honey    = Transition(label='Harvest Honey')
product_label    = Transition(label='Product Label')
market_ship      = Transition(label='Market Ship')

# 1. Initial setup: site survey → flora mapping → hive setup → sensor install
initial_po = StrictPartialOrder(nodes=[site_survey, flora_mapping, hive_setup, sensor_install])
initial_po.order.add_edge(site_survey, flora_mapping)
initial_po.order.add_edge(flora_mapping, hive_setup)
initial_po.order.add_edge(hive_setup, sensor_install)

# 2. Monitoring loop: check health & log data, then optionally swarm control or pest treatment, repeat
loop_body = StrictPartialOrder(nodes=[health_check, data_logging])
loop_body.order.add_edge(health_check, data_logging)

treatment_choice = OperatorPOWL(operator=Operator.XOR,
                                children=[swarm_control, pest_treatment])

monitor_loop = OperatorPOWL(operator=Operator.LOOP,
                           children=[loop_body, treatment_choice])

# 3. Post‐monitoring: forecast yield
#    → then in parallel plan compliance, workshops, pollination mapping
#    → then community meet (after compliance & workshop)
#    → then harvest, label & ship
final_po = StrictPartialOrder(nodes=[
    yield_forecast,
    compliance_audit,
    workshop_plan,
    community_meet,
    pollination_map,
    harvest_honey,
    product_label,
    market_ship
])
# forecast to parallel tasks
final_po.order.add_edge(yield_forecast, compliance_audit)
final_po.order.add_edge(yield_forecast, workshop_plan)
final_po.order.add_edge(yield_forecast, pollination_map)
# compliance & workshop converge to community meet
final_po.order.add_edge(compliance_audit, community_meet)
final_po.order.add_edge(workshop_plan, community_meet)
# compliance & pollination → harvest
final_po.order.add_edge(compliance_audit, harvest_honey)
final_po.order.add_edge(pollination_map, harvest_honey)
# harvest → label → ship
final_po.order.add_edge(harvest_honey, product_label)
final_po.order.add_edge(product_label, market_ship)

# 4. Root: initial setup → monitoring loop → yield forecast → final activities
root = StrictPartialOrder(nodes=[initial_po, monitor_loop, yield_forecast, final_po])
root.order.add_edge(initial_po, monitor_loop)
root.order.add_edge(monitor_loop, yield_forecast)
root.order.add_edge(yield_forecast, final_po)