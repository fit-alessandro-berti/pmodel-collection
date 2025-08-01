# Generated from: f42a4591-f3b7-4982-ba5d-7876f70e399f.json
# Description: This process outlines the intricate steps involved in restoring valuable antiques to their original condition while preserving historical integrity. It begins with detailed inspection and provenance verification, followed by careful disassembly and cleaning using specialized techniques. After assessment, necessary repairs are performed using period-appropriate materials and methods. Surface treatments and finishes are applied to match the original appearance. The process concludes with reassembly, quality assurance, and archival documentation to ensure transparency and authenticity for future owners or exhibitions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transition objects
Inspect_Item = Transition(label='Inspect Item')
Verify_Provenance = Transition(label='Verify Provenance')
Document_Condition = Transition(label='Document Condition')
Disassemble_Parts = Transition(label='Disassemble Parts')
Clean_Components = Transition(label='Clean Components')
Analyze_Damage = Transition(label='Analyze Damage')
Select_Materials = Transition(label='Select Materials')
Perform_Repairs = Transition(label='Perform Repairs')
Match_Finishes = Transition(label='Match Finishes')
Apply_Treatments = Transition(label='Apply Treatments')
Reassemble_Item = Transition(label='Reassemble Item')
Quality_Check = Transition(label='Quality Check')
Photograph_Results = Transition(label='Photograph Results')
Update_Archive = Transition(label='Update Archive')
Client_Review = Transition(label='Client Review')
Finalize_Report = Transition(label='Finalize Report')

# Build partial orders to reflect the process flow respecting partial concurrency

# Step 1: Inspect Item and Verify Provenance and Document Condition are sequential
step1 = StrictPartialOrder(nodes=[Inspect_Item, Verify_Provenance, Document_Condition])
step1.order.add_edge(Inspect_Item, Verify_Provenance)
step1.order.add_edge(Verify_Provenance, Document_Condition)

# Step 2: Disassemble Parts and Clean Components sequential
step2 = StrictPartialOrder(nodes=[Disassemble_Parts, Clean_Components])
step2.order.add_edge(Disassemble_Parts, Clean_Components)

# Step 3: Analyze Damage
step3 = Analyze_Damage

# Step 4: Select Materials and Perform Repairs sequential
step4 = StrictPartialOrder(nodes=[Select_Materials, Perform_Repairs])
step4.order.add_edge(Select_Materials, Perform_Repairs)

# Step 5: Match Finishes and Apply Treatments sequential
step5 = StrictPartialOrder(nodes=[Match_Finishes, Apply_Treatments])
step5.order.add_edge(Match_Finishes, Apply_Treatments)

# Step 6: Reassemble Item, Quality Check sequential
step6 = StrictPartialOrder(nodes=[Reassemble_Item, Quality_Check])
step6.order.add_edge(Reassemble_Item, Quality_Check)

# Step 7: Photograph Results and Update Archive sequential
step7 = StrictPartialOrder(nodes=[Photograph_Results, Update_Archive])
step7.order.add_edge(Photograph_Results, Update_Archive)

# Step 8: Client Review followed by Finalize Report sequential
step8 = StrictPartialOrder(nodes=[Client_Review, Finalize_Report])
step8.order.add_edge(Client_Review, Finalize_Report)

# Now create the full process StrictPartialOrder capturing the overall flow with edges between steps.
# According to description the order is:
# Step1 -> Step2 -> Step3 -> Step4 -> Step5 -> Step6 -> Step7 -> Step8

nodes = [
    step1,
    step2,
    step3,
    step4,
    step5,
    step6,
    step7,
    step8
]
root = StrictPartialOrder(nodes=nodes)
root.order.add_edge(step1, step2)
root.order.add_edge(step2, step3)
root.order.add_edge(step3, step4)
root.order.add_edge(step4, step5)
root.order.add_edge(step5, step6)
root.order.add_edge(step6, step7)
root.order.add_edge(step7, step8)