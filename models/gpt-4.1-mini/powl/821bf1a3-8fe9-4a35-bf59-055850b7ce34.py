# Generated from: 821bf1a3-8fe9-4a35-bf59-055850b7ce34.json
# Description: This process outlines the comprehensive steps involved in establishing a fully operational urban vertical farm within a repurposed industrial building. It includes activities from initial site assessment, modular system design, and environmental simulation to crop selection, nutrient cycling optimization, and integrated pest management. The process also covers automation integration, energy efficiency calibration, and community engagement for sustainable urban agriculture. Continuous monitoring and adaptive control ensure maximized yield and minimal resource consumption in a confined urban environment, creating a scalable and eco-friendly food production model.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Load_Analysis = Transition(label='Load Analysis')
System_Design = Transition(label='System Design')
Env_Simulation = Transition(label='Env Simulation')

# Crop selection area with parallel seed prep and nutrient mix
Crop_Select = Transition(label='Crop Select')
Seed_Prep = Transition(label='Seed Prep')
Nutrient_Mix = Transition(label='Nutrient Mix')

Module_Setup = Transition(label='Module Setup')
Irrigation_Tune = Transition(label='Irrigation Tune')
Lighting_Adjust = Transition(label='Lighting Adjust')
Pest_Control = Transition(label='Pest Control')

Energy_Audit = Transition(label='Energy Audit')
Automation_Sync = Transition(label='Automation Sync')

Yield_Monitor = Transition(label='Yield Monitor')
Waste_Cycle = Transition(label='Waste Cycle')

Community_Meet = Transition(label='Community Meet')
Data_Review = Transition(label='Data Review')
System_Upgrade = Transition(label='System Upgrade')

# Define partial orders for concurrency inside crop selection area:
# Seed Prep and Nutrient Mix can run concurrently before Crop Select
# So let's model Seed Prep and Nutrient Mix in parallel, then Crop Select depends on both

crop_prep = StrictPartialOrder(nodes=[Seed_Prep, Nutrient_Mix])
# no order edges = Seed_Prep and Nutrient_Mix run concurrently

crop_select_po = StrictPartialOrder(nodes=[crop_prep, Crop_Select])
crop_select_po.order.add_edge(crop_prep, Crop_Select)

# Setup tuning steps in a partial order (Irrigation, Lighting, Pest Control) can be concurrent
tuning = StrictPartialOrder(nodes=[Irrigation_Tune, Lighting_Adjust, Pest_Control])
# no orders edges, fully concurrent

# Monitoring and waste cycle in partial order (concurrent)
monitoring = StrictPartialOrder(nodes=[Yield_Monitor, Waste_Cycle])
# no order edges

# Community Meet and Data Review, then System Upgrade
community_part = StrictPartialOrder(nodes=[Community_Meet, Data_Review, System_Upgrade])
community_part.order.add_edge(Data_Review, System_Upgrade)
community_part.order.add_edge(Community_Meet, System_Upgrade)

# Build the main process partial order
# Initial sequence: Site Survey -> Load Analysis -> System Design -> Env Simulation
# Then parallel: crop_select_po and module setup related

setup_modules = StrictPartialOrder(nodes=[
    Module_Setup,
    tuning
])
# Module Setup before tuning activities (all concurrent)
setup_modules.order.add_edge(Module_Setup, tuning)

# Automation Sync and Energy Audit can be concurrent but both after tuning
auto_energy = StrictPartialOrder(nodes=[Automation_Sync, Energy_Audit])
# no order edges

# Yield Monitor and Waste Cycle occur after automation and energy audit
monitoring_after = StrictPartialOrder(nodes=[monitoring])

# Finally Community part last

root = StrictPartialOrder(nodes=[
    Site_Survey,
    Load_Analysis,
    System_Design,
    Env_Simulation,
    crop_select_po,
    setup_modules,
    auto_energy,
    monitoring_after,
    community_part
])

# Adding order edges reflecting main flow dependencies:
root.order.add_edge(Site_Survey, Load_Analysis)
root.order.add_edge(Load_Analysis, System_Design)
root.order.add_edge(System_Design, Env_Simulation)

root.order.add_edge(Env_Simulation, crop_select_po)
root.order.add_edge(Env_Simulation, setup_modules)

# crop_select_po before automation and energy audit
root.order.add_edge(crop_select_po, auto_energy)

# module tuning before automation and energy audit
root.order.add_edge(setup_modules, auto_energy)

# automation and energy audit before monitoring
root.order.add_edge(auto_energy, monitoring_after)

# monitoring before community phase
root.order.add_edge(monitoring_after, community_part)