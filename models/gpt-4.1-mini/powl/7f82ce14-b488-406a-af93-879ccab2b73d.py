# Generated from: 7f82ce14-b488-406a-af93-879ccab2b73d.json
# Description: This process outlines the establishment of an urban vertical farm within a densely populated city environment. It involves specialized steps including site assessment for structural integrity, climate control system design tailored to microclimates, modular hydroponic installation, custom nutrient formula development, and integration of AI-driven crop monitoring. The process further incorporates community engagement for sustainable sourcing, waste recycling through bio-composting, and adaptive lighting schedules to optimize growth cycles. Each activity ensures the farm operates efficiently while minimizing environmental impact and maximizing yield in limited urban space.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Site_Assess = Transition(label='Site Assess')
Structure_Check = Transition(label='Structure Check')
Climate_Design = Transition(label='Climate Design')
Hydroponic_Setup = Transition(label='Hydroponic Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
AI_Integration = Transition(label='AI Integration')
Crop_Monitor = Transition(label='Crop Monitor')
Lighting_Adjust = Transition(label='Lighting Adjust')
Waste_Recycle = Transition(label='Waste Recycle')
Bio_Compost = Transition(label='Bio-Compost')
Water_Testing = Transition(label='Water Testing')
Energy_Audit = Transition(label='Energy Audit')
Seed_Selection = Transition(label='Seed Selection')
Community_Meet = Transition(label='Community Meet')
Yield_Forecast = Transition(label='Yield Forecast')

# Step 1 & 2 (site assessment and structure check): sequential mandatory steps
site_structure_PO = StrictPartialOrder(nodes=[Site_Assess, Structure_Check])
site_structure_PO.order.add_edge(Site_Assess, Structure_Check)

# Step 3: Climate design (depends on structure check)
# Step 4: Hydroponic setup (after climate design)
# Step 5: Nutrient mix (after hydroponic)
climate_hydro_nutrient_PO = StrictPartialOrder(nodes=[Climate_Design, Hydroponic_Setup, Nutrient_Mix])
climate_hydro_nutrient_PO.order.add_edge(Climate_Design, Hydroponic_Setup)
climate_hydro_nutrient_PO.order.add_edge(Hydroponic_Setup, Nutrient_Mix)

# Connect structure check to climate design
# Combine site_structure_PO and climate_hydro_nutrient_PO partial orders by adding edges from site_structure_PO to climate_hydro_nutrient_PO
# We'll combine all these nodes and edges in a larger PO after

# Step 6: AI Integration and Crop Monitor are connected (monitor depends on integration)
ai_PO = StrictPartialOrder(nodes=[AI_Integration, Crop_Monitor])
ai_PO.order.add_edge(AI_Integration, Crop_Monitor)

# Step 7: Lighting Adjust (adaptive lighting schedules to optimize growth cycles)
# Step 8&9: Waste recycle and Bio-Compost (waste recycling through bio-composting)
waste_PO = StrictPartialOrder(nodes=[Waste_Recycle, Bio_Compost])
waste_PO.order.add_edge(Waste_Recycle, Bio_Compost)

# Step 11,12,13: Water Testing, Energy Audit, Seed Selection - supportive activities, likely can be done in parallel after Nutrient Mix
supportive_PO = StrictPartialOrder(nodes=[Water_Testing, Energy_Audit, Seed_Selection])

# Step 14: Community Meet (community engagement for sustainable sourcing)
# Step 15: Yield Forecast (final forecast, after most activities completed)
# Community Meet likely depends on Waste Recycle (to be sustainable sourcing)

# Combine all together:
# We'll make a big PO including:
# site_structure_PO + climate_hydro_nutrient_PO + ai_PO + waste_PO + supportive_PO + Community_Meet + Lighting_Adjust + Yield_Forecast
#
# Add edges to represent dependencies:
# Structure_Check --> Climate_Design (already in separate pos but need to join)
# Nutrient_Mix --> AI_Integration (likely after fert mix AI integration)
# Nutrient_Mix --> Lighting_Adjust (adaptive lighting to nutrient)
# AI_Integration --> Crop_Monitor (already in ai_PO)
# Waste_Recycle --> Community_Meet
# Bio_Compost --> Community_Meet
# Water_Testing, Energy_Audit, Seed_Selection all after Nutrient_Mix
# Community_Meet --> Yield_Forecast
# Crop_Monitor --> Yield_Forecast
# Lighting_Adjust --> Yield_Forecast

all_nodes = [
    Site_Assess,
    Structure_Check,
    Climate_Design,
    Hydroponic_Setup,
    Nutrient_Mix,
    AI_Integration,
    Crop_Monitor,
    Lighting_Adjust,
    Waste_Recycle,
    Bio_Compost,
    Water_Testing,
    Energy_Audit,
    Seed_Selection,
    Community_Meet,
    Yield_Forecast,
]

root = StrictPartialOrder(nodes=all_nodes)

# Add order edges
# Site assess to structure check
root.order.add_edge(Site_Assess, Structure_Check)
# Structure check to climate design
root.order.add_edge(Structure_Check, Climate_Design)
# Climate design to hydroponic setup
root.order.add_edge(Climate_Design, Hydroponic_Setup)
# Hydroponic setup to nutrient mix
root.order.add_edge(Hydroponic_Setup, Nutrient_Mix)
# Nutrient mix to AI integration
root.order.add_edge(Nutrient_Mix, AI_Integration)
# Nutrient mix to lighting adjust
root.order.add_edge(Nutrient_Mix, Lighting_Adjust)
# AI integration to crop monitor
root.order.add_edge(AI_Integration, Crop_Monitor)
# Waste recycle to bio-compost
root.order.add_edge(Waste_Recycle, Bio_Compost)
# Waste recycle and bio-compost to community meet
root.order.add_edge(Waste_Recycle, Community_Meet)
root.order.add_edge(Bio_Compost, Community_Meet)
# Nutrient mix to water testing, energy audit, seed selection (parallel)
root.order.add_edge(Nutrient_Mix, Water_Testing)
root.order.add_edge(Nutrient_Mix, Energy_Audit)
root.order.add_edge(Nutrient_Mix, Seed_Selection)
# Community meet, crop monitor, lighting adjust to yield forecast
root.order.add_edge(Community_Meet, Yield_Forecast)
root.order.add_edge(Crop_Monitor, Yield_Forecast)
root.order.add_edge(Lighting_Adjust, Yield_Forecast)