# Generated from: f154e7e8-51ec-455c-bd30-04f37239023f.json
# Description: This process outlines the comprehensive management of urban beekeeping operations, combining environmental monitoring, community engagement, hive maintenance, and honey production. It involves site selection based on urban flora assessments, regular hive health checks using digital sensors, pest control with organic methods, and coordination with local authorities for compliance. Additionally, the process includes educational workshops for residents, seasonal honey extraction, quality testing, packaging, and distribution through local markets, ensuring sustainable practices and community support while maximizing honey yield and bee welfare in a city environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all atomic activities
site_survey      = Transition(label='Site Survey')
flora_mapping    = Transition(label='Flora Mapping')
hive_setup       = Transition(label='Hive Setup')
sensor_install   = Transition(label='Sensor Install')
health_check     = Transition(label='Health Check')
pest_control     = Transition(label='Pest Control')
data_logging     = Transition(label='Data Logging')
community_meet   = Transition(label='Community Meet')
workshop_plan    = Transition(label='Workshop Plan')
honey_extract    = Transition(label='Honey Extract')
quality_test     = Transition(label='Quality Test')
packaging        = Transition(label='Packaging')
waste_manage     = Transition(label='Waste Manage')
market_setup     = Transition(label='Market Setup')
sales_report     = Transition(label='Sales Report')
regulation_check = Transition(label='Regulation Check')
seasonal_review  = Transition(label='Seasonal Review')

# 1) Initial setup sequence: Site Survey -> Flora Mapping -> Hive Setup -> Sensor Install
initial_setup = StrictPartialOrder(
    nodes=[site_survey, flora_mapping, hive_setup, sensor_install]
)
initial_setup.order.add_edge(site_survey, flora_mapping)
initial_setup.order.add_edge(flora_mapping, hive_setup)
initial_setup.order.add_edge(hive_setup, sensor_install)

# 2) Community engagement: Community Meet -> Workshop Plan
community_seq = StrictPartialOrder(
    nodes=[community_meet, workshop_plan]
)
community_seq.order.add_edge(community_meet, workshop_plan)

# 3) Hive health loop: (Health Check -> Pest Control -> Data Logging) repeated
health_seq = StrictPartialOrder(
    nodes=[health_check, pest_control, data_logging]
)
health_seq.order.add_edge(health_check, pest_control)
health_seq.order.add_edge(pest_control, data_logging)
health_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[health_seq, health_seq]  # initial + repeating part are the same
)

# 4) Production cycle loop:
#    Seasonal Review -> Honey Extract -> Quality Test -> Packaging -> Waste Manage -> Market Setup -> Sales Report
prod_seq = StrictPartialOrder(
    nodes=[seasonal_review, honey_extract, quality_test,
           packaging, waste_manage, market_setup, sales_report]
)
prod_nodes = [seasonal_review, honey_extract, quality_test,
              packaging, waste_manage, market_setup, sales_report]
for i in range(len(prod_nodes) - 1):
    prod_seq.order.add_edge(prod_nodes[i], prod_nodes[i + 1])
prod_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[prod_seq, prod_seq]
)

# 5) Root model: all submodels in parallel but regulated by an initial compliance check
root = StrictPartialOrder(
    nodes=[initial_setup,
           regulation_check,
           community_seq,
           health_loop,
           prod_loop]
)
# initial_setup precedes the regulation check
root.order.add_edge(initial_setup, regulation_check)
# after compliance, the three strands run in (partial) parallel
root.order.add_edge(regulation_check, community_seq)
root.order.add_edge(regulation_check, health_loop)
root.order.add_edge(regulation_check, prod_loop)
# also we require that community, health and production not start before initial setup
root.order.add_edge(initial_setup, community_seq)
root.order.add_edge(initial_setup, health_loop)
root.order.add_edge(initial_setup, prod_loop)