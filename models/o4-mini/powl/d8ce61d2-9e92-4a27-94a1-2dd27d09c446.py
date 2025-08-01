# Generated from: d8ce61d2-9e92-4a27-94a1-2dd27d09c446.json
# Description: This process involves tracking and verifying the provenance of rare custom artifacts from creation through multiple ownership transfers, restorations, and exhibitions. It requires coordination between artists, historians, appraisers, logistics providers, and legal experts to ensure authenticity, condition, and rightful ownership are maintained and documented at every stage. The process integrates physical inspections, digital ledger updates, encrypted ownership transfers, and compliance checks with international cultural property laws, culminating in periodic public showcase events and archival storage preparation, thus safeguarding the artifact’s legacy and market value over decades.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
initial_audit     = Transition(label='Initial Audit')
artist_review     = Transition(label='Artist Review')
material_check    = Transition(label='Material Check')
condition_scan    = Transition(label='Condition Scan')
ownership_verify  = Transition(label='Ownership Verify')
appraisal_update  = Transition(label='Appraisal Update')
restoration_plan  = Transition(label='Restoration Plan')
restoration_track = Transition(label='Restoration Track')
logistics_book    = Transition(label='Logistics Book')
shipping_monitor  = Transition(label='Shipping Monitor')
customs_clear     = Transition(label='Customs Clear')
legal_compliance  = Transition(label='Legal Compliance')
ledger_update     = Transition(label='Ledger Update')
exhibition_setup  = Transition(label='Exhibition Setup')
public_showcase   = Transition(label='Public Showcase')
archival_prep     = Transition(label='Archival Prep')
final_report      = Transition(label='Final Report')

# Loop for restoration cycle: plan → track → plan → …
restoration_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[restoration_plan, restoration_track]
)

# Loop for periodic public showcases: setup → showcase → setup → …
exhibition_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[exhibition_setup, public_showcase]
)

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    initial_audit, artist_review, material_check, condition_scan,
    ownership_verify, appraisal_update, restoration_loop,
    logistics_book, shipping_monitor, customs_clear,
    legal_compliance, ledger_update,
    exhibition_loop, archival_prep, final_report
])

# Define the precedence relations
o = root.order
o.add_edge(initial_audit, artist_review)
o.add_edge(artist_review, material_check)
o.add_edge(material_check, condition_scan)
o.add_edge(condition_scan, ownership_verify)
o.add_edge(ownership_verify, appraisal_update)
o.add_edge(appraisal_update, restoration_loop)
o.add_edge(restoration_loop, logistics_book)
o.add_edge(logistics_book, shipping_monitor)
o.add_edge(shipping_monitor, customs_clear)

# After customs clearance, compliance and ledger updates run in parallel
o.add_edge(customs_clear, legal_compliance)
o.add_edge(customs_clear, ledger_update)

# Both must complete before moving to exhibition loop
o.add_edge(legal_compliance, exhibition_loop)
o.add_edge(ledger_update, exhibition_loop)

# After exhibition loop, archive prep and final reporting
o.add_edge(exhibition_loop, archival_prep)
o.add_edge(archival_prep, final_report)