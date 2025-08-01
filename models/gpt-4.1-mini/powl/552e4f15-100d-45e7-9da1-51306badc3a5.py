# Generated from: 552e4f15-100d-45e7-9da1-51306badc3a5.json
# Description: This process outlines the comprehensive steps involved in authenticating rare historical artifacts for a museum acquisition. It begins with preliminary research and provenance verification, followed by scientific testing and expert consultations. The workflow includes digital documentation, condition assessment, fraud detection using advanced imaging, and legal clearance. Each stage involves collaborative decision-making between historians, scientists, and legal advisors to ensure the artifact's authenticity and legal compliance before final acquisition and exhibition planning. The process concludes with secure storage and periodic re-evaluation to maintain integrity over time.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all the activities as transitions
Initial_Research = Transition(label='Initial Research')
Provenance_Check = Transition(label='Provenance Check')
Material_Testing = Transition(label='Material Testing')
Expert_Review = Transition(label='Expert Review')
Imaging_Scan = Transition(label='Imaging Scan')
Fraud_Analysis = Transition(label='Fraud Analysis')
Condition_Report = Transition(label='Condition Report')
Legal_Review = Transition(label='Legal Review')
Digital_Catalog = Transition(label='Digital Catalog')
Stakeholder_Meeting = Transition(label='Stakeholder Meeting')
Acquisition_Approval = Transition(label='Acquisition Approval')
Secure_Storage = Transition(label='Secure Storage')
Exhibit_Planning = Transition(label='Exhibit Planning')
Reevaluation = Transition(label='Reevaluation')
Documentation_Update = Transition(label='Documentation Update')

# Step 1: Initial Research --> Provenance Check (sequential)
step1 = StrictPartialOrder(nodes=[Initial_Research, Provenance_Check])
step1.order.add_edge(Initial_Research, Provenance_Check)

# Step 2: Scientific Testing and Expert Consultations concurrently after provenance check
# Material Testing --> Expert Review sequential
sci_expert = StrictPartialOrder(nodes=[Material_Testing, Expert_Review])
sci_expert.order.add_edge(Material_Testing, Expert_Review)

# Step 3: After step1, proceed concurrently to sci_expert and Stakeholder Meeting
# Note: Stakeholder Meeting used later, place for parallelism here

step2 = StrictPartialOrder(nodes=[step1, sci_expert, Stakeholder_Meeting])
step2.order.add_edge(step1, sci_expert)
step2.order.add_edge(step1, Stakeholder_Meeting)

# Step 4: Fraud detection using Imaging Scan and Fraud Analysis sequential
fraud_seq = StrictPartialOrder(nodes=[Imaging_Scan, Fraud_Analysis])
fraud_seq.order.add_edge(Imaging_Scan, Fraud_Analysis)

# Step 5: Condition assessment and legal clearance happen concurrently after step2 and fraud detection
cond_legal = StrictPartialOrder(nodes=[Condition_Report, Legal_Review])
# no order edges => concurrent

# Combine step2, fraud detection, and cond_legal after step2 and fraud detection
# So fraud detection depends on step2 done before? From description it's after expert consultations etc.

step3 = StrictPartialOrder(nodes=[step2, fraud_seq])
step3.order.add_edge(step2, fraud_seq)

# Then cond_legal after step3 in parallel
step4 = StrictPartialOrder(nodes=[step3, cond_legal])
step4.order.add_edge(step3, cond_legal)

# Step 6: Digital Documentation and Stakeholder Meeting concurrently with cond_legal?
# Stakeholder Meeting included at step2, assume second stakeholder meeting is part of digital catalog
# But Stakeholder Meeting is given only once, assume the same node used before.
# Let's include Digital Catalog and Stakeholder Meeting concurrently after cond_legal

doc_and_meeting = StrictPartialOrder(nodes=[Digital_Catalog, Stakeholder_Meeting])
# concurrent, no order edges

step5 = StrictPartialOrder(nodes=[step4, doc_and_meeting])
step5.order.add_edge(step4, doc_and_meeting)

# Step 7: Acquisition Approval after documentation and stakeholder meeting
step6 = StrictPartialOrder(nodes=[step5, Acquisition_Approval])
step6.order.add_edge(step5, Acquisition_Approval)

# Step 8: Exhibit Planning after Acquisition Approval
step7 = StrictPartialOrder(nodes=[step6, Exhibit_Planning])
step7.order.add_edge(step6, Exhibit_Planning)

# Step 9: Secure Storage and Reevaluation & Documentation Update loop after Exhibit Planning
# Reevaluation and Documentation Update likely looped together

# loop content: Reevaluation and Documentation Update sequentially, loop body = [Documentation Update, Reevaluation]
reeval_update = StrictPartialOrder(nodes=[Reevaluation, Documentation_Update])
reeval_update.order.add_edge(Reevaluation, Documentation_Update)

loop_node = OperatorPOWL(operator=Operator.LOOP,
                         children=[Reevaluation, Documentation_Update])

# Since loop contains Reevaluation then Documentation Update
# Let's follow the definition correctly: * (A, B) means A then choose exit or B then A again
# We'll model Reevaluation as A and Documentation Update as B

loop_node = OperatorPOWL(operator=Operator.LOOP,
                         children=[Reevaluation, Documentation_Update])

step8 = StrictPartialOrder(nodes=[step7, Secure_Storage, loop_node])
step8.order.add_edge(step7, Secure_Storage)
step8.order.add_edge(step7, loop_node)

# root is the whole StrictPartialOrder
root = step8