# Generated from: 451e3882-a15c-4940-9a01-32c961f404ec.json
# Description: This process describes the complex steps involved in exporting artisanal cheese from small-scale farms to international gourmet markets. It includes sourcing raw milk, ensuring compliance with health regulations, aging cheese under controlled conditions, packaging with eco-friendly materials, coordinating custom inspections, managing cold-chain logistics, and negotiating with boutique retailers abroad. The process requires meticulous quality checks, documentation for export licenses, and adapting to varying market preferences while maintaining product authenticity and traceability throughout the supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Curd_Formation = Transition(label='Curd Formation')
Pressing_Cheese = Transition(label='Pressing Cheese')
Aging_Control = Transition(label='Aging Control')
Flavor_Sampling = Transition(label='Flavor Sampling')
Packaging_Prep = Transition(label='Packaging Prep')
Eco_Labeling = Transition(label='Eco Labeling')
Health_Inspection = Transition(label='Health Inspection')
Export_Licensing = Transition(label='Export Licensing')
Customs_Clearance = Transition(label='Customs Clearance')
Cold_Storage = Transition(label='Cold Storage')
Logistics_Planning = Transition(label='Logistics Planning')
Retail_Negotiation = Transition(label='Retail Negotiation')
Traceability_Audit = Transition(label='Traceability Audit')
Market_Feedback = Transition(label='Market Feedback')

# Build Aging sub-process with optional Flavor Sampling loop
flavor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Flavor_Sampling, Aging_Control]
)

# Packaging with Eco Labeling runs after Packaging Prep concurrently
packaging_po = StrictPartialOrder(nodes=[Packaging_Prep, Eco_Labeling])
packaging_po.order.add_edge(Packaging_Prep, Eco_Labeling)

# Logistics sub-process handles Cold Storage and Logistics Planning in partial order (concurrent)
logistics_po = StrictPartialOrder(nodes=[Cold_Storage, Logistics_Planning])

# Export sub-process: Health Inspection --> Export Licensing --> Customs Clearance
export_po = StrictPartialOrder(
    nodes=[Health_Inspection, Export_Licensing, Customs_Clearance]
)
export_po.order.add_edge(Health_Inspection, Export_Licensing)
export_po.order.add_edge(Export_Licensing, Customs_Clearance)

# Overall Quality Check and Traceability Audit is done after Aging and Packaging
quality_traceability_po = StrictPartialOrder(
    nodes=[Quality_Testing, Traceability_Audit]
)
quality_traceability_po.order.add_edge(Quality_Testing, Traceability_Audit)

# Market Feedback and Retail Negotiation are concurrent end activities after Certification steps
end_activities_po = StrictPartialOrder(nodes=[Retail_Negotiation, Market_Feedback])

# Cheese production sequential: Milk Sourcing -> Quality Testing -> Curd Formation -> Pressing Cheese -> Aging with optional Flavor Sampling
cheese_production_po = StrictPartialOrder(
    nodes=[Milk_Sourcing, Quality_Testing, Curd_Formation, Pressing_Cheese, flavor_loop]
)
cheese_production_po.order.add_edge(Milk_Sourcing, Quality_Testing)
cheese_production_po.order.add_edge(Quality_Testing, Curd_Formation)
cheese_production_po.order.add_edge(Curd_Formation, Pressing_Cheese)
cheese_production_po.order.add_edge(Pressing_Cheese, flavor_loop)

# Packaging after cheese production
cheese_packaging_po = StrictPartialOrder(
    nodes=[cheese_production_po, packaging_po]
)
cheese_packaging_po.order.add_edge(cheese_production_po, packaging_po)

# Certification (Health Inspection and Export) after packaging
certification_po = StrictPartialOrder(
    nodes=[cheese_packaging_po, export_po, quality_traceability_po]
)
certification_po.order.add_edge(cheese_packaging_po, export_po)
certification_po.order.add_edge(cheese_packaging_po, quality_traceability_po)

# Logistics planning after certification
certification_logistics_po = StrictPartialOrder(
    nodes=[certification_po, logistics_po]
)
certification_logistics_po.order.add_edge(certification_po, logistics_po)

# End activities after logistics
final_po = StrictPartialOrder(
    nodes=[certification_logistics_po, end_activities_po]
)
final_po.order.add_edge(certification_logistics_po, end_activities_po)

root = final_po