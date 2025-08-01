# Generated from: 5b074e06-0c26-457c-8100-093d5363d378.json
# Description: This process outlines the intricate steps involved in producing and distributing artisanal cheese from farm to boutique retail. It begins with selective milk sourcing from specific breeds of livestock, followed by precise milk testing and standardization. The milk is then cultured using unique bacterial blends before curdling and gentle cutting. After molding and initial aging, the cheese undergoes repeated washing and brushing to develop its rind. Quality control includes sensory evaluation and microbial testing. Packaging is customized to preserve flavor and texture, with cold chain logistics ensuring freshness during transport. Marketing targets niche markets emphasizing provenance and craftsmanship, culminating in boutique retail placement and consumer feedback collection to refine future batches.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
MilkSourcing = Transition(label='Milk Sourcing')
MilkTesting = Transition(label='Milk Testing')
MilkStandardization = Transition(label='Milk Standardization')
CulturePreparation = Transition(label='Culture Preparation')
MilkCulturing = Transition(label='Milk Culturing')
CurdCutting = Transition(label='Curd Cutting')
MoldingCheese = Transition(label='Molding Cheese')
InitialAging = Transition(label='Initial Aging')
RindWashing = Transition(label='Rind Washing')
RindBrushing = Transition(label='Rind Brushing')
SensoryCheck = Transition(label='Sensory Check')
MicrobialTest = Transition(label='Microbial Test')
CustomPackaging = Transition(label='Custom Packaging')
ColdTransport = Transition(label='Cold Transport')
MarketTargeting = Transition(label='Market Targeting')
RetailPlacement = Transition(label='Retail Placement')
FeedbackGathering = Transition(label='Feedback Gathering')

# Silent transition for loop exit
skip = SilentTransition()

# Loop for repeated rind washing and brushing
PO_wash_brush = StrictPartialOrder(nodes=[RindWashing, RindBrushing])
PO_wash_brush.order.add_edge(RindWashing, RindBrushing)
loop_rind = OperatorPOWL(operator=Operator.LOOP, children=[PO_wash_brush, skip])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    MilkSourcing,
    MilkTesting,
    MilkStandardization,
    CulturePreparation,
    MilkCulturing,
    CurdCutting,
    MoldingCheese,
    InitialAging,
    loop_rind,
    SensoryCheck,
    MicrobialTest,
    CustomPackaging,
    ColdTransport,
    MarketTargeting,
    RetailPlacement,
    FeedbackGathering
])

# Define the sequence of dependencies
root.order.add_edge(MilkSourcing, MilkTesting)
root.order.add_edge(MilkTesting, MilkStandardization)
root.order.add_edge(MilkStandardization, CulturePreparation)
root.order.add_edge(CulturePreparation, MilkCulturing)
root.order.add_edge(MilkCulturing, CurdCutting)
root.order.add_edge(CurdCutting, MoldingCheese)
root.order.add_edge(MoldingCheese, InitialAging)
root.order.add_edge(InitialAging, loop_rind)
root.order.add_edge(loop_rind, SensoryCheck)
root.order.add_edge(SensoryCheck, MicrobialTest)
root.order.add_edge(MicrobialTest, CustomPackaging)
root.order.add_edge(CustomPackaging, ColdTransport)
root.order.add_edge(ColdTransport, MarketTargeting)
root.order.add_edge(MarketTargeting, RetailPlacement)
root.order.add_edge(RetailPlacement, FeedbackGathering)