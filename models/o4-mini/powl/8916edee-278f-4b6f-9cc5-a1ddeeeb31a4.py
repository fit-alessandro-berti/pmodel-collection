# Generated from: 8916edee-278f-4b6f-9cc5-a1ddeeeb31a4.json
# Description: This process involves the systematic authentication of rare cultural artifacts using a multi-layered approach combining physical examination, advanced imaging, chemical analysis, provenance verification, and blockchain registration. Initial activities include detailed surface scanning and material composition tests to detect anomalies or restorations. Simultaneously, provenance data is cross-referenced with historical databases and auction records to verify ownership lineage. A specialized AI model then analyzes the collected data to predict authenticity confidence scores. Parallelly, a legal compliance check ensures adherence to international cultural property laws. Upon successful validation, the artifact details are encrypted and recorded on a blockchain ledger to guarantee tamper-proof provenance. Finally, a certified authentication report is generated and digitally signed for stakeholders, while an optional insurance appraisal is conducted to assess market value based on authentication results.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Atomic activities
surface_scan = Transition(label='Surface Scan')
material_test = Transition(label='Material Test')
condition_assess = Transition(label='Condition Assess')
restoration_detect = Transition(label='Restoration Detect')

provenance_check = Transition(label='Provenance Check')
data_crossref = Transition(label='Data Crossref')
historical_match = Transition(label='Historical Match')
ownership_verify = Transition(label='Ownership Verify')

ai_analysis = Transition(label='AI Analysis')
legal_review = Transition(label='Legal Review')

blockchain_log = Transition(label='Blockchain Log')

report_draft = Transition(label='Report Draft')
digital_sign = Transition(label='Digital Sign')
stakeholder_notify = Transition(label='Stakeholder Notify')

insurance_appraisal = Transition(label='Insurance Appraisal')
skip = SilentTransition()

# Optional insurance appraisal (exclusive choice)
insurance_choice = OperatorPOWL(operator=Operator.XOR, children=[insurance_appraisal, skip])

# Physical examination sub-process (surface scan and material test feeding into assessments)
physical_po = StrictPartialOrder(nodes=[
    surface_scan, material_test, condition_assess, restoration_detect
])
physical_po.order.add_edge(surface_scan, condition_assess)
physical_po.order.add_edge(material_test, restoration_detect)

# Provenance verification sub-process
provenance_po = StrictPartialOrder(nodes=[
    provenance_check, data_crossref, historical_match, ownership_verify
])
provenance_po.order.add_edge(provenance_check, data_crossref)
provenance_po.order.add_edge(data_crossref, historical_match)
provenance_po.order.add_edge(data_crossref, ownership_verify)

# Root process: combine sub-processes, analysis, review, logging, reporting, and optional appraisal
root = StrictPartialOrder(nodes=[
    physical_po,
    provenance_po,
    ai_analysis,
    legal_review,
    blockchain_log,
    report_draft,
    digital_sign,
    stakeholder_notify,
    insurance_choice
])

# Dependencies
# Initial sub-processes -> AI analysis and legal review
root.order.add_edge(physical_po, ai_analysis)
root.order.add_edge(provenance_po, ai_analysis)
root.order.add_edge(physical_po, legal_review)
root.order.add_edge(provenance_po, legal_review)

# After analysis and review -> blockchain logging
root.order.add_edge(ai_analysis, blockchain_log)
root.order.add_edge(legal_review, blockchain_log)

# After blockchain -> report generation and optional insurance appraisal
root.order.add_edge(blockchain_log, report_draft)
root.order.add_edge(blockchain_log, insurance_choice)

# Reporting sequence
root.order.add_edge(report_draft, digital_sign)
root.order.add_edge(digital_sign, stakeholder_notify)