# Generated from: e771c32b-3447-4078-be78-99a9a223c7ed.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farming operation within a repurposed warehouse space. It includes site assessment, climate control design, hydroponic system installation, and integration of AI-driven monitoring tools. The process also covers sourcing specialized seeds, nutrient solution formulation, labor training for crop management, and implementation of sustainable energy solutions. Post-installation activities involve trial cultivation cycles, yield analysis, and continuous optimization of environmental parameters to maximize productivity and minimize resource consumption. Additionally, the process addresses regulatory compliance, waste recycling protocols, and community engagement initiatives to promote urban agriculture awareness.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Survey = Transition(label='Site Survey')
Climate_Plan = Transition(label='Climate Plan')
System_Design = Transition(label='System Design')
AI_Setup = Transition(label='AI Setup')
Seed_Sourcing = Transition(label='Seed Sourcing')
Nutrient_Mix = Transition(label='Nutrient Mix')
Install_Hydro = Transition(label='Install Hydro')
Energy_Audit = Transition(label='Energy Audit')
Staff_Training = Transition(label='Staff Training')
Trial_Growth = Transition(label='Trial Growth')
Yield_Measure = Transition(label='Yield Measure')
Waste_Cycle = Transition(label='Waste Cycle')
Compliance_Check = Transition(label='Compliance Check')
Market_Study = Transition(label='Market Study')
Community_Meet = Transition(label='Community Meet')
Optimize_Environment = Transition(label='Optimize Environment')

# Phase 1: Initial setup partial order
# Site Survey -> Climate Plan -> System Design -> AI Setup (sequential)
# Seed Sourcing and Nutrient Mix concurrent
# Install Hydro after System Design and Seed Sourcing+Nutrient Mix (so join first)
phase1 = StrictPartialOrder(nodes=[
    Site_Survey, Climate_Plan, System_Design, AI_Setup,
    Seed_Sourcing, Nutrient_Mix, Install_Hydro
])
phase1.order.add_edge(Site_Survey, Climate_Plan)
phase1.order.add_edge(Climate_Plan, System_Design)
phase1.order.add_edge(System_Design, AI_Setup)
phase1.order.add_edge(Seed_Sourcing, Install_Hydro)
phase1.order.add_edge(Nutrient_Mix, Install_Hydro)
phase1.order.add_edge(AI_Setup, Install_Hydro)

# Phase 2: Parallel activities after Install Hydro
# Energy Audit and Staff Training concurrent
phase2 = StrictPartialOrder(nodes=[Energy_Audit, Staff_Training])

# Phase 3: Trial Growth cycle with loop
# Trial Growth -> Yield Measure -> Optimize Environment (loop keeps Optimize Environment and Trial Growth repeating, finally exiting)
# Model loop: *(Trial Growth, Yield Measure + Optimize Environment)
# We first do Trial Growth, then loop with choice to exit or repeat Yield Measure and Optimize Environment then Trial Growth again

# Loop body: partial order Yield Measure -> Optimize Environment
body = StrictPartialOrder(nodes=[Yield_Measure, Optimize_Environment])
body.order.add_edge(Yield_Measure, Optimize_Environment)

loop = OperatorPOWL(operator=Operator.LOOP, children=[Trial_Growth, body])

# Phase 4: Community and compliance concurrent with loop
# Compliance Check and Waste Cycle (could be concurrent, but Compliance often a must before others)
# Market Study and Community Meet concurrent
# Compliance Check -> Waste Cycle
comp_waste = StrictPartialOrder(nodes=[Compliance_Check, Waste_Cycle])
comp_waste.order.add_edge(Compliance_Check, Waste_Cycle)

market_community = StrictPartialOrder(nodes=[Market_Study, Community_Meet])

# Combine compliance/waste and market/community concurrently
post_install = StrictPartialOrder(nodes=[comp_waste, market_community])
# comp_waste and market_community are concurrent (no edges between them)

# Combine phase2, loop (phase3), and post_install concurrently after phase1 + Install Hydro
# So the root partial order includes phase1, phase2, loop, post_install
root = StrictPartialOrder(nodes=[phase1, phase2, loop, post_install])

# Define dependencies:
# phase1 must finish before phase2, loop, and post_install can start
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase1, loop)
root.order.add_edge(phase1, post_install)