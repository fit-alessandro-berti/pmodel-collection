# Generated from: f809f07d-752b-4d60-862e-6c114c2857a8.json
# Description: This process involves the intricate authentication of rare cultural artifacts obtained through unconventional channels. The workflow begins with provenance verification, followed by material composition analysis using advanced spectroscopy. Parallelly, historical context validation is performed via archival research and expert consultations. Once initial checks pass, the artifact undergoes digital 3D scanning and microscopic wear pattern analysis. Subsequent steps include cross-referencing with stolen artifact databases and coordinating with international law enforcement. Final stages involve certification issuance, secure documentation, and client briefing. This atypical process ensures high confidence in artifact legitimacy, balancing scientific rigor with legal compliance and ethical considerations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
ProvenanceCheck = Transition(label='Provenance Check')
MaterialTest = Transition(label='Material Test')
ArchiveSearch = Transition(label='Archive Search')
ExpertReview = Transition(label='Expert Review')
Scanning3D = Transition(label='3D Scanning')
WearAnalysis = Transition(label='Wear Analysis')
DatabaseCross = Transition(label='Database Cross')
LawConsult = Transition(label='Law Consult')
ForgeryDetect = Transition(label='Forgery Detect')
Certification = Transition(label='Certification')
DocumentPrep = Transition(label='Document Prep')
ClientBrief = Transition(label='Client Brief')
SecureStorage = Transition(label='Secure Storage')
RiskAssessment = Transition(label='Risk Assessment')
FinalApproval = Transition(label='Final Approval')

# First part: provenance verification then material test
first_seq = StrictPartialOrder(nodes=[ProvenanceCheck, MaterialTest])
first_seq.order.add_edge(ProvenanceCheck, MaterialTest)

# Parallel historical context validation: ArchiveSearch and ExpertReview concurrent
historical_validation = StrictPartialOrder(nodes=[ArchiveSearch, ExpertReview])

# After provenance and material test, and historical validations complete concurrently
# Construct partial order with first_seq and historical_validation concurrent
initial_checks = StrictPartialOrder(nodes=[first_seq, historical_validation])
initial_checks.order.add_edge(first_seq, historical_validation)  # first_seq must finish before historical_validation starts

# According to description, "Parallelly, historical context validation is performed via archival research and expert consultations."  
# But also "Once initial checks pass" includes these. So Order: (ProvenanceCheck -> MaterialTest) --> (ArchiveSearch || ExpertReview)

# After initial checks pass, two parallel activities: 3D Scanning and Wear Analysis concurrent
scanning_wear = StrictPartialOrder(nodes=[Scanning3D, WearAnalysis])
# no order between them, concurrent

# After scanning and wear analysis, next two steps in parallel: DatabaseCross and LawConsult
db_law = StrictPartialOrder(nodes=[DatabaseCross, LawConsult])

# "Subsequent steps include cross-referencing with stolen artifact databases and coordinating with international law enforcement."
# So both happen after scanning and wear analysis
# Order: scanning_wear --> db_law

scan_wear_to_db_law = StrictPartialOrder(nodes=[scanning_wear, db_law])
scan_wear_to_db_law.order.add_edge(scanning_wear, db_law)

# ForgeryDetect and RiskAssessment are logically validation/risk steps
# Description mentions "RiskAssessment" and "ForgeryDetect" were not explicitly detailed in order.
# We can consider ForgeryDetect after DatabaseCross and LawConsult (to verify forgery risk)
# RiskAssessment may come after ForgeryDetect as a critical evaluation step

forgery_risk_seq = StrictPartialOrder(nodes=[ForgeryDetect, RiskAssessment])
forgery_risk_seq.order.add_edge(ForgeryDetect, RiskAssessment)

# Link db_law to forgery_risk_seq
db_law_to_forgery_risk = StrictPartialOrder(nodes=[db_law, forgery_risk_seq])
db_law_to_forgery_risk.order.add_edge(db_law, forgery_risk_seq)

# Final approval after risk assessment
final_approval_seq = StrictPartialOrder(nodes=[RiskAssessment, FinalApproval])
final_approval_seq.order.add_edge(RiskAssessment, FinalApproval)

# Connect forgery_risk_seq with FinalApproval
forgery_risk_to_final = StrictPartialOrder(nodes=[forgery_risk_seq, FinalApproval])
forgery_risk_to_final.order.add_edge(forgery_risk_seq, FinalApproval)

# Certification, Document Prep, Client Brief, Secure Storage are final stages
# The description states final stages involve certification issuance, secure documentation, client briefing
# Likely these 4 activities run concurrently after FinalApproval

final_stages = StrictPartialOrder(nodes=[Certification, DocumentPrep, ClientBrief, SecureStorage])

# FinalApproval --> final_stages
final_seq = StrictPartialOrder(nodes=[FinalApproval, final_stages])
final_seq.order.add_edge(FinalApproval, final_stages)

# Compose larger parts stepwise:

# 1) initial_checks (ProvenanceCheck->MaterialTest -> (ArchiveSearch || ExpertReview))
# 2) scanning_wear (3D Scanning || Wear Analysis)
# 3) db_law (DatabaseCross || LawConsult)
# 4) forgery_risk_seq (ForgeryDetect->RiskAssessment)
# 5) FinalApproval
# 6) final_stages (Certification, DocumentPrep, ClientBrief, SecureStorage concurrent)

# Compose scanning and db_law with forgery risk and final approval
step_2_3_4_5 = StrictPartialOrder(
    nodes=[scanning_wear, db_law, forgery_risk_seq, FinalApproval]
)
step_2_3_4_5.order.add_edge(scanning_wear, db_law)
step_2_3_4_5.order.add_edge(db_law, forgery_risk_seq)
step_2_3_4_5.order.add_edge(forgery_risk_seq, FinalApproval)

# Compose all from initial_checks through final stages
all_but_final_stages = StrictPartialOrder(
    nodes=[initial_checks, scanning_wear, db_law, forgery_risk_seq, FinalApproval]
)
all_but_final_stages.order.add_edge(initial_checks, scanning_wear)
all_but_final_stages.order.add_edge(scanning_wear, db_law)
all_but_final_stages.order.add_edge(db_law, forgery_risk_seq)
all_but_final_stages.order.add_edge(forgery_risk_seq, FinalApproval)

root = StrictPartialOrder(
    nodes=[all_but_final_stages, final_stages]
)
root.order.add_edge(all_but_final_stages, final_stages)