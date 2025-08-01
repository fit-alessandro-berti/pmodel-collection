# Generated from: 3494b32b-b5df-485f-84ac-02261f628c66.json
# Description: This process manages the unique supply chain for artisanal cheese production, starting from sourcing rare milk varieties from micro-dairies, through customized fermentation and aging procedures, to specialized packaging and direct distribution to niche markets. It incorporates quality control at every step, traceability of origin, and coordination with seasonal production cycles, ensuring product authenticity and maintaining the delicate balance between traditional methods and modern food safety standards. The process also involves managing limited edition batches, handling small-scale logistics, and engaging with artisan networks for collaborative innovation and market positioning.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
MilkSourcing = Transition(label='Milk Sourcing')
QualityTesting = Transition(label='Quality Testing')
MilkPasteurize = Transition(label='Milk Pasteurize')
StarterCulture = Transition(label='Starter Culture')
Coagulation = Transition(label='Coagulation')
CurdCutting = Transition(label='Curd Cutting')
WheyDrain = Transition(label='Whey Drain')
MoldingPress = Transition(label='Molding Press')
SaltingStage = Transition(label='Salting Stage')
Fermentation = Transition(label='Fermentation')
AgingMonitor = Transition(label='Aging Monitor')
FlavorTesting = Transition(label='Flavor Testing')
BatchLabeling = Transition(label='Batch Labeling')
CustomPackaging = Transition(label='Custom Packaging')
MarketDelivery = Transition(label='Market Delivery')
TraceabilityLog = Transition(label='Traceability Log')
InventoryAudit = Transition(label='Inventory Audit')

# Quality control and traceability occur "at every step"
# To model this, include TraceabilityLog after each main production stage and QualityTesting to gate initial quality

# 1. Initial sourcing and milk preparation with quality checks and pasteurization:
initial_PO = StrictPartialOrder(nodes=[
    MilkSourcing, 
    QualityTesting, 
    MilkPasteurize,
    TraceabilityLog
])
initial_PO.order.add_edge(MilkSourcing, QualityTesting)
initial_PO.order.add_edge(QualityTesting, MilkPasteurize)
initial_PO.order.add_edge(MilkPasteurize, TraceabilityLog)

# 2. Cheese production steps in sequence:
production_PO = StrictPartialOrder(nodes=[
    StarterCulture,
    Coagulation,
    CurdCutting,
    WheyDrain,
    MoldingPress,
    SaltingStage,
    Fermentation,
    TraceabilityLog
])
production_PO.order.add_edge(StarterCulture, Coagulation)
production_PO.order.add_edge(Coagulation, CurdCutting)
production_PO.order.add_edge(CurdCutting, WheyDrain)
production_PO.order.add_edge(WheyDrain, MoldingPress)
production_PO.order.add_edge(MoldingPress, SaltingStage)
production_PO.order.add_edge(SaltingStage, Fermentation)
production_PO.order.add_edge(Fermentation, TraceabilityLog)

# 3. Aging and quality checks with possible repeated aging monitoring (loop)
aging_loop_body = StrictPartialOrder(nodes=[AgingMonitor, FlavorTesting, TraceabilityLog])
aging_loop_body.order.add_edge(AgingMonitor, FlavorTesting)
aging_loop_body.order.add_edge(FlavorTesting, TraceabilityLog)

aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[AgingMonitor, StrictPartialOrder(nodes=[FlavorTesting, TraceabilityLog])])
# The loop structure is: aging monitoring then either exit or do flavor testing + traceability then aging monitor again.
# We use AgingMonitor as A, and PO of FlavorTesting and TraceabilityLog (sequential) as B inside loop.

# Let's build B as sequential FlavorTesting -> TraceabilityLog
B = StrictPartialOrder(nodes=[FlavorTesting, TraceabilityLog])
B.order.add_edge(FlavorTesting, TraceabilityLog)

aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[AgingMonitor, B])

# 4. Final packaging and delivery with quality and inventory audit

final_PO = StrictPartialOrder(nodes=[
    BatchLabeling,
    CustomPackaging,
    MarketDelivery,
    InventoryAudit,
    TraceabilityLog
])
final_PO.order.add_edge(BatchLabeling, CustomPackaging)
final_PO.order.add_edge(CustomPackaging, MarketDelivery)
final_PO.order.add_edge(MarketDelivery, InventoryAudit)
final_PO.order.add_edge(InventoryAudit, TraceabilityLog)

# Combine all main stages in sequence with embedded traceability logs and quality testing at start

root = StrictPartialOrder(nodes=[initial_PO, production_PO, aging_loop, final_PO])
root.order.add_edge(initial_PO, production_PO)
root.order.add_edge(production_PO, aging_loop)
root.order.add_edge(aging_loop, final_PO)