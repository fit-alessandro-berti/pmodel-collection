# Generated from: 760c96fa-5026-4fc1-9c27-e8561c476962.json
# Description: This process involves identifying, validating, and procuring rare and exotic materials from remote locations worldwide for specialized manufacturing. It includes multi-layered supplier vetting, environmental compliance verification, logistical coordination across multiple jurisdictions, and risk management involving geopolitical and climate factors. The process ensures traceability, ethical sourcing certifications, and integration with quality control teams to maintain material integrity throughout transit and storage before delivery to production facilities.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Survey = Transition(label='Site Survey')
Supplier_Vetting = Transition(label='Supplier Vetting')
Compliance_Check = Transition(label='Compliance Check')
Risk_Assessment = Transition(label='Risk Assessment')
Sample_Testing = Transition(label='Sample Testing')
Contract_Draft = Transition(label='Contract Draft')
Permit_Request = Transition(label='Permit Request')
Logistics_Plan = Transition(label='Logistics Plan')
Customs_Review = Transition(label='Customs Review')
Shipping_Schedule = Transition(label='Shipping Schedule')
Traceability_Log = Transition(label='Traceability Log')
Ethics_Audit = Transition(label='Ethics Audit')
Storage_Prep = Transition(label='Storage Prep')
Quality_Verify = Transition(label='Quality Verify')
Final_Delivery = Transition(label='Final Delivery')

# Construct subtasks according to the description

# Supplier vetting consists of multi-layered checks:
# Supplier Vetting -> Compliance Check -> Risk Assessment
vetting = StrictPartialOrder(nodes=[Supplier_Vetting, Compliance_Check, Risk_Assessment])
vetting.order.add_edge(Supplier_Vetting, Compliance_Check)
vetting.order.add_edge(Compliance_Check, Risk_Assessment)

# Contract and permit sequence: Contract Draft -> Permit Request
contract_permit = StrictPartialOrder(nodes=[Contract_Draft, Permit_Request])
contract_permit.order.add_edge(Contract_Draft, Permit_Request)

# Logistics coordination consists of:
# Logistics Plan -> Customs Review -> Shipping Schedule
logistics = StrictPartialOrder(nodes=[Logistics_Plan, Customs_Review, Shipping_Schedule])
logistics.order.add_edge(Logistics_Plan, Customs_Review)
logistics.order.add_edge(Customs_Review, Shipping_Schedule)

# Material testing and audit:
# Sample Testing -> XOR of (Traceability Log, Ethics Audit) (both are separate audits,
# but assuming exclusive is not needed: Let's treat them concurrent)
# So let's do partial order with these two concurrent:
testing_audit = StrictPartialOrder(nodes=[Sample_Testing, Traceability_Log, Ethics_Audit])
testing_audit.order.add_edge(Sample_Testing, Traceability_Log)
testing_audit.order.add_edge(Sample_Testing, Ethics_Audit)
# Traceability_Log and Ethics_Audit concurrent

# Storage preparation and quality verification sequence:
# Storage Prep -> Quality Verify
storage_quality = StrictPartialOrder(nodes=[Storage_Prep, Quality_Verify])
storage_quality.order.add_edge(Storage_Prep, Quality_Verify)

# Overall sequence:
# Site Survey first
# then vetting
# then testing and audits
# concurrently contract_permit and logistics (they depend on vetting, but can run in parallel)
# then storage_quality
# then final delivery

# contract_permit and logistics are concurrent after vetting
contract_logistics = StrictPartialOrder(nodes=[contract_permit, logistics])
# no order edges here - concurrent

# testing_audit occurs after vetting and before contract_logistics (to align sequence)
# To model testing_audit before contract_permit and logistics, connect vetting->testing_audit and testing_audit->contract_logistics

middle = StrictPartialOrder(
    nodes=[vetting, testing_audit, contract_logistics]
)
middle.order.add_edge(vetting, testing_audit)
middle.order.add_edge(testing_audit, contract_logistics)

# site_survey -> middle
first_part = StrictPartialOrder(
    nodes=[Site_Survey, middle]
)
first_part.order.add_edge(Site_Survey, middle)

# after contract_logistics, storage_quality and then final delivery
last_part = StrictPartialOrder(
    nodes=[contract_logistics, storage_quality, Final_Delivery]
)
last_part.order.add_edge(contract_logistics, storage_quality)
last_part.order.add_edge(storage_quality, Final_Delivery)

# Combine first_part and last_part and connect properly
root = StrictPartialOrder(
    nodes=[first_part, last_part]
)
root.order.add_edge(first_part, last_part)