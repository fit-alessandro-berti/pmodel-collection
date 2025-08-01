# Generated from: c8a5d28f-ffc6-4a17-82b2-16abf23b7f08.json
# Description: This process involves the intricate steps required to produce, certify, package, and export artisanal cheese internationally. Starting from raw milk sourcing from specific breeds, it includes quality testing, controlled fermentation, aging under precise conditions, and sensory evaluation. Following production, the process entails obtaining health certifications, custom labeling, cold-chain packaging, and coordinating with logistics partners specialized in perishable goods. Regulatory compliance checks, export documentation, tariff classification, and final customs clearance are integral. Post-shipment tracking and feedback collection from international clients complete this atypical yet realistic export workflow.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
milk_sourcing    = Transition(label='Milk Sourcing')
quality_testing  = Transition(label='Quality Testing')
milk_pasteurize  = Transition(label='Milk Pasteurize')
culture_add      = Transition(label='Culture Addition')
curd_cutting     = Transition(label='Curd Cutting')
whey_drain       = Transition(label='Whey Drain')
cheese_molding   = Transition(label='Cheese Molding')
controlled_age   = Transition(label='Controlled Aging')
sensory_check    = Transition(label='Sensory Check')
health_certify   = Transition(label='Health Certify')
custom_labeling  = Transition(label='Custom Labeling')
cold_packaging   = Transition(label='Cold Packaging')
logistics_setup  = Transition(label='Logistics Setup')
export_docs      = Transition(label='Export Docs')
customs_clear    = Transition(label='Customs Clearance')
shipment_track   = Transition(label='Shipment Track')
client_feedback  = Transition(label='Client Feedback')

# Build the partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing, quality_testing, milk_pasteurize, culture_add,
    curd_cutting, whey_drain, cheese_molding, controlled_age,
    sensory_check, health_certify, custom_labeling, cold_packaging,
    logistics_setup, export_docs, customs_clear, shipment_track,
    client_feedback
])

# Production sequence
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, milk_pasteurize)
root.order.add_edge(milk_pasteurize, culture_add)
root.order.add_edge(culture_add, curd_cutting)
root.order.add_edge(curd_cutting, whey_drain)
root.order.add_edge(whey_drain, cheese_molding)
root.order.add_edge(cheese_molding, controlled_age)
root.order.add_edge(controlled_age, sensory_check)

# Certification and labeling
root.order.add_edge(sensory_check, health_certify)
root.order.add_edge(health_certify, custom_labeling)

# Parallel branches: packaging and export docs
root.order.add_edge(custom_labeling, cold_packaging)
root.order.add_edge(custom_labeling, export_docs)

# Packaging branch
root.order.add_edge(cold_packaging, logistics_setup)
# Export documents branch
root.order.add_edge(export_docs, customs_clear)

# Join before shipment
root.order.add_edge(logistics_setup, shipment_track)
root.order.add_edge(customs_clear, shipment_track)

# Final feedback
root.order.add_edge(shipment_track, client_feedback)