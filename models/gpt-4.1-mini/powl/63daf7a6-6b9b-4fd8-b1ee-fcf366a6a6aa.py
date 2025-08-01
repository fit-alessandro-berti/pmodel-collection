# Generated from: 63daf7a6-6b9b-4fd8-b1ee-fcf366a6a6aa.json
# Description: This process outlines the establishment of a fully automated urban vertical farm within a repurposed industrial warehouse. It involves site analysis, modular system design, environmental control integration, automated nutrient delivery, crop scheduling via AI, pest monitoring with drones, and real-time data analytics for yield optimization. The process also includes community engagement for local produce distribution, sustainability assessments, and iterative system upgrades to improve energy efficiency and crop variety diversification. Coordination between engineers, agronomists, and logistics managers is critical throughout to ensure seamless operation and scalability within dense urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Install_Modules = Transition(label='Install Modules')
Setup_HVAC = Transition(label='Setup HVAC')
Integrate_Sensors = Transition(label='Integrate Sensors')
Deploy_Drones = Transition(label='Deploy Drones')
Configure_AI = Transition(label='Configure AI')
Nutrient_Mix = Transition(label='Nutrient Mix')
Plant_Seeding = Transition(label='Plant Seeding')
Schedule_Crops = Transition(label='Schedule Crops')
Monitor_Growth = Transition(label='Monitor Growth')
Pest_Control = Transition(label='Pest Control')
Harvest_Plan = Transition(label='Harvest Plan')
Data_Analysis = Transition(label='Data Analysis')
Community_Outreach = Transition(label='Community Outreach')
Energy_Audit = Transition(label='Energy Audit')
Upgrade_Systems = Transition(label='Upgrade Systems')

# Partial order for site preparation and installation
preparation_installation = StrictPartialOrder(nodes=[Site_Survey, Design_Layout, Install_Modules])
preparation_installation.order.add_edge(Site_Survey, Design_Layout)
preparation_installation.order.add_edge(Design_Layout, Install_Modules)

# Environmental control: HVAC and Sensors can be done in parallel after modules installed
env_control = StrictPartialOrder(nodes=[Setup_HVAC, Integrate_Sensors])
# No edges: concurrent

# Deploy Drones after environmental control
drones = Deploy_Drones

# Configure AI and Nutrient Mix can be parallel after Deploy Drones
configure_ai_nutrient = StrictPartialOrder(nodes=[Configure_AI, Nutrient_Mix])
# No edges: concurrent

# Plant Seeding after nutrient mix and configure AI
plant_seeding = Plant_Seeding

# Schedule Crops after Plant Seeding
schedule_crops = Schedule_Crops

# Growth Monitoring and Pest Control are concurrent after scheduling crops
growth_monitoring_pest_control = StrictPartialOrder(nodes=[Monitor_Growth, Pest_Control])
# No edges: concurrent

# Harvest Plan after monitoring & pest control
harvest_plan = Harvest_Plan

# Data analysis after harvest planning
data_analysis = Data_Analysis

# Community Outreach and Energy Audit can happen in parallel after data analysis
community_energy = StrictPartialOrder(nodes=[Community_Outreach, Energy_Audit])
# No edges: concurrent

# Upgrade Systems after Energy Audit - form loop with Upgrade Systems feeding again (iteration)
loop_upgrade = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Energy_Audit, Upgrade_Systems]
)

# Construct the total process as a partial order with edges representing causal dependencies

nodes = [
    preparation_installation,
    env_control,
    drones,
    configure_ai_nutrient,
    plant_seeding,
    schedule_crops,
    growth_monitoring_pest_control,
    harvest_plan,
    data_analysis,
    community_energy,
    loop_upgrade
]

root = StrictPartialOrder(nodes=nodes)

# Add edges for the control flow

# Site prep -> Env control
root.order.add_edge(preparation_installation, env_control)

# Env control -> Deploy Drones
root.order.add_edge(env_control, drones)

# Deploy Drones -> Configure AI and Nutrient Mix
root.order.add_edge(drones, configure_ai_nutrient)

# Configure AI & Nutrient Mix -> Plant Seeding
root.order.add_edge(configure_ai_nutrient, plant_seeding)

# Plant Seeding -> Schedule Crops
root.order.add_edge(plant_seeding, schedule_crops)

# Schedule Crops -> (Monitor Growth, Pest Control)
root.order.add_edge(schedule_crops, growth_monitoring_pest_control)

# Monitor Growth & Pest Control -> Harvest Plan
root.order.add_edge(growth_monitoring_pest_control, harvest_plan)

# Harvest Plan -> Data Analysis
root.order.add_edge(harvest_plan, data_analysis)

# Data Analysis -> Community Outreach & Energy Audit
root.order.add_edge(data_analysis, community_energy)

# Energy Audit -> Upgrade Systems loop
root.order.add_edge(community_energy, loop_upgrade)

# Note: Community Outreach and Energy Audit are concurrent, edge goes from community_energy node to loop_upgrade,
# but loop_upgrade is a loop starting from energy audit and upgrade systems, which is modeled inside loop_upgrade.

# This captures the coordination, iterative upgrade, and concurrency described in the process.