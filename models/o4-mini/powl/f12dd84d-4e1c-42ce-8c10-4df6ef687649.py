# Generated from: f12dd84d-4e1c-42ce-8c10-4df6ef687649.json
# Description: This process outlines the intricate supply chain and quality assurance workflow for artisan cheese production, starting from sourcing rare raw milk varieties to aging in controlled environments. It includes activities such as microbial testing, traditional curdling, seasonal staff coordination, and niche market distribution. The process also covers sustainable packaging decisions, traceability logging, and customer feedback integration to maintain authenticity and meet artisanal standards while navigating regulatory compliance and fluctuating seasonal yields.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
milk             = Transition(label='Milk Sourcing')
qt               = Transition(label='Quality Testing')
curd             = Transition(label='Curd Processing')
salt             = Transition(label='Salt Application')
mold             = Transition(label='Mold Inoculation')
press            = Transition(label='Press Molding')
brine            = Transition(label='Brine Soaking')
aging            = Transition(label='Aging Setup')
humidity         = Transition(label='Humidity Control')
micro            = Transition(label='Microbial Check')
pkg              = Transition(label='Packaging Design')
label            = Transition(label='Label Printing')
saudit           = Transition(label='Sustainability Audit')
trace            = Transition(label='Trace Logging')
dist             = Transition(label='Distribution Plan')
review           = Transition(label='Customer Review')
inventory        = Transition(label='Inventory Audit')

# Silent transitions for choice and loop rework
skip_choice      = SilentTransition()
retry            = SilentTransition()

# Body of the QC loop: from Quality Testing through Microbial Check
body_proc = StrictPartialOrder(nodes=[
    qt, curd, salt, mold, press, brine, aging, humidity, micro
])
body_proc.order.add_edge(qt,      curd)
body_proc.order.add_edge(curd,    salt)
body_proc.order.add_edge(salt,    mold)
body_proc.order.add_edge(mold,    press)
body_proc.order.add_edge(press,   brine)
body_proc.order.add_edge(brine,   aging)
body_proc.order.add_edge(aging,   humidity)
body_proc.order.add_edge(humidity, micro)

# LOOP: repeat the QC body if 'retry' happens, else exit
qc_loop = OperatorPOWL(operator=Operator.LOOP, children=[body_proc, retry])

# XOR: optional sustainability audit before proceeding
xor_sustain = OperatorPOWL(operator=Operator.XOR, children=[saudit, skip_choice])

# Assemble the full workflow as a partial order
root = StrictPartialOrder(nodes=[
    milk, qc_loop, pkg, label, xor_sustain,
    trace, dist, review, inventory
])
root.order.add_edge(milk,       qc_loop)
root.order.add_edge(qc_loop,    pkg)
root.order.add_edge(pkg,        label)
root.order.add_edge(label,      xor_sustain)
root.order.add_edge(xor_sustain, trace)
root.order.add_edge(trace,      dist)
# After distribution two activities can proceed in parallel:
root.order.add_edge(dist,       review)
root.order.add_edge(dist,       inventory)