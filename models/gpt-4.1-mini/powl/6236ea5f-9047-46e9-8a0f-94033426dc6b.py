# Generated from: 6236ea5f-9047-46e9-8a0f-94033426dc6b.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farming operation within a dense metropolitan area. It includes site assessment, infrastructure customization to maximize limited space, integration of IoT sensors for environmental control, selection of crop varieties suited for vertical growth, installation of automated hydroponic systems, and the deployment of a renewable energy solution. The process further encompasses regulatory compliance with urban agriculture policies, staff training on advanced farming technologies, implementation of a logistics framework for fresh produce distribution, and continuous monitoring for yield optimization and sustainability metrics. This atypical yet realistic process addresses the complexities of modern urban farming to achieve efficient, scalable, and eco-friendly food production within city limits.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Assess = Transition(label='Site Assess')
Space_Design = Transition(label='Space Design')
IoT_Setup = Transition(label='IoT Setup')
Crop_Select = Transition(label='Crop Select')
Hydroponic_Install = Transition(label='Hydroponic Install')
Energy_Install = Transition(label='Energy Install')
Policy_Review = Transition(label='Policy Review')
Permit_Obtain = Transition(label='Permit Obtain')
Staff_Train = Transition(label='Staff Train')
System_Test = Transition(label='System Test')
Growth_Monitor = Transition(label='Growth Monitor')
Yield_Analyze = Transition(label='Yield Analyze')
Logistics_Plan = Transition(label='Logistics Plan')
Market_Launch = Transition(label='Market Launch')
Sustainability_Audit = Transition(label='Sustainability Audit')

# Step 1: Site Assess --> Space Design --> IoT Setup
po1 = StrictPartialOrder(nodes=[Site_Assess, Space_Design, IoT_Setup])
po1.order.add_edge(Site_Assess, Space_Design)
po1.order.add_edge(Space_Design, IoT_Setup)

# Step 2: Crop Select and Installations (Hydroponic, Energy) in partial order (parallel after IoT Setup)
installations = StrictPartialOrder(nodes=[Crop_Select, Hydroponic_Install, Energy_Install])
# no edges, so Crop Select, Hydroponic Install and Energy Install can happen concurrently

# Connect IoT_Setup to all of them in a PO including po1 and installations
po2 = StrictPartialOrder(nodes=[po1, installations])
po2.order.add_edge(po1, installations)  # po1 before installations

# Alternatively, we must model po1 ends before starting Crop_Select etc.

# Because StrictPartialOrder nodes can be mixed with other POWL, to better express partial order: 
# We'll build explicit big PO with all nodes and edges.

nodes = [Site_Assess, Space_Design, IoT_Setup,
         Crop_Select, Hydroponic_Install, Energy_Install,
         Policy_Review, Permit_Obtain,
         Staff_Train, System_Test,
         Growth_Monitor, Yield_Analyze,
         Logistics_Plan, Market_Launch,
         Sustainability_Audit]

root = StrictPartialOrder(nodes=nodes)

# Order dependencies:

# Initial setup:
root.order.add_edge(Site_Assess, Space_Design)
root.order.add_edge(Space_Design, IoT_Setup)

# After IoT_Setup: Crop_Select, Hydroponic_Install, Energy_Install in parallel (no edges among them)
root.order.add_edge(IoT_Setup, Crop_Select)
root.order.add_edge(IoT_Setup, Hydroponic_Install)
root.order.add_edge(IoT_Setup, Energy_Install)

# After installations: Policy_Review --> Permit_Obtain
root.order.add_edge(Crop_Select, Policy_Review)     # Crop_Select before Policy_Review
root.order.add_edge(Hydroponic_Install, Policy_Review)
root.order.add_edge(Energy_Install, Policy_Review)

root.order.add_edge(Policy_Review, Permit_Obtain)

# After permits obtained: Staff_Train
root.order.add_edge(Permit_Obtain, Staff_Train)

# After staff trained: System_Test
root.order.add_edge(Staff_Train, System_Test)

# After system test: Growth_Monitor
root.order.add_edge(System_Test, Growth_Monitor)

# Yield_Analyze depends on Growth_Monitor
root.order.add_edge(Growth_Monitor, Yield_Analyze)

# Logistics_Plan depends on Yield_Analyze
root.order.add_edge(Yield_Analyze, Logistics_Plan)

# Market_Launch depends on Logistics_Plan
root.order.add_edge(Logistics_Plan, Market_Launch)

# Sustainability_Audit happens concurrently with Growth Monitoring and Yield Analysis steps, but should come after Market_Launch
# real-world intuition: continuous sustainability audit likely concurrent with Growth_Monitor and Yield_Analyze, but 
# description says continuous monitoring and sustainability metrics, so let's put it starting after System_Test and concurrent with Growth_Monitor, Yield_Analyze

# Since concurrent nodes: no order edges are necessary to Growth_Monitor or Yield_Analyze, but Sustainability_Audit should come after System_Test.

root.order.add_edge(System_Test, Sustainability_Audit)

# Sustainability_Audit can happen in parallel with Growth_Monitor and Yield_Analyze and Logistics_Plan so no other edges 

# Summary:
# The process is linear mostly but with some concurrency after IoT_Setup for crop & installations, and concurrency of Sustainability audit in the later phase.

# Final root is a StrictPartialOrder as constructed
