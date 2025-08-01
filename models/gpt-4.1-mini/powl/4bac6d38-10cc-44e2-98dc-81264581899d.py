# Generated from: 4bac6d38-10cc-44e2-98dc-81264581899d.json
# Description: This process describes the intricate supply chain management for a network of artisan craftsmen producing bespoke furniture. It integrates raw material sourcing from sustainable forests, handcrafting stages with quality checkpoints, coordination of custom design inputs, and decentralized logistics involving local couriers. The process also includes adaptive inventory forecasting based on seasonal demand fluctuations and real-time artisan feedback, ensuring minimal waste and maximum customer satisfaction through personalized delivery schedules and post-sale care services.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
SourceTimber = Transition(label='Source Timber')
InspectLogs = Transition(label='Inspect Logs')
DesignDraft = Transition(label='Design Draft')
MaterialPrep = Transition(label='Material Prep')
CraftAssembly = Transition(label='Craft Assembly')
QualityCheck = Transition(label='Quality Check')
ClientReview = Transition(label='Client Review')
AdjustDesign = Transition(label='Adjust Design')
FinishSurface = Transition(label='Finish Surface')
PackageGoods = Transition(label='Package Goods')
SchedulePickup = Transition(label='Schedule Pickup')
LocalCourier = Transition(label='Local Courier')
TrackDelivery = Transition(label='Track Delivery')
InventoryUpdate = Transition(label='Inventory Update')
CollectFeedback = Transition(label='Collect Feedback')
AftercareSetup = Transition(label='Aftercare Setup')

skip = SilentTransition()

# Loop for design adjustment after client review: ClientReview -> loop with (AdjustDesign, DesignDraft)
design_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[ClientReview, OperatorPOWL(operator=Operator.XOR, children=[AdjustDesign, skip])]
)

# Partial order for the crafting subprocess:
# MaterialPrep -> CraftAssembly -> QualityCheck -> design_loop -> FinishSurface
craft_po = StrictPartialOrder(nodes=[
    MaterialPrep, CraftAssembly, QualityCheck, design_loop, FinishSurface
])
craft_po.order.add_edge(MaterialPrep, CraftAssembly)
craft_po.order.add_edge(CraftAssembly, QualityCheck)
craft_po.order.add_edge(QualityCheck, design_loop)
craft_po.order.add_edge(design_loop, FinishSurface)

# Partial order for sourcing:
# SourceTimber -> InspectLogs -> DesignDraft
source_po = StrictPartialOrder(nodes=[SourceTimber, InspectLogs, DesignDraft])
source_po.order.add_edge(SourceTimber, InspectLogs)
source_po.order.add_edge(InspectLogs, DesignDraft)

# Partial order for logistics:
# SchedulePickup -> LocalCourier -> TrackDelivery
logistics_po = StrictPartialOrder(nodes=[SchedulePickup, LocalCourier, TrackDelivery])
logistics_po.order.add_edge(SchedulePickup, LocalCourier)
logistics_po.order.add_edge(LocalCourier, TrackDelivery)

# Partial order for feedback loop and inventory:
# CollectFeedback -> InventoryUpdate
feedback_po = StrictPartialOrder(nodes=[CollectFeedback, InventoryUpdate])
feedback_po.order.add_edge(CollectFeedback, InventoryUpdate)

# Final sequence partial order:
# source_po -> craft_po -> PackageGoods -> logistics_po -> feedback_po -> AftercareSetup
root = StrictPartialOrder(nodes=[
    source_po,
    craft_po,
    PackageGoods,
    logistics_po,
    feedback_po,
    AftercareSetup
])

root.order.add_edge(source_po, craft_po)
root.order.add_edge(craft_po, PackageGoods)
root.order.add_edge(PackageGoods, logistics_po)
root.order.add_edge(logistics_po, feedback_po)
root.order.add_edge(feedback_po, AftercareSetup)