# Generated from: 1d29cf0d-0774-496b-bcaa-492af72a3a06.json
# Description: This process involves the comprehensive examination and validation of historical artifacts to confirm their authenticity prior to acquisition or exhibition. It integrates multidisciplinary expert assessments, including material analysis, provenance research, and forensic imaging. The workflow starts with artifact reception and initial inspection, followed by detailed scientific testing such as radiocarbon dating and pigment analysis. Parallel provenance verification is conducted through archival research and expert interviews. Subsequent steps include digital 3D modeling and comparative stylistic evaluation against known authentic items. Findings are consolidated into a comprehensive report reviewed by a certification board. The final stage involves secure cataloging and preparation for either acquisition, loan, or public display with strict condition monitoring protocols. Throughout the process, data integrity and chain of custody are rigorously maintained to ensure credibility and traceability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ArtifactReception = Transition(label='Artifact Reception')
InitialInspection = Transition(label='Initial Inspection')
MaterialSampling = Transition(label='Material Sampling')
RadiocarbonTest = Transition(label='Radiocarbon Test')
PigmentAnalysis = Transition(label='Pigment Analysis')
ProvenanceCheck = Transition(label='Provenance Check')
ArchiveResearch = Transition(label='Archive Research')
ExpertInterviews = Transition(label='Expert Interviews')
ForensicImaging = Transition(label='Forensic Imaging')
Modeling3D = Transition(label='3D Modeling')
StylisticReview = Transition(label='Stylistic Review')
ReportCompilation = Transition(label='Report Compilation')
CertificationReview = Transition(label='Certification Review')
CatalogEntry = Transition(label='Catalog Entry')
ConditionPrep = Transition(label='Condition Prep')
DataVerification = Transition(label='Data Verification')
ChainCustody = Transition(label='Chain Custody')

# Detailed scientific testing partial order: Material Sampling -> Radiocarbon Test and Pigment Analysis in parallel
scientificTesting = StrictPartialOrder(
    nodes=[MaterialSampling, RadiocarbonTest, PigmentAnalysis]
)
scientificTesting.order.add_edge(MaterialSampling, RadiocarbonTest)
scientificTesting.order.add_edge(MaterialSampling, PigmentAnalysis)

# Provenance verification partial order: Provenance Check -> Archive Research and Expert Interviews in parallel
provenanceVerification = StrictPartialOrder(
    nodes=[ProvenanceCheck, ArchiveResearch, ExpertInterviews]
)
provenanceVerification.order.add_edge(ProvenanceCheck, ArchiveResearch)
provenanceVerification.order.add_edge(ProvenanceCheck, ExpertInterviews)

# Parallel provenance verification and scientific testing
verifications = StrictPartialOrder(
    nodes=[scientificTesting, provenanceVerification]
)
# no order edges between scientificTesting and provenanceVerification => concurrent

# Parallel after Initial Inspection: verifications and Forensic Imaging
# So after Initial Inspection, Forensic Imaging and verifications are concurrent
postInspection = StrictPartialOrder(
    nodes=[verifications, ForensicImaging]
)
# no edges => parallel

# After those, 3D modeling and stylistic review sequentially
modelAndReview = StrictPartialOrder(
    nodes=[Modeling3D, StylisticReview]
)
modelAndReview.order.add_edge(Modeling3D, StylisticReview)

# Report Compilation after both modelAndReview and also depends on verifications and forensic imaging
# So report compilation after all detailed analyses:
# Since verifications and Forensic Imaging are concurrent with modelAndReview too,
# and all must precede report compilation, let's compose partial order with these as nodes:

preReportNodes = StrictPartialOrder(
    nodes=[postInspection, modelAndReview]
)
# We want report after them all, so we will create a PO with nodes preReportNodes and ReportCompilation,
# with edges from postInspection and modelAndReview to ReportCompilation

preReportAll = StrictPartialOrder(
    nodes=[preReportNodes, ReportCompilation]
)
preReportAll.order.add_edge(preReportNodes, ReportCompilation)

# Certification Review after Report Compilation
certification = StrictPartialOrder(
    nodes=[ReportCompilation, CertificationReview]
)
certification.order.add_edge(ReportCompilation, CertificationReview)

# Final stage parallel activities: Catalog Entry and Condition Prep with strict condition monitoring
finalStage = StrictPartialOrder(
    nodes=[CatalogEntry, ConditionPrep]
)
# both concurrent

# After Certification Review, Data Verification and Chain Custody must be maintained during the process,
# but they apply to final stage to ensure credibility and traceability.
# Assume they happen right after certification and before or during final stage.
# Model Data Verification and Chain Custody concurrently, and both precede finalStage:

dataChain = StrictPartialOrder(
    nodes=[DataVerification, ChainCustody]
)

finalAfterCert = StrictPartialOrder(
    nodes=[dataChain, finalStage]
)
finalAfterCert.order.add_edge(dataChain, finalStage)

# Compose the full sequential order:
# Artifact Reception -> Initial Inspection -> verifications & forensic imaging -> 3D modeling & stylistic review -> report -> certification -> data/chain -> final stage

step1 = ArtifactReception
step2 = InitialInspection

step3 = postInspection         # verifications & forensic imaging in parallel after Initial Inspection
step4 = modelAndReview         # sequential 3D Modeling -> Stylistic Review after verifications and forensic imaging
step5 = ReportCompilation
step6 = CertificationReview
step7 = finalAfterCert         # data verification & chain custody -> final stage concurrent activities

# Compose steps by linking edges

root = StrictPartialOrder(
    nodes=[step1, step2, step3, step4, step5, step6, step7]
)
root.order.add_edge(step1, step2)
root.order.add_edge(step2, step3)
root.order.add_edge(step3, step4)
root.order.add_edge(step4, step5)
root.order.add_edge(step5, step6)
root.order.add_edge(step6, step7)