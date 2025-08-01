# Generated from: 5e9b1592-4abe-45af-a761-1e7d07763c76.json
# Description: This process involves the complex orchestration of launching an urban vertical farm within a densely populated city environment. It includes site analysis, modular design planning, securing permits, integrating IoT sensors for climate control, sourcing sustainable materials, recruiting specialized agronomists, installing hydroponic systems, setting up renewable energy sources, executing controlled environment tests, developing a local supply chain, initiating community engagement programs, implementing waste recycling methods, launching a direct-to-consumer platform, conducting ongoing crop yield analysis, and establishing scalability frameworks for future expansion. Each step requires precise coordination of technology, regulatory compliance, and stakeholder involvement to ensure the farm's viability and sustainability in an unconventional agricultural setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Analysis = Transition(label='Site Analysis')
Design_Planning = Transition(label='Design Planning')
Permit_Securing = Transition(label='Permit Securing')
IoT_Integration = Transition(label='IoT Integration')
Material_Sourcing = Transition(label='Material Sourcing')
Recruit_Agronomists = Transition(label='Recruit Agronomists')
Hydroponic_Setup = Transition(label='Hydroponic Setup')
Energy_Installation = Transition(label='Energy Installation')
Environment_Testing = Transition(label='Environment Testing')
Supply_Chain = Transition(label='Supply Chain')
Community_Outreach = Transition(label='Community Outreach')
Waste_Recycling = Transition(label='Waste Recycling')
Platform_Launch = Transition(label='Platform Launch')
Yield_Analysis = Transition(label='Yield Analysis')
Scale_Framework = Transition(label='Scale Framework')

# Construct partial order representing the process flow and partial concurrency

# Create the strict partial order with all nodes
root = StrictPartialOrder(nodes=[
    Site_Analysis,
    Design_Planning,
    Permit_Securing,
    IoT_Integration,
    Material_Sourcing,
    Recruit_Agronomists,
    Hydroponic_Setup,
    Energy_Installation,
    Environment_Testing,
    Supply_Chain,
    Community_Outreach,
    Waste_Recycling,
    Platform_Launch,
    Yield_Analysis,
    Scale_Framework
])

# Define the order edges representing causality and concurrency constraints

# Initial site analysis leads to design planning and permit securing (these two can run concurrently after design)
root.order.add_edge(Site_Analysis, Design_Planning)
root.order.add_edge(Site_Analysis, Permit_Securing)

# After design planning: IoT integration and material sourcing can start concurrently
root.order.add_edge(Design_Planning, IoT_Integration)
root.order.add_edge(Design_Planning, Material_Sourcing)

# After permit securing: recruit agronomists (depends on permit)
root.order.add_edge(Permit_Securing, Recruit_Agronomists)

# Hydroponic setup depends on recruiting agronomists and sourcing materials (both must complete)
root.order.add_edge(Recruit_Agronomists, Hydroponic_Setup)
root.order.add_edge(Material_Sourcing, Hydroponic_Setup)

# Energy installation depends on design planning (can start once design is done)
root.order.add_edge(Design_Planning, Energy_Installation)

# Environment testing depends on hydroponic setup, IoT integration, and energy installation (all must complete)
root.order.add_edge(Hydroponic_Setup, Environment_Testing)
root.order.add_edge(IoT_Integration, Environment_Testing)
root.order.add_edge(Energy_Installation, Environment_Testing)

# Supply chain and community outreach start after environment testing - can run concurrently
root.order.add_edge(Environment_Testing, Supply_Chain)
root.order.add_edge(Environment_Testing, Community_Outreach)

# Waste recycling depends on community outreach
root.order.add_edge(Community_Outreach, Waste_Recycling)

# Platform launch depends on waste recycling and supply chain (both must complete)
root.order.add_edge(Waste_Recycling, Platform_Launch)
root.order.add_edge(Supply_Chain, Platform_Launch)

# Yield analysis depends on platform launch
root.order.add_edge(Platform_Launch, Yield_Analysis)

# Scale framework depends on yield analysis
root.order.add_edge(Yield_Analysis, Scale_Framework)