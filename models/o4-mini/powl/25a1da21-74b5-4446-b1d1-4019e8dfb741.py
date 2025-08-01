# Generated from: 25a1da21-74b5-4446-b1d1-4019e8dfb741.json
# Description: This process involves the thorough authentication of historical artifacts intended for museum acquisition. It begins with preliminary provenance research, followed by multispectral imaging and material composition analysis. Specialist consultations are conducted to verify stylistic consistency. Trace element profiling and radiocarbon dating provide scientific validation. Parallelly, legal ownership checks and export compliance reviews ensure ethical acquisition. The workflow culminates in compiling a comprehensive authentication report and final approval by the acquisitions board, minimizing the risk of counterfeit or illegally sourced artifacts entering the collection.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# Define all activities as POWL transitions
pc       = Transition(label='Provenance Check')
img      = Transition(label='Image Capture')
mat      = Transition(label='Material Scan')
style    = Transition(label='Style Review')
experts  = Transition(label='Consult Experts')
elem     = Transition(label='Element Analysis')
carbon   = Transition(label='Carbon Dating')
ow       = Transition(label='Ownership Verify')
exp      = Transition(label='Export Review')
legal    = Transition(label='Legal Clearance')
integr   = Transition(label='Data Integration')
report   = Transition(label='Report Draft')
board    = Transition(label='Board Review')
final    = Transition(label='Final Approval')
archive  = Transition(label='Archive Data')

# Create the root partial order with all nodes
root = StrictPartialOrder(nodes=[
    pc, img, mat,
    style, experts,
    elem, carbon,
    ow, exp, legal,
    integr,
    report, board, final,
    archive
])

# Add ordering relations
# 1. Provenance research precedes imaging, scanning, and ethical checks
root.order.add_edge(pc, img)
root.order.add_edge(pc, mat)
root.order.add_edge(pc, ow)
root.order.add_edge(pc, exp)

# 2. Imaging & scanning precede stylistic review & expert consultation
root.order.add_edge(img, style)
root.order.add_edge(mat, style)
root.order.add_edge(img, experts)
root.order.add_edge(mat, experts)

# 3. Style review & expert consultation precede element analysis & carbon dating
root.order.add_edge(style, elem)
root.order.add_edge(experts, elem)
root.order.add_edge(style, carbon)
root.order.add_edge(experts, carbon)

# 4. Ownership verify & export review precede legal clearance
root.order.add_edge(ow, legal)
root.order.add_edge(exp, legal)

# 5. Scientific validations & legal clearance precede data integration
root.order.add_edge(elem, integr)
root.order.add_edge(carbon, integr)
root.order.add_edge(legal, integr)

# 6. Integration precedes report drafting, board review, final approval, and archiving
root.order.add_edge(integr, report)
root.order.add_edge(report, board)
root.order.add_edge(board, final)
root.order.add_edge(final, archive)