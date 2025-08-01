# Generated from: 57c7532b-52b1-4519-bb87-602a34507822.json
# Description: This process outlines the intricate supply chain of artisan cheese production, from sourcing rare milk varieties from remote farms to aging cheese in specialized microclimates. It involves quality testing at multiple stages, customized packaging based on cheese type, coordinating with boutique retailers, managing seasonal demand fluctuations, and ensuring traceability for food safety compliance. The process also includes collaborative recipe refinement with cheesemakers, digital inventory reconciliation, and international shipping logistics under controlled temperature conditions to maintain product integrity and enhance customer satisfaction in niche markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ms = Transition(label='Milk Sourcing')
qt = Transition(label='Quality Testing')
rr = Transition(label='Recipe Refinement')
curd = Transition(label='Curd Formation')
press = Transition(label='Pressing Cheese')
salt = Transition(label='Salting Stage')
aging_setup = Transition(label='Aging Setup')
mc = Transition(label='Microclimate Control')
temp = Transition(label='Temperature Monitor')
inv = Transition(label='Inventory Check')
pd = Transition(label='Packaging Design')
lp = Transition(label='Label Printing')
op = Transition(label='Order Processing')
rc = Transition(label='Retail Coordination')
sp = Transition(label='Shipping Prep')
ca = Transition(label='Compliance Audit')
sf = Transition(label='Sales Feedback')
df = Transition(label='Demand Forecast')

# Build the loop for collaborative recipe refinement with demand feedback
# B-part: Sales Feedback -> Demand Forecast
b_loop = StrictPartialOrder(nodes=[sf, df])
b_loop.order.add_edge(sf, df)
# LOOP operator: A = Recipe Refinement, B = feedback subprocess
loop_recipe = OperatorPOWL(operator=Operator.LOOP, children=[rr, b_loop])

# Build the loop for aging under microclimate control and periodic temperature monitoring
mc_loop = OperatorPOWL(operator=Operator.LOOP, children=[mc, temp])

# Build the packaging subprocess: Packaging Design -> Label Printing
packaging_sub = StrictPartialOrder(nodes=[pd, lp])
packaging_sub.order.add_edge(pd, lp)

# Assemble the top‐level partial order
root = StrictPartialOrder(nodes=[
    ms, qt, loop_recipe,
    curd, press, salt,
    aging_setup, mc_loop,
    inv, packaging_sub,
    op, rc, sp, temp, ca
])

# Define the control‐flow dependencies
root.order.add_edge(ms, qt)
root.order.add_edge(qt, loop_recipe)
root.order.add_edge(loop_recipe, curd)
root.order.add_edge(curd, press)
root.order.add_edge(press, salt)
root.order.add_edge(salt, aging_setup)
root.order.add_edge(aging_setup, mc_loop)
root.order.add_edge(mc_loop, inv)
# Inventory Check and Packaging subprocess run concurrently, then both feed into Order Processing
root.order.add_edge(inv, op)
root.order.add_edge(packaging_sub, op)
root.order.add_edge(op, rc)
root.order.add_edge(rc, sp)
root.order.add_edge(sp, temp)
root.order.add_edge(temp, ca)