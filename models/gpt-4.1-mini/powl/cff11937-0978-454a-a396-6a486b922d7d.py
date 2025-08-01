# Generated from: cff11937-0978-454a-a396-6a486b922d7d.json
# Description: This process describes the end-to-end supply chain of artisan cheese production, starting from sourcing rare milk varieties from remote farms, followed by precise fermentation and aging in controlled cave environments. The process includes quality sampling, custom packaging design, cold-chain logistics coordination, market trend analysis for flavor adjustments, direct-to-consumer sales via pop-up events, and feedback incorporation for continuous product refinement. It ensures the preservation of traditional methods while leveraging modern technology for traceability and customer engagement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

MilkSourcing = Transition(label='Milk Sourcing')
QualityTesting = Transition(label='Quality Testing')
StarterCulture = Transition(label='Starter Culture')
MilkFermentation = Transition(label='Milk Fermentation')
CurdCutting = Transition(label='Curd Cutting')
WheyDraining = Transition(label='Whey Draining')
PressingCheese = Transition(label='Pressing Cheese')
CaveAging = Transition(label='Cave Aging')
SampleTasting = Transition(label='Sample Tasting')
FlavorProfiling = Transition(label='Flavor Profiling')
PackagingDesign = Transition(label='Packaging Design')
ColdStorage = Transition(label='Cold Storage')
LogisticsPlanning = Transition(label='Logistics Planning')
PopupSales = Transition(label='Pop-up Sales')
CustomerFeedback = Transition(label='Customer Feedback')
RecipeAdjusting = Transition(label='Recipe Adjusting')

# Production partial order
production = StrictPartialOrder(
    nodes=[
        MilkSourcing, QualityTesting, StarterCulture, MilkFermentation, CurdCutting,
        WheyDraining, PressingCheese, CaveAging
    ]
)
production.order.add_edge(MilkSourcing, QualityTesting)
production.order.add_edge(QualityTesting, StarterCulture)
production.order.add_edge(StarterCulture, MilkFermentation)
production.order.add_edge(MilkFermentation, CurdCutting)
production.order.add_edge(CurdCutting, WheyDraining)
production.order.add_edge(WheyDraining, PressingCheese)
production.order.add_edge(PressingCheese, CaveAging)

# Sampling partial order (from aging)
sampling = StrictPartialOrder(
    nodes=[SampleTasting, FlavorProfiling]
)
sampling.order.add_edge(SampleTasting, FlavorProfiling)

# Packaging partial order
packaging = StrictPartialOrder(
    nodes=[PackagingDesign, ColdStorage, LogisticsPlanning]
)
packaging.order.add_edge(PackagingDesign, ColdStorage)
packaging.order.add_edge(ColdStorage, LogisticsPlanning)

# Sales partial order
sales = StrictPartialOrder(
    nodes=[PopupSales, CustomerFeedback, RecipeAdjusting]
)
sales.order.add_edge(PopupSales, CustomerFeedback)
sales.order.add_edge(CustomerFeedback, RecipeAdjusting)

# Combine all into root with partial orders and edges to reflect the process flow:
root = StrictPartialOrder(
    nodes=[production, sampling, packaging, sales]
)
root.order.add_edge(production, sampling)
root.order.add_edge(production, packaging)
root.order.add_edge(packaging, sales)
root.order.add_edge(sampling, sales)