# Generated from: a14766d8-584d-4723-beb5-abf2afa23479.json
# Description: This process outlines the adaptive urban farming cycle designed to optimize crop yield and resource efficiency within constrained city environments. It integrates dynamic environmental sensing, soil nutrient recalibration, automated planting, and waste recycling while incorporating community feedback and local market trends. The cycle continuously adjusts irrigation, lighting, and nutrient delivery based on real-time data, ensuring sustainability and responsiveness to urban microclimates. Additionally, it includes predictive pest control measures and periodic crop rotation planning to maintain soil health and biodiversity. Post-harvest, the system manages distribution logistics and engages in regenerative practices by leveraging organic waste for composting, creating a closed-loop ecosystem that maximizes productivity and minimizes environmental impact in urban settings.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
sensor_setup       = Transition(label='Sensor Setup')
data_capture       = Transition(label='Data Capture')
nutrient_test      = Transition(label='Nutrient Test')
soil_recalibrate   = Transition(label='Soil Recalibrate')
seed_selection     = Transition(label='Seed Selection')
automated_planting = Transition(label='Automated Planting')
irrigation_adjust  = Transition(label='Irrigation Adjust')
lighting_control   = Transition(label='Lighting Control')
pest_prediction    = Transition(label='Pest Prediction')
crop_rotation      = Transition(label='Crop Rotation')
waste_collection   = Transition(label='Waste Collection')
compost_process    = Transition(label='Compost Process')
yield_forecast     = Transition(label='Yield Forecast')
market_survey      = Transition(label='Market Survey')
distribution_plan  = Transition(label='Distribution Plan')
community_feedback = Transition(label='Community Feedback')

# A silent transition to serve as the loop-exit choice
skip = SilentTransition()

# Concurrent adjustment of irrigation and lighting
concurrent_adjust = StrictPartialOrder(
    nodes=[irrigation_adjust, lighting_control]
)
# No edges => they are concurrent

# Define one full cycle of the urban‐farming process
cycle = StrictPartialOrder(nodes=[
    sensor_setup,
    data_capture,
    nutrient_test,
    soil_recalibrate,
    seed_selection,
    automated_planting,
    concurrent_adjust,
    pest_prediction,
    crop_rotation,
    yield_forecast,
    market_survey,
    distribution_plan,
    community_feedback,
    waste_collection,
    compost_process
])

# Sequential ordering of the cycle steps
cycle.order.add_edge(sensor_setup, data_capture)
cycle.order.add_edge(data_capture, nutrient_test)
cycle.order.add_edge(nutrient_test, soil_recalibrate)
cycle.order.add_edge(soil_recalibrate, seed_selection)
cycle.order.add_edge(seed_selection, automated_planting)
cycle.order.add_edge(automated_planting, concurrent_adjust)
cycle.order.add_edge(concurrent_adjust, pest_prediction)
cycle.order.add_edge(pest_prediction, crop_rotation)
cycle.order.add_edge(crop_rotation, yield_forecast)
cycle.order.add_edge(yield_forecast, market_survey)
cycle.order.add_edge(market_survey, distribution_plan)
cycle.order.add_edge(distribution_plan, community_feedback)
cycle.order.add_edge(community_feedback, waste_collection)
cycle.order.add_edge(waste_collection, compost_process)

# Build an unbounded loop around the cycle
# children[0] = body to execute, children[1] = silent exit (skip)
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[cycle, skip]
)