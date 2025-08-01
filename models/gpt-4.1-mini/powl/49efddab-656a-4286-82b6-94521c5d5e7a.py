# Generated from: 49efddab-656a-4286-82b6-94521c5d5e7a.json
# Description: This process outlines the intricate steps involved in transforming underutilized urban rooftop spaces into productive, sustainable farms. It includes assessing structural integrity, securing permits, designing modular irrigation systems, sourcing organic seeds, and training local community members. The workflow also addresses crop rotation planning to maximize yield, integrating solar-powered sensors for optimal growth conditions, managing waste composting onsite, coordinating with local markets for direct sales, and implementing seasonal maintenance protocols to ensure long-term farm health and community engagement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Inspect_Roof = Transition(label='Inspect Roof')
Permit_Apply = Transition(label='Permit Apply')
Design_Layout = Transition(label='Design Layout')
Irrigation_Setup = Transition(label='Irrigation Setup')
Seed_Sourcing = Transition(label='Seed Sourcing')
Soil_Testing = Transition(label='Soil Testing')
Install_Sensors = Transition(label='Install Sensors')
Compost_Setup = Transition(label='Compost Setup')
Plant_Seeds = Transition(label='Plant Seeds')
Train_Staff = Transition(label='Train Staff')
Crop_Rotate = Transition(label='Crop Rotate')
Market_Plan = Transition(label='Market Plan')
Waste_Collect = Transition(label='Waste Collect')
Harvest_Crop = Transition(label='Harvest Crop')
Maintenance_Check = Transition(label='Maintenance Check')
Community_Meet = Transition(label='Community Meet')

# Phase 1: Assess and Approval
phase1 = StrictPartialOrder(nodes=[Inspect_Roof, Permit_Apply])
phase1.order.add_edge(Inspect_Roof, Permit_Apply)

# Phase 2: Design and Setup: Design Layout, Irrigation Setup, Soil Testing, Install Sensors, Compost Setup
phase2 = StrictPartialOrder(nodes=[Design_Layout, Irrigation_Setup, Soil_Testing, Install_Sensors, Compost_Setup])
phase2.order.add_edge(Design_Layout, Irrigation_Setup)
phase2.order.add_edge(Design_Layout, Soil_Testing)
phase2.order.add_edge(Design_Layout, Install_Sensors)
phase2.order.add_edge(Design_Layout, Compost_Setup)

# Phase 3: Seed and Plant Preparation: Seed Sourcing, Plant Seeds, Train Staff
phase3 = StrictPartialOrder(nodes=[Seed_Sourcing, Plant_Seeds, Train_Staff])
phase3.order.add_edge(Seed_Sourcing, Plant_Seeds)
phase3.order.add_edge(Train_Staff, Plant_Seeds)  # Staff training concurrent with seed sourcing but must finish before planting

# Phase 4: Crop Management: Crop Rotate, Market Plan, Waste Collect
phase4 = StrictPartialOrder(nodes=[Crop_Rotate, Market_Plan, Waste_Collect])
# Crop rotation affects harvesting, Market plan and waste collect concurrent

# Phase 5: Harvest and Maintenance Loop: Harvest Crop, Maintenance Check, Community Meet
maintenance_loop_body = StrictPartialOrder(nodes=[Harvest_Crop, Maintenance_Check, Community_Meet])
maintenance_loop_body.order.add_edge(Harvest_Crop, Maintenance_Check)
maintenance_loop_body.order.add_edge(Maintenance_Check, Community_Meet)

# Loop: After harvest, do maintenance and community meet, then can repeat or exit
harvest_maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[Harvest_Crop, StrictPartialOrder(nodes=[Maintenance_Check, Community_Meet])])

# Connect the maintenance loop properly - but needs to do maintenance and community after each harvest, so use LOOP operator sensibly:
# LOOP(body=Harvest_Crop, redo=PO(Maintenance_Check and Community_Meet))
# However, the LOOP operator takes exactly two children: A, B. 
# The usual meaning: do A, then choose to exit or do B then A again.
# So set:
loop_body = Harvest_Crop
loop_recur = StrictPartialOrder(nodes=[Maintenance_Check, Community_Meet])  # concurrent maintenance and meet

harvest_maintenance = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, loop_recur])

# Define the main workflow partial order, connecting phases
root = StrictPartialOrder(nodes=[
    phase1,
    phase2,
    phase3,
    phase4,
    harvest_maintenance,
])

# Connect phases: phase1 --> phase2 --> phase3 --> phase4 --> harvest_maintenance
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, phase3)
root.order.add_edge(phase3, phase4)
root.order.add_edge(phase4, harvest_maintenance)