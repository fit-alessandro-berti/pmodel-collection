# Generated from: f16c6a99-d440-49c1-ad75-d36c578e95fa.json
# Description: This process outlines the complex and multifaceted steps required to establish an urban vertical farming system within a constrained metropolitan environment. It involves site analysis, modular design adaptation, integrating IoT sensors for environmental control, selecting optimal crop varieties, installing hydroponic and aeroponic systems, setting up renewable energy sources, managing water recycling, implementing pest management protocols, establishing supply chain logistics for fresh produce delivery, securing regulatory approvals, conducting staff training on advanced agricultural technologies, and creating data analytics dashboards for ongoing yield optimization. This atypical business process combines elements of agriculture, technology, sustainability, and urban planning to create a scalable and efficient food production model tailored for city environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Sensor_Deploy = Transition(label='Sensor Deploy')
Crop_Select = Transition(label='Crop Select')
System_Install = Transition(label='System Install')
Energy_Setup = Transition(label='Energy Setup')
Water_Cycle = Transition(label='Water Cycle')
Pest_Control = Transition(label='Pest Control')
Regulatory_Check = Transition(label='Regulatory Check')
Staff_Training = Transition(label='Staff Training')
Data_Configure = Transition(label='Data Configure')
Supply_Plan = Transition(label='Supply Plan')
Harvest_Schedule = Transition(label='Harvest Schedule')
Quality_Audit = Transition(label='Quality Audit')
Market_Launch = Transition(label='Market Launch')
Feedback_Loop = Transition(label='Feedback Loop')

# Construct the workflow as partial orders and operators

# Phase 1: Site survey and design
phase1 = StrictPartialOrder(
    nodes=[Site_Survey, Design_Layout],
)
phase1.order.add_edge(Site_Survey, Design_Layout)

# Phase 2: Sensor deployment and crop selection can be concurrent after design
phase2 = StrictPartialOrder(
    nodes=[Sensor_Deploy, Crop_Select],
    # no order edges: concurrent
)

# Phase 3: System Install, Energy Setup, Water Cycle, Pest Control can run in parallel after phase 2
phase3 = StrictPartialOrder(
    nodes=[System_Install, Energy_Setup, Water_Cycle, Pest_Control],
)
# no order edges: concurrent

# Phase 4: Regulatory Check and Staff Training after phase 3 (in parallel)
phase4 = StrictPartialOrder(
    nodes=[Regulatory_Check, Staff_Training],
)
# no order edges

# Phase 5: Data Configure and Supply Plan after phase 4 (concurrent)
phase5 = StrictPartialOrder(
    nodes=[Data_Configure, Supply_Plan],
)

# Phase 6: Harvest Schedule and Quality Audit after phase 5 (concurrent)
phase6 = StrictPartialOrder(
    nodes=[Harvest_Schedule, Quality_Audit],
)

# Phase 7: Market Launch after harvest and audit
phase7 = StrictPartialOrder(
    nodes=[Market_Launch],
)

# Feedback loop: After Market Launch, option to go through Feedback_Loop then Data Configure again (repeat)
# Represented as a loop:
# Loop body (A): Market Launch (M)
# Loop redo (B): Feedback Loop (F) then Data Configure (D)

# To model loop: LOOP(A, B)
# A = Market_Launch
# B = StrictPartialOrder(nodes=[Feedback_Loop, Data_Configure], order={Feedback_Loop-->Data_Configure})

loop_redo = StrictPartialOrder(
    nodes=[Feedback_Loop, Data_Configure]
)
loop_redo.order.add_edge(Feedback_Loop, Data_Configure)

loop = OperatorPOWL(operator=Operator.LOOP, children=[Market_Launch, loop_redo])

# Compose all phases in partial order according to dependencies:

root = StrictPartialOrder(
    nodes=[
        phase1,       # Site Survey -> Design Layout
        phase2,       # Sensor Deploy || Crop Select
        phase3,       # System Install || Energy Setup || Water Cycle || Pest Control
        phase4,       # Regulatory Check || Staff Training
        phase5,       # Data Configure || Supply Plan
        phase6,       # Harvest Schedule || Quality Audit
        loop          # Market Launch with Feedback Loop
    ]
)

# Add ordering edges connecting the phases:

# phase1 --> phase2
root.order.add_edge(phase1, phase2)
# phase2 --> phase3
root.order.add_edge(phase2, phase3)
# phase3 --> phase4
root.order.add_edge(phase3, phase4)
# phase4 --> phase5
root.order.add_edge(phase4, phase5)
# phase5 --> phase6
root.order.add_edge(phase5, phase6)
# phase6 --> loop (Market Launch + feedback)
root.order.add_edge(phase6, loop)