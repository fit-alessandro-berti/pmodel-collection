# Generated from: d7350d4e-575a-4305-9dc0-aee716b70261.json
# Description: This process involves the comprehensive authentication of rare historical artifacts before acquisition by a museum. It begins with preliminary provenance research, followed by multi-modal scientific analysis including spectroscopy and radiocarbon dating. Expert consultations assess cultural significance and authenticity. Legal clearances ensure compliance with international heritage laws. Digitization of findings supports archival and future reference. The artifact then undergoes conservation planning with specialized restorers. Finally, a detailed report is compiled, and acquisition approval is secured through stakeholder review. This atypical process integrates scientific, legal, and cultural evaluations to ensure the artifact's legitimacy and preservation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Provenance_Check = Transition(label='Provenance Check')

Sample_Collection = Transition(label='Sample Collection')
Spectroscopy_Test = Transition(label='Spectroscopy Test')
Carbon_Dating = Transition(label='Carbon Dating')

Expert_Review = Transition(label='Expert Review')

Legal_Clearance = Transition(label='Legal Clearance')

Cultural_Assessment = Transition(label='Cultural Assessment')

Digital_Scan = Transition(label='Digital Scan')

Restoration_Plan = Transition(label='Restoration Plan')
Condition_Report = Transition(label='Condition Report')
Archival_Entry = Transition(label='Archival Entry')

Report_Draft = Transition(label='Report Draft')

Stakeholder_Meet = Transition(label='Stakeholder Meet')
Acquisition_Vote = Transition(label='Acquisition Vote')
Final_Approval = Transition(label='Final Approval')

# Scientific analysis partial order: Sample Collection --> {Spectroscopy Test, Carbon Dating} concurrently --> Expert Review
scientific_tests = StrictPartialOrder(nodes=[Spectroscopy_Test, Carbon_Dating])
# no order edges: tests concurrent

scientific_analysis = StrictPartialOrder(
    nodes=[Sample_Collection, scientific_tests, Expert_Review]
)
scientific_analysis.order.add_edge(Sample_Collection, scientific_tests)
scientific_analysis.order.add_edge(scientific_tests, Expert_Review)

# Note: scientific_tests is a POWL node (Partial Order), so add edges from its implicit start to its nodes?
# In POWL modeling the partial order inside is a node itself 
# So we link Sample_Collection --> scientific_tests (the PO node)
# And scientific_tests --> Expert_Review
# parallelism inside scientific_tests

# Cultural and legal assessments concurrent after expert review
cultural_legal = StrictPartialOrder(
    nodes=[Legal_Clearance, Cultural_Assessment]
)
# concurrent: no order edges

assessment = StrictPartialOrder(
    nodes=[cultural_legal, Expert_Review]
)
assessment.order.add_edge(Expert_Review, cultural_legal)

# Digitization after cultural and legal assessments
digit_archival = StrictPartialOrder(
    nodes=[Digital_Scan, Restoration_Plan]
)
# Restorers (= Restoration_Plan + subtasks) not fully detailed beyond Restoration_Plan
# Condition Report and Archival Entry seem related to conservation and digitization

# Condition Report & Archival Entry after Restoration Plan and Digital Scan, respectively
post_restoration = StrictPartialOrder(
    nodes=[Condition_Report, Archival_Entry]
)
# They can happen concurrently (no edge)

# Link digitization to post restoration archival and condition reporting:
digit_restoration = StrictPartialOrder(
    nodes=[digit_archival, post_restoration]
)
digit_restoration.order.add_edge(digit_archival, post_restoration)

# The artifact undergoes restoration plan after digitization and assessments
# But digit_archival has Restoration Plan, so fine

# Final reporting & approval sequence
report_approval = StrictPartialOrder(
    nodes=[Report_Draft, Stakeholder_Meet, Acquisition_Vote, Final_Approval]
)
report_approval.order.add_edge(Report_Draft, Stakeholder_Meet)
report_approval.order.add_edge(Stakeholder_Meet, Acquisition_Vote)
report_approval.order.add_edge(Acquisition_Vote, Final_Approval)

# Overall collection: Provenance Check --> scientific analysis --> assessments (legal & cultural) --> digitization/restoration + post-restoration --> reporting & approval

stage1 = StrictPartialOrder(
    nodes=[Provenance_Check, scientific_analysis]
)
stage1.order.add_edge(Provenance_Check, scientific_analysis)

stage2 = StrictPartialOrder(
    nodes=[stage1, assessment]
)
stage2.order.add_edge(stage1, assessment)

stage3 = StrictPartialOrder(
    nodes=[stage2, digit_restoration]
)
stage3.order.add_edge(stage2, digit_restoration)

root = StrictPartialOrder(
    nodes=[stage3, report_approval]
)
root.order.add_edge(stage3, report_approval)