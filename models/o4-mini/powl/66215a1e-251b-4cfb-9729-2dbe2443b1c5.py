# Generated from: 66215a1e-251b-4cfb-9729-2dbe2443b1c5.json
# Description: This process outlines the end-to-end supply chain for artisan cheese production, starting from sourcing rare milk varieties from select farms, through specialized fermentation and aging techniques in unique microclimates, to customized packaging and niche market distribution. It involves seasonal ingredient adjustments, quality audits at multiple stages, collaboration with local artisans for flavor profiling, and direct-to-consumer subscription management. Unexpected factors such as weather impacts on milk quality and regulatory checks for raw milk cheeses are integrated to ensure compliance and product excellence throughout the chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
M            = Transition(label='Milk Sourcing')
QT           = Transition(label='Quality Testing')
PCulture     = Transition(label='Starter Culture')
MPaste       = Transition(label='Milk Pasteurize')
CCut         = Transition(label='Curd Cutting')
WDrain       = Transition(label='Whey Draining')
PPress       = Transition(label='Pressing Cheese')
ACtrl        = Transition(label='Aging Control')
MCCheck      = Transition(label='Microclimate Check')
FProfile     = Transition(label='Flavor Profiling')
PDesign      = Transition(label='Packaging Design')
LPrint       = Transition(label='Label Printing')
RAudit       = Transition(label='Regulatory Audit')
OProcess     = Transition(label='Order Processing')
SSetup       = Transition(label='Subscription Setup')
DSched       = Transition(label='Delivery Scheduling')
CFeedback    = Transition(label='Customer Feedback')

# Silent transitions for choices
skip_reg     = SilentTransition()
skip_flavor  = SilentTransition()

# 1) Seasonal ingredient adjustment loop: do QA then possibly re-culture until OK
seasonal_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[QT, PCulture]
)

# 2) Optional regulatory audit after QA
xor_reg = OperatorPOWL(
    operator=Operator.XOR,
    children=[RAudit, skip_reg]
)

# 3) Aging control with possible microclimate re-check
aging_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[ACtrl, MCCheck]
)

# 4) Optional flavor profiling
xor_flavor = OperatorPOWL(
    operator=Operator.XOR,
    children=[FProfile, skip_flavor]
)

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    M,
    PCulture,
    seasonal_loop,
    xor_reg,
    MPaste,
    CCut,
    WDrain,
    PPress,
    aging_loop,
    xor_flavor,
    PDesign,
    LPrint,
    OProcess,
    SSetup,
    DSched,
    CFeedback
])

# Add control‐flow edges
root.order.add_edge(M,           PCulture)
root.order.add_edge(PCulture,    seasonal_loop)
root.order.add_edge(seasonal_loop, xor_reg)
root.order.add_edge(xor_reg,     MPaste)
root.order.add_edge(MPaste,      CCut)
root.order.add_edge(CCut,        WDrain)
root.order.add_edge(WDrain,      PPress)
root.order.add_edge(PPress,      aging_loop)
root.order.add_edge(aging_loop,  xor_flavor)
root.order.add_edge(xor_flavor,  PDesign)
root.order.add_edge(PDesign,     LPrint)

# Packaging leads to both order processing and subscription setup (concurrent)
root.order.add_edge(LPrint,      OProcess)
root.order.add_edge(LPrint,      SSetup)

# Both must complete before delivery scheduling
root.order.add_edge(OProcess,    DSched)
root.order.add_edge(SSetup,      DSched)

# Finally, customer feedback
root.order.add_edge(DSched,      CFeedback)