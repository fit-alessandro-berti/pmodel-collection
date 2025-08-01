# Generated from: 79e65744-531b-40f0-9898-51d3498290bc.json
# Description: This process involves the meticulous examination and verification of rare antique artifacts to determine their authenticity, provenance, and historical significance. It includes initial visual screening, advanced imaging techniques, material composition analysis, historical record cross-referencing, expert consultations, and final certification. The process ensures that collectors and institutions acquire genuine pieces while preventing forgeries from entering the market. It also incorporates secure documentation, digital archiving, and legal compliance checks to maintain integrity throughout the artifact's lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
t_init     = Transition(label="Initial Screening")
t_vis      = Transition(label="Visual Inspection")
t_img      = Transition(label="Imaging Capture")
t_mat      = Transition(label="Material Testing")
t_prov     = Transition(label="Provenance Check")
t_db       = Transition(label="Database Search")
t_hist     = Transition(label="Historical Crossref")
t_forg     = Transition(label="Forgery Analysis")
t_exp      = Transition(label="Expert Review")
t_cond     = Transition(label="Condition Report")
t_lega     = Transition(label="Legal Compliance")
t_cert     = Transition(label="Certificate Issue")
t_arch     = Transition(label="Digital Archive")
t_pres     = Transition(label="Client Presentation")
t_store    = Transition(label="Secure Storage")
t_final    = Transition(label="Final Approval")

# Loop for repeated forgery analysis and expert review
forg_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[t_forg, t_exp]
)

# Concurrency of imaging capture and material testing
imaging_mat = StrictPartialOrder(nodes=[t_img, t_mat])

# Sequential provenance check steps
prov_seq = StrictPartialOrder(nodes=[t_db, t_hist])
prov_seq.order.add_edge(t_db, t_hist)

# Build the overall partial order
root = StrictPartialOrder(
    nodes=[
        t_init,
        t_vis,
        imaging_mat,
        t_prov,
        prov_seq,
        forg_loop,
        t_cond,
        t_lega,
        t_cert,
        t_arch,
        t_store,
        t_pres,
        t_final
    ]
)

# Define the control-flow/order relations
root.order.add_edge(t_init, imaging_mat)       # Initial -> parallel imaging/material
root.order.add_edge(t_init, t_vis)             # Initial -> Visual Inspection
root.order.add_edge(t_vis, imaging_mat)        # Visual Inspection -> parallel part
root.order.add_edge(imaging_mat, t_prov)       # After imaging/material -> provenance check
root.order.add_edge(t_prov, prov_seq)          # Provenance Check -> DB & Historical
root.order.add_edge(prov_seq, forg_loop)       # Provenance result -> forgery loop
root.order.add_edge(forg_loop, t_cond)         # After forgery loop -> Condition Report
root.order.add_edge(t_cond, t_lega)            # Condition -> Legal Compliance
root.order.add_edge(t_lega, t_cert)            # Legal -> Certificate Issue
root.order.add_edge(t_cert, t_arch)            # Certificate -> Digital Archive
root.order.add_edge(t_cert, t_store)           # Certificate -> Secure Storage
root.order.add_edge(t_cert, t_pres)            # Certificate -> Client Presentation
root.order.add_edge(t_arch, t_final)           # Archive -> Final Approval
root.order.add_edge(t_store, t_final)          # Storage -> Final Approval
root.order.add_edge(t_pres, t_final)           # Presentation -> Final Approval