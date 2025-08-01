# Generated from: 70bb1489-ee11-4326-a8a9-4564dde78a7d.json
# Description: This process outlines the complex setup and operationalization of an urban vertical farming system that integrates hydroponics, IoT sensors, automated climate control, and waste recycling. The procedure includes site assessment, modular installation, nutrient balancing, real-time monitoring, pest management, and yield optimization. Each phase involves cross-disciplinary collaboration between agronomists, engineers, and data analysts to ensure sustainable production of fresh produce within constrained city spaces, minimizing resource consumption and environmental impact while maximizing output and quality.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Install_Frames = Transition(label='Install Frames')
Setup_Hydroponics = Transition(label='Setup Hydroponics')
Configure_Sensors = Transition(label='Configure Sensors')
Calibrate_Climate = Transition(label='Calibrate Climate')
Nutrient_Mix = Transition(label='Nutrient Mix')
Seed_Planting = Transition(label='Seed Planting')
Monitor_Growth = Transition(label='Monitor Growth')
Adjust_Lighting = Transition(label='Adjust Lighting')
Pest_Control = Transition(label='Pest Control')
Waste_Recycle = Transition(label='Waste Recycle')
Data_Analysis = Transition(label='Data Analysis')
Harvest_Crops = Transition(label='Harvest Crops')
Quality_Check = Transition(label='Quality Check')
Market_Dispatch = Transition(label='Market Dispatch')

# Phase 1: Site Survey -> Design Layout
phase1 = StrictPartialOrder(nodes=[Site_Survey, Design_Layout])
phase1.order.add_edge(Site_Survey, Design_Layout)

# Phase 2: Modular Installation steps in strict order
phase2_nODES = [
    Install_Frames, 
    Setup_Hydroponics, 
    Configure_Sensors, 
    Calibrate_Climate
]
phase2 = StrictPartialOrder(nodes=phase2_nODES)
for i in range(len(phase2_nODES)-1):
    phase2.order.add_edge(phase2_nODES[i], phase2_nODES[i+1])

# Phase 3: Nutrient Mixing and Seed Planting strictly ordered
phase3 = StrictPartialOrder(nodes=[Nutrient_Mix, Seed_Planting])
phase3.order.add_edge(Nutrient_Mix, Seed_Planting)

# Phase 4: Monitoring loop that supports repeated monitoring, adjustments, and pest control
# Model the loop as LOOP(Monitor_Growth, XOR(Adjust_Lighting, Pest_Control))
adjust_or_pest = OperatorPOWL(operator=Operator.XOR, children=[Adjust_Lighting, Pest_Control])
loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[Monitor_Growth, adjust_or_pest])

# Phase 5: Waste Recycle and Data Analysis done concurrently after monitoring loop ends
phase5 = StrictPartialOrder(nodes=[Waste_Recycle, Data_Analysis])
# No edges, concurrent

# Phase 6: Harvest -> Quality Check -> Market Dispatch
phase6_nODES = [Harvest_Crops, Quality_Check, Market_Dispatch]
phase6 = StrictPartialOrder(nodes=phase6_nODES)
for i in range(len(phase6_nODES)-1):
    phase6.order.add_edge(phase6_nODES[i], phase6_nODES[i+1])

# Compose overall process with partial orders specifying dependencies between phases
# site survey -> design layout -> phase2 -> phase3 -> monitoring loop -> phase5 -> phase6

all_nodes = [phase1, phase2, phase3, loop_monitor, phase5, phase6]
root = StrictPartialOrder(nodes=all_nodes)
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, phase3)
root.order.add_edge(phase3, loop_monitor)
root.order.add_edge(loop_monitor, phase5)
root.order.add_edge(phase5, phase6)