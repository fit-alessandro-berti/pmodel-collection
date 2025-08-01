# Generated from: dd7bc2cb-e945-49b7-bdff-008a99bba3ed.json
# Description: This process outlines the intricate steps involved in sourcing, aging, and distributing artisan cheeses from small-scale farms to gourmet retailers. It begins with farm selection, ensuring ethical animal treatment and unique milk qualities, followed by milk testing, curdling, and controlled aging in specialized environments. Quality inspections occur at multiple stages, including texture and flavor profiling. Packaging is customized for each cheese type to maintain freshness and brand identity. The distribution involves cold chain logistics with real-time monitoring and retailer training on product handling. Finally, customer feedback is collected to refine future batches and maintain artisanal standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Farm_Select = Transition(label='Farm Select')
Milk_Test = Transition(label='Milk Test')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Curd_Form = Transition(label='Curd Form')
Whey_Drain = Transition(label='Whey Drain')
Cheese_Press = Transition(label='Cheese Press')
Salt_Rub = Transition(label='Salt Rub')
Aging_Set = Transition(label='Aging Set')
Flavor_Check = Transition(label='Flavor Check')
Texture_Scan = Transition(label='Texture Scan')
Quality_Approve = Transition(label='Quality Approve')
Custom_Pack = Transition(label='Custom Pack')
Cold_Ship = Transition(label='Cold Ship')
Retail_Train = Transition(label='Retail Train')
Feedback_Log = Transition(label='Feedback Log')
Batch_Adjust = Transition(label='Batch Adjust')

# Quality inspection choice: Flavor check or Texture scan
quality_inspection = OperatorPOWL(operator=Operator.XOR, children=[Flavor_Check, Texture_Scan])

# Quality approval after both flavor and texture inspection: means both Flavor and Texture must be done before approve
inspection_PO = StrictPartialOrder(nodes=[Flavor_Check, Texture_Scan, Quality_Approve])
inspection_PO.order.add_edge(Flavor_Check, Quality_Approve)
inspection_PO.order.add_edge(Texture_Scan, Quality_Approve)

# Production partial order of cheese processing steps before aging
production_PO = StrictPartialOrder(
    nodes=[
        Farm_Select, Milk_Test, Milk_Pasteurize,
        Curd_Form, Whey_Drain, Cheese_Press, Salt_Rub,
        Aging_Set,
        inspection_PO
    ]
)
production_PO.order.add_edge(Farm_Select, Milk_Test)
production_PO.order.add_edge(Milk_Test, Milk_Pasteurize)
production_PO.order.add_edge(Milk_Pasteurize, Curd_Form)
production_PO.order.add_edge(Curd_Form, Whey_Drain)
production_PO.order.add_edge(Whey_Drain, Cheese_Press)
production_PO.order.add_edge(Cheese_Press, Salt_Rub)
production_PO.order.add_edge(Salt_Rub, Aging_Set)
production_PO.order.add_edge(Aging_Set, inspection_PO)

# Packaging follows quality approval
packaging_PO = StrictPartialOrder(nodes=[Quality_Approve, Custom_Pack])
packaging_PO.order.add_edge(Quality_Approve, Custom_Pack)

# Distribution partial order: Cold Ship then Retail Train
distribution_PO = StrictPartialOrder(nodes=[Custom_Pack, Cold_Ship, Retail_Train])
distribution_PO.order.add_edge(Custom_Pack, Cold_Ship)
distribution_PO.order.add_edge(Cold_Ship, Retail_Train)

# Feedback loop: Feedback Log then Batch Adjust then re-starts at Farm Select (using LOOP operator)
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Log, Batch_Adjust])

# Assemble full partial order nodes
root = StrictPartialOrder(
    nodes=[production_PO, packaging_PO, distribution_PO, feedback_loop]
)

# Connect the segments
# Production leads to Packaging
root.order.add_edge(production_PO, packaging_PO)
# Packaging leads to Distribution
root.order.add_edge(packaging_PO, distribution_PO)
# Distribution leads to Feedback Log (loop body start)
root.order.add_edge(distribution_PO, feedback_loop)