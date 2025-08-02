# Generated from: 26473754-185a-4207-9ff3-1f252898d213.json
# Description: This process outlines the adaptive urban farming cycle designed to optimize crop yield in limited city spaces by dynamically integrating environmental data, community feedback, and resource constraints. It begins with microclimate analysis to assess localized conditions, followed by tailored seed selection that suits the urban microenvironment. Subsequent activities involve nutrient profiling and automated irrigation scheduling to maximize growth efficiency. The system incorporates pest monitoring using AI-powered sensors, triggering organic treatment protocols only when thresholds are exceeded. Community engagement is facilitated through real-time data sharing and volunteer coordination, ensuring social sustainability. Harvest timing is continuously adjusted based on predictive growth models, while post-harvest handling includes immediate quality grading and distribution planning to minimize waste. Finally, data from each cycle feeds into machine learning models to refine future operations, creating a resilient and self-improving urban agricultural ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Microclimate_Scan = Transition(label='Microclimate Scan')
Seed_Selection = Transition(label='Seed Selection')
Nutrient_Profile = Transition(label='Nutrient Profile')
Irrigation_Plan = Transition(label='Irrigation Plan')
Soil_Testing = Transition(label='Soil Testing')
Pest_Monitoring = Transition(label='Pest Monitoring')
Organic_Treatment = Transition(label='Organic Treatment')
Growth_Tracking = Transition(label='Growth Tracking')
Volunteer_Sync = Transition(label='Volunteer Sync')
Data_Sharing = Transition(label='Data Sharing')
Harvest_Timing = Transition(label='Harvest Timing')
Quality_Grading = Transition(label='Quality Grading')
Waste_Minimization = Transition(label='Waste Minimization')
Distribution_Plan = Transition(label='Distribution Plan')
Cycle_Feedback = Transition(label='Cycle Feedback')
Model_Training = Transition(label='Model Training')

# Construct pest monitoring with conditional organic treatment:
# pest_monitoring followed by loop:
# if threshold exceeded -> organic_treatment else skip
# modeled as a loop where after pest_monitoring we either exit or do organic_treatment then pest_monitoring again
# Here, * (Organic_Treatment, Pest_Monitoring) would loop on pest monitoring with organic treatment in between
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[Pest_Monitoring, Organic_Treatment])

# Community engagement: Data Sharing and Volunteer Sync occur concurrently
community_engagement = StrictPartialOrder(nodes=[Data_Sharing, Volunteer_Sync])

# Post-harvest handling sequence: Quality Grading -> Waste Minimization -> Distribution Plan
post_harvest = StrictPartialOrder(nodes=[Quality_Grading, Waste_Minimization, Distribution_Plan])
post_harvest.order.add_edge(Quality_Grading, Waste_Minimization)
post_harvest.order.add_edge(Waste_Minimization, Distribution_Plan)

# Final feedback loop: Cycle Feedback -> Model Training
feedback = StrictPartialOrder(nodes=[Cycle_Feedback, Model_Training])
feedback.order.add_edge(Cycle_Feedback, Model_Training)

# Initial growth preparation sequence:
# Microclimate Scan -> Seed Selection -> Nutrient Profile -> Irrigation Plan -> Soil Testing
growth_prep = StrictPartialOrder(nodes=[Microclimate_Scan, Seed_Selection, Nutrient_Profile, Irrigation_Plan, Soil_Testing])
growth_prep.order.add_edge(Microclimate_Scan, Seed_Selection)
growth_prep.order.add_edge(Seed_Selection, Nutrient_Profile)
growth_prep.order.add_edge(Nutrient_Profile, Irrigation_Plan)
growth_prep.order.add_edge(Irrigation_Plan, Soil_Testing)

# Growth Tracking and Harvest Timing happen after pest monitoring and community engagement,
# Harvest Timing lead to post-harvest
# After post-harvest, Cycle Feedback and Model Training (the feedback loop)

# Define growth tracking and harvest timing sequence:
growth_harvest = StrictPartialOrder(nodes=[Growth_Tracking, Harvest_Timing])
growth_harvest.order.add_edge(Growth_Tracking, Harvest_Timing)

# Combine Pest Monitoring loop and Community Engagement concurrently
pm_ce = StrictPartialOrder(nodes=[pest_loop, community_engagement])

# The full main partial order:
# growth_prep -> pm_ce -> growth_harvest -> post_harvest -> feedback
root = StrictPartialOrder(
    nodes=[growth_prep, pm_ce, growth_harvest, post_harvest, feedback]
)
root.order.add_edge(growth_prep, pm_ce)
root.order.add_edge(pm_ce, growth_harvest)
root.order.add_edge(growth_harvest, post_harvest)
root.order.add_edge(post_harvest, feedback)