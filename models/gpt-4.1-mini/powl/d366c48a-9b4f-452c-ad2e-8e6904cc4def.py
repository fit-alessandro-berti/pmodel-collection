# Generated from: d366c48a-9b4f-452c-ad2e-8e6904cc4def.json
# Description: This process outlines the integration of urban vertical farming systems within existing city infrastructure to optimize food production and sustainability. It involves site assessment, environmental monitoring, modular installation, crop selection based on microclimate data, automated nutrient delivery, pest management using bio-controls, energy optimization via renewable sources, waste recycling through composting, real-time growth analytics, market demand forecasting, community engagement programs, regulatory compliance checks, supply chain synchronization, and continuous system upgrades. The process ensures efficient resource use, minimal environmental impact, and scalable urban agriculture solutions tailored for high-density metropolitan areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Survey = Transition(label='Site Survey')
Climate_Scan = Transition(label='Climate Scan')
Module_Setup = Transition(label='Module Setup')
Crop_Choice = Transition(label='Crop Choice')
Nutrient_Feed = Transition(label='Nutrient Feed')
Pest_Control = Transition(label='Pest Control')
Energy_Audit = Transition(label='Energy Audit')
Waste_Cycle = Transition(label='Waste Cycle')
Growth_Track = Transition(label='Growth Track')
Demand_Plan = Transition(label='Demand Plan')
Community_Link = Transition(label='Community Link')
Regulation_Check = Transition(label='Regulation Check')
Supply_Sync = Transition(label='Supply Sync')
System_Upgrade = Transition(label='System Upgrade')
Data_Backup = Transition(label='Data Backup')

# Build partial order according to process description with reasonable ordering and concurrency

# Early assessment and setup phase: Site Survey and Climate Scan concurrent, then Module Setup
early_assessment = StrictPartialOrder(nodes=[Site_Survey, Climate_Scan, Module_Setup])
early_assessment.order.add_edge(Site_Survey, Module_Setup)
early_assessment.order.add_edge(Climate_Scan, Module_Setup)

# Crop Choice depends on Climate Scan (microclimate data)
crop_choice_PO = StrictPartialOrder(nodes=[Crop_Choice])
crop_choice = StrictPartialOrder(nodes=[Climate_Scan, Crop_Choice])
crop_choice.order.add_edge(Climate_Scan, Crop_Choice)

# Nutrient Feed and Pest Control can start after Crop Choice and Module Setup
nutrient_pest_PO = StrictPartialOrder(
    nodes=[Nutrient_Feed, Pest_Control, Crop_Choice, Module_Setup])
nutrient_pest_PO.order.add_edge(Crop_Choice, Nutrient_Feed)
nutrient_pest_PO.order.add_edge(Crop_Choice, Pest_Control)
nutrient_pest_PO.order.add_edge(Module_Setup, Nutrient_Feed)
nutrient_pest_PO.order.add_edge(Module_Setup, Pest_Control)

# Energy Audit and Waste Cycle can happen concurrently after Module Setup
energy_waste_PO = StrictPartialOrder(nodes=[Energy_Audit, Waste_Cycle, Module_Setup])
energy_waste_PO.order.add_edge(Module_Setup, Energy_Audit)
energy_waste_PO.order.add_edge(Module_Setup, Waste_Cycle)

# Growth Track depends on Nutrient Feed and Pest Control
growth_PO = StrictPartialOrder(nodes=[Growth_Track, Nutrient_Feed, Pest_Control])
growth_PO.order.add_edge(Nutrient_Feed, Growth_Track)
growth_PO.order.add_edge(Pest_Control, Growth_Track)

# Demand Plan and Community Link can run concurrently after Growth Track
demand_community_PO = StrictPartialOrder(nodes=[Demand_Plan, Community_Link, Growth_Track])
demand_community_PO.order.add_edge(Growth_Track, Demand_Plan)
demand_community_PO.order.add_edge(Growth_Track, Community_Link)

# Regulation Check after Demand Plan and Community Link
regulation_PO = StrictPartialOrder(nodes=[Regulation_Check, Demand_Plan, Community_Link])
regulation_PO.order.add_edge(Demand_Plan, Regulation_Check)
regulation_PO.order.add_edge(Community_Link, Regulation_Check)

# Supply Sync after Regulation Check
supply_PO = StrictPartialOrder(nodes=[Supply_Sync, Regulation_Check])
supply_PO.order.add_edge(Regulation_Check, Supply_Sync)

# System Upgrade after Supply Sync and Growth Track (continuous improvements)
upgrade_PO = StrictPartialOrder(nodes=[System_Upgrade, Supply_Sync, Growth_Track])
upgrade_PO.order.add_edge(Supply_Sync, System_Upgrade)
upgrade_PO.order.add_edge(Growth_Track, System_Upgrade)

# Data Backup can be concurrent anytime, but typically after System Upgrade
backup_PO = StrictPartialOrder(nodes=[Data_Backup, System_Upgrade])
backup_PO.order.add_edge(System_Upgrade, Data_Backup)

# Combine all partial orders as concurrent where appropriate
# First combine early phases: early_assessment and crop_choice_PO
phase1 = StrictPartialOrder(
    nodes=[early_assessment, Crop_Choice])
phase1.order.add_edge(early_assessment, Crop_Choice)

# Combine nutrient/pest with energy/waste concurrent to each other after early phases
phase2 = StrictPartialOrder(
    nodes=[nutrient_pest_PO, energy_waste_PO])
# no order edges between nutrient_pest_PO and energy_waste_PO, concurrent

# Combine growth tracking and later phases sequentially:
phase3 = StrictPartialOrder(
    nodes=[growth_PO, demand_community_PO])
phase3.order.add_edge(growth_PO, demand_community_PO)

phase4 = StrictPartialOrder(
    nodes=[regulation_PO, supply_PO])
phase4.order.add_edge(regulation_PO, supply_PO)

phase5 = StrictPartialOrder(
    nodes=[upgrade_PO, backup_PO])
phase5.order.add_edge(upgrade_PO, backup_PO)

# Now assemble all major phases according to logical flow:

root = StrictPartialOrder(
    nodes=[phase1, phase2, phase3, phase4, phase5])

# Define order edges between phases:

root.order.add_edge(phase1, phase2)      # after early assessment and crop choice -> nutrient_pest and energy_waste
root.order.add_edge(phase2, phase3)      # after nutrient/energy -> growth and demand/community
root.order.add_edge(phase3, phase4)      # after growth/demand -> regulation and supply
root.order.add_edge(phase4, phase5)      # after supply -> system upgrade and backup