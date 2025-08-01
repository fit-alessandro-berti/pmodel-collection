# Generated from: 89333b83-4ecd-4e6f-b171-1c8c3d5cebd4.json
# Description: This process involves verifying the authenticity and provenance of historical artifacts through a multi-step evaluation combining scientific analysis, archival research, expert consultations, and cross-referencing with digital databases. It begins with initial artifact inspection and sampling, followed by radiocarbon dating and material composition analysis. Concurrently, archival research is conducted to trace the artifact’s documented history, including ownership and exhibition records. Expert panels review findings to assess stylistic consistency and historical context. Parallelly, digital provenance databases are queried to identify known forgeries or ownership disputes. Subsequent steps include legal clearance for export or sale, condition reporting, and preparing certification documents. The process concludes with secure artifact storage or transfer to authorized parties, ensuring chain-of-custody integrity and compliance with international cultural property laws.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
InitialInspection = Transition(label='Initial Inspection')
SampleCollection = Transition(label='Sample Collection')
MaterialAnalysis = Transition(label='Material Analysis')
RadiocarbonTest = Transition(label='Radiocarbon Test')
ArchivalSearch = Transition(label='Archival Search')
OwnershipTrace = Transition(label='Ownership Trace')
StylisticReview = Transition(label='Stylistic Review')
ExpertPanel = Transition(label='Expert Panel')
DatabaseQuery = Transition(label='Database Query')
ForgeryCheck = Transition(label='Forgery Check')
LegalClearance = Transition(label='Legal Clearance')
ConditionReport = Transition(label='Condition Report')
CertificationPrep = Transition(label='Certification Prep')
ChainCustody = Transition(label='Chain Custody')
SecureStorage = Transition(label='Secure Storage')

# Define partial orders for concurrent branches inside radiocarbon/material analysis branch
# Material analysis branch: SampleCollection --> RadiocarbonTest and MaterialAnalysis in parallel
# Since RadiocarbonTest and MaterialAnalysis are parallel after SampleCollection
sample_branch = StrictPartialOrder(nodes=[SampleCollection, RadiocarbonTest, MaterialAnalysis])
sample_branch.order.add_edge(SampleCollection, RadiocarbonTest)
sample_branch.order.add_edge(SampleCollection, MaterialAnalysis)
# RadiocarbonTest and MaterialAnalysis are concurrent (no order between them)

# Archival research branch: ArchivalSearch --> OwnershipTrace
archival_branch = StrictPartialOrder(nodes=[ArchivalSearch, OwnershipTrace])
archival_branch.order.add_edge(ArchivalSearch, OwnershipTrace)

# Expert panel branch: StylisticReview --> ExpertPanel
expert_branch = StrictPartialOrder(nodes=[StylisticReview, ExpertPanel])
expert_branch.order.add_edge(StylisticReview, ExpertPanel)

# Database query branch: DatabaseQuery --> ForgeryCheck
database_branch = StrictPartialOrder(nodes=[DatabaseQuery, ForgeryCheck])
database_branch.order.add_edge(DatabaseQuery, ForgeryCheck)

# Combine Expert and Database branches in parallel (both occur together)
expert_db_parallel = StrictPartialOrder(nodes=[expert_branch, database_branch])
# no order edges, concurrent

# Combine Archival branch and expert_db_parallel in parallel (all three run concurrently)
archival_expertdb_parallel = StrictPartialOrder(nodes=[archival_branch, expert_db_parallel])
# no order edges, all concurrent

# After initial inspection, we do sample_branch and archival_expertdb_parallel in parallel
initial_to_sampling_archival = StrictPartialOrder(
    nodes=[InitialInspection, sample_branch, archival_expertdb_parallel]
)
initial_to_sampling_archival.order.add_edge(InitialInspection, sample_branch)
initial_to_sampling_archival.order.add_edge(InitialInspection, archival_expertdb_parallel)
# sample_branch and archival_expertdb_parallel concurrent

# After these parallel branches, synchronization before proceeding:
# Next steps: LegalClearance --> ConditionReport --> CertificationPrep
legal_seq = StrictPartialOrder(nodes=[LegalClearance, ConditionReport, CertificationPrep])
legal_seq.order.add_edge(LegalClearance, ConditionReport)
legal_seq.order.add_edge(ConditionReport, CertificationPrep)

# Then ChainCustody --> SecureStorage
final_seq = StrictPartialOrder(nodes=[ChainCustody, SecureStorage])
final_seq.order.add_edge(ChainCustody, SecureStorage)

# Assemble full process partial order:
# initial_to_sampling_archival --> legal_seq --> final_seq
full_process = StrictPartialOrder(
    nodes=[initial_to_sampling_archival, legal_seq, final_seq]
)
full_process.order.add_edge(initial_to_sampling_archival, legal_seq)
full_process.order.add_edge(legal_seq, final_seq)

root = full_process