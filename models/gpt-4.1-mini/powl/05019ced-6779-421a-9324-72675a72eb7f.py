# Generated from: 05019ced-6779-421a-9324-72675a72eb7f.json
# Description: This complex process outlines the journey of artisanal cheese production and distribution, beginning with raw milk sourcing from specialized farms. It includes quality testing, maturation under controlled conditions, custom flavor infusion, packaging with eco-friendly materials, and finally, niche market distribution. The process involves coordination between farmers, microbiologists, flavor experts, logistic teams, and retail partners to ensure product authenticity, safety, and uniqueness. Continuous feedback loops support refinement of both product and delivery, adapting to seasonal variations and customer preferences while maintaining traditional craftsmanship standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Milk_Sourcing = Transition(label='Milk Sourcing')
Farm_Inspection = Transition(label='Farm Inspection')
Quality_Testing = Transition(label='Quality Testing')

Starter_Culture = Transition(label='Starter Culture')
Coagulation = Transition(label='Coagulation')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Draining = Transition(label='Whey Draining')
Molding_Cheese = Transition(label='Molding Cheese')

Flavor_Infusion = Transition(label='Flavor Infusion')

Controlled_Aging = Transition(label='Controlled Aging')
Texture_Checking = Transition(label='Texture Checking')

Eco_Packaging = Transition(label='Eco Packaging')
Label_Printing = Transition(label='Label Printing')
Inventory_Logging = Transition(label='Inventory Logging')

Order_Processing = Transition(label='Order Processing')

Special_Handling = Transition(label='Special Handling')

Shipment_Dispatch = Transition(label='Shipment Dispatch')

Retail_Setup = Transition(label='Retail Setup')

# Silent transition to represent optional/exits
skip = SilentTransition()

# ---- Build loops for continuous feedback loops supporting refinement ----
# Loop1: Controlled Aging with Texture Checking, potentially repeat aging step after checking
aging_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Controlled_Aging, Texture_Checking]
)
# semantics: Controlled_Aging -> (exit or Texture_Checking -> Controlled_Aging again)

# Loop2: Order Processing with Special Handling (special handling optional, refinement)
order_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Order_Processing, Special_Handling]
)
# semantics: Order_Processing -> (exit or Special_Handling -> Order_Processing again)

# ---- Packaging partial order: Eco Packaging and Label Printing can proceed concurrently,
# then Inventory Logging last (dependent on both packaging and printing) ----
packaging_po = StrictPartialOrder(
    nodes=[Eco_Packaging, Label_Printing, Inventory_Logging]
)
packaging_po.order.add_edge(Eco_Packaging, Inventory_Logging)
packaging_po.order.add_edge(Label_Printing, Inventory_Logging)

# ---- Production partial order prior to packaging:
# After Milk Sourcing and Farm Inspection (order),
# then Quality Testing,
# then starter culture sequence (Starter Culture -> Coagulation -> Curd Cutting -> Whey Draining -> Molding Cheese),
# then Flavor Infusion,
# then aging loop (aging_loop) ----

# Starter Culture chain
starter_seq = StrictPartialOrder(
    nodes=[Starter_Culture, Coagulation, Curd_Cutting, Whey_Draining, Molding_Cheese]
)
starter_seq.order.add_edge(Starter_Culture, Coagulation)
starter_seq.order.add_edge(Coagulation, Curd_Cutting)
starter_seq.order.add_edge(Curd_Cutting, Whey_Draining)
starter_seq.order.add_edge(Whey_Draining, Molding_Cheese)

# Production sequence:
prod_seq = StrictPartialOrder(
    nodes=[
        Milk_Sourcing,
        Farm_Inspection,
        Quality_Testing,
        starter_seq,
        Flavor_Infusion,
        aging_loop
    ]
)
prod_seq.order.add_edge(Milk_Sourcing, Farm_Inspection)
prod_seq.order.add_edge(Farm_Inspection, Quality_Testing)
prod_seq.order.add_edge(Quality_Testing, starter_seq)
prod_seq.order.add_edge(starter_seq, Flavor_Infusion)
prod_seq.order.add_edge(Flavor_Infusion, aging_loop)

# ---- Final distribution partial order:
# Packaging sequence --> order_loop --> Shipment_Dispatch --> Retail_Setup

distribution_seq = StrictPartialOrder(
    nodes=[packaging_po, order_loop, Shipment_Dispatch, Retail_Setup]
)
distribution_seq.order.add_edge(packaging_po, order_loop)
distribution_seq.order.add_edge(order_loop, Shipment_Dispatch)
distribution_seq.order.add_edge(Shipment_Dispatch, Retail_Setup)

# ---- Root partial order: production_seq --> distribution_seq

root = StrictPartialOrder(
    nodes=[prod_seq, distribution_seq]
)
root.order.add_edge(prod_seq, distribution_seq)