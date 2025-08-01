# Generated from: 7d728a9f-3ed8-456e-a8ad-094306a54950.json
# Description: This process outlines the complex setup of an urban vertical farm integrating hydroponic systems, renewable energy sources, and IoT-based environmental controls. It involves selecting optimal building spaces, designing multi-layer crop layouts, installing climate and nutrient monitoring sensors, automating irrigation schedules, and integrating blockchain for supply chain transparency. The process ensures sustainable food production in dense city environments by balancing energy efficiency, crop yield optimization, and waste reduction through smart analytics and adaptive resource management strategies.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Survey = Transition(label='Site Survey')
Space_Design = Transition(label='Space Design')
Structural_Check = Transition(label='Structural Check')
System_Layout = Transition(label='System Layout')
Sensor_Install = Transition(label='Sensor Install')
Irrigation_Setup = Transition(label='Irrigation Setup')
Lighting_Config = Transition(label='Lighting Config')
Climate_Control = Transition(label='Climate Control')
Nutrient_Mix = Transition(label='Nutrient Mix')
Energy_Connect = Transition(label='Energy Connect')
Data_Sync = Transition(label='Data Sync')
Automation_Test = Transition(label='Automation Test')
Crop_Seeding = Transition(label='Crop Seeding')
Growth_Monitor = Transition(label='Growth Monitor')
Harvest_Plan = Transition(label='Harvest Plan')
Waste_Handle = Transition(label='Waste Handle')
Supply_Audit = Transition(label='Supply Audit')

# Design partial orders following the process description

# Phase 1: selecting optimal building spaces and designing layout and checking structure
phase1 = StrictPartialOrder(nodes=[
    Site_Survey,
    Space_Design,
    Structural_Check,
])
phase1.order.add_edge(Site_Survey, Space_Design)
phase1.order.add_edge(Site_Survey, Structural_Check)

# Phase 2: System layout and sensor install (concurrent with irrigation setup, lighting, climate control, nutrient mix)
phase2a = StrictPartialOrder(nodes=[System_Layout, Sensor_Install])
phase2a.order.add_edge(System_Layout, Sensor_Install)

# Phase 2b: irrigation, lighting, climate control, nutrient mix can be concurrent after system layout
phase2b = StrictPartialOrder(nodes=[Irrigation_Setup, Lighting_Config, Climate_Control, Nutrient_Mix])

# Phase 2 combined: system layout -> sensor install, concurrently with irrigation, lighting, climate, nutrient
phase2 = StrictPartialOrder(nodes=[phase2a, phase2b])
phase2.order.add_edge(phase2a, phase2b)  # system+sensor before irrigation, lighting, etc.

# Phase 3: energy connect and data sync (must come after system and sensor setup)
phase3 = StrictPartialOrder(nodes=[Energy_Connect, Data_Sync])
phase3.order.add_edge(Energy_Connect, Data_Sync)

# Phase 4: automation test comes after data sync
phase4 = Automation_Test

# Phase 5: crop seeding and growth monitor in partial order, growth monitor before harvest plan
phase5 = StrictPartialOrder(nodes=[Crop_Seeding, Growth_Monitor, Harvest_Plan])
phase5.order.add_edge(Crop_Seeding, Growth_Monitor)
phase5.order.add_edge(Growth_Monitor, Harvest_Plan)

# Phase 6: waste handling and supply audit (post harvest), can be concurrent
phase6 = StrictPartialOrder(nodes=[Waste_Handle, Supply_Audit])

# Compose main flow as partial order:

# Phase1 -> Phase2 -> Phase3 -> Phase4 -> Phase5 -> Phase6
root = StrictPartialOrder(nodes=[phase1, phase2, phase3, phase4, phase5, phase6])

root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, phase3)
root.order.add_edge(phase3, phase4)
root.order.add_edge(phase4, phase5)
root.order.add_edge(phase5, phase6)