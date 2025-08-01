# Generated from: 6aa15e3d-b314-4b3e-aa3a-1fb199de8173.json
# Description: This process manages the complex sequence of activities involved in the global return and refurbishment of electronic devices. It begins with customer return initiation, followed by multi-modal transportation coordination to centralized refurbishment hubs. The process includes quality assessment, component harvesting, data sanitization, and environmental compliance checks. Refurbished units are then repackaged and redistributed through secondary markets or donation programs. The process ensures traceability, cost optimization, and regulatory adherence across diverse jurisdictions while minimizing environmental impact and maximizing asset recovery value.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Return_Initiation = Transition(label='Return Initiation')
Transport_Scheduling = Transition(label='Transport Scheduling')
Customs_Clearance = Transition(label='Customs Clearance')
Inbound_Sorting = Transition(label='Inbound Sorting')
Quality_Check = Transition(label='Quality Check')
Data_Wiping = Transition(label='Data Wiping')
Component_Harvest = Transition(label='Component Harvest')
Compliance_Audit = Transition(label='Compliance Audit')
Refurbishment = Transition(label='Refurbishment')
Packaging = Transition(label='Packaging')
Inventory_Update = Transition(label='Inventory Update')
Secondary_Sales = Transition(label='Secondary Sales')
Donation_Handling = Transition(label='Donation Handling')
Waste_Disposal = Transition(label='Waste Disposal')
Reporting = Transition(label='Reporting')

# Create choice for post-packaging options: Secondary Sales or Donation Handling
post_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[Secondary_Sales, Donation_Handling, Waste_Disposal])

# Partial order modeling main flow:

# 1. Return Initiation --> Transport Scheduling --> Customs Clearance --> Inbound Sorting
# 2. Inbound Sorting --> Quality Check
# 3. Quality Check --> three concurrent activities:
#    - Data Wiping --> Compliance Audit
#    - Component Harvest
#    - Compliance Audit (from Data Wiping path)
# To model concurrency of Component Harvest and Data Wiping+Compliance Audit, we include them as concurrent nodes.
# After compliance audit and component harvest, both must finish before Refurbishment
# Then Packaging --> Inventory Update --> choice (Secondary Sales, Donation Handling, Waste Disposal)
# Finally Reporting

# nodes
nodes = [
    Return_Initiation,
    Transport_Scheduling,
    Customs_Clearance,
    Inbound_Sorting,
    Quality_Check,
    Data_Wiping,
    Component_Harvest,
    Compliance_Audit,
    Refurbishment,
    Packaging,
    Inventory_Update,
    post_packaging_choice,
    Reporting
]

root = StrictPartialOrder(nodes=nodes)

# Add edges for sequence
root.order.add_edge(Return_Initiation, Transport_Scheduling)
root.order.add_edge(Transport_Scheduling, Customs_Clearance)
root.order.add_edge(Customs_Clearance, Inbound_Sorting)
root.order.add_edge(Inbound_Sorting, Quality_Check)

# Quality Check leads to Data Wiping and Component Harvest concurrently,
# but Compliance Audit depends on Data Wiping finishing
root.order.add_edge(Quality_Check, Data_Wiping)
root.order.add_edge(Quality_Check, Component_Harvest)
root.order.add_edge(Data_Wiping, Compliance_Audit)

# Refurbishment depends on Component Harvest and Compliance Audit both finishing
root.order.add_edge(Component_Harvest, Refurbishment)
root.order.add_edge(Compliance_Audit, Refurbishment)

# Then continue
root.order.add_edge(Refurbishment, Packaging)
root.order.add_edge(Packaging, Inventory_Update)
root.order.add_edge(Inventory_Update, post_packaging_choice)

# The choice leads to Reporting regardless of choice taken
root.order.add_edge(post_packaging_choice, Reporting)