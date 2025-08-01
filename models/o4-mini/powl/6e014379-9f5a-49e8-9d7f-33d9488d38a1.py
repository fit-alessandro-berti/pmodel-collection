# Generated from: 6e014379-9f5a-49e8-9d7f-33d9488d38a1.json
# Description: This process manages the complex coordination of loaning valuable art pieces between multiple international museums and private collectors. It involves provenance verification, condition reporting, diplomatic clearance, insurance arrangements, logistical planning for secure transport, installation oversight, exhibition scheduling, and post-loan audits. The process requires collaboration between curators, legal teams, conservators, transport specialists, and financial departments to ensure artworks are safely and legally moved, displayed, and returned, maintaining cultural heritage integrity and compliance with international laws.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# Define all transitions
verify = Transition(label='Verify Provenance')
assess = Transition(label='Assess Condition')
draft = Transition(label='Draft Contract')
clearance = Transition(label='Obtain Clearance')
insurance = Transition(label='Arrange Insurance')
schedule = Transition(label='Schedule Transport')
pack = Transition(label='Pack Artwork')
track = Transition(label='Track Shipment')
install = Transition(label='Install Exhibit')
monitor = Transition(label='Monitor Environment')
tours = Transition(label='Conduct Tours')
queries = Transition(label='Handle Queries')
deinstall = Transition(label='Deinstall Art')
return_shipment = Transition(label='Return Shipment')
audit = Transition(label='Audit Records')
feedback = Transition(label='Review Feedback')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    verify, assess,
    draft, clearance, insurance,
    schedule, pack, track,
    install, monitor, tours, queries,
    deinstall, return_shipment,
    audit, feedback
])

# Provenance before condition
root.order.add_edge(verify, assess)

# After condition, three parallel admin tasks
for admin in (draft, clearance, insurance):
    root.order.add_edge(assess, admin)

# Once all admin tasks are done, schedule transport
for admin in (draft, clearance, insurance):
    root.order.add_edge(admin, schedule)

# Schedule → Pack → Track → Install
root.order.add_edge(schedule, pack)
root.order.add_edge(pack, track)
root.order.add_edge(track, install)

# After installation, monitoring, tours, and queries run in parallel
for task in (monitor, tours, queries):
    root.order.add_edge(install, task)

# Once exhibition activities finish, deinstallation
for task in (monitor, tours, queries):
    root.order.add_edge(task, deinstall)

# Deinstall → Return → Audit & Feedback
root.order.add_edge(deinstall, return_shipment)
root.order.add_edge(return_shipment, audit)
root.order.add_edge(return_shipment, feedback)