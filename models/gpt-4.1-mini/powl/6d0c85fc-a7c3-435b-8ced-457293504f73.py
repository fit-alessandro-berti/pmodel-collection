# Generated from: 6d0c85fc-a7c3-435b-8ced-457293504f73.json
# Description: This process involves the meticulous restoration of antique items, blending historical research, material analysis, and precision craftsmanship. It begins with initial assessment and provenance verification, followed by detailed condition reporting and risk evaluation. Restoration planning includes sourcing period-appropriate materials and consulting specialists. The workflow proceeds with careful disassembly, cleaning, repair, and replacement of damaged elements using traditional techniques. Quality control is continuous, ensuring authenticity and structural integrity. Finally, documentation and preservation recommendations complete the process, supporting future maintenance and historical value retention.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Initial_Assess = Transition(label='Initial Assess')
Provenance_Check = Transition(label='Provenance Check')
Condition_Report = Transition(label='Condition Report')
Risk_Evaluate = Transition(label='Risk Evaluate')
Material_Source = Transition(label='Material Source')
Expert_Consult = Transition(label='Expert Consult')
Restoration_Plan = Transition(label='Restoration Plan')
Item_Disassemble = Transition(label='Item Disassemble')
Surface_Clean = Transition(label='Surface Clean')
Structural_Repair = Transition(label='Structural Repair')
Element_Replace = Transition(label='Element Replace')
Traditional_Finish = Transition(label='Traditional Finish')
Quality_Control = Transition(label='Quality Control')
Documentation = Transition(label='Documentation')
Preservation_Advise = Transition(label='Preservation Advise')
Final_Review = Transition(label='Final Review')

# Step 1: Initial assessment and provenance verification (concurrent)
step1 = StrictPartialOrder(nodes=[Initial_Assess, Provenance_Check])
# No order edges => concurrent

# Step 2: Condition report and risk evaluation (sequential)
step2 = StrictPartialOrder(nodes=[Condition_Report, Risk_Evaluate])
step2.order.add_edge(Condition_Report, Risk_Evaluate)

# Step 3: Restoration planning includes material source and expert consult (concurrent), followed by restoration plan
planning_concurrent = StrictPartialOrder(nodes=[Material_Source, Expert_Consult])
# No edges, concurrent
planning = StrictPartialOrder(nodes=[planning_concurrent, Restoration_Plan])
planning.order.add_edge(planning_concurrent, Restoration_Plan)

# Step 4: Disassembly, cleaning, repair, replacement, traditional finish in sequence
step4 = StrictPartialOrder(nodes=[Item_Disassemble, Surface_Clean, Structural_Repair, Element_Replace, Traditional_Finish])
step4.order.add_edge(Item_Disassemble, Surface_Clean)
step4.order.add_edge(Surface_Clean, Structural_Repair)
step4.order.add_edge(Structural_Repair, Element_Replace)
step4.order.add_edge(Element_Replace, Traditional_Finish)

# Step 5: Quality control continuous: model as loop with silent exit
# Quality control runs after some restoration steps and potentially loops with finishing steps again
# Model a loop where body A = Quality_Control, body B = Traditional_Finish (repeating Traditional_Finish + Quality_Control)
# But Traditional_Finish already in step4, so we include QC after step4 as loop around finishing

# Since quality control is continuous and ensures authenticity,
# we will model the loop around Traditional_Finish and Quality_Control, repeating Traditional_Finish then Quality_Control until exit.

# loop children: A=Traditional_Finish, B=Quality_Control
loop = OperatorPOWL(operator=Operator.LOOP, children=[Traditional_Finish, Quality_Control])

# Replace Traditional_Finish in step4 with the loop node (because finish + QC loop)
# So step4 without Traditional_Finish is first 4 steps only
step4a = StrictPartialOrder(nodes=[Item_Disassemble, Surface_Clean, Structural_Repair, Element_Replace])
step4a.order.add_edge(Item_Disassemble, Surface_Clean)
step4a.order.add_edge(Surface_Clean, Structural_Repair)
step4a.order.add_edge(Structural_Repair, Element_Replace)

# Now link step4a to loop (Traditional_Finish + QC loop)
step4_final = StrictPartialOrder(nodes=[step4a, loop])
step4_final.order.add_edge(step4a, loop)

# Step 6: Documentation and Preservation Advice concurrent, followed by Final Review
doc_pres = StrictPartialOrder(nodes=[Documentation, Preservation_Advise])
# concurrent no edges
final_steps = StrictPartialOrder(nodes=[doc_pres, Final_Review])
final_steps.order.add_edge(doc_pres, Final_Review)

# Combine all steps in sequence:
# step1 -> step2 -> planning -> step4_final -> final_steps
root = StrictPartialOrder(nodes=[step1, step2, planning, step4_final, final_steps])
root.order.add_edge(step1, step2)
root.order.add_edge(step2, planning)
root.order.add_edge(planning, step4_final)
root.order.add_edge(step4_final, final_steps)