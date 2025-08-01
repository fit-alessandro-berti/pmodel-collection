# Generated from: 2a5cbb7d-29a0-4ff4-83a5-322326c38bf7.json
# Description: This process involves the design, sourcing, and assembly of custom drones tailored for specialized industrial applications such as agriculture, surveillance, and delivery. It begins with client requirement analysis, followed by prototype design and iterative testing. Components are sourced globally through a vetting process ensuring quality and compliance. Skilled technicians perform modular assembly, integrating avionics, propulsion, and sensor systems. Each unit undergoes rigorous calibration, flight simulation, and safety validation. The process concludes with packaging, client training, and after-sales support planning to ensure optimal operational performance and client satisfaction.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the individual activities
cb = Transition(label='Client Brief')
dd = Transition(label='Draft Design')
pb = Transition(label='Prototype Build')
it = Transition(label='Initial Testing')
dr = Transition(label='Design Revision')
cs = Transition(label='Component Sourcing')
sv = Transition(label='Supplier Vetting')
fa = Transition(label='Final Assembly')
si = Transition(label='System Integration')
cal = Transition(label='Calibration Setup')
fs = Transition(label='Flight Simulation')
sc = Transition(label='Safety Check')
pp = Transition(label='Packaging Prep')
ct = Transition(label='Client Training')
ss = Transition(label='Support Setup')

# Build the loop for prototype build & testing with possible design revision
loop_body = StrictPartialOrder(nodes=[pb, it])
loop_body.order.add_edge(pb, it)

iterative_testing = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, dr])

# Assemble the full process as a partial order
root = StrictPartialOrder(
    nodes=[cb, dd, iterative_testing,
           cs, sv,
           fa, si,
           cal, fs, sc,
           pp, ct, ss]
)

# Define the sequencing
root.order.add_edge(cb, dd)
root.order.add_edge(dd, iterative_testing)
root.order.add_edge(iterative_testing, cs)
root.order.add_edge(cs, sv)
root.order.add_edge(sv, fa)
root.order.add_edge(fa, si)
root.order.add_edge(si, cal)
root.order.add_edge(cal, fs)
root.order.add_edge(fs, sc)
root.order.add_edge(sc, pp)
root.order.add_edge(pp, ct)
root.order.add_edge(ct, ss)