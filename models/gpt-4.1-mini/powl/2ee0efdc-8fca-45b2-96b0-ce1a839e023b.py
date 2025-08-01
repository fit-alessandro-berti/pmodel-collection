# Generated from: 2ee0efdc-8fca-45b2-96b0-ce1a839e023b.json
# Description: This process involves the detailed verification and validation of antique artifacts to determine their authenticity and provenance. Experts collaborate to perform material analysis, historical research, and stylistic comparisons, while coordinating with legal authorities for ownership checks. The process includes advanced imaging, carbon dating, and provenance documentation, followed by expert panel review and final certification. This atypical yet realistic procedure ensures that artifacts entering collections or markets are genuine, legally owned, and accurately described, minimizing fraud and preserving cultural heritage.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

ArtifactIntake = Transition(label='Artifact Intake')
InitialSurvey = Transition(label='Initial Survey')

# Material analysis branch: Material Testing and Carbon Dating in parallel and then join
MaterialTesting = Transition(label='Material Testing')
CarbonDating = Transition(label='Carbon Dating')

# Stylistic and historical research branch: Style Compare and Historical Check in parallel and then join
StyleCompare = Transition(label='Style Compare')
HistoricalCheck = Transition(label='Historical Check')

# Legal authorities coordination branch: Ownership Verify and Legal Review with Provenance Trace and Imaging Scan
OwnershipVerify = Transition(label='Ownership Verify')
LegalReview = Transition(label='Legal Review')
ProvenanceTrace = Transition(label='Provenance Trace')
ImagingScan = Transition(label='Imaging Scan')

# Expert Consult after imaging and checks
ExpertConsult = Transition(label='Expert Consult')

# Condition Report before panel review
ConditionReport = Transition(label='Condition Report')

# Panel Review, Certification, Final Archive serial execution
PanelReview = Transition(label='Panel Review')
Certification = Transition(label='Certification')
FinalArchive = Transition(label='Final Archive')

# Construct partial orders inside branches:

# Material analysis PO: Material Testing and Carbon Dating concurrent
material_analysis = StrictPartialOrder(nodes=[MaterialTesting, CarbonDating])

# Stylistic & historical research PO: Style Compare and Historical Check concurrent
stylistic_historical = StrictPartialOrder(nodes=[StyleCompare, HistoricalCheck])

# Legal coordination PO: Ownership Verify -> Legal Review, and also Provenance Trace and Imaging Scan concurrency
legal_coordination = StrictPartialOrder(nodes=[OwnershipVerify, LegalReview, ProvenanceTrace, ImagingScan])
legal_coordination.order.add_edge(OwnershipVerify, LegalReview)
# Provenance Trace and Imaging Scan concurrent with OwnershipVerify & LegalReview (no edges to them)

# Merge imaging scans and legal review results before Expert Consult
pre_expert_nodes = [legal_coordination, ImagingScan]
# ImagingScan is part of legal_coordination, so included. Actually ImagingScan inside legal_coordination.

# So to join the branches: 
# after Initial Survey comes 3 branches in parallel:
# 1) material_analysis
# 2) stylistic_historical
# 3) legal_coordination

# We'll represent these three branches as parallel nodes of a PO after Initial Survey.

# After all 3 branches, expert consult.

# Define a PO for the parallel branches after Initial Survey
branches_after_survey = StrictPartialOrder(
    nodes=[material_analysis, stylistic_historical, legal_coordination]
)
# No ordering edges as they are concurrent

# Define partial order from Artifact Intake -> Initial Survey -> (3 branches after survey)
root = StrictPartialOrder(
    nodes=[ArtifactIntake, InitialSurvey, material_analysis, stylistic_historical, legal_coordination,
           ExpertConsult, ConditionReport, PanelReview, Certification, FinalArchive]
)
root.order.add_edge(ArtifactIntake, InitialSurvey)
root.order.add_edge(InitialSurvey, material_analysis)
root.order.add_edge(InitialSurvey, stylistic_historical)
root.order.add_edge(InitialSurvey, legal_coordination)

# After the three branches complete, Expert Consult
root.order.add_edge(material_analysis, ExpertConsult)
root.order.add_edge(stylistic_historical, ExpertConsult)
root.order.add_edge(legal_coordination, ExpertConsult)

# Then linear sequence after Expert Consult
root.order.add_edge(ExpertConsult, ConditionReport)
root.order.add_edge(ConditionReport, PanelReview)
root.order.add_edge(PanelReview, Certification)
root.order.add_edge(Certification, FinalArchive)