# Generated from: b5c88fff-9675-49cc-b823-f96e3fd3f473.json
# Description: This process outlines the complex and multifaceted steps required to launch an urban vertical farming operation within a dense metropolitan area. It involves site selection, environmental impact analysis, technology integration for hydroponics and aeroponics systems, regulatory compliance checks, community stakeholder engagement, and supply chain coordination. The process also includes pilot crop cycles, real-time data monitoring setup, energy optimization, waste recycling protocols, and marketing strategies tailored to urban consumers. Each activity ensures sustainability, efficiency, and scalability while addressing unique urban constraints and opportunities to create a resilient local food production system.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Create transitions for all activities
Site_Survey = Transition(label='Site Survey')
Impact_Study = Transition(label='Impact Study')
Tech_Setup = Transition(label='Tech Setup')
System_Design = Transition(label='System Design')
Regulation_Check = Transition(label='Regulation Check')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Pilot_Planting = Transition(label='Pilot Planting')
Data_Monitor = Transition(label='Data Monitor')
Energy_Audit = Transition(label='Energy Audit')
Waste_Plan = Transition(label='Waste Plan')
Supply_Align = Transition(label='Supply Align')
Crop_Cycle = Transition(label='Crop Cycle')
Market_Launch = Transition(label='Market Launch')
Feedback_Loop = Transition(label='Feedback Loop')
Scale_Strategy = Transition(label='Scale Strategy')

# Model the core order of activities respecting described dependencies and concurrency possibilities:

# Phase 1: Site Survey -> Impact Study
phase1 = StrictPartialOrder(nodes=[Site_Survey, Impact_Study])
phase1.order.add_edge(Site_Survey, Impact_Study)

# Phase 2: Tech Setup and System Design in partial order, Tech Setup then System Design
phase2 = StrictPartialOrder(nodes=[Tech_Setup, System_Design])
phase2.order.add_edge(Tech_Setup, System_Design)

# Phase 3: Regulation Check and Stakeholder Meet can be concurrent after System Design
phase3 = StrictPartialOrder(nodes=[Regulation_Check, Stakeholder_Meet])

# Phase 4: Pilot Planting (after Regulation Check and Stakeholder Meet)
phase4 = Pilot_Planting

# Phase 5: Setup monitoring and audit tasks concurrently
monitor_and_audit = StrictPartialOrder(nodes=[Data_Monitor, Energy_Audit, Waste_Plan])
# no order edges means fully concurrent

# Phase 6: Supply Align after Pilot Planting (can be concurrent or after monitoring)
# Let's assume Supply Align concurrent with monitor_and_audit, but after Pilot Planting
phase5 = StrictPartialOrder(nodes=[Pilot_Planting, Supply_Align])
phase5.order.add_edge(Pilot_Planting, Supply_Align)

# Combine Phase 5 and monitoring/audit with concurrency
phase5_and_monitor = StrictPartialOrder(
    nodes=[phase5, monitor_and_audit]
)
phase5_and_monitor.order.add_edge(phase5, monitor_and_audit)

# Phase 7: Crop Cycle after Supply Align and monitoring/audit
phase6 = Crop_Cycle

# Phase 8: Loop of Feedback Loop and Crop Cycle (repeat improvements)
loop_feedback = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Crop_Cycle, Feedback_Loop]
)

# Phase 9: Market Launch and Scale Strategy after Feedback Loop (concurrent)
phase7 = StrictPartialOrder(nodes=[Market_Launch, Scale_Strategy])

# Assemble all phases with dependencies in a single partial order
root = StrictPartialOrder(
    nodes=[phase1, phase2, phase3, phase5_and_monitor, phase6, loop_feedback, phase7]
)

# Add edges to respect dependencies:
# phase1 (Site Survey->Impact Study) -> phase2 (Tech Setup->System Design)
root.order.add_edge(phase1, phase2)

# phase2 -> phase3 (Reg Check, Stakeholder Meet)
root.order.add_edge(phase2, phase3)

# phase3 -> phase5_and_monitor (Pilot Planting + Supply Align concurrent with monitoring)
root.order.add_edge(phase3, phase5_and_monitor)

# phase5_and_monitor -> phase6 (Crop Cycle)
root.order.add_edge(phase5_and_monitor, phase6)

# phase6 -> loop_feedback (Feedback Loop)
root.order.add_edge(phase6, loop_feedback)

# loop_feedback -> phase7 (Market Launch, Scale Strategy)
root.order.add_edge(loop_feedback, phase7)