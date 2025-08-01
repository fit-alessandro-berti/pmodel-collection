# Generated from: 0c9a71a9-262d-4b3d-9858-d7dcd2f3b895.json
# Description: This process outlines the comprehensive steps involved in authenticating antique items for resale or auction. It begins with initial item intake and visual inspection, followed by provenance research and materials analysis using advanced spectroscopy. Expert consultations and historical context verification ensure accurate dating and origin identification. Condition reporting and restoration feasibility assessments are conducted next, before generating a detailed certification report. Finally, the item is digitally documented, insured, and prepared for market listing or archival storage, ensuring traceability and compliance with legal regulations throughout the process.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
item_intake        = Transition(label='Item Intake')
visual_inspect     = Transition(label='Visual Inspect')
provenance_check   = Transition(label='Provenance Check')
materials_scan     = Transition(label='Materials Scan')
spectroscopy_test  = Transition(label='Spectroscopy Test')
expert_consult     = Transition(label='Expert Consult')
context_verify     = Transition(label='Context Verify')
date_confirm       = Transition(label='Date Confirm')
origin_identify    = Transition(label='Origin Identify')
condition_report   = Transition(label='Condition Report')
restoration_plan   = Transition(label='Restoration Plan')
certification_gen  = Transition(label='Certification Gen')
digital_archive    = Transition(label='Digital Archive')
insurance_setup    = Transition(label='Insurance Setup')
market_prep        = Transition(label='Market Prep')

# Build the partial order
root = StrictPartialOrder(nodes=[
    item_intake,
    visual_inspect,
    provenance_check,
    materials_scan,
    spectroscopy_test,
    expert_consult,
    context_verify,
    date_confirm,
    origin_identify,
    condition_report,
    restoration_plan,
    certification_gen,
    digital_archive,
    insurance_setup,
    market_prep
])

# Define the control flow
root.order.add_edge(item_intake,      visual_inspect)

# Split into two parallel branches after inspection
root.order.add_edge(visual_inspect,   provenance_check)
root.order.add_edge(visual_inspect,   materials_scan)

# Provenance research branch
root.order.add_edge(provenance_check, expert_consult)
root.order.add_edge(expert_consult,   context_verify)
root.order.add_edge(context_verify,   date_confirm)
root.order.add_edge(date_confirm,     origin_identify)

# Materials analysis branch
root.order.add_edge(materials_scan,     spectroscopy_test)

# Synchronize branches into condition reporting
root.order.add_edge(spectroscopy_test,  condition_report)
root.order.add_edge(origin_identify,    condition_report)

# Continue sequentially to market prep
root.order.add_edge(condition_report,   restoration_plan)
root.order.add_edge(restoration_plan,   certification_gen)
root.order.add_edge(certification_gen,  digital_archive)
root.order.add_edge(digital_archive,    insurance_setup)
root.order.add_edge(insurance_setup,    market_prep)