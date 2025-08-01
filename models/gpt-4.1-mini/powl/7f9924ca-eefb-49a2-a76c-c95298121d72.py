# Generated from: 7f9924ca-eefb-49a2-a76c-c95298121d72.json
# Description: This process involves establishing an urban vertical farming system within a repurposed industrial building. It begins with site analysis and environmental assessment, followed by modular structure design and installation of hydroponic systems. Nutrient solution formulation and automated climate control calibration ensure optimal plant growth. Seed selection is tailored to urban demand and lighting conditions, while integrated pest management practices are implemented to maintain crop health. Data collection and remote monitoring systems enable real-time adjustments. Harvest scheduling and packaging logistics align with local distribution channels. Finally, waste recycling protocols and energy consumption audits ensure sustainability and operational efficiency throughout the farming lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Site_Analysis = Transition(label='Site Analysis')
Env_Assessment = Transition(label='Env Assessment')
Structure_Design = Transition(label='Structure Design')
Module_Install = Transition(label='Module Install')
Hydroponic_Setup = Transition(label='Hydroponic Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Calibrate = Transition(label='Climate Calibrate')
Seed_Selection = Transition(label='Seed Selection')
Pest_Control = Transition(label='Pest Control')
Data_Capture = Transition(label='Data Capture')
Remote_Monitor = Transition(label='Remote Monitor')
Harvest_Plan = Transition(label='Harvest Plan')
Packaging_Prep = Transition(label='Packaging Prep')
Distribution_Map = Transition(label='Distribution Map')
Waste_Recycle = Transition(label='Waste Recycle')
Energy_Audit = Transition(label='Energy Audit')

# Partial orders reflecting sequence and concurrency:

# Phase 1: Site analysis and environmental assessment in sequence
phase1 = StrictPartialOrder(nodes=[Site_Analysis, Env_Assessment])
phase1.order.add_edge(Site_Analysis, Env_Assessment)

# Phase 2: Structure design followed by concurrent installation and setup
# Structure Design --> Module Install and Hydroponic Setup execute concurrently
phase2 = StrictPartialOrder(
    nodes=[Structure_Design, Module_Install, Hydroponic_Setup]
)
phase2.order.add_edge(Structure_Design, Module_Install)
phase2.order.add_edge(Structure_Design, Hydroponic_Setup)

# Phase 3: Nutrient mix and climate calibration in sequence
phase3 = StrictPartialOrder(nodes=[Nutrient_Mix, Climate_Calibrate])
phase3.order.add_edge(Nutrient_Mix, Climate_Calibrate)

# Phase 4: Seed Selection and Pest Control are concurrent
phase4 = StrictPartialOrder(nodes=[Seed_Selection, Pest_Control])

# Phase 5: Data Capture and Remote Monitor in sequence
phase5 = StrictPartialOrder(nodes=[Data_Capture, Remote_Monitor])
phase5.order.add_edge(Data_Capture, Remote_Monitor)

# Phase 6: Harvest Plan followed by Packaging Prep and Distribution Map concurrent
phase6 = StrictPartialOrder(
    nodes=[Harvest_Plan, Packaging_Prep, Distribution_Map]
)
phase6.order.add_edge(Harvest_Plan, Packaging_Prep)
phase6.order.add_edge(Harvest_Plan, Distribution_Map)

# Phase 7: Waste Recycle and Energy Audit concurrent
phase7 = StrictPartialOrder(nodes=[Waste_Recycle, Energy_Audit])

# Compose all phases in sequence respecting overall order
# Phase1 --> Phase2 --> Phase3 --> Phase4 --> Phase5 --> Phase6 --> Phase7

# To do this, create a top-level StrictPartialOrder containing all phases as nodes

# Since phases are POWL models themselves, we can compose higher-level PO with edges
root = StrictPartialOrder(
    nodes=[phase1, phase2, phase3, phase4, phase5, phase6, phase7]
)
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, phase3)
root.order.add_edge(phase3, phase4)
root.order.add_edge(phase4, phase5)
root.order.add_edge(phase5, phase6)
root.order.add_edge(phase6, phase7)