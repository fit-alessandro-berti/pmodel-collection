# Generated from: 62456c42-47de-4e2a-9066-fff64616273e.json
# Description: This process outlines the establishment of a vertical farming facility within an urban environment, integrating advanced hydroponic systems, renewable energy sources, and AI-driven crop monitoring. It begins with site analysis and structural assessment, followed by modular farm design and procurement of specialized equipment. Installation includes climate control setup, nutrient delivery systems, and automated lighting. Continuous data collection enables real-time adjustments to optimize growth cycles. The process incorporates waste recycling, pest management without chemicals, and community engagement initiatives to promote sustainable urban agriculture. Final stages involve yield analysis, distribution logistics, and scalability planning to expand operations efficiently.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Analysis = Transition(label='Site Analysis')
Structure_Check = Transition(label='Structure Check')
Design_Farm = Transition(label='Design Farm')
Order_Equipment = Transition(label='Order Equipment')
Install_Hydroponics = Transition(label='Install Hydroponics')
Setup_Climate = Transition(label='Setup Climate')
Configure_Lighting = Transition(label='Configure Lighting')
Program_AI = Transition(label='Program AI')
Calibrate_Sensors = Transition(label='Calibrate Sensors')
Nutrient_Mix = Transition(label='Nutrient Mix')
Waste_Recycling = Transition(label='Waste Recycling')
Pest_Control = Transition(label='Pest Control')
Data_Monitoring = Transition(label='Data Monitoring')
Community_Outreach = Transition(label='Community Outreach')
Yield_Assessment = Transition(label='Yield Assessment')
Logistics_Plan = Transition(label='Logistics Plan')
Scale_Strategy = Transition(label='Scale Strategy')

# Phase 1: Site analysis and structural assessment
phase1 = StrictPartialOrder(nodes=[Site_Analysis, Structure_Check])
phase1.order.add_edge(Site_Analysis, Structure_Check)

# Phase 2: Modular farm design and procurement
phase2 = StrictPartialOrder(nodes=[Design_Farm, Order_Equipment])
phase2.order.add_edge(Design_Farm, Order_Equipment)

# Phase 3: Installation (climate control, nutrient delivery, lighting)
installation = StrictPartialOrder(
    nodes=[Install_Hydroponics, Setup_Climate, Nutrient_Mix, Configure_Lighting]
)
installation.order.add_edge(Install_Hydroponics, Setup_Climate)
installation.order.add_edge(Install_Hydroponics, Nutrient_Mix)
installation.order.add_edge(Install_Hydroponics, Configure_Lighting)

# Phase 4: AI-driven setup (program AI, calibrate sensors)
ai_setup = StrictPartialOrder(nodes=[Program_AI, Calibrate_Sensors])
ai_setup.order.add_edge(Program_AI, Calibrate_Sensors)

# Phase 5: Operations management (waste recycling, pest control, data monitoring, community outreach)
ops_mgmt = StrictPartialOrder(
    nodes=[Waste_Recycling, Pest_Control, Data_Monitoring, Community_Outreach]
)
# No order edges to represent concurrency

# Phase 6: Final stages (yield assessment, logistics plan, scale strategy)
final_stages = StrictPartialOrder(
    nodes=[Yield_Assessment, Logistics_Plan, Scale_Strategy]
)
final_stages.order.add_edge(Yield_Assessment, Logistics_Plan)
final_stages.order.add_edge(Logistics_Plan, Scale_Strategy)

# Compose overall partial order
nodes = [phase1, phase2, installation, ai_setup, ops_mgmt, final_stages]
root = StrictPartialOrder(nodes=nodes)

# Define inter-phase ordering based on process description
root.order.add_edge(phase1, phase2)         # After site analysis & structure check -> design & order
root.order.add_edge(phase2, installation)   # After design & order -> installation
root.order.add_edge(installation, ai_setup) # After installation -> AI setup
root.order.add_edge(ai_setup, ops_mgmt)     # After AI setup -> operations management
root.order.add_edge(ops_mgmt, final_stages) # After operations -> final stages