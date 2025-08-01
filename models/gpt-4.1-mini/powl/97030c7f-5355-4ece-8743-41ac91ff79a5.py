# Generated from: 97030c7f-5355-4ece-8743-41ac91ff79a5.json
# Description: This process outlines the complete operational cycle of an urban vertical farm, integrating advanced IoT monitoring, automated nutrient delivery, and energy-efficient lighting adjustments. It involves crop selection based on market trends, seed germination in controlled chambers, continuous environmental data collection, adaptive irrigation, pest detection through AI imaging, yield forecasting, and post-harvest quality analysis. This atypical business process blends agricultural science with smart technology to optimize crop production in limited urban spaces while minimizing resource consumption and ensuring consistent product quality for local distribution networks.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Trend_Analysis = Transition(label='Trend Analysis')
Seed_Germination = Transition(label='Seed Germination')
Chamber_Setup = Transition(label='Chamber Setup')
Env_Monitoring = Transition(label='Env Monitoring')
Irrigation_Control = Transition(label='Irrigation Control')
Nutrient_Mix = Transition(label='Nutrient Mix')
Lighting_Adjust = Transition(label='Lighting Adjust')
Pest_Detection = Transition(label='Pest Detection')
Growth_Tracking = Transition(label='Growth Tracking')
Yield_Forecast = Transition(label='Yield Forecast')
Climate_Adjust = Transition(label='Climate Adjust')
Harvest_Plan = Transition(label='Harvest Plan')
Quality_Check = Transition(label='Quality Check')
Packaging_Prep = Transition(label='Packaging Prep')
Delivery_Schedule = Transition(label='Delivery Schedule')

# Define partial orders representing the logical flow of the process
# Step 1: Crop selection and seed preparation
# Trend Analysis -> Chamber Setup -> Seed Germination
preparation = StrictPartialOrder(nodes=[Trend_Analysis, Chamber_Setup, Seed_Germination])
preparation.order.add_edge(Trend_Analysis, Chamber_Setup)
preparation.order.add_edge(Chamber_Setup, Seed_Germination)

# Step 2: Environmental monitoring loop with adaptive controls
# Seed Germination -> loop of Env Monitoring and adjustments before growth tracking

# Loop body: 
# Env Monitoring -> XOR of (Irrigation Control, Nutrient Mix, Lighting Adjust, Climate Adjust)
# This represents adaptive actions during environment monitoring

env_adjustments_xor = OperatorPOWL(operator=Operator.XOR, children=[
    Irrigation_Control, Nutrient_Mix, Lighting_Adjust, Climate_Adjust,
])

env_monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    Env_Monitoring,
    env_adjustments_xor
])

# From Seed Germination to loop then Growth Tracking
env_loop_partial = StrictPartialOrder(nodes=[Seed_Germination, env_monitoring_loop, Growth_Tracking])
env_loop_partial.order.add_edge(Seed_Germination, env_monitoring_loop)
env_loop_partial.order.add_edge(env_monitoring_loop, Growth_Tracking)

# Step 3: Pest Detection and Yield Forecast happen in parallel after Growth Tracking
post_growth_parallel = StrictPartialOrder(nodes=[Growth_Tracking, Pest_Detection, Yield_Forecast])
# Growth Tracking precedes Pest Detection and Yield Forecast, which are concurrent
post_growth_parallel.order.add_edge(Growth_Tracking, Pest_Detection)
post_growth_parallel.order.add_edge(Growth_Tracking, Yield_Forecast)

# Step 4: Harvest Plan after Yield Forecast
# Harvest Plan follows Yield Forecast
harvest_phase = StrictPartialOrder(nodes=[Yield_Forecast, Harvest_Plan])
harvest_phase.order.add_edge(Yield_Forecast, Harvest_Plan)

# Step 5: Quality Check after Harvest Plan
quality_phase = StrictPartialOrder(nodes=[Harvest_Plan, Quality_Check])
quality_phase.order.add_edge(Harvest_Plan, Quality_Check)

# Step 6: Packaging Prep and Delivery Schedule after Quality Check, sequential order
final_phase = StrictPartialOrder(nodes=[Quality_Check, Packaging_Prep, Delivery_Schedule])
final_phase.order.add_edge(Quality_Check, Packaging_Prep)
final_phase.order.add_edge(Packaging_Prep, Delivery_Schedule)

# Compose all phases in the overall partial order, connect by edges accordingly

# Combine all major phases as nodes
root = StrictPartialOrder(nodes=[
    preparation,
    env_loop_partial,
    post_growth_parallel,
    harvest_phase,
    quality_phase,
    final_phase,
])

# Add edges connecting phases in proper sequence
root.order.add_edge(preparation, env_loop_partial)
root.order.add_edge(env_loop_partial, post_growth_parallel)
root.order.add_edge(post_growth_parallel, harvest_phase)
root.order.add_edge(harvest_phase, quality_phase)
root.order.add_edge(quality_phase, final_phase)