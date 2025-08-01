# Generated from: b336605e-7b9d-44f9-a850-8b35bf42cad7.json
# Description: This process manages the licensing of digital artifacts that are dynamically created and modified based on user interactions and environmental conditions. It involves capturing artifact metadata, verifying usage rights in real-time, negotiating adaptive license terms with multiple stakeholders, executing smart contracts, monitoring ongoing compliance through automated audits, and dynamically updating license conditions as artifacts evolve. The process ensures secure distribution, handles dispute resolution via decentralized arbitration, and integrates with external content management systems to synchronize license statuses. It also involves periodic reporting to licensors and licensees, enabling transparent usage tracking and payment settlements based on actual consumption patterns. This atypical licensing workflow combines legal, technical, and operational activities to support continuously changing digital assets in a robust, scalable, and compliant manner.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
cap    = Transition(label='Capture Metadata')
ver    = Transition(label='Verify Rights')
neg    = Transition(label='Negotiate Terms')
exe    = Transition(label='Execute Contract')
dist   = Transition(label='Distribute Artifact')
sync   = Transition(label='Sync Systems')
mon    = Transition(label='Monitor Usage')
aud    = Transition(label='Audit Compliance')
upd    = Transition(label='Update License')
res    = Transition(label='Resolve Disputes')
track  = Transition(label='Track Consumption')
pay    = Transition(label='Process Payments')
rep    = Transition(label='Generate Reports')
notif  = Transition(label='Notify Stakeholders')
arch   = Transition(label='Archive Records')
rev    = Transition(label='Review Feedback')
adj    = Transition(label='Adjust Pricing')

# Build the dispute‐aware audit/update choice:
# Option 1: straight audit -> update
po_simple = StrictPartialOrder(nodes=[aud, upd])
po_simple.order.add_edge(aud, upd)

# Option 2: dispute resolution -> audit -> update
po_with_dispute = StrictPartialOrder(nodes=[res, aud, upd])
po_with_dispute.order.add_edge(res, aud)
po_with_dispute.order.add_edge(aud, upd)

# Exclusive choice between simple compliance update or involving dispute resolution
conflict_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[po_simple, po_with_dispute]
)

# Loop: continuously monitor usage then do one compliance/update iteration
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[mon, conflict_choice]
)

# Assemble the top‐level partial order
root = StrictPartialOrder(nodes=[
    cap, ver, neg, exe,
    dist, sync,
    loop,
    track, pay, rep, notif,
    arch, rev, adj
])

# Define the control‐flow edges
root.order.add_edge(cap,   ver)
root.order.add_edge(ver,   neg)
root.order.add_edge(neg,   exe)
root.order.add_edge(exe,   dist)
root.order.add_edge(dist,  sync)

# After syncing, start monitoring‐loop and start consumption/payment/reporting in parallel
root.order.add_edge(sync,  loop)
root.order.add_edge(sync,  track)
root.order.add_edge(track, pay)
root.order.add_edge(pay,   rep)
root.order.add_edge(pay,   notif)

# Final archiving and review steps
root.order.add_edge(rep,   arch)
root.order.add_edge(notif, arch)
root.order.add_edge(arch,  rev)
root.order.add_edge(rev,   adj)