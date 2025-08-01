# Generated from: 3df00e75-ba43-445b-849f-d59070b9b370.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban rooftop farm. It includes site assessment, structural analysis, soil preparation, microclimate optimization, seed selection, irrigation system design, pest management planning, community engagement, regulatory compliance, crop rotation scheduling, harvest logistics, waste recycling, and market distribution. Each activity ensures environmental sustainability, economic viability, and social inclusiveness in the unique context of urban agriculture on rooftops, accounting for space constraints, weather variability, and local regulations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Site_Survey = Transition(label='Site Survey')
Load_Analysis = Transition(label='Load Analysis')
Soil_Testing = Transition(label='Soil Testing')
Climate_Study = Transition(label='Climate Study')
Seed_Selection = Transition(label='Seed Selection')
Irrigation_Plan = Transition(label='Irrigation Plan')
Pest_Control = Transition(label='Pest Control')
Community_Meet = Transition(label='Community Meet')
Permit_Filing = Transition(label='Permit Filing')
Crop_Rotation = Transition(label='Crop Rotation')
Planting_Setup = Transition(label='Planting Setup')
Growth_Monitoring = Transition(label='Growth Monitoring')
Harvest_Prep = Transition(label='Harvest Prep')
Waste_Sorting = Transition(label='Waste Sorting')
Market_Delivery = Transition(label='Market Delivery')

# Model construction notes:
# - Initial site and structural assessment: Site Survey -> Load Analysis & Soil Testing (concurrent)
# - Microclimate and seed selection: Climate Study -> Seed Selection (sequential)
# - Irrigation and pest control plan: Irrigation Plan and Pest Control concurrent after seed
# - Community and permit: Community Meet and Permit Filing concurrent after irrigation+pest
# - Crop Rotation scheduling before actual planting/setup and monitoring (loop over crop rotation cycle)
# - Planting Setup -> Growth Monitoring -> Harvest Prep -> Waste Sorting -> Market Delivery (main production flow)
# - Crop Rotation loop: execute Crop Rotation then Planting Setup etc, then optionally repeat Crop Rotation or exit
# - All these flows should be maintained as PO and loop where relevant
#
# Step 1: Site Survey then parallel Load Analysis and Soil Testing
start_PO1 = StrictPartialOrder(nodes=[Site_Survey, Load_Analysis, Soil_Testing])
start_PO1.order.add_edge(Site_Survey, Load_Analysis)
start_PO1.order.add_edge(Site_Survey, Soil_Testing)

# Step 2: Climate Study then Seed Selection
seed_PO = StrictPartialOrder(nodes=[Climate_Study, Seed_Selection])
seed_PO.order.add_edge(Climate_Study, Seed_Selection)

# Step 3: Irrigation Plan and Pest Control concurrent after Seed Selection
irrig_pest_PO = StrictPartialOrder(nodes=[Irrigation_Plan, Pest_Control])

# Step 4: Community Meet and Permit Filing concurrent after irrigation+pest
comm_permit_PO = StrictPartialOrder(nodes=[Community_Meet, Permit_Filing])

# Step 5: Crop Rotation scheduling (loop node start)
# Step 6: The main production sequence after Crop Rotation:
production_PO = StrictPartialOrder(nodes=[Planting_Setup, Growth_Monitoring, Harvest_Prep, Waste_Sorting, Market_Delivery])
production_PO.order.add_edge(Planting_Setup, Growth_Monitoring)
production_PO.order.add_edge(Growth_Monitoring, Harvest_Prep)
production_PO.order.add_edge(Harvest_Prep, Waste_Sorting)
production_PO.order.add_edge(Waste_Sorting, Market_Delivery)

# Build step flows combining the above partial orders in order with edges

# After Seed selection -> irrigation and pest control concurrent
seed_to_irrig_pest_PO = StrictPartialOrder(nodes=[seed_PO, irrig_pest_PO])
seed_to_irrig_pest_PO.order.add_edge(seed_PO, irrig_pest_PO)

# After irrigation+pest -> community+permit
irrig_pest_to_comm_permit_PO = StrictPartialOrder(nodes=[irrig_pest_PO, comm_permit_PO])
irrig_pest_to_comm_permit_PO.order.add_edge(irrig_pest_PO, comm_permit_PO)

# After community+permit -> Loop over crop rotation and production
# Define loop: * (Crop_Rotation, production_PO)
loop_crop_production = OperatorPOWL(operator=Operator.LOOP, children=[Crop_Rotation, production_PO])

# Now, all main nodes combined into a big PO:
# Combine start_PO1, seed_to_irrig_pest_PO, irrig_pest_to_comm_permit_PO, loop_crop_production

root = StrictPartialOrder(
    nodes=[start_PO1, seed_to_irrig_pest_PO, irrig_pest_to_comm_permit_PO, loop_crop_production]
)

# Add orders:
root.order.add_edge(start_PO1, seed_to_irrig_pest_PO)
root.order.add_edge(seed_to_irrig_pest_PO, irrig_pest_to_comm_permit_PO)
root.order.add_edge(irrig_pest_to_comm_permit_PO, loop_crop_production)