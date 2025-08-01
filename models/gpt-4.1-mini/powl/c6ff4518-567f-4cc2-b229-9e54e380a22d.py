# Generated from: c6ff4518-567f-4cc2-b229-9e54e380a22d.json
# Description: This process describes the end-to-end supply chain for artisanal cheese production, starting from sourcing rare local milk varieties to aging cheese in controlled microclimates. It involves unique activities such as microbial culture selection, hand molding, natural rind treatment, and seasonal flavor profiling. Quality control is conducted through sensory panel reviews and microscopic texture inspections. Packaging is eco-friendly and customized per batch, followed by niche market distribution targeting specialty food stores and luxury restaurants. The process ensures traceability of every cheese wheel through blockchain-enabled records, enhancing transparency and consumer trust in a highly specialized product category.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Milk_Sourcing = Transition(label='Milk Sourcing')
Culture_Prep = Transition(label='Culture Prep')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Coagulation = Transition(label='Coagulation')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Draining = Transition(label='Whey Draining')
Hand_Molding = Transition(label='Hand Molding')
Pressing = Transition(label='Pressing')
Salting = Transition(label='Salting')
Rind_Treatment = Transition(label='Rind Treatment')
Aging_Setup = Transition(label='Aging Setup')
Microclimate_Control = Transition(label='Microclimate Control')
Flavor_Profiling = Transition(label='Flavor Profiling')
Quality_Check = Transition(label='Quality Check')
Sensory_Review = Transition(label='Sensory Review')
Texture_Inspect = Transition(label='Texture Inspect')
Eco_Packaging = Transition(label='Eco Packaging')
Batch_Labeling = Transition(label='Batch Labeling')
Blockchain_Log = Transition(label='Blockchain Log')
Niche_Shipping = Transition(label='Niche Shipping')

# Quality check modeled as concurrency of sensory review and texture inspect before finalizing QC
Quality_Check_PO = StrictPartialOrder(nodes=[Quality_Check, Sensory_Review, Texture_Inspect])
Quality_Check_PO.order.add_edge(Quality_Check, Sensory_Review)
Quality_Check_PO.order.add_edge(Quality_Check, Texture_Inspect)

# Aging involves setup, microclimate control, and flavor profiling as partial order (concurrent except aging setup before microclimate)
Aging_PO = StrictPartialOrder(
    nodes=[Aging_Setup, Microclimate_Control, Flavor_Profiling]
)
Aging_PO.order.add_edge(Aging_Setup, Microclimate_Control)
# Flavor Profiling can happen concurrently with microclimate control (no edge)

# Packaging involves eco-friendly packaging and batch labeling in parallel
Packaging_PO = StrictPartialOrder(nodes=[Eco_Packaging, Batch_Labeling])

# Blockchain logging and niche shipping happen in order: blockchain log then niche shipping for traceability & shipping
Trace_Ship_PO = StrictPartialOrder(nodes=[Blockchain_Log, Niche_Shipping])
Trace_Ship_PO.order.add_edge(Blockchain_Log, Niche_Shipping)

# Production stages before quality check
Production_PO = StrictPartialOrder(nodes=[
    Milk_Sourcing, Culture_Prep, Milk_Pasteurize, Coagulation,
    Curd_Cutting, Whey_Draining, Hand_Molding, Pressing, Salting,
    Rind_Treatment
])
Production_PO.order.add_edge(Milk_Sourcing, Culture_Prep)
Production_PO.order.add_edge(Culture_Prep, Milk_Pasteurize)
Production_PO.order.add_edge(Milk_Pasteurize, Coagulation)
Production_PO.order.add_edge(Coagulation, Curd_Cutting)
Production_PO.order.add_edge(Curd_Cutting, Whey_Draining)
Production_PO.order.add_edge(Whey_Draining, Hand_Molding)
Production_PO.order.add_edge(Hand_Molding, Pressing)
Production_PO.order.add_edge(Pressing, Salting)
Production_PO.order.add_edge(Salting, Rind_Treatment)

# Combine production, aging, quality check, packaging, traceability & shipping in sequence
root = StrictPartialOrder(
    nodes=[
        Production_PO,
        Aging_PO,
        Quality_Check_PO,
        Packaging_PO,
        Trace_Ship_PO
    ]
)

root.order.add_edge(Production_PO, Aging_PO)
root.order.add_edge(Aging_PO, Quality_Check_PO)
root.order.add_edge(Quality_Check_PO, Packaging_PO)
root.order.add_edge(Packaging_PO, Trace_Ship_PO)