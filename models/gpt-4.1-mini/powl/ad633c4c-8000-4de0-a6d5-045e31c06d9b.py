# Generated from: ad633c4c-8000-4de0-a6d5-045e31c06d9b.json
# Description: This process involves a multi-stage verification of historical artifacts to confirm authenticity and provenance before acquisition or sale. Experts conduct material analysis using non-invasive technology, cross-reference historical databases, and perform stylistic comparisons. Legal clearance is obtained to ensure no ownership disputes exist. Marketing teams develop narrative stories to increase artifact value. Finally, secure transportation and insurance arrangements are made to protect the artifact during transfer to buyers or exhibits, ensuring compliance with cultural heritage laws throughout all steps.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Initial_Review = Transition(label='Initial Review')
Material_Scan = Transition(label='Material Scan')
Database_Check = Transition(label='Database Check')
Style_Compare = Transition(label='Style Compare')
Expert_Panel = Transition(label='Expert Panel')
Provenance_Verify = Transition(label='Provenance Verify')
Legal_Clearance = Transition(label='Legal Clearance')
Risk_Assess = Transition(label='Risk Assess')
Value_Estimate = Transition(label='Value Estimate')
Narrative_Craft = Transition(label='Narrative Craft')
Marketing_Plan = Transition(label='Marketing Plan')
Buyer_Vetting = Transition(label='Buyer Vetting')
Contract_Draft = Transition(label='Contract Draft')
Insurance_Setup = Transition(label='Insurance Setup')
Secure_Transport = Transition(label='Secure Transport')
Final_Handover = Transition(label='Final Handover')

# Material analysis group as partial order (Material Scan, Database Check, Style Compare) in parallel,
# followed by Expert Panel and Provenance Verify sequentially
material_analysis = StrictPartialOrder(
    nodes=[Material_Scan, Database_Check, Style_Compare, Expert_Panel, Provenance_Verify]
)
# The first three are concurrent (no order)
# Expert Panel after all three
material_analysis.order.add_edge(Material_Scan, Expert_Panel)
material_analysis.order.add_edge(Database_Check, Expert_Panel)
material_analysis.order.add_edge(Style_Compare, Expert_Panel)
# Provenance Verify after Expert Panel
material_analysis.order.add_edge(Expert_Panel, Provenance_Verify)

# Marketing group: Value Estimate, Narrative Craft, Marketing Plan sequentially
marketing = StrictPartialOrder(
    nodes=[Value_Estimate, Narrative_Craft, Marketing_Plan]
)
marketing.order.add_edge(Value_Estimate, Narrative_Craft)
marketing.order.add_edge(Narrative_Craft, Marketing_Plan)

# Legal and risk group: Legal Clearance and Risk Assess concurrent (no order)
legal_risk = StrictPartialOrder(
    nodes=[Legal_Clearance, Risk_Assess]
)

# Buyer preparation group: Buyer Vetting and Contract Draft sequentially
buyer_prep = StrictPartialOrder(
    nodes=[Buyer_Vetting, Contract_Draft]
)
buyer_prep.order.add_edge(Buyer_Vetting, Contract_Draft)

# Final logistics group: Insurance Setup and Secure Transport sequentially
logistics = StrictPartialOrder(
    nodes=[Insurance_Setup, Secure_Transport]
)
logistics.order.add_edge(Insurance_Setup, Secure_Transport)

# Overall root partial order: 
# Initial Review first
# then material analysis, legal & risk, marketing (these three concurrent)
# then buyer prep
# then logistics
# then final handover
root = StrictPartialOrder(
    nodes=[
        Initial_Review,
        material_analysis,
        legal_risk,
        marketing,
        buyer_prep,
        logistics,
        Final_Handover,
    ]
)

# Order dependencies:
root.order.add_edge(Initial_Review, material_analysis)
root.order.add_edge(Initial_Review, legal_risk)
root.order.add_edge(Initial_Review, marketing)
root.order.add_edge(material_analysis, buyer_prep)
root.order.add_edge(legal_risk, buyer_prep)
root.order.add_edge(marketing, buyer_prep)
root.order.add_edge(buyer_prep, logistics)
root.order.add_edge(logistics, Final_Handover)