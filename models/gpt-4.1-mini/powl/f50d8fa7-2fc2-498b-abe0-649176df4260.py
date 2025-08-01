# Generated from: f50d8fa7-2fc2-498b-abe0-649176df4260.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban vertical farm within a repurposed industrial building. It integrates architectural retrofitting, advanced hydroponic system installation, energy-efficient lighting calibration, and IoT-based environmental monitoring. The process manages supply chain logistics for seeds and nutrients, secures regulatory compliance for urban agriculture, and coordinates labor training on both agricultural and technological operations. Continuous data analysis is employed to optimize crop yields while minimizing resource consumption, all within the constraints of urban zoning and community engagement initiatives. The process concludes with market launch planning and distribution network setup for fresh produce delivery.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define Activities
Site_Survey = Transition(label='Site Survey')
Design_Plan = Transition(label='Design Plan')
Permit_Acquire = Transition(label='Permit Acquire')
Structural_Retrofit = Transition(label='Structural Retrofit')
System_Install = Transition(label='System Install')
Lighting_Setup = Transition(label='Lighting Setup')
Sensor_Deploy = Transition(label='Sensor Deploy')
Seed_Sourcing = Transition(label='Seed Sourcing')
Nutrient_Prep = Transition(label='Nutrient Prep')
Staff_Training = Transition(label='Staff Training')
Data_Monitor = Transition(label='Data Monitor')
Yield_Analyze = Transition(label='Yield Analyze')
Compliance_Check = Transition(label='Compliance Check')
Community_Meet = Transition(label='Community Meet')
Market_Launch = Transition(label='Market Launch')
Logistics_Plan = Transition(label='Logistics Plan')

# High-level structure reasoning:
# Phase 1: Site Survey → Design Plan → Permit Acquire
phase1 = StrictPartialOrder(nodes=[Site_Survey, Design_Plan, Permit_Acquire])
phase1.order.add_edge(Site_Survey, Design_Plan)
phase1.order.add_edge(Design_Plan, Permit_Acquire)

# Phase 2: Structural Retrofit (after permit)
# Phase 3: Equipment installation in partial order (System Install, Lighting Setup, Sensor Deploy)
phase3 = StrictPartialOrder(nodes=[System_Install, Lighting_Setup, Sensor_Deploy])
# These 3 can be concurrent (no order edges)

phase2 = StrictPartialOrder(nodes=[Structural_Retrofit, phase3])
phase2.order.add_edge(Structural_Retrofit, phase3)

# Phase 4: Supply management handled in parallel (Seed Sourcing, Nutrient Prep)
supply = StrictPartialOrder(nodes=[Seed_Sourcing, Nutrient_Prep])
# concurrent, no order

# Phase 5: Staffing training (Staff Training)
# Phase 6: Compliance & Community (Compliance Check, Community Meet)
comp_comm = StrictPartialOrder(nodes=[Compliance_Check, Community_Meet])
# concurrent but no order edges

# Phase 7: Monitoring loop: Data Monitor then Yield Analyze repeatedly
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Data_Monitor, Yield_Analyze]
)

# Phase 8: Market launch and logistics plan (Market Launch → Logistics Plan)
market_phase = StrictPartialOrder(nodes=[Market_Launch, Logistics_Plan])
market_phase.order.add_edge(Market_Launch, Logistics_Plan)

# Build partial orders for phases 4,5,6 together, assumed to be done after phase 2.
# Staff Training is standalone but in parallel with supply and compliance & community
suppliers_staff_compliance = StrictPartialOrder(
    nodes=[supply, Staff_Training, comp_comm]
)
# no additional order edges → all concurrent

# Combine phases after permit acquire sequentially:
# permit_acquire → structural retrofit & system install → (suppliers/staff/compliance) → monitoring loop → market phase
root = StrictPartialOrder(
    nodes=[
        phase1,
        phase2,
        suppliers_staff_compliance,
        monitor_loop,
        market_phase
    ]
)
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, suppliers_staff_compliance)
root.order.add_edge(suppliers_staff_compliance, monitor_loop)
root.order.add_edge(monitor_loop, market_phase)