# Generated from: 28032bcd-8cff-4dc1-8213-287b4e850e03.json
# Description: This process details the end-to-end workflow of exporting artisanal cheese from small-scale farms to international gourmet markets. It involves curating unique cheese varieties, obtaining health certifications, managing cold chain logistics, coordinating with customs brokers, and ensuring compliance with varying import regulations across countries. The process also includes marketing strategies tailored to niche markets, packaging design to maintain freshness and brand identity, and post-delivery feedback collection to continuously improve product quality and customer satisfaction. Special attention is given to traceability and sustainability certifications to meet modern consumer expectations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Farm_Selection = Transition(label='Farm Selection')
Milk_Testing = Transition(label='Milk Testing')
Cheese_Aging = Transition(label='Cheese Aging')
Quality_Check = Transition(label='Quality Check')
Health_Certify = Transition(label='Health Certify')
Packaging_Design = Transition(label='Packaging Design')
Label_Approval = Transition(label='Label Approval')
Cold_Storage = Transition(label='Cold Storage')
Customs_Filing = Transition(label='Customs Filing')
Transport_Booking = Transition(label='Transport Booking')
Export_Negotiation = Transition(label='Export Negotiation')
Market_Research = Transition(label='Market Research')
Order_Processing = Transition(label='Order Processing')
Customer_Outreach = Transition(label='Customer Outreach')
Feedback_Review = Transition(label='Feedback Review')
Sustainability_Audit = Transition(label='Sustainability Audit')

# Define partial orders for key process segments

# Cheese production chain: Farm Selection -> Milk Testing -> Cheese Aging -> Quality Check
prod_chain = StrictPartialOrder(nodes=[Farm_Selection, Milk_Testing, Cheese_Aging, Quality_Check])
prod_chain.order.add_edge(Farm_Selection, Milk_Testing)
prod_chain.order.add_edge(Milk_Testing, Cheese_Aging)
prod_chain.order.add_edge(Cheese_Aging, Quality_Check)

# Health and sustainability certifications proceed after quality check
certifications = StrictPartialOrder(nodes=[Health_Certify, Sustainability_Audit])
# They can be done in parallel, no order edges

# Packaging design and label approval run sequentially after certifications
packaging = StrictPartialOrder(nodes=[Packaging_Design, Label_Approval])
packaging.order.add_edge(Packaging_Design, Label_Approval)

# Logistics and export: Cold Storage -> Customs Filing -> Transport Booking -> Export Negotiation
logistics = StrictPartialOrder(nodes=[Cold_Storage, Customs_Filing, Transport_Booking, Export_Negotiation])
logistics.order.add_edge(Cold_Storage, Customs_Filing)
logistics.order.add_edge(Customs_Filing, Transport_Booking)
logistics.order.add_edge(Transport_Booking, Export_Negotiation)

# Market research and order processing run concurrently, then customer outreach, then feedback review
market_and_orders = StrictPartialOrder(nodes=[Market_Research, Order_Processing, Customer_Outreach, Feedback_Review])
market_and_orders.order.add_edge(Market_Research, Customer_Outreach)
market_and_orders.order.add_edge(Order_Processing, Customer_Outreach)
market_and_orders.order.add_edge(Customer_Outreach, Feedback_Review)

# Combine certifications and packaging in a partial order: Certifications -> Packaging chain
cert_pack = StrictPartialOrder(nodes=[certifications, packaging])
cert_pack.order.add_edge(certifications, packaging)

# Combine prod_chain -> cert_pack -> logistics -> market_and_orders
root = StrictPartialOrder(nodes=[prod_chain, cert_pack, logistics, market_and_orders])
root.order.add_edge(prod_chain, cert_pack)
root.order.add_edge(cert_pack, logistics)
root.order.add_edge(logistics, market_and_orders)