# Generated from: 6aa15e3d-b314-4b3e-aa3a-1fb199de8173.json
# Description: This process manages the complex sequence of activities involved in the global return and refurbishment of electronic devices. It begins with customer return initiation, followed by multi-modal transportation coordination to centralized refurbishment hubs. The process includes quality assessment, component harvesting, data sanitization, and environmental compliance checks. Refurbished units are then repackaged and redistributed through secondary markets or donation programs. The process ensures traceability, cost optimization, and regulatory adherence across diverse jurisdictions while minimizing environmental impact and maximizing asset recovery value.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# define activities
RI = Transition(label='Return Initiation')
TS = Transition(label='Transport Scheduling')
CC = Transition(label='Customs Clearance')
IS = Transition(label='Inbound Sorting')
QC = Transition(label='Quality Check')
DW = Transition(label='Data Wiping')
CH = Transition(label='Component Harvest')
CA = Transition(label='Compliance Audit')
R  = Transition(label='Refurbishment')
P  = Transition(label='Packaging')
IU = Transition(label='Inventory Update')
SS = Transition(label='Secondary Sales')
DH = Transition(label='Donation Handling')
WD = Transition(label='Waste Disposal')
RP = Transition(label='Reporting')

# parallel quality/data/component/compliance & waste-disposal after harvest
po_pre = StrictPartialOrder(nodes=[QC, DW, CH, CA, WD])
po_pre.order.add_edge(CH, WD)

# sequential refurbishment, packaging, inventory update
po_post = StrictPartialOrder(nodes=[R, P, IU])
po_post.order.add_edge(R, P)
po_post.order.add_edge(P, IU)

# choice between sales and donation
choice = OperatorPOWL(operator=Operator.XOR, children=[SS, DH])

# overall workflow
root = StrictPartialOrder(nodes=[RI, TS, CC, IS, po_pre, po_post, choice, RP])
root.order.add_edge(RI, TS)
root.order.add_edge(TS, CC)
root.order.add_edge(CC, IS)
root.order.add_edge(IS, po_pre)
root.order.add_edge(po_pre, po_post)
root.order.add_edge(po_post, choice)
root.order.add_edge(choice, RP)