# Generated from: 486ea4a2-bf97-48f6-a25c-5a179d97d2aa.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farming operation within a constrained city environment. It includes securing appropriate permits, designing modular farm units, sourcing sustainable materials, implementing automated hydroponic systems, integrating IoT sensors for environmental monitoring, training specialized staff, establishing supply chain contracts for organic seeds and nutrients, conducting iterative growth trials, optimizing energy usage with renewable sources, setting up waste recycling for zero discharge, marketing niche urban produce, ensuring compliance with health regulations, and deploying a digital platform to manage farm operations and customer orders. The process demands cross-functional coordination across urban planning, agriculture technology, environmental science, and business development to successfully launch a profitable and sustainable vertical farm.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Permit_Acquisition = Transition(label='Permit Acquisition')
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Material_Sourcing = Transition(label='Material Sourcing')
System_Assembly = Transition(label='System Assembly')
IoT_Integration = Transition(label='IoT Integration')
Staff_Training = Transition(label='Staff Training')
Seed_Procurement = Transition(label='Seed Procurement')
Growth_Trials = Transition(label='Growth Trials')
Energy_Optimization = Transition(label='Energy Optimization')
Waste_Recycling = Transition(label='Waste Recycling')
Regulation_Check = Transition(label='Regulation Check')
Supply_Contracts = Transition(label='Supply Contracts')
Marketing_Launch = Transition(label='Marketing Launch')
Platform_Deployment = Transition(label='Platform Deployment')
Customer_Onboarding = Transition(label='Customer Onboarding')
Performance_Review = Transition(label='Performance Review')

# Build partial orders for the main sequential flow that requires order:

# Phase 1: Permit Acquisition and Site Survey (likely sequential)
phase1 = StrictPartialOrder(nodes=[Permit_Acquisition, Site_Survey])
phase1.order.add_edge(Permit_Acquisition, Site_Survey)

# Phase 2: Design and sourcing and assembly
phase2 = StrictPartialOrder(nodes=[Design_Layout, Material_Sourcing, System_Assembly])
phase2.order.add_edge(Design_Layout, Material_Sourcing)
phase2.order.add_edge(Material_Sourcing, System_Assembly)

# Phase 3: IoT integration and Staff Training (IoT first, then Staff Training)
phase3 = StrictPartialOrder(nodes=[IoT_Integration, Staff_Training])
phase3.order.add_edge(IoT_Integration, Staff_Training)

# Phase 4: Seed Procurement and Supply Contracts (both related to supply chain)
phase4 = StrictPartialOrder(nodes=[Seed_Procurement, Supply_Contracts])
# no enforced order between seed procurement and supply contracts => concurrent

# Growth trials loop with Performance Review
# We will model Growth Trials, then a loop where Energy Optimization, Waste Recycling, Regulation Check run potentially repeated optimizing cycle before performance review

# Define the loop body: the repeated activities before re-running growth trials
# We model this as a partial order of Energy Optimization --> Waste Recycling --> Regulation Check
# This sequence can be considered a single activity in the loop
loop_body_seq = StrictPartialOrder(nodes=[Energy_Optimization, Waste_Recycling, Regulation_Check])
loop_body_seq.order.add_edge(Energy_Optimization, Waste_Recycling)
loop_body_seq.order.add_edge(Waste_Recycling, Regulation_Check)

# The loop is Growth Trials, then optionally repeat (loop_body_seq + Growth Trials)
loop = OperatorPOWL(operator=Operator.LOOP, children=[Growth_Trials, loop_body_seq])

# After loop finish, Performance Review occurs
post_growth = Performance_Review

# Marketing Launch and Platform Deployment and Customer Onboarding are business launch activities
# Marketing Launch and Platform Deployment likely concurrent start, followed by Customer Onboarding
marketing_platform = StrictPartialOrder(nodes=[Marketing_Launch, Platform_Deployment, Customer_Onboarding])
# Marketing Launch and Platform Deployment concurrent (no edges)
marketing_platform.order.add_edge(Marketing_Launch, Customer_Onboarding)
marketing_platform.order.add_edge(Platform_Deployment, Customer_Onboarding)

# Now compose all parts in order reflecting the process dependencies:
# phase1 -> phase2 -> phase3 -> phase4(concurrent Seed Proc and Supply Contracts) -> loop -> Performance Review -> marketing_platform

# Compose phase4 as partial order with two concurrent nodes
phase4 = StrictPartialOrder(nodes=[Seed_Procurement, Supply_Contracts])
# no order edge (concurrent)

# Compose whole partial order root
root = StrictPartialOrder(
    nodes=[
        phase1,
        phase2,
        phase3,
        phase4,
        loop,
        post_growth,
        marketing_platform
    ]
)

# Add edges to enforce sequence between phases
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, phase3)
root.order.add_edge(phase3, phase4)
root.order.add_edge(phase4, loop)
root.order.add_edge(loop, post_growth)
root.order.add_edge(post_growth, marketing_platform)