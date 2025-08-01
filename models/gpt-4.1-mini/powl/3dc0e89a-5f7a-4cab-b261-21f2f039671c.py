# Generated from: 3dc0e89a-5f7a-4cab-b261-21f2f039671c.json
# Description: This process outlines the steps involved in authenticating rare historical artifacts before acquisition by a museum. It begins with preliminary provenance verification followed by scientific material analysis using spectroscopy and radiocarbon dating. Experts then conduct microscopic examinations and stylistic comparison against known examples. Concurrently, digital imaging technology is employed to detect restorations or forgeries. Results are compiled and reviewed in a cross-disciplinary panel including historians, chemists, and conservators. If authenticity is confirmed, legal ownership documentation is finalized and the artifact is prepared for insured transport. The process ensures thorough validation combining historical, scientific, and legal perspectives to mitigate risks of acquiring counterfeit or misrepresented items.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Verify_Provenance = Transition(label='Verify Provenance')
Collect_Samples = Transition(label='Collect Samples')
Conduct_Spectroscopy = Transition(label='Conduct Spectroscopy')
Radiocarbon_Test = Transition(label='Radiocarbon Test')
Microscopic_Exam = Transition(label='Microscopic Exam')
Stylistic_Check = Transition(label='Stylistic Check')
Digital_Imaging = Transition(label='Digital Imaging')
Forgery_Detection = Transition(label='Forgery Detection')
Compile_Results = Transition(label='Compile Results')
Panel_Review = Transition(label='Panel Review')
Legal_Verification = Transition(label='Legal Verification')
Ownership_Transfer = Transition(label='Ownership Transfer')
Prepare_Transport = Transition(label='Prepare Transport')
Insurance_Setup = Transition(label='Insurance Setup')
Finalize_Acquisition = Transition(label='Finalize Acquisition')

# Scientific Analysis partial order:
# Collect Samples -> (Conduct Spectroscopy and Radiocarbon Test concurrent)
sci_analysis_nodes = [Collect_Samples, Conduct_Spectroscopy, Radiocarbon_Test]
sci_analysis = StrictPartialOrder(nodes=sci_analysis_nodes)
sci_analysis.order.add_edge(Collect_Samples, Conduct_Spectroscopy)
sci_analysis.order.add_edge(Collect_Samples, Radiocarbon_Test)

# Expert Examination partial order:
# Microscopic Exam -> Stylistic Check
expert_exam = StrictPartialOrder(nodes=[Microscopic_Exam, Stylistic_Check])
expert_exam.order.add_edge(Microscopic_Exam, Stylistic_Check)

# Digital Imaging parallel with expert examination
# (Digital Imaging -> Forgery Detection)
digital_imaging_seq = StrictPartialOrder(nodes=[Digital_Imaging, Forgery_Detection])
digital_imaging_seq.order.add_edge(Digital_Imaging, Forgery_Detection)

# Combine expert exam and digital imaging concurrent
exam_imaging = StrictPartialOrder(nodes=[expert_exam, digital_imaging_seq])
# no order edges between expert_exam and digital_imaging_seq means concurrency

# Compile Results and Panel Review sequence
review_seq = StrictPartialOrder(nodes=[Compile_Results, Panel_Review])
review_seq.order.add_edge(Compile_Results, Panel_Review)

# Legal and Preparation sequence
legal_prep_seq = StrictPartialOrder(nodes=[Legal_Verification, Ownership_Transfer, Prepare_Transport, Insurance_Setup])
legal_prep_seq.order.add_edge(Legal_Verification, Ownership_Transfer)
legal_prep_seq.order.add_edge(Ownership_Transfer, Prepare_Transport)
legal_prep_seq.order.add_edge(Prepare_Transport, Insurance_Setup)

# Finalize Acquisition
finalize = Finalize_Acquisition

# Create a loop for the review step: 
# * (Review, Re-examination) where Re-examination is expert exam + digital imaging
loop_review = OperatorPOWL(operator=Operator.LOOP, children=[review_seq, exam_imaging])

# The main process order:
# Verify Provenance -> Scientific Analysis -> Loop Review -> Legal & Prep -> Finalize Acquisition

# Build main sequence nodes
main_nodes = [Verify_Provenance, sci_analysis, loop_review, legal_prep_seq, finalize]
root = StrictPartialOrder(nodes=main_nodes)

root.order.add_edge(Verify_Provenance, sci_analysis)
root.order.add_edge(sci_analysis, loop_review)
root.order.add_edge(loop_review, legal_prep_seq)
root.order.add_edge(legal_prep_seq, finalize)