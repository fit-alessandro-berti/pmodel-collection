# Generated from: f131da4d-47d1-41ec-811f-b92c38a83a07.json
# Description: This process entails the end-to-end creation and distribution of artisan cheese, starting from specialized milk sourcing through unique fermentation techniques, quality assurance, packaging, and finally niche market delivery. It integrates seasonal milk variations, custom aging environments, microbial culture selection, and direct-to-consumer logistics, ensuring product distinctiveness and traceability in a highly regulated food sector. Each step involves collaboration between farmers, microbiologists, quality inspectors, and boutique retailers, all coordinated to maintain authenticity and meet regulatory standards while optimizing freshness and customer satisfaction.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
MilkSourcing = Transition(label='Milk Sourcing')
CultureSelection = Transition(label='Culture Selection')
MilkTesting = Transition(label='Milk Testing')

FermentationStart = Transition(label='Fermentation Start')
TemperatureControl = Transition(label='Temperature Control')
pHMonitoring = Transition(label='pH Monitoring')

CurdCutting = Transition(label='Curd Cutting')
WheyDraining = Transition(label='Whey Draining')

MoldingCheese = Transition(label='Molding Cheese')
SaltingProcess = Transition(label='Salting Process')

AgingSetup = Transition(label='Aging Setup')
QualityCheck = Transition(label='Quality Check')

PackagingPrep = Transition(label='Packaging Prep')
LabelDesign = Transition(label='Label Design')

DistributionPlan = Transition(label='Distribution Plan')
RetailDelivery = Transition(label='Retail Delivery')

CustomerFeedback = Transition(label='Customer Feedback')

# Create partial orders and loop where appropriate

# Fermentation monitoring loop: TemperatureControl and pHMonitoring periodically before continuing
fermentationMonitoringLoop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[OperatorPOWL(
        operator=Operator.XOR,
        children=[TemperatureControl, pHMonitoring]
    ), SilentTransition()]
)

# Cheese making order: CurdCutting --> WheyDraining --> MoldingCheese --> SaltingProcess
cheeseMaking = StrictPartialOrder(nodes=[CurdCutting, WheyDraining, MoldingCheese, SaltingProcess])
cheeseMaking.order.add_edge(CurdCutting, WheyDraining)
cheeseMaking.order.add_edge(WheyDraining, MoldingCheese)
cheeseMaking.order.add_edge(MoldingCheese, SaltingProcess)

# Packaging design parallel with Packaging Prep
packagingPhase = StrictPartialOrder(nodes=[PackagingPrep, LabelDesign])

# Distribution plan before retail delivery and customer feedback
distributionPhase = StrictPartialOrder(nodes=[DistributionPlan, RetailDelivery, CustomerFeedback])
distributionPhase.order.add_edge(DistributionPlan, RetailDelivery)
distributionPhase.order.add_edge(RetailDelivery, CustomerFeedback)

# Quality assurance before packaging
qualityPhase = StrictPartialOrder(nodes=[QualityCheck])
# (solo node)

# Aging and quality check in sequence
agingAndQuality = StrictPartialOrder(nodes=[AgingSetup, qualityPhase])
agingAndQuality.order.add_edge(AgingSetup, qualityPhase)

# Define milk preparation partial order (MilkSourcing and CultureSelection concurrent, then MilkTesting)
milkPrep = StrictPartialOrder(nodes=[MilkSourcing, CultureSelection, MilkTesting])
milkPrep.order.add_edge(MilkSourcing, MilkTesting)
milkPrep.order.add_edge(CultureSelection, MilkTesting)

# Fermentation phase: FermentationStart then fermentationMonitoringLoop
fermentationPhase = StrictPartialOrder(nodes=[FermentationStart, fermentationMonitoringLoop])
fermentationPhase.order.add_edge(FermentationStart, fermentationMonitoringLoop)

# Assemble main production flow partial order
productionFlow = StrictPartialOrder(
    nodes=[
        milkPrep,
        fermentationPhase,
        cheeseMaking,
        agingAndQuality,
        packagingPhase,
        distributionPhase
    ]
)

# Define main order edges
# The sub-orders are their own nodes, so edges are between them

productionFlow.order.add_edge(milkPrep, fermentationPhase)
productionFlow.order.add_edge(fermentationPhase, cheeseMaking)
productionFlow.order.add_edge(cheeseMaking, agingAndQuality)
productionFlow.order.add_edge(agingAndQuality, packagingPhase)
productionFlow.order.add_edge(packagingPhase, distributionPhase)

root = productionFlow