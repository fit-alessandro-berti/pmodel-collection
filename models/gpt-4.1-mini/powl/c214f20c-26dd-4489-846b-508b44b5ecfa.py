# Generated from: c214f20c-26dd-4489-846b-508b44b5ecfa.json
# Description: This process outlines the integration of urban vertical farming systems into existing city infrastructure. It involves site analysis, modular farm design, environmental impact assessment, community engagement, regulatory approval, resource logistics, automated planting, crop monitoring, pest control, data analytics, harvest scheduling, waste recycling, energy optimization, distribution planning, and continuous system refinement to ensure sustainable food production within dense urban environments while minimizing ecological footprint and maximizing yield efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Analysis = Transition(label='Site Analysis')
Design_Modules = Transition(label='Design Modules')
Impact_Assess = Transition(label='Impact Assess')
Engage_Community = Transition(label='Engage Community')
Obtain_Approval = Transition(label='Obtain Approval')
Logistics_Plan = Transition(label='Logistics Plan')
Automated_Plant = Transition(label='Automated Plant')
Crop_Monitor = Transition(label='Crop Monitor')
Pest_Control = Transition(label='Pest Control')
Data_Analytics = Transition(label='Data Analytics')
Schedule_Harvest = Transition(label='Schedule Harvest')
Recycle_Waste = Transition(label='Recycle Waste')
Optimize_Energy = Transition(label='Optimize Energy')
Plan_Distribution = Transition(label='Plan Distribution')
Refine_System = Transition(label='Refine System')

# Define a partial order for the main process flow
root = StrictPartialOrder(nodes=[
    Site_Analysis,
    Design_Modules,
    Impact_Assess,
    Engage_Community,
    Obtain_Approval,
    Logistics_Plan,
    Automated_Plant,
    Crop_Monitor,
    Pest_Control,
    Data_Analytics,
    Schedule_Harvest,
    Recycle_Waste,
    Optimize_Energy,
    Plan_Distribution,
    Refine_System
])

# Adding edges to reflect logical orderings and partial concurrency
root.order.add_edge(Site_Analysis, Design_Modules)
root.order.add_edge(Design_Modules, Impact_Assess)
root.order.add_edge(Impact_Assess, Engage_Community)
root.order.add_edge(Engage_Community, Obtain_Approval)

root.order.add_edge(Obtain_Approval, Logistics_Plan)

# After Logistics Plan, several activities can be done concurrently and partially ordered
root.order.add_edge(Logistics_Plan, Automated_Plant)
root.order.add_edge(Logistics_Plan, Crop_Monitor)
root.order.add_edge(Logistics_Plan, Pest_Control)

# Crop monitoring and pest control likely overlap but do not strictly depend on each other
# Data analytics depends on Crop Monitor and Pest Control
root.order.add_edge(Crop_Monitor, Data_Analytics)
root.order.add_edge(Pest_Control, Data_Analytics)

# Schedule Harvest depends on Data Analytics
root.order.add_edge(Data_Analytics, Schedule_Harvest)

# Waste recycling and energy optimization can happen in parallel and depend on Schedule Harvest
root.order.add_edge(Schedule_Harvest, Recycle_Waste)
root.order.add_edge(Schedule_Harvest, Optimize_Energy)

# Plan Distribution depends on Schedule Harvest
root.order.add_edge(Schedule_Harvest, Plan_Distribution)

# Refine System depends on completion of Recycling, Energy, Distribution (converging point)
root.order.add_edge(Recycle_Waste, Refine_System)
root.order.add_edge(Optimize_Energy, Refine_System)
root.order.add_edge(Plan_Distribution, Refine_System)