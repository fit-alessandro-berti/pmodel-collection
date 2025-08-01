# Generated from: cdccf476-9ee9-4e31-8175-559567c6dcb1.json
# Description: This process details the complex supply chain of artisan cheese production, starting from sourcing rare milk varieties from remote farms, followed by precise curdling and aging in controlled environments. It involves quality validation through microbial testing, packaging with environmentally sustainable materials, managing inventory under strict temperature controls, coordinating logistics with specialized carriers, and finally ensuring traceability through blockchain records. The process also includes customer feedback loops to adjust future batches and compliance audits to meet international food safety standards, emphasizing both tradition and innovation in food craftsmanship.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Milk_Sourcing = Transition(label='Milk Sourcing')
Curd_Formation = Transition(label='Curd Formation')
Microbial_Test = Transition(label='Microbial Test')
Whey_Removal = Transition(label='Whey Removal')
Pressing_Cheese = Transition(label='Pressing Cheese')
Salt_Application = Transition(label='Salt Application')
Aging_Control = Transition(label='Aging Control')
Quality_Check = Transition(label='Quality Check')
Eco_Packaging = Transition(label='Eco Packaging')
Inventory_Log = Transition(label='Inventory Log')
Temp_Monitoring = Transition(label='Temp Monitoring')
Carrier_Booking = Transition(label='Carrier Booking')
Trace_Recording = Transition(label='Trace Recording')
Feedback_Review = Transition(label='Feedback Review')
Compliance_Audit = Transition(label='Compliance Audit')
Batch_Adjustment = Transition(label='Batch Adjustment')

# Loop for feedback to adjust future batches:
# Loop with body: Batch_Adjustment
# Loop condition: Feedback_Review
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Batch_Adjustment, Feedback_Review])

# Loop for compliance audits after quality check:
# Loop body: Compliance_Audit
# Loop condition: SilentTransition (exit)
compliance_loop = OperatorPOWL(operator=Operator.LOOP, children=[Compliance_Audit, SilentTransition()])

# Package stage partial order, Packaging + Inventory + Temperature Monitoring
packaging_PO = StrictPartialOrder(nodes=[Eco_Packaging, Inventory_Log, Temp_Monitoring])
# No edges means fully concurrent

# Logistics partial order: Carrier Booking then Trace Recording (traceability after logistics)
logistics_PO = StrictPartialOrder(nodes=[Carrier_Booking, Trace_Recording])
logistics_PO.order.add_edge(Carrier_Booking, Trace_Recording)

# Cheese processing partial order:
# After Whey Removal: Pressing Cheese --> Salt Application --> Aging Control --> Quality Check --> compliance_loop
cheese_processing_PO = StrictPartialOrder(
    nodes=[Whey_Removal, Pressing_Cheese, Salt_Application, Aging_Control, Quality_Check, compliance_loop]
)
cheese_processing_PO.order.add_edge(Whey_Removal, Pressing_Cheese)
cheese_processing_PO.order.add_edge(Pressing_Cheese, Salt_Application)
cheese_processing_PO.order.add_edge(Salt_Application, Aging_Control)
cheese_processing_PO.order.add_edge(Aging_Control, Quality_Check)
cheese_processing_PO.order.add_edge(Quality_Check, compliance_loop)

# Quality validation choice after Curd Formation: Microbial Test (mandatory)
# The NOP of Curd Formation --> Microbial Test --> Whey Removal (start cheese processing)
quality_PO = StrictPartialOrder(nodes=[Curd_Formation, Microbial_Test, cheese_processing_PO])
quality_PO.order.add_edge(Curd_Formation, Microbial_Test)
quality_PO.order.add_edge(Microbial_Test, cheese_processing_PO)

# Initial phase partial order: Milk Sourcing --> Curd Formation --> quality_PO
initial_PO = StrictPartialOrder(nodes=[Milk_Sourcing, quality_PO])
initial_PO.order.add_edge(Milk_Sourcing, quality_PO)

# Combine the full process partial order:
# initial_PO --> packaging_PO --> logistics_PO --> Trace Recording --> feedback_loop

full_PO_nodes = [initial_PO, packaging_PO, logistics_PO, feedback_loop]
root = StrictPartialOrder(nodes=full_PO_nodes)

# Ordering between major phases:
root.order.add_edge(initial_PO, packaging_PO)
root.order.add_edge(packaging_PO, logistics_PO)
root.order.add_edge(logistics_PO, feedback_loop)