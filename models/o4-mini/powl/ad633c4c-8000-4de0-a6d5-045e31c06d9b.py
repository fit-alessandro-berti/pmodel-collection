# Generated from: ad633c4c-8000-4de0-a6d5-045e31c06d9b.json
# Description: This process involves a multi-stage verification of historical artifacts to confirm authenticity and provenance before acquisition or sale. Experts conduct material analysis using non-invasive technology, cross-reference historical databases, and perform stylistic comparisons. Legal clearance is obtained to ensure no ownership disputes exist. Marketing teams develop narrative stories to increase artifact value. Finally, secure transportation and insurance arrangements are made to protect the artifact during transfer to buyers or exhibits, ensuring compliance with cultural heritage laws throughout all steps.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
initialReview   = Transition(label='Initial Review')
materialScan    = Transition(label='Material Scan')
databaseCheck   = Transition(label='Database Check')
styleCompare    = Transition(label='Style Compare')
expertPanel     = Transition(label='Expert Panel')
provenanceVerify= Transition(label='Provenance Verify')
legalClearance  = Transition(label='Legal Clearance')
riskAssess      = Transition(label='Risk Assess')
valueEstimate   = Transition(label='Value Estimate')
narrativeCraft  = Transition(label='Narrative Craft')
marketingPlan   = Transition(label='Marketing Plan')
buyerVetting    = Transition(label='Buyer Vetting')
contractDraft   = Transition(label='Contract Draft')
insuranceSetup  = Transition(label='Insurance Setup')
secureTransport = Transition(label='Secure Transport')
finalHandover   = Transition(label='Final Handover')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    initialReview, materialScan, databaseCheck, styleCompare,
    expertPanel, provenanceVerify, legalClearance, riskAssess,
    valueEstimate, narrativeCraft, marketingPlan, buyerVetting,
    contractDraft, insuranceSetup, secureTransport, finalHandover
])

# Initial review precedes all analyses
root.order.add_edge(initialReview, materialScan)
root.order.add_edge(initialReview, databaseCheck)
root.order.add_edge(initialReview, styleCompare)

# Analyses converge to expert panel
root.order.add_edge(materialScan, expertPanel)
root.order.add_edge(databaseCheck, expertPanel)
root.order.add_edge(styleCompare, expertPanel)

# Sequential steps
root.order.add_edge(expertPanel, provenanceVerify)
root.order.add_edge(provenanceVerify, legalClearance)
root.order.add_edge(legalClearance, riskAssess)
root.order.add_edge(riskAssess, valueEstimate)

# After estimating value, craft narrative and plan marketing in parallel
root.order.add_edge(valueEstimate, narrativeCraft)
root.order.add_edge(valueEstimate, marketingPlan)

# Narrative and marketing feed into buyer vetting
root.order.add_edge(narrativeCraft, buyerVetting)
root.order.add_edge(marketingPlan, buyerVetting)

# Finalization steps
root.order.add_edge(buyerVetting, contractDraft)
root.order.add_edge(contractDraft, insuranceSetup)
root.order.add_edge(insuranceSetup, secureTransport)
root.order.add_edge(secureTransport, finalHandover)