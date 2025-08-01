# Generated from: 2ab236de-c4e7-47ed-8484-49412bb1ded9.json
# Description: This process involves the detailed restoration of ancient artifacts discovered during archaeological digs. It requires initial assessment of artifact condition, cleaning using specialized chemical and mechanical methods, structural stabilization with reversible adhesives, pigment analysis through spectroscopy, digital reconstruction for visualization, and finally, controlled environment packaging to ensure long-term preservation. Each step demands meticulous documentation and quality checks to maintain historical integrity and scientific accuracy while enabling future research and exhibition possibilities.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all atomic activities
IA   = Transition(label='Initial Assessment')
SC   = Transition(label='Surface Cleaning')
CW   = Transition(label='Chemical Wash')
MC   = Transition(label='Mechanical Cleaning')
DM   = Transition(label='Damage Mapping')
CR   = Transition(label='Condition Reporting')
AA   = Transition(label='Adhesive Application')
SR   = Transition(label='Structural Repair')
PA   = Transition(label='Pigment Analysis')
MT   = Transition(label='Material Testing')
DS   = Transition(label='Digital Scan')
REC3 = Transition(label='3D Reconstruction')
QR   = Transition(label='Quality Review')
PP   = Transition(label='Packaging Prep')
CC   = Transition(label='Climate Control')
FD   = Transition(label='Final Documentation')

# Surface cleaning is done by two concurrent methods
cleaning = StrictPartialOrder(
    nodes=[SC, CW, MC]
)
cleaning.order.add_edge(SC, CW)
cleaning.order.add_edge(SC, MC)

# Structural stabilization: apply adhesive, then repair
stabilization = StrictPartialOrder(
    nodes=[AA, SR]
)
stabilization.order.add_edge(AA, SR)

# Scientific testing: pigment analysis and material testing can run in parallel
testing = StrictPartialOrder(
    nodes=[PA, MT]
)

# Assemble the overall process
root = StrictPartialOrder(
    nodes=[IA,
           cleaning,
           DM,
           CR,
           stabilization,
           testing,
           DS,
           REC3,
           QR,
           PP,
           CC,
           FD]
)

# Define the high‐level sequencing
root.order.add_edge(IA,    cleaning)
root.order.add_edge(cleaning, DM)
root.order.add_edge(DM,    CR)
root.order.add_edge(CR,    stabilization)
root.order.add_edge(stabilization, testing)
root.order.add_edge(testing, DS)
root.order.add_edge(DS,    REC3)
root.order.add_edge(REC3,  QR)
root.order.add_edge(QR,    PP)
root.order.add_edge(PP,    CC)
root.order.add_edge(CC,    FD)