# Generated from: 0118959c-dea9-49d7-b296-7aee7e449369.json
# Description: This process governs the detailed restoration of valuable antiques, combining historical research, material analysis, and delicate repair techniques to preserve authenticity while enhancing structural integrity. It involves documentation, condition assessment, sourcing period-appropriate materials, and employing specialized cleaning and consolidation methods. Experts coordinate with conservation scientists to ensure reversible interventions, aesthetic fidelity, and compliance with legal and ethical standards. The workflow also includes digital archiving of restoration stages and client consultations to balance preservation goals with market value considerations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
survey       = Transition(label="Item Survey")
history      = Transition(label="History Check")
material     = Transition(label="Material Test")
damage       = Transition(label="Damage Map")
source       = Transition(label="Source Parts")
clean        = Transition(label="Clean Surface")
consol       = Transition(label="Consolidate Wood")
stabil       = Transition(label="Stabilize Base")
repair       = Transition(label="Repair Joints")
retouch      = Transition(label="Retouch Paint")
doc          = Transition(label="Document Changes")
archive      = Transition(label="Digital Archive")
client       = Transition(label="Client Review")
legal        = Transition(label="Legal Verify")
audit        = Transition(label="Quality Audit")
final_polish = Transition(label="Final Polish")
shipping     = Transition(label="Shipping Prep")

# Build the restoration unit (sequence of refinement actions)
restorationUnit = StrictPartialOrder(
    nodes=[clean, consol, stabil, repair, retouch]
)
restorationUnit.order.add_edge(clean, consol)
restorationUnit.order.add_edge(consol, stabil)
restorationUnit.order.add_edge(stabil, repair)
restorationUnit.order.add_edge(repair, retouch)

# Build the review phase (sequence of documentation & review)
reviewPhase = StrictPartialOrder(
    nodes=[doc, archive, client, legal, audit]
)
reviewPhase.order.add_edge(doc, archive)
reviewPhase.order.add_edge(archive, client)
reviewPhase.order.add_edge(client, legal)
reviewPhase.order.add_edge(legal, audit)

# Create a loop: do restorationUnit, then either exit or execute reviewPhase and repeat
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[restorationUnit, reviewPhase]
)

# Assemble the full process as a partial order
root = StrictPartialOrder(
    nodes=[survey, history, material, damage, source, loop, final_polish, shipping]
)

# Specify the partial order dependencies
root.order.add_edge(survey, history)
root.order.add_edge(survey, material)
root.order.add_edge(survey, damage)

root.order.add_edge(history, source)
root.order.add_edge(material, source)
root.order.add_edge(damage, source)

root.order.add_edge(source, loop)

root.order.add_edge(loop, final_polish)
root.order.add_edge(final_polish, shipping)