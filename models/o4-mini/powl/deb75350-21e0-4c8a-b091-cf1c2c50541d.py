# Generated from: deb75350-21e0-4c8a-b091-cf1c2c50541d.json
# Description: This process outlines the detailed steps involved in authenticating historical artifacts for museum acquisition. It includes initial artifact intake, physical and chemical analysis, provenance verification through archival research, expert consultation, digital imaging, and condition reporting. The workflow ensures that each artifact undergoes rigorous scrutiny to confirm authenticity and historical significance before final acquisition decisions are made. Additionally, it integrates risk assessment related to forgery detection and coordinates with legal teams for compliance with cultural property laws. The process concludes with cataloging and secure storage preparation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
intake        = Transition(label='Intake Review')
visual        = Transition(label='Visual Inspect')
material      = Transition(label='Material Test')
archival      = Transition(label='Archival Search')
expert        = Transition(label='Expert Consult')
prov_check    = Transition(label='Provenance Check')
scanner       = Transition(label='Digital Scan')
condition     = Transition(label='Condition Report')
risk          = Transition(label='Risk Analysis')
forgery       = Transition(label='Forgery Assess')
legal         = Transition(label='Legal Review')
vote          = Transition(label='Acquisition Vote')
catalog       = Transition(label='Catalog Entry')
storage       = Transition(label='Storage Prep')
final_approve = Transition(label='Final Approval')

# Loop body for repeated risk handling: Forgery Assess -> Legal Review
risk_body = StrictPartialOrder(nodes=[forgery, legal])
risk_body.order.add_edge(forgery, legal)

# LOOP: do Risk Analysis then either exit or execute (Forgery Assess -> Legal Review) and repeat
risk_loop = OperatorPOWL(operator=Operator.LOOP, children=[risk, risk_body])

# Root partial order
root = StrictPartialOrder(nodes=[
    intake,
    visual,
    material,
    scanner,
    condition,
    archival,
    expert,
    prov_check,
    risk_loop,
    vote,
    catalog,
    storage,
    final_approve
])

# Define the control-flow dependencies
root.order.add_edge(intake, visual)
root.order.add_edge(intake, material)

root.order.add_edge(visual, scanner)
root.order.add_edge(visual, condition)

root.order.add_edge(material, archival)
root.order.add_edge(material, expert)

root.order.add_edge(archival, prov_check)
root.order.add_edge(expert, prov_check)

root.order.add_edge(prov_check, risk_loop)

root.order.add_edge(risk_loop, vote)
root.order.add_edge(vote, catalog)
root.order.add_edge(catalog, storage)
root.order.add_edge(storage, final_approve)