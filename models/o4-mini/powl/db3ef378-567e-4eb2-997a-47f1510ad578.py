# Generated from: db3ef378-567e-4eb2-997a-47f1510ad578.json
# Description: This process outlines the complex and atypical supply chain for artisan cheese production, emphasizing the coordination between small-scale dairy farms, quality-controlled aging facilities, and niche distribution channels. The process involves raw milk collection from specialized breeds, microbial culture preparation, curd formation, controlled aging under precise humidity and temperature, artisanal packaging, and direct-to-consumer marketing through exclusive events and subscription models. It integrates traceability at each step, ensuring compliance with regional food safety laws while maintaining the unique flavor profiles that distinguish the product in a competitive market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
MilkCollection     = Transition(label='Milk Collection')
CulturePrep        = Transition(label='Culture Prep')
CurdFormation      = Transition(label='Curd Formation')
WheySeparation     = Transition(label='Whey Separation')
MoldingCheese      = Transition(label='Molding Cheese')
SaltingProcess     = Transition(label='Salting Process')
InitialAging       = Transition(label='Initial Aging')
HumidityControl    = Transition(label='Humidity Control')
TemperatureCheck   = Transition(label='Temperature Check')
FlavorTesting      = Transition(label='Flavor Testing')
FinalAging         = Transition(label='Final Aging')
PackagingArtisanal = Transition(label='Packaging Artisanal')
LabelPrinting      = Transition(label='Label Printing')
InventoryAudit     = Transition(label='Inventory Audit')
OrderFulfillment   = Transition(label='Order Fulfillment')
SubscriptionSetup  = Transition(label='Subscription Setup')
EventMarketing     = Transition(label='Event Marketing')

# Create the strict partial order model
root = StrictPartialOrder(nodes=[
    MilkCollection,
    CulturePrep,
    CurdFormation,
    WheySeparation,
    MoldingCheese,
    SaltingProcess,
    InitialAging,
    HumidityControl,
    TemperatureCheck,
    FlavorTesting,
    FinalAging,
    PackagingArtisanal,
    LabelPrinting,
    InventoryAudit,
    OrderFulfillment,
    SubscriptionSetup,
    EventMarketing
])

# Define the control flow dependencies
root.order.add_edge(MilkCollection, CulturePrep)
root.order.add_edge(CulturePrep, CurdFormation)
root.order.add_edge(CurdFormation, WheySeparation)
root.order.add_edge(WheySeparation, MoldingCheese)
root.order.add_edge(MoldingCheese, SaltingProcess)
root.order.add_edge(SaltingProcess, InitialAging)

# Quality-controlled aging checks before flavor testing
root.order.add_edge(InitialAging, HumidityControl)
root.order.add_edge(InitialAging, TemperatureCheck)
root.order.add_edge(HumidityControl, FlavorTesting)
root.order.add_edge(TemperatureCheck, FlavorTesting)

# Continue aging after successful flavor test
root.order.add_edge(FlavorTesting, FinalAging)

# Packaging and labeling
root.order.add_edge(FinalAging, PackagingArtisanal)
root.order.add_edge(PackagingArtisanal, LabelPrinting)
root.order.add_edge(LabelPrinting, InventoryAudit)

# Concurrent distribution channels
root.order.add_edge(InventoryAudit, OrderFulfillment)
root.order.add_edge(InventoryAudit, SubscriptionSetup)
root.order.add_edge(InventoryAudit, EventMarketing)