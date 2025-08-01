# Generated from: d79a83e7-efee-49df-9195-826e638d64aa.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farming operation within a metropolitan environment. It covers site selection, environmental assessment, regulatory compliance, modular infrastructure setup, crop selection based on local demand, integration of IoT sensors for real-time monitoring, nutrient circulation system design, automated lighting calibration, staff training on sustainable practices, implementation of pest control protocols without pesticides, marketing strategy development targeting local consumers, logistics planning for fresh produce distribution, continuous yield optimization through data analytics, and establishing community engagement programs to promote urban agriculture awareness and education.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey        = Transition(label="Site Survey")
env_assessment     = Transition(label="Env Assessment")
reg_compliance     = Transition(label="Reg Compliance")
modular_setup      = Transition(label="Modular Setup")
crop_selection     = Transition(label="Crop Selection")
iot_integration    = Transition(label="IoT Integration")
nutrient_flow      = Transition(label="Nutrient Flow")
light_calibration  = Transition(label="Light Calibration")
staff_training     = Transition(label="Staff Training")
pest_control       = Transition(label="Pest Control")
market_strategy    = Transition(label="Market Strategy")
logistics_plan     = Transition(label="Logistics Plan")
yield_analysis     = Transition(label="Yield Analysis")
data_review        = Transition(label="Data Review")
community_engage   = Transition(label="Community Engage")

# Build a loop for continuous yield optimization:
#   first do yield_analysis, then either exit or do data_review and repeat
yield_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[yield_analysis, data_review]
)

# Assemble the overall partial order
nodes = [
    site_survey,
    env_assessment,
    reg_compliance,
    modular_setup,
    crop_selection,
    iot_integration,
    nutrient_flow,
    light_calibration,
    staff_training,
    pest_control,
    market_strategy,
    logistics_plan,
    yield_loop,
    community_engage
]

root = StrictPartialOrder(nodes=nodes)

# Add sequential dependencies
for src, tgt in zip(nodes, nodes[1:]):
    root.order.add_edge(src, tgt)