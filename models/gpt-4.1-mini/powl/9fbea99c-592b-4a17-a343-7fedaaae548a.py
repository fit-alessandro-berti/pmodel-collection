# Generated from: 9fbea99c-592b-4a17-a343-7fedaaae548a.json
# Description: This process involves rapidly restoring disrupted supply chains following unexpected global crises such as natural disasters, geopolitical conflicts, or pandemics. It requires cross-functional coordination to assess damage, identify alternate suppliers, reroute logistics, and ensure compliance with emergency regulations. Continuous risk monitoring and stakeholder communication are crucial to adapt strategies as conditions evolve. The process also incorporates contingency financing, technology deployment for real-time tracking, and post-crisis analysis to strengthen future resilience, making it a complex and dynamic recovery operation atypical in routine supply management.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Damage_Assess = Transition(label='Damage Assess')
Risk_Monitor = Transition(label='Risk Monitor')
Supplier_Vet = Transition(label='Supplier Vet')
Alternate_Source = Transition(label='Alternate Source')
Compliance_Check = Transition(label='Compliance Check')
Logistics_Reroute = Transition(label='Logistics Reroute')
Emergency_Finance = Transition(label='Emergency Finance')
Stakeholder_Sync = Transition(label='Stakeholder Sync')
Tech_Deploy = Transition(label='Tech Deploy')
Inventory_Audit = Transition(label='Inventory Audit')
Transport_Secure = Transition(label='Transport Secure')
Customs_Expedite = Transition(label='Customs Expedite')
Demand_Forecast = Transition(label='Demand Forecast')
Communication_Plan = Transition(label='Communication Plan')
Post_Crisis_Review = Transition(label='Post-Crisis Review')

# Define partial order for the initial assessment and vetting:
# Damage Assess --> Supplier Vet and Compliance Check concurrent after Damage Assess
# Supplier Vet and Compliance Check run in parallel after Damage Assess
# Alternate Source depends on Supplier Vet
# Logistics Reroute depends on Compliance Check
# Emergency Finance depends on the completion of Alternate Source and Logistics Reroute

# Combine Supplier Vet and Compliance Check in parallel after Damage Assess
# Similarly, Stakeholder Sync, Tech Deploy, and Demand Forecast run concurrently after Emergency Finance

# Communication Plan and Risk Monitor run continuously in a loop together
# Post Crisis Review after all main activities

# Loop to model continuous Risk Monitor and Communication Plan
monitor_comm_loop = OperatorPOWL(operator=Operator.LOOP, children=[Risk_Monitor, Communication_Plan])

# Partial order of initial assessment and vetting
initial_po = StrictPartialOrder(nodes=[
    Damage_Assess,
    Supplier_Vet,
    Compliance_Check,
    Alternate_Source,
    Logistics_Reroute,
    Emergency_Finance,
    Stakeholder_Sync,
    Tech_Deploy,
    Demand_Forecast,
    Inventory_Audit,
    Transport_Secure,
    Customs_Expedite,
    Post_Crisis_Review,
    monitor_comm_loop
])

# Define edges (dependencies)

# Damage Assess --> Supplier Vet, Compliance Check
initial_po.order.add_edge(Damage_Assess, Supplier_Vet)
initial_po.order.add_edge(Damage_Assess, Compliance_Check)

# Supplier Vet --> Alternate Source
initial_po.order.add_edge(Supplier_Vet, Alternate_Source)

# Compliance Check --> Logistics Reroute
initial_po.order.add_edge(Compliance_Check, Logistics_Reroute)

# Alternate Source and Logistics Reroute --> Emergency Finance
initial_po.order.add_edge(Alternate_Source, Emergency_Finance)
initial_po.order.add_edge(Logistics_Reroute, Emergency_Finance)

# Emergency Finance --> Stakeholder Sync, Tech Deploy, Demand Forecast (concurrent)
initial_po.order.add_edge(Emergency_Finance, Stakeholder_Sync)
initial_po.order.add_edge(Emergency_Finance, Tech_Deploy)
initial_po.order.add_edge(Emergency_Finance, Demand_Forecast)

# Stakeholder Sync, Tech Deploy, Demand Forecast --> Inventory Audit, Transport Secure, Customs Expedite (all concurrent)
initial_po.order.add_edge(Stakeholder_Sync, Inventory_Audit)
initial_po.order.add_edge(Tech_Deploy, Inventory_Audit)
initial_po.order.add_edge(Demand_Forecast, Inventory_Audit)

initial_po.order.add_edge(Stakeholder_Sync, Transport_Secure)
initial_po.order.add_edge(Tech_Deploy, Transport_Secure)
initial_po.order.add_edge(Demand_Forecast, Transport_Secure)

initial_po.order.add_edge(Stakeholder_Sync, Customs_Expedite)
initial_po.order.add_edge(Tech_Deploy, Customs_Expedite)
initial_po.order.add_edge(Demand_Forecast, Customs_Expedite)

# After these audits and securing activities, post crisis review occurs
initial_po.order.add_edge(Inventory_Audit, Post_Crisis_Review)
initial_po.order.add_edge(Transport_Secure, Post_Crisis_Review)
initial_po.order.add_edge(Customs_Expedite, Post_Crisis_Review)

# The loop (Risk Monitor, Communication Plan) can be concurrent with Emergency Finance and subsequent activities,
# we add edges to prevent deadlock and ensure loop runs continuously but does not constrain critical path

# To express concurrency and partial ordering, add edges from loop to Emergency Finance and Post Crisis Review to model coordination
initial_po.order.add_edge(monitor_comm_loop, Emergency_Finance)
initial_po.order.add_edge(Post_Crisis_Review, monitor_comm_loop)  # loop can restart or end after Post Crisis Review

# Save the final root node
root = initial_po