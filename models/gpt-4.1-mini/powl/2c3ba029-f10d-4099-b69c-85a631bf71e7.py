# Generated from: 2c3ba029-f10d-4099-b69c-85a631bf71e7.json
# Description: This process outlines the comprehensive setup of an urban vertical farm, integrating advanced hydroponic systems with AI-driven climate control. It starts with site analysis and structural retrofitting, followed by nutrient solution formulation and seed selection tailored for vertical growth. Continuous monitoring includes pest detection via machine vision and predictive yield modeling. The process concludes with automated harvesting and supply chain integration to local markets, ensuring sustainability and minimal environmental impact throughout the farm's lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Analysis = Transition(label='Site Analysis')
Structural_Retrofit = Transition(label='Structural Retrofit')
Hydroponic_Setup = Transition(label='Hydroponic Setup')
Seed_Selection = Transition(label='Seed Selection')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Tuning = Transition(label='Climate Tuning')
Lighting_Install = Transition(label='Lighting Install')
AI_Calibration = Transition(label='AI Calibration')
Pest_Detection = Transition(label='Pest Detection')
Growth_Monitoring = Transition(label='Growth Monitoring')
Water_Recycling = Transition(label='Water Recycling')
Yield_Prediction = Transition(label='Yield Prediction')
Automated_Harvest = Transition(label='Automated Harvest')
Packaging_Prep = Transition(label='Packaging Prep')
Market_Integration = Transition(label='Market Integration')

# Setup order reflecting the described workflow:

# 1. Start with Site Analysis and Structural Retrofit (sequential)
# 2. Then Nutrient Mix and Seed Selection (can be concurrent, both after Structural Retrofit)
# 3. Hydroponic Setup after Nutrient Mix and Seed Selection finish (partial order)
# 4. Climate Tuning, Lighting Install, AI Calibration (concurrent after Hydroponic Setup)
# 5. Pest Detection and Growth Monitoring (concurrent) after climate-related activities
# 6. Water Recycling concurrent after Pest Detection (assume monitoring before recycling)
# 7. Yield Prediction after Growth Monitoring (and possibly Pest Detection)
# 8. Automated Harvest after Yield Prediction
# 9. Packaging Prep and Market Integration sequential after Automated Harvest

# Build partial orders stepwise

# First phase: Site Analysis -> Structural Retrofit
phase1 = StrictPartialOrder(nodes=[Site_Analysis, Structural_Retrofit])
phase1.order.add_edge(Site_Analysis, Structural_Retrofit)

# Second phase: Nutrient Mix and Seed Selection (concurrent) after Structural Retrofit
phase2 = StrictPartialOrder(nodes=[Nutrient_Mix, Seed_Selection])
# No edges between Nutrient Mix and Seed Selection - concurrent

# Third phase: Hydroponic Setup after both Nutrient Mix and Seed Selection
phase3_nodes = [Hydroponic_Setup]
phase3 = StrictPartialOrder(nodes=phase3_nodes)  # single node

# Fourth phase: Climate Tuning, Lighting Install, AI Calibration concurrent after Hydroponic Setup
phase4 = StrictPartialOrder(nodes=[Climate_Tuning, Lighting_Install, AI_Calibration])
# concurrent - no edges

# Fifth phase: Pest Detection and Growth Monitoring concurrent after climate-related
phase5 = StrictPartialOrder(nodes=[Pest_Detection, Growth_Monitoring])

# Sixth phase: Water Recycling after Pest Detection (can start after Pest Detection)
phase6 = StrictPartialOrder(nodes=[Water_Recycling])

# Seventh phase: Yield Prediction after Growth Monitoring and Pest Detection
phase7 = StrictPartialOrder(nodes=[Yield_Prediction])

# Eighth phase: Automated Harvest after Yield Prediction
phase8 = StrictPartialOrder(nodes=[Automated_Harvest])

# Ninth phase: Packaging Prep -> Market Integration sequential after Automated Harvest
phase9 = StrictPartialOrder(nodes=[Packaging_Prep, Market_Integration])
phase9.order.add_edge(Packaging_Prep, Market_Integration)

# Now combine all phases in one big partial order

# Gather all nodes
all_nodes = [
    Site_Analysis, Structural_Retrofit,
    Nutrient_Mix, Seed_Selection,
    Hydroponic_Setup,
    Climate_Tuning, Lighting_Install, AI_Calibration,
    Pest_Detection, Growth_Monitoring,
    Water_Recycling,
    Yield_Prediction,
    Automated_Harvest,
    Packaging_Prep, Market_Integration
]

root = StrictPartialOrder(nodes=all_nodes)

# Add order edges within phases
root.order.add_edge(Site_Analysis, Structural_Retrofit)
# From Structural Retrofit to Nutrient Mix and Seed Selection (both)
root.order.add_edge(Structural_Retrofit, Nutrient_Mix)
root.order.add_edge(Structural_Retrofit, Seed_Selection)
# Nutrient Mix and Seed Selection to Hydroponic Setup
root.order.add_edge(Nutrient_Mix, Hydroponic_Setup)
root.order.add_edge(Seed_Selection, Hydroponic_Setup)
# Hydroponic Setup to Climate Tuning, Lighting Install, AI Calibration (all concurrent)
root.order.add_edge(Hydroponic_Setup, Climate_Tuning)
root.order.add_edge(Hydroponic_Setup, Lighting_Install)
root.order.add_edge(Hydroponic_Setup, AI_Calibration)
# Climate Tuning, Lighting Install, AI Calibration to Pest Detection and Growth Monitoring (both concurrent)
for parent in [Climate_Tuning, Lighting_Install, AI_Calibration]:
    root.order.add_edge(parent, Pest_Detection)
    root.order.add_edge(parent, Growth_Monitoring)
# Pest Detection to Water Recycling
root.order.add_edge(Pest_Detection, Water_Recycling)
# Pest Detection and Growth Monitoring to Yield Prediction
root.order.add_edge(Pest_Detection, Yield_Prediction)
root.order.add_edge(Growth_Monitoring, Yield_Prediction)
# Yield Prediction to Automated Harvest
root.order.add_edge(Yield_Prediction, Automated_Harvest)
# Automated Harvest to Packaging Prep to Market Integration
root.order.add_edge(Automated_Harvest, Packaging_Prep)
root.order.add_edge(Packaging_Prep, Market_Integration)