# Generated from: 8770e290-bec0-4e0b-bc0a-8eaa5b352d04.json
# Description: This process outlines the establishment of a sustainable urban vertical farm in a multi-story building. It begins with site analysis and structural assessment, followed by environmental impact evaluation. Next, the process involves modular farming unit design, nutrient solution formulation, and automated climate control setup. Concurrently, seed selection and germination protocols are developed. The installation phase includes lighting system integration, hydroponic channel assembly, and sensor network deployment for real-time monitoring. Once operational, the process continues with data-driven growth optimization, pest management using biocontrol agents, and harvest scheduling. Finally, produce packaging and distribution logistics are coordinated with local markets to ensure freshness and minimal environmental footprint, closing the loop with waste recycling and energy efficiency audits.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Site_Analysis = Transition(label='Site Analysis')
Structural_Check = Transition(label='Structural Check')
Impact_Study = Transition(label='Impact Study')
Unit_Design = Transition(label='Unit Design')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Setup = Transition(label='Climate Setup')
Seed_Selection = Transition(label='Seed Selection')
Germination_Prep = Transition(label='Germination Prep')
Lighting_Install = Transition(label='Lighting Install')
Channel_Assembly = Transition(label='Channel Assembly')
Sensor_Deploy = Transition(label='Sensor Deploy')
Growth_Optimize = Transition(label='Growth Optimize')
Pest_Control = Transition(label='Pest Control')
Harvest_Plan = Transition(label='Harvest Plan')
Packaging = Transition(label='Packaging')
Distribution = Transition(label='Distribution')
Waste_Audit = Transition(label='Waste Audit')
Energy_Review = Transition(label='Energy Review')

# Phase 1: Site analysis and structural assessment
phase1 = StrictPartialOrder(nodes=[Site_Analysis, Structural_Check])
phase1.order.add_edge(Site_Analysis, Structural_Check)

# Phase 2: Environmental impact evaluation
phase2 = Impact_Study

# Phase 3: Modular farming unit design, nutrient solution formulation, and automated climate control setup
phase3 = StrictPartialOrder(nodes=[Unit_Design, Nutrient_Mix, Climate_Setup])
phase3.order.add_edge(Unit_Design, Nutrient_Mix)
phase3.order.add_edge(Nutrient_Mix, Climate_Setup)

# Phase 4: Concurrently seed selection and germination protocols
phase4 = StrictPartialOrder(nodes=[Seed_Selection, Germination_Prep])
# No edges because they are concurrent

# Phase 5: Installation phase includes lighting system integration, hydroponic channel assembly, sensor network deployment
phase5 = StrictPartialOrder(nodes=[Lighting_Install, Channel_Assembly, Sensor_Deploy])
phase5.order.add_edge(Lighting_Install, Channel_Assembly)
phase5.order.add_edge(Channel_Assembly, Sensor_Deploy)

# Phase 6: Once operational, data-driven growth optimization, pest management using biocontrol agents, and harvest scheduling
phase6 = StrictPartialOrder(nodes=[Growth_Optimize, Pest_Control, Harvest_Plan])
phase6.order.add_edge(Growth_Optimize, Pest_Control)
phase6.order.add_edge(Pest_Control, Harvest_Plan)

# Phase 7: Produce packaging and distribution logistics coordinated with local markets
phase7 = StrictPartialOrder(nodes=[Packaging, Distribution])
phase7.order.add_edge(Packaging, Distribution)

# Phase 8: Closing the loop with waste recycling and energy efficiency audits
phase8 = StrictPartialOrder(nodes=[Waste_Audit, Energy_Review])
phase8.order.add_edge(Waste_Audit, Energy_Review)

# Combine phase4 (Seed_Selection & Germination_Prep) concurrent to phase3 (Unit Design to Climate Setup)
phase3_4 = StrictPartialOrder(nodes=[phase3, phase4])
phase3_4.order.add_edge(phase3, phase4)

# Combine phase5 (installation) starts after phases 3&4
phase34_5 = StrictPartialOrder(nodes=[phase3_4, phase5])
phase34_5.order.add_edge(phase3_4, phase5)

# Combine phases 1, 2, then 3&4, then 5, then 6, then 7, then 8
root = StrictPartialOrder(
    nodes=[phase1, phase2, phase34_5, phase6, phase7, phase8]
)

root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, phase34_5)
root.order.add_edge(phase34_5, phase6)
root.order.add_edge(phase6, phase7)
root.order.add_edge(phase7, phase8)