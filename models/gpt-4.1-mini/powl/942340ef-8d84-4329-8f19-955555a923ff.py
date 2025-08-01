# Generated from: 942340ef-8d84-4329-8f19-955555a923ff.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban rooftop farm on a commercial building. It involves site analysis, structural assessment, environmental impact evaluation, crop selection based on microclimate, soil preparation with imported organic matter, installation of automated irrigation systems, pest control planning, integration of renewable energy sources, community engagement for training, regulatory compliance checks, and continuous monitoring of crop growth and resource usage to ensure optimal yield and sustainability within an urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Survey = Transition(label='Site Survey')
Load_Test = Transition(label='Load Test')
Climate_Study = Transition(label='Climate Study')
Crop_Choose = Transition(label='Crop Choose')
Soil_Prep = Transition(label='Soil Prep')
Irrigation_Install = Transition(label='Irrigation Install')
Pest_Plan = Transition(label='Pest Plan')
Energy_Setup = Transition(label='Energy Setup')
Permits_Acquire = Transition(label='Permits Acquire')
Community_Meet = Transition(label='Community Meet')
Training_Plan = Transition(label='Training Plan')
Plant_Seed = Transition(label='Plant Seed')
Growth_Monitor = Transition(label='Growth Monitor')
Harvest_Plan = Transition(label='Harvest Plan')
Waste_Manage = Transition(label='Waste Manage')
Yield_Analyze = Transition(label='Yield Analyze')

# Build the partial orders reflecting the process structure:

# Step 1: Site Analysis and Structural Assessment
site_structural_po = StrictPartialOrder(nodes=[Site_Survey, Load_Test])
site_structural_po.order.add_edge(Site_Survey, Load_Test)

# Step 2: Environmental Impact & Crop Selection
env_crop_po = StrictPartialOrder(nodes=[Climate_Study, Crop_Choose])
env_crop_po.order.add_edge(Climate_Study, Crop_Choose)

# Step 3: Soil Preparation and Irrigation Installation
soil_irrigation_po = StrictPartialOrder(nodes=[Soil_Prep, Irrigation_Install])
soil_irrigation_po.order.add_edge(Soil_Prep, Irrigation_Install)

# Step 4: Pest Plan and Energy Setup in parallel (no direct ordering)
pest_energy_po = StrictPartialOrder(nodes=[Pest_Plan, Energy_Setup])

# Step 5: Regulatory and Community-related activities (Permits Acquire before Community Meet & Training Plan)
permits = Permits_Acquire
community_training_po = StrictPartialOrder(nodes=[Community_Meet, Training_Plan])
community_training_po.order.add_edge(Community_Meet, Training_Plan)
permits_community_po = StrictPartialOrder(nodes=[permits, community_training_po])
permits_community_po.order.add_edge(permits, community_training_po)

# Since StrictPartialOrder.nodes expects a list of POWL nodes, 
# and community_training_po is a StrictPartialOrder, treat as node.

# Step 6: Plant Seed after training plan
# Combine Plant Seed after Training Plan
plant_seed_po = StrictPartialOrder(nodes=[community_training_po, Plant_Seed])
plant_seed_po.order.add_edge(community_training_po, Plant_Seed)

# Step 7: Monitoring loop (Growth Monitor): 
# model a loop where Growth Monitor is done repeatedly, optionally Harvest Plan happens (then loop again)
# but this is more like:
# loop: (* (Growth Monitor, Harvest Plan))

monitor_harvest_loop = OperatorPOWL(operator=Operator.LOOP, children=[Growth_Monitor, Harvest_Plan])

# Step 8: After loop, Waste Manage and Yield Analyze in partial order (can be concurrent)
waste_yield_po = StrictPartialOrder(nodes=[Waste_Manage, Yield_Analyze])

# Now combine all higher level steps into a partial order according to sequence:

# site_structural_po --> env_crop_po --> soil_irrigation_po --> pest_energy_po --> permits_community_po --> plant_seed_po --> monitor_harvest_loop --> waste_yield_po

root = StrictPartialOrder(
    nodes=[
        site_structural_po,
        env_crop_po,
        soil_irrigation_po,
        pest_energy_po,
        permits_community_po,
        plant_seed_po,
        monitor_harvest_loop,
        waste_yield_po,
    ]
)

root.order.add_edge(site_structural_po, env_crop_po)
root.order.add_edge(env_crop_po, soil_irrigation_po)
root.order.add_edge(soil_irrigation_po, pest_energy_po)
root.order.add_edge(pest_energy_po, permits_community_po)
root.order.add_edge(permits_community_po, plant_seed_po)
root.order.add_edge(plant_seed_po, monitor_harvest_loop)
root.order.add_edge(monitor_harvest_loop, waste_yield_po)