# Generated from: d8ce61d2-9e92-4a27-94a1-2dd27d09c446.json
# Description: This process involves tracking and verifying the provenance of rare custom artifacts from creation through multiple ownership transfers, restorations, and exhibitions. It requires coordination between artists, historians, appraisers, logistics providers, and legal experts to ensure authenticity, condition, and rightful ownership are maintained and documented at every stage. The process integrates physical inspections, digital ledger updates, encrypted ownership transfers, and compliance checks with international cultural property laws, culminating in periodic public showcase events and archival storage preparation, thus safeguarding the artifact’s legacy and market value over decades.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
InitialAudit = Transition(label='Initial Audit')
ArtistReview = Transition(label='Artist Review')
MaterialCheck = Transition(label='Material Check')
ConditionScan = Transition(label='Condition Scan')
OwnershipVerify = Transition(label='Ownership Verify')
AppraisalUpdate = Transition(label='Appraisal Update')
RestorationPlan = Transition(label='Restoration Plan')
RestorationTrack = Transition(label='Restoration Track')
LogisticsBook = Transition(label='Logistics Book')
ShippingMonitor = Transition(label='Shipping Monitor')
CustomsClear = Transition(label='Customs Clear')
LegalCompliance = Transition(label='Legal Compliance')
LedgerUpdate = Transition(label='Ledger Update')
ExhibitionSetup = Transition(label='Exhibition Setup')
PublicShowcase = Transition(label='Public Showcase')
ArchivalPrep = Transition(label='Archival Prep')
FinalReport = Transition(label='Final Report')

# Model restoration loop: plan restoration, track restoration, then either exit or repeat restoration
restoration_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[RestorationPlan, RestorationTrack]
)

# Model shipping monitoring choices after logistics booking:
# either ShippingMonitor or CustomsClear (exclusive choice)
shipping_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[ShippingMonitor, CustomsClear]
)

# Setup partial order nodes
nodes = [
    InitialAudit,
    ArtistReview,
    MaterialCheck,
    ConditionScan,
    OwnershipVerify,
    AppraisalUpdate,
    restoration_loop,
    LogisticsBook,
    shipping_choice,
    LegalCompliance,
    LedgerUpdate,
    ExhibitionSetup,
    PublicShowcase,
    ArchivalPrep,
    FinalReport
]

root = StrictPartialOrder(nodes=nodes)

# Define order edges based on process description dependencies

# Initial auditing phases roughly sequential and partially ordered
root.order.add_edge(InitialAudit, ArtistReview)
root.order.add_edge(ArtistReview, MaterialCheck)
root.order.add_edge(MaterialCheck, ConditionScan)

# ConditionScan leads to OwnershipVerify and AppraisalUpdate (both parallel)
root.order.add_edge(ConditionScan, OwnershipVerify)
root.order.add_edge(ConditionScan, AppraisalUpdate)

# OwnershipVerify must complete before RestorationPlan (loop)
root.order.add_edge(OwnershipVerify, restoration_loop)

# AppraisalUpdate before LogisticsBook
root.order.add_edge(AppraisalUpdate, LogisticsBook)

# After Restoration loop is done, proceed to LogisticsBook (restorations finish before logistics)
root.order.add_edge(restoration_loop, LogisticsBook)

# LogisticsBook leads to choice of ShippingMonitor or CustomsClear
root.order.add_edge(LogisticsBook, shipping_choice)

# Both legal compliance and ledger update depend on completion of shipping choice
root.order.add_edge(shipping_choice, LegalCompliance)
root.order.add_edge(shipping_choice, LedgerUpdate)

# LegalCompliance and LedgerUpdate independent and both precede ExhibitionSetup
root.order.add_edge(LegalCompliance, ExhibitionSetup)
root.order.add_edge(LedgerUpdate, ExhibitionSetup)

# Exhibition setup precedes public showcase
root.order.add_edge(ExhibitionSetup, PublicShowcase)

# Public showcase leads to archival prep
root.order.add_edge(PublicShowcase, ArchivalPrep)

# Archival prep leads to final report
root.order.add_edge(ArchivalPrep, FinalReport)