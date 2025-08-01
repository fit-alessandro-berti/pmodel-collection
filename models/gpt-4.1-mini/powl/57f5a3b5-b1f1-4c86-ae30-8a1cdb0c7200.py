# Generated from: 57f5a3b5-b1f1-4c86-ae30-8a1cdb0c7200.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farming system within a repurposed industrial building. It involves site analysis, environmental control installation, hydroponic system setup, seed selection, nutrient management, and continuous monitoring to optimize crop yield in limited urban spaces. The process also includes integration of IoT sensors for real-time data collection, pest control management using bio-agents, employee training for system operation, and coordination with local distributors for efficient produce delivery. Additionally, it covers waste recycling protocols to minimize environmental impact and the implementation of energy-efficient lighting and climate control systems to ensure sustainable operation throughout varied seasonal conditions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Install_HVAC = Transition(label='Install HVAC')
Setup_Hydroponics = Transition(label='Setup Hydroponics')
Seed_Selection = Transition(label='Seed Selection')
Nutrient_Mix = Transition(label='Nutrient Mix')
IoT_Integration = Transition(label='IoT Integration')
Monitor_Growth = Transition(label='Monitor Growth')
Pest_Control = Transition(label='Pest Control')
Harvest_Plan = Transition(label='Harvest Plan')
Employee_Train = Transition(label='Employee Train')
Waste_Recycle = Transition(label='Waste Recycle')
Energy_Audit = Transition(label='Energy Audit')
Packaging_Prep = Transition(label='Packaging Prep')
Distributor_Sync = Transition(label='Distributor Sync')

# Logical partial order with dependencies based on description:

# Phase 1: Site Survey -> Design Layout
# Phase 2: Design Layout -> Install HVAC & Energy Audit (can be concurrent after Design Layout)
# Phase 3: Install HVAC -> Setup Hydroponics
# Phase 4: Setup Hydroponics -> Seed Selection -> Nutrient Mix
# Phase 5: IoT Integration (can be concurrent with Pest Control and Employee Train)
# Phase 6: After Nutrient Mix, Monitor Growth and Pest Control can happen concurrently
# Phase 7: After Monitor Growth and Pest Control, Harvest Plan
# Phase 8: After Harvest Plan, Packaging Prep
# Phase 9: After Packaging Prep, Distributor Sync
# Phase 10: Waste Recycle is ongoing, assume concurrent at the end after Employee Train and Pest Control.

# Construct partial orders and concurrency along with these constraints:

# Build partial orders step by step:

# First partial order for initial steps:
po1 = StrictPartialOrder(nodes=[Site_Survey, Design_Layout])
po1.order.add_edge(Site_Survey, Design_Layout)

# Next after Design Layout: Install HVAC and Energy Audit concurrent after Design Layout
po2 = StrictPartialOrder(nodes=[Design_Layout, Install_HVAC, Energy_Audit])
po2.order.add_edge(Design_Layout, Install_HVAC)
po2.order.add_edge(Design_Layout, Energy_Audit)

# After Install HVAC: Setup Hydroponics
po3 = StrictPartialOrder(nodes=[Install_HVAC, Setup_Hydroponics])
po3.order.add_edge(Install_HVAC, Setup_Hydroponics)

# After Setup Hydroponics: Seed Selection
po4 = StrictPartialOrder(nodes=[Setup_Hydroponics, Seed_Selection])
po4.order.add_edge(Setup_Hydroponics, Seed_Selection)

# After Seed Selection: Nutrient Mix
po5 = StrictPartialOrder(nodes=[Seed_Selection, Nutrient_Mix])
po5.order.add_edge(Seed_Selection, Nutrient_Mix)

# After Nutrient Mix: Monitor Growth, Pest Control, Employee Train run concurrently
concurrent_mp = StrictPartialOrder(nodes=[Monitor_Growth, Pest_Control, Employee_Train])

# After Monitor Growth and Pest Control: Harvest Plan, so add edges from Monitor Growth and Pest Control to Harvest Plan
po_after_mp = StrictPartialOrder(nodes=[Monitor_Growth, Pest_Control, Harvest_Plan])
po_after_mp.order.add_edge(Monitor_Growth, Harvest_Plan)
po_after_mp.order.add_edge(Pest_Control, Harvest_Plan)

# Employee Train can be concurrent but probably needs to precede Waste Recycle (training for system)
# We'll consider Waste Recycle after Employee Train and possibly concurrent with Harvest-related activities

# After Harvest Plan: Packaging Prep
po_harvest = StrictPartialOrder(nodes=[Harvest_Plan, Packaging_Prep])
po_harvest.order.add_edge(Harvest_Plan, Packaging_Prep)

# After Packaging Prep: Distributor Sync
po_pack = StrictPartialOrder(nodes=[Packaging_Prep, Distributor_Sync])
po_pack.order.add_edge(Packaging_Prep, Distributor_Sync)

# Waste Recycle and IoT Integration concurrent with last phases (Employee Train and Packaging):
po_end_concurrent = StrictPartialOrder(nodes=[Employee_Train, Waste_Recycle, IoT_Integration])

# Finally combine all partial orders into a big one maintaining order edges:

# Combine all nodes:
all_nodes = [Site_Survey, Design_Layout, Install_HVAC, Energy_Audit, Setup_Hydroponics,
             Seed_Selection, Nutrient_Mix, Monitor_Growth, Pest_Control, Employee_Train,
             Harvest_Plan, Packaging_Prep, Distributor_Sync, Waste_Recycle, IoT_Integration]

root = StrictPartialOrder(nodes=all_nodes)

# Add edges based on all partial orders above:

# po1:
root.order.add_edge(Site_Survey, Design_Layout)

# po2:
root.order.add_edge(Design_Layout, Install_HVAC)
root.order.add_edge(Design_Layout, Energy_Audit)

# po3:
root.order.add_edge(Install_HVAC, Setup_Hydroponics)

# po4:
root.order.add_edge(Setup_Hydroponics, Seed_Selection)

# po5:
root.order.add_edge(Seed_Selection, Nutrient_Mix)

# concurrent_mp (Monitor_Growth, Pest_Control, Employee_Train) after Nutrient Mix:
root.order.add_edge(Nutrient_Mix, Monitor_Growth)
root.order.add_edge(Nutrient_Mix, Pest_Control)
root.order.add_edge(Nutrient_Mix, Employee_Train)

# After Monitor and Pest Control -> Harvest Plan
root.order.add_edge(Monitor_Growth, Harvest_Plan)
root.order.add_edge(Pest_Control, Harvest_Plan)

# Harvest Plan -> Packaging Prep -> Distributor Sync
root.order.add_edge(Harvest_Plan, Packaging_Prep)
root.order.add_edge(Packaging_Prep, Distributor_Sync)

# Waste Recycle after Employee Train (training supports recycling procedure)
root.order.add_edge(Employee_Train, Waste_Recycle)

# IoT Integration can start after Nutrient Mix (installation for real-time data)
root.order.add_edge(Nutrient_Mix, IoT_Integration)

# Waste Recycle and IoT Integration concurrent with post Employee Train and before Distributor Sync:
# No further order edge needed here; Waste Recycle and IoT Integration are independent after Employee Train

# Energy Audit independent after Design Layout and can run concurrent with everything until Distributor Sync (no strict order needed)

# The above completes the partial order description.
