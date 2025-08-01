# Generated from: e16455eb-0f7a-43f6-9556-450f96ca92fa.json
# Description: This process outlines the complex coordination required to manage the international loan of high-value artwork between museums. It involves verifying provenance, arranging climate-controlled transport, managing customs clearance, coordinating insurance coverage, scheduling installation by specialized handlers, monitoring environmental conditions during display, facilitating scholarly access, and overseeing secure return logistics. Each step demands meticulous attention to legal, logistical, and conservation requirements to ensure the artwork's integrity and compliance with international cultural property laws throughout the loan period.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
VP = Transition(label='Verify Provenance')
AC = Transition(label='Assess Condition')
NT = Transition(label='Negotiate Terms')
AT = Transition(label='Arrange Transport')
CC = Transition(label='Customs Clearance')
SI = Transition(label='Secure Insurance')
SH = Transition(label='Schedule Handlers')
IA = Transition(label='Install Artwork')
Mon = Transition(label='Monitor Climate')
Sec = Transition(label='Manage Security')
Fac = Transition(label='Facilitate Access')
Doc = Transition(label='Document Display')
Evt = Transition(label='Coordinate Events')
IP = Transition(label='Inspect Periodically')
PR = Transition(label='Plan Return')
DA = Transition(label='Deinstall Artwork')
FR = Transition(label='Finalize Reports')

# Concurrent display‐period activities
PO_display = StrictPartialOrder(nodes=[Mon, Sec, Fac, Doc, Evt])
# No edges added ⇒ they all execute in parallel during the display period

# Loop: perform one display period, then either exit or inspect and loop again
loop_display = OperatorPOWL(
    operator=Operator.LOOP,
    children=[PO_display, IP]
)

# Build the overall process as a strict partial order
root = StrictPartialOrder(
    nodes=[VP, AC, NT, AT, CC, SI, SH, IA, loop_display, PR, DA, FR]
)

# Add the sequencing edges
root.order.add_edge(VP, AC)
root.order.add_edge(AC, NT)
root.order.add_edge(NT, AT)
root.order.add_edge(AT, CC)
root.order.add_edge(CC, SI)
root.order.add_edge(SI, SH)
root.order.add_edge(SH, IA)
root.order.add_edge(IA, loop_display)
root.order.add_edge(loop_display, PR)
root.order.add_edge(PR, DA)
root.order.add_edge(DA, FR)