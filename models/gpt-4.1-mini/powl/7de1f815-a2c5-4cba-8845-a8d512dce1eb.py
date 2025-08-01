# Generated from: 7de1f815-a2c5-4cba-8845-a8d512dce1eb.json
# Description: This process outlines the setup of an urban rooftop farm, integrating advanced hydroponics with renewable energy sources and waste recycling systems. It involves site assessment, structural analysis, soil and water testing, equipment procurement, installation of solar panels and water recycling units, seed selection, planting schedules, pest control using natural predators, data monitoring through IoT devices, and community engagement for educational workshops. The process ensures sustainability, maximizes crop yield in limited space, and promotes urban greening while adhering to local regulations and safety standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transition objects
Site_Survey = Transition(label='Site Survey')
Structure_Check = Transition(label='Structure Check')
Soil_Sample = Transition(label='Soil Sample')
Water_Test = Transition(label='Water Test')
Procure_Gear = Transition(label='Procure Gear')
Install_Panels = Transition(label='Install Panels')
Setup_Hydro = Transition(label='Setup Hydro')
Seed_Select = Transition(label='Seed Select')
Plant_Crop = Transition(label='Plant Crop')
Pest_Control = Transition(label='Pest Control')
IoT_Config = Transition(label='IoT Config')
Data_Monitor = Transition(label='Data Monitor')
Waste_Recycle = Transition(label='Waste Recycle')
Safety_Audit = Transition(label='Safety Audit')
Host_Workshop = Transition(label='Host Workshop')
Yield_Review = Transition(label='Yield Review')

# Define partial orders representing logical grouping and concurrency

# Assessment phase (site, structure, soil and water tests): partially ordered, some concurrency
assessment = StrictPartialOrder(nodes=[Site_Survey, Structure_Check, Soil_Sample, Water_Test])
assessment.order.add_edge(Site_Survey, Structure_Check)
assessment.order.add_edge(Site_Survey, Soil_Sample)
assessment.order.add_edge(Site_Survey, Water_Test)

# Procurement and installation - first Procure Gear, then Install Panels and Setup Hydro in parallel
installation = StrictPartialOrder(nodes=[Procure_Gear, Install_Panels, Setup_Hydro])
installation.order.add_edge(Procure_Gear, Install_Panels)
installation.order.add_edge(Procure_Gear, Setup_Hydro)

# Planting phase - Seed Select then Plant Crop
planting = StrictPartialOrder(nodes=[Seed_Select, Plant_Crop])
planting.order.add_edge(Seed_Select, Plant_Crop)

# Environmental control phase: Pest Control, IoT Config and Data Monitor in partial order
# Pest Control before Data Monitor
env_monitor = StrictPartialOrder(nodes=[Pest_Control, IoT_Config, Data_Monitor])
env_monitor.order.add_edge(Pest_Control, Data_Monitor)
# IoT Config before Data Monitor
env_monitor.order.add_edge(IoT_Config, Data_Monitor)

# Sustainability systems: Waste Recycle and Safety Audit can be concurrent
sustainability = StrictPartialOrder(nodes=[Waste_Recycle, Safety_Audit])

# Community engagement: Host Workshop after Sustainability and Planting (community best after setup)
community = Host_Workshop

# Yield review after data monitoring and planting and safety audit (ensuring all done)
final_review = Yield_Review

# Build partial order root combining all phases with dependencies representing process flow

root = StrictPartialOrder(
    nodes=[assessment, installation, planting, env_monitor, sustainability, community, final_review]
)

# Order edges between phases
root.order.add_edge(assessment, installation)     # assessment before installation
root.order.add_edge(installation, planting)      # installation before planting
root.order.add_edge(planting, env_monitor)       # planting before environment monitoring
root.order.add_edge(sustainability, community)   # sustainability before community workshop

# community workshop after planting (community engagement after crop planted)
root.order.add_edge(planting, community)

# data monitor before yield review, safety audit before yield review, planting before yield review
root.order.add_edge(env_monitor, final_review)
root.order.add_edge(sustainability, final_review)
root.order.add_edge(planting, final_review)