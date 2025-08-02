# Generated from: 8916edee-278f-4b6f-9cc5-a1ddeeeb31a4.json
# Description: This process involves the systematic authentication of rare cultural artifacts using a multi-layered approach combining physical examination, advanced imaging, chemical analysis, provenance verification, and blockchain registration. Initial activities include detailed surface scanning and material composition tests to detect anomalies or restorations. Simultaneously, provenance data is cross-referenced with historical databases and auction records to verify ownership lineage. A specialized AI model then analyzes the collected data to predict authenticity confidence scores. Parallelly, a legal compliance check ensures adherence to international cultural property laws. Upon successful validation, the artifact details are encrypted and recorded on a blockchain ledger to guarantee tamper-proof provenance. Finally, a certified authentication report is generated and digitally signed for stakeholders, while an optional insurance appraisal is conducted to assess market value based on authentication results.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transition instances
Surface_Scan = Transition(label='Surface Scan')
Material_Test = Transition(label='Material Test')
Condition_Assess = Transition(label='Condition Assess')
Restoration_Detect = Transition(label='Restoration Detect')

Provenance_Check = Transition(label='Provenance Check')
Historical_Match = Transition(label='Historical Match')
Ownership_Verify = Transition(label='Ownership Verify')
Data_Crossref = Transition(label='Data Crossref')

AI_Analysis = Transition(label='AI Analysis')

Legal_Review = Transition(label='Legal Review')

Blockchain_Log = Transition(label='Blockchain Log')

Report_Draft = Transition(label='Report Draft')
Digital_Sign = Transition(label='Digital Sign')

Insurance_Appraisal = Transition(label='Insurance Appraisal')

Stakeholder_Notify = Transition(label='Stakeholder Notify')

skip = SilentTransition()

# Physical exam PO: Surface Scan -> (Condition Assess & Restoration Detect in parallel) and Material Test in parallel with Surface Scan activities
# Actually "Surface Scan" and "Material Test" are initial activities done simultaneously
# Condition Assess and Restoration Detect relate to those initial activities (detect anomalies/restorations), so modeled as sequential dependencies after Surface Scan and Material Test
# We can consider Physical Exam PO as parallel between Surface Scan and Material Test, then after Surface Scan: Condition Assess and Restoration Detect sequentially.

# Create a physical exam partial order
physical_nodes = [Surface_Scan, Material_Test, Condition_Assess, Restoration_Detect]
physical_PO = StrictPartialOrder(nodes=physical_nodes)
# After Surface Scan: Condition Assess --> Restoration Detect
physical_PO.order.add_edge(Surface_Scan, Condition_Assess)
physical_PO.order.add_edge(Condition_Assess, Restoration_Detect)
# Material Test concurrent to Surface Scan and its condition chain, so no order edges added from Material Test to others (they run in parallel)

# Provenance data check PO: Provenance Check -> (Historical Match & Ownership Verify in parallel) -> Data Crossref
# Provenance Check first, then Historical Match and Ownership Verify parallel, then Data Crossref

provenance_nodes = [Provenance_Check, Historical_Match, Ownership_Verify, Data_Crossref]
provenance_PO = StrictPartialOrder(nodes=provenance_nodes)
provenance_PO.order.add_edge(Provenance_Check, Historical_Match)
provenance_PO.order.add_edge(Provenance_Check, Ownership_Verify)
# Historical Match and Ownership Verify in parallel, both precede Data Crossref
provenance_PO.order.add_edge(Historical_Match, Data_Crossref)
provenance_PO.order.add_edge(Ownership_Verify, Data_Crossref)

# Combine provenance_PO and physical_PO in parallel, both must finish before AI_Analysis

# Parallel physical exam and provenance check
initial_parallel_nodes = [physical_PO, provenance_PO]

initial_PO = StrictPartialOrder(nodes=initial_parallel_nodes)
# No edges between physical_PO and provenance_PO - parallel

# AI Analysis depends on both groups finishing
ai_analysis_PO = StrictPartialOrder(nodes=[initial_PO, AI_Analysis])
ai_analysis_PO.order.add_edge(initial_PO, AI_Analysis)

# Legal Review runs in parallel with AI Analysis (parallel branches)
# So after AI Analysis and Legal Review in parallel, then both must finish to continue.

# Parallel AI Analysis and Legal Review
post_analysis_PO = StrictPartialOrder(nodes=[ai_analysis_PO, Legal_Review])
# No order edges between ai_analysis_PO and Legal_Review (parallel)

# After successful validation, Blockchain Log happens.
# Both ai_analysis_PO and Legal_Review must finish before Blockchain Log

blockchain_PO = StrictPartialOrder(nodes=[post_analysis_PO, Blockchain_Log])
blockchain_PO.order.add_edge(post_analysis_PO, Blockchain_Log)

# After Blockchain Log, Report Draft & Digital Sign sequential

report_PO = StrictPartialOrder(nodes=[Report_Draft, Digital_Sign])
report_PO.order.add_edge(Report_Draft, Digital_Sign)

# After Digital Sign, Stakeholder Notify

notify_PO = StrictPartialOrder(nodes=[report_PO, Stakeholder_Notify])
notify_PO.order.add_edge(report_PO, Stakeholder_Notify)

# Optional Insurance Appraisal: choice between skip or Insurance Appraisal

insurance_xor = OperatorPOWL(operator=Operator.XOR, children=[Insurance_Appraisal, skip])

# Insurance Appraisal and notify run in parallel, as appraisal is optional and conducted alongside stakeholder notification

final_parallel = StrictPartialOrder(nodes=[notify_PO, insurance_xor])
# no order edges needed because optional insurance appraisal can run concurrently with stakeholder notify

# Build the full process: chain blockchain_PO -> final_parallel

root = StrictPartialOrder(nodes=[blockchain_PO, final_parallel])
root.order.add_edge(blockchain_PO, final_parallel)