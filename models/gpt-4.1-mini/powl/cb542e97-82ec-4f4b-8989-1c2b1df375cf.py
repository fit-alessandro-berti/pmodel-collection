# Generated from: cb542e97-82ec-4f4b-8989-1c2b1df375cf.json
# Description: This process involves the meticulous authentication and provenance verification of antique artifacts destined for high-profile auctions. It combines physical examination, historical research, scientific testing, and expert consultation to ensure authenticity and legal compliance. The workflow includes artifact intake, condition assessment, material analysis, archival research, comparative study, expert panel review, restoration evaluation, provenance documentation, legal verification, appraisal, cataloging, marketing strategy development, auction preparation, final certification, and post-sale reporting. This atypical process ensures the artifact's value and legitimacy in a niche market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as transitions
ArtifactIntake = Transition(label='Artifact Intake')
ConditionCheck = Transition(label='Condition Check')
MaterialTest = Transition(label='Material Test')
ArchivalSearch = Transition(label='Archival Search')
StyleCompare = Transition(label='Style Compare')
ExpertReview = Transition(label='Expert Review')
RestorationCheck = Transition(label='Restoration Check')
ProvenanceTrace = Transition(label='Provenance Trace')
LegalVerify = Transition(label='Legal Verify')
ValueAppraise = Transition(label='Value Appraise')
CatalogEntry = Transition(label='Catalog Entry')
MarketingPlan = Transition(label='Marketing Plan')
AuctionSetup = Transition(label='Auction Setup')
CertifyFinal = Transition(label='Certify Final')
SalesReport = Transition(label='Sales Report')

# Partial order nodes as needed, with concurrency when applicable.
# Based on description, logical partial order approximation:

# Step 1: Artifact Intake -> Condition Check
# Step 2: Three parallel activities after Condition Check:
#    Material Test, Archival Search, Style Compare
# Step 3: After those three finish, Expert Review
# Step 4: Parallel: Restoration Check and Provenance Trace
# Step 5: After that, Legal Verify
# Step 6: Then appraise the value (Value Appraise)
# Step 7: Then parallel Catalog Entry and Marketing Plan
# Step 8: After both finish, Auction Setup
# Step 9: Then Certify Final
# Step 10: Finally Sales Report

# Create partial orders for concurrency between Material Test, Archival Search, Style Compare
# and between Catalog Entry and Marketing Plan

# Create node sets for concurrency
material = MaterialTest
archival = ArchivalSearch
style = StyleCompare

catalog = CatalogEntry
marketing = MarketingPlan

# Step nodes and partial orders

# Step 2 partial order: activities concurrent after Condition Check
step2_PO = StrictPartialOrder(nodes=[material, archival, style])
# No order edges, concurrent

# Step 4 parallel node with Restoration Check and Provenance Trace
step4_PO = StrictPartialOrder(nodes=[RestorationCheck, ProvenanceTrace])
# concurrent, no edges

# Step 7 parallel node with Catalog Entry and Marketing Plan
step7_PO = StrictPartialOrder(nodes=[catalog, marketing])
# concurrent, no edges

# Now build the main PO with all nodes and the order edges
root_nodes = [
    ArtifactIntake,
    ConditionCheck,
    step2_PO,
    ExpertReview,
    step4_PO,
    LegalVerify,
    ValueAppraise,
    step7_PO,
    AuctionSetup,
    CertifyFinal,
    SalesReport
]

root = StrictPartialOrder(nodes=root_nodes)

# Add order edges:

# Artifact Intake --> Condition Check
root.order.add_edge(ArtifactIntake, ConditionCheck)

# Condition Check --> all three parallel activities at step 2
root.order.add_edge(ConditionCheck, step2_PO)

# All three parallel activities --> Expert Review
root.order.add_edge(step2_PO, ExpertReview)

# Expert Review --> step4_PO (Restoration Check, Provenance Trace)
root.order.add_edge(ExpertReview, step4_PO)

# step4_PO --> Legal Verify
root.order.add_edge(step4_PO, LegalVerify)

# Legal Verify --> Value Appraise
root.order.add_edge(LegalVerify, ValueAppraise)

# Value Appraise --> step7_PO (Catalog Entry and Marketing Plan)
root.order.add_edge(ValueAppraise, step7_PO)

# step7_PO --> Auction Setup
root.order.add_edge(step7_PO, AuctionSetup)

# Auction Setup --> Certify Final
root.order.add_edge(AuctionSetup, CertifyFinal)

# Certify Final --> Sales Report
root.order.add_edge(CertifyFinal, SalesReport)