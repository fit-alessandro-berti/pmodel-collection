# Generated from: 2e4fb759-1206-4286-8d9c-5f3dce1864c9.json
# Description: This process describes the iterative cycle of cross-industry innovation where insights from disparate sectors are systematically gathered, synthesized, and applied to develop breakthrough products or services. It begins with environmental scanning and trend spotting across unrelated markets, followed by ideation sessions leveraging diverse expert panels. Concepts are rapidly prototyped using agile methodologies and tested through pilot programs in controlled environments. Feedback loops incorporate user data and expert reviews to refine solutions before scaling. The process also includes strategic partnerships formation, IP management, and continuous knowledge dissemination to ensure competitive advantage and sustainable innovation across industries.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Trend_Scan = Transition(label='Trend Scan')
Market_Mapping = Transition(label='Market Mapping')
Expert_Panel = Transition(label='Expert Panel')
Idea_Generation = Transition(label='Idea Generation')
Concept_Sketch = Transition(label='Concept Sketch')
Rapid_Prototype = Transition(label='Rapid Prototype')
Pilot_Launch = Transition(label='Pilot Launch')
User_Feedback = Transition(label='User Feedback')
Data_Analysis = Transition(label='Data Analysis')
Solution_Refinement = Transition(label='Solution Refinement')
Partnership_Setup = Transition(label='Partnership Setup')
IP_Review = Transition(label='IP Review')
Knowledge_Share = Transition(label='Knowledge Share')
Scale_Planning = Transition(label='Scale Planning')
Impact_Audit = Transition(label='Impact Audit')
Continuous_Loop = Transition(label='Continuous Loop')

# Loop body: after executing the cycle, choose to exit or repeat
# The iterative cycle involves:
# 1. Environmental scanning & trend spotting: Trend Scan, Market Mapping (parallel)
# 2. Ideation sessions & expert panels: Expert Panel -> Idea Generation (strict order)
# 3. Prototyping & pilot testing: Concept Sketch -> Rapid Prototype -> Pilot Launch (strict order)
# 4. Feedback loops: User Feedback -> Data Analysis -> Solution Refinement (strict order)
# 5. Strategic partnerships, IP management, knowledge dissemination, scaling, auditing (parallel):
# Partnership Setup, IP Review, Knowledge Share, Scale Planning, Impact Audit

# Step 1: Parallel of Trend Scan and Market Mapping
step1 = StrictPartialOrder(nodes=[Trend_Scan, Market_Mapping])

# Step 2: Expert Panel -> Idea Generation
step2 = StrictPartialOrder(nodes=[Expert_Panel, Idea_Generation])
step2.order.add_edge(Expert_Panel, Idea_Generation)

# Step 3: Concept Sketch -> Rapid Prototype -> Pilot Launch
step3 = StrictPartialOrder(nodes=[Concept_Sketch, Rapid_Prototype, Pilot_Launch])
step3.order.add_edge(Concept_Sketch, Rapid_Prototype)
step3.order.add_edge(Rapid_Prototype, Pilot_Launch)

# Step 4: User Feedback -> Data Analysis -> Solution Refinement
step4 = StrictPartialOrder(nodes=[User_Feedback, Data_Analysis, Solution_Refinement])
step4.order.add_edge(User_Feedback, Data_Analysis)
step4.order.add_edge(Data_Analysis, Solution_Refinement)

# Step 5: Parallel strategic steps
step5 = StrictPartialOrder(nodes=[Partnership_Setup, IP_Review, Knowledge_Share, Scale_Planning, Impact_Audit])

# Assemble the cycle partial order:
# Join steps in order, connecting step1 -> step2 -> step3 -> step4 -> step5
cycle_nodes = [step1, step2, step3, step4, step5]

cycle = StrictPartialOrder(nodes=cycle_nodes)
cycle.order.add_edge(step1, step2)
cycle.order.add_edge(step2, step3)
cycle.order.add_edge(step3, step4)
cycle.order.add_edge(step4, step5)

# Loop: execute cycle, then either exit or do Continuous Loop and then cycle again
root = OperatorPOWL(operator=Operator.LOOP, children=[cycle, Continuous_Loop])