# Generated from: 451e3882-a15c-4940-9a01-32c961f404ec.json
# Description: This process describes the complex steps involved in exporting artisanal cheese from small-scale farms to international gourmet markets. It includes sourcing raw milk, ensuring compliance with health regulations, aging cheese under controlled conditions, packaging with eco-friendly materials, coordinating custom inspections, managing cold-chain logistics, and negotiating with boutique retailers abroad. The process requires meticulous quality checks, documentation for export licenses, and adapting to varying market preferences while maintaining product authenticity and traceability throughout the supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# Define all activities as POWL transitions
milk_sourcing     = Transition(label="Milk Sourcing")
quality_testing   = Transition(label="Quality Testing")
curd_formation    = Transition(label="Curd Formation")
pressing_cheese   = Transition(label="Pressing Cheese")
aging_control     = Transition(label="Aging Control")
flavor_sampling   = Transition(label="Flavor Sampling")
packaging_prep    = Transition(label="Packaging Prep")
eco_labeling      = Transition(label="Eco Labeling")
health_inspection = Transition(label="Health Inspection")
export_licensing  = Transition(label="Export Licensing")
customs_clearance = Transition(label="Customs Clearance")
cold_storage      = Transition(label="Cold Storage")
logistics_planning= Transition(label="Logistics Planning")
retail_negotiation= Transition(label="Retail Negotiation")
traceability_audit= Transition(label="Traceability Audit")
market_feedback   = Transition(label="Market Feedback")

# Build the partial‐order model
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_testing,
    curd_formation,
    pressing_cheese,
    aging_control,
    flavor_sampling,
    packaging_prep,
    eco_labeling,
    health_inspection,
    export_licensing,
    customs_clearance,
    cold_storage,
    logistics_planning,
    retail_negotiation,
    traceability_audit,
    market_feedback
])

# sequential dependencies
root.order.add_edge(milk_sourcing,     quality_testing)
root.order.add_edge(quality_testing,   curd_formation)
root.order.add_edge(curd_formation,    pressing_cheese)
root.order.add_edge(pressing_cheese,   aging_control)
root.order.add_edge(aging_control,     flavor_sampling)
root.order.add_edge(flavor_sampling,   packaging_prep)
root.order.add_edge(packaging_prep,    eco_labeling)
root.order.add_edge(eco_labeling,      health_inspection)
root.order.add_edge(health_inspection, export_licensing)
root.order.add_edge(export_licensing,  customs_clearance)
root.order.add_edge(customs_clearance, cold_storage)
root.order.add_edge(cold_storage,      retail_negotiation)
root.order.add_edge(retail_negotiation,traceability_audit)
root.order.add_edge(traceability_audit,market_feedback)

# logistics planning can overlap with the core chain once quality tests complete
root.order.add_edge(quality_testing, logistics_planning)