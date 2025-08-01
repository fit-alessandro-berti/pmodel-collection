# Generated from: e16455eb-0f7a-43f6-9556-450f96ca92fa.json
# Description: This process outlines the complex coordination required to manage the international loan of high-value artwork between museums. It involves verifying provenance, arranging climate-controlled transport, managing customs clearance, coordinating insurance coverage, scheduling installation by specialized handlers, monitoring environmental conditions during display, facilitating scholarly access, and overseeing secure return logistics. Each step demands meticulous attention to legal, logistical, and conservation requirements to ensure the artwork's integrity and compliance with international cultural property laws throughout the loan period.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Verify_Provenance = Transition(label='Verify Provenance')
Assess_Condition = Transition(label='Assess Condition')
Negotiate_Terms = Transition(label='Negotiate Terms')
Arrange_Transport = Transition(label='Arrange Transport')
Customs_Clearance = Transition(label='Customs Clearance')
Secure_Insurance = Transition(label='Secure Insurance')
Schedule_Handlers = Transition(label='Schedule Handlers')
Install_Artwork = Transition(label='Install Artwork')
Monitor_Climate = Transition(label='Monitor Climate')
Manage_Security = Transition(label='Manage Security')
Facilitate_Access = Transition(label='Facilitate Access')
Document_Display = Transition(label='Document Display')
Coordinate_Events = Transition(label='Coordinate Events')
Inspect_Periodically = Transition(label='Inspect Periodically')
Plan_Return = Transition(label='Plan Return')
Deinstall_Artwork = Transition(label='Deinstall Artwork')
Finalize_Reports = Transition(label='Finalize Reports')

# Model installation and display phase as a partial order with some concurrency:
# Installation requires scheduling handlers, install artwork, then document display and coordinate events can run concurrently
installation_phase = StrictPartialOrder(nodes=[Schedule_Handlers, Install_Artwork, Document_Display, Coordinate_Events])
installation_phase.order.add_edge(Schedule_Handlers, Install_Artwork)
installation_phase.order.add_edge(Install_Artwork, Document_Display)
installation_phase.order.add_edge(Install_Artwork, Coordinate_Events)

# Display monitoring phase: monitor climate, manage security, facilitate access and inspect periodically as partly concurrent
display_monitoring = StrictPartialOrder(nodes=[Monitor_Climate, Manage_Security, Facilitate_Access, Inspect_Periodically])
# Let's allow Inspect_periodically depends on Monitor_Climate (inspection based on climate monitoring)
display_monitoring.order.add_edge(Monitor_Climate, Inspect_Periodically)

# Return phase partial order: plan return, deinstall artwork, finalize reports sequentially
return_phase = StrictPartialOrder(nodes=[Plan_Return, Deinstall_Artwork, Finalize_Reports])
return_phase.order.add_edge(Plan_Return, Deinstall_Artwork)
return_phase.order.add_edge(Deinstall_Artwork, Finalize_Reports)

# Preliminary steps partial order:
# Verify provenance and assess condition can be concurrent, but both precede negotiate terms
preliminaries = StrictPartialOrder(nodes=[Verify_Provenance, Assess_Condition, Negotiate_Terms])
preliminaries.order.add_edge(Verify_Provenance, Negotiate_Terms)
preliminaries.order.add_edge(Assess_Condition, Negotiate_Terms)

# Logistics partial order: arrange transport, customs clearance, secure insurance
# Customs clearance depends on arrange transport, secure insurance can be concurrent with customs clearance
logistics = StrictPartialOrder(nodes=[Arrange_Transport, Customs_Clearance, Secure_Insurance])
logistics.order.add_edge(Arrange_Transport, Customs_Clearance)

# Assemble the full workflow partial order:
# preliminaries precede logistics
# logistics precede installation_phase
# installation_phase precedes display_monitoring
# display_monitoring precedes return_phase

root = StrictPartialOrder(
    nodes=[preliminaries, logistics, installation_phase, display_monitoring, return_phase]
)
root.order.add_edge(preliminaries, logistics)
root.order.add_edge(logistics, installation_phase)
root.order.add_edge(installation_phase, display_monitoring)
root.order.add_edge(display_monitoring, return_phase)