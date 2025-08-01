# Generated from: 760c96fa-5026-4fc1-9c27-e8561c476962.json
# Description: This process involves identifying, validating, and procuring rare and exotic materials from remote locations worldwide for specialized manufacturing. It includes multi-layered supplier vetting, environmental compliance verification, logistical coordination across multiple jurisdictions, and risk management involving geopolitical and climate factors. The process ensures traceability, ethical sourcing certifications, and integration with quality control teams to maintain material integrity throughout transit and storage before delivery to production facilities.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
supplier_vetting = Transition(label='Supplier Vetting')
compliance_check = Transition(label='Compliance Check')
risk_assessment = Transition(label='Risk Assessment')
sample_testing = Transition(label='Sample Testing')
contract_draft = Transition(label='Contract Draft')
permit_request = Transition(label='Permit Request')
logistics_plan = Transition(label='Logistics Plan')
customs_review = Transition(label='Customs Review')
shipping_schedule = Transition(label='Shipping Schedule')
traceability_log = Transition(label='Traceability Log')
ethics_audit = Transition(label='Ethics Audit')
storage_prep = Transition(label='Storage Prep')
quality_verify = Transition(label='Quality Verify')
final_delivery = Transition(label='Final Delivery')

# Loop for permit request and compliance re-check
loop_permit = OperatorPOWL(
    operator=Operator.LOOP,
    children=[permit_request, compliance_check]
)

# Build the overall partially ordered workflow
root = StrictPartialOrder(nodes=[
    site_survey,
    supplier_vetting,
    compliance_check,
    risk_assessment,
    sample_testing,
    contract_draft,
    loop_permit,
    logistics_plan,
    customs_review,
    shipping_schedule,
    traceability_log,
    ethics_audit,
    storage_prep,
    quality_verify,
    final_delivery
])

# Define control-flow dependencies
root.order.add_edge(site_survey, supplier_vetting)
root.order.add_edge(supplier_vetting, compliance_check)
root.order.add_edge(compliance_check, risk_assessment)
root.order.add_edge(risk_assessment, sample_testing)
root.order.add_edge(sample_testing, contract_draft)
root.order.add_edge(contract_draft, loop_permit)
root.order.add_edge(loop_permit, logistics_plan)
root.order.add_edge(logistics_plan, customs_review)
root.order.add_edge(customs_review, shipping_schedule)
root.order.add_edge(shipping_schedule, traceability_log)
root.order.add_edge(shipping_schedule, ethics_audit)
root.order.add_edge(traceability_log, storage_prep)
root.order.add_edge(ethics_audit, storage_prep)
root.order.add_edge(storage_prep, quality_verify)
root.order.add_edge(quality_verify, final_delivery)