# Generated from: a0ec933c-a3a3-4191-b732-c18bc858d9ff.json
# Description: This process describes the end-to-end supply chain for artisanal cheese production, focusing on unique challenges such as seasonal milk sourcing, traditional fermentation monitoring, and small-batch aging. It involves coordination between local dairy farms, quality inspections of raw milk, controlled fermentation environments, handcrafting by cheesemakers, detailed aging schedules, and niche market distribution including direct-to-consumer and boutique retailers. Each step requires specialized skills to maintain authenticity and product integrity, while adapting to fluctuating supply and demand. The process also includes feedback loops for sensory evaluation and recipe adjustments to preserve traditional flavors and textures, ensuring customer satisfaction in a competitive gourmet market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
milkSourcing      = Transition(label='Milk Sourcing')
milkSourcing_loop = Transition(label='Milk Sourcing')    # for the quality‐check loop
qualityCheck      = Transition(label='Quality Check')
milkPasteurize    = Transition(label='Milk Pasteurize')
fermentationStart = Transition(label='Fermentation Start')
phMonitoring      = Transition(label='pH Monitoring')
curdCutting       = Transition(label='Curd Cutting')
wheyDrain         = Transition(label='Whey Drain')
moldingPress      = Transition(label='Molding Press')
saltingStage      = Transition(label='Salting Stage')
initialAging      = Transition(label='Initial Aging')
flipSchedule      = Transition(label='Flip Schedule')
humidityControl   = Transition(label='Humidity Control')
sensoryTest       = Transition(label='Sensory Test')
packagingPrep     = Transition(label='Packaging Prep')
orderFulfill      = Transition(label='Order Fulfill')
customerFeedback  = Transition(label='Customer Feedback')
recipeAdjust      = Transition(label='Recipe Adjust')

# Silent transition for loops that just repeat the monitor
tau = SilentTransition()

# LOOP: after sourcing, check quality; if fail, source again
qualityLoop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[qualityCheck, milkSourcing_loop]
)

# LOOP: periodic pH monitoring during fermentation
phLoop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[phMonitoring, tau]
)

# LOOP: during aging, alternate flip and humidity control
flipLoop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[flipSchedule, humidityControl]
)

# LOOP: after customer feedback, optionally adjust recipe and feedback again
fbLoop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[customerFeedback, recipeAdjust]
)

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    milkSourcing,
    qualityLoop,
    milkPasteurize,
    fermentationStart,
    phLoop,
    curdCutting,
    wheyDrain,
    moldingPress,
    saltingStage,
    initialAging,
    flipLoop,
    sensoryTest,
    packagingPrep,
    orderFulfill,
    fbLoop
])

# Sequencing edges
root.order.add_edge(milkSourcing,   qualityLoop)
root.order.add_edge(qualityLoop,    milkPasteurize)
root.order.add_edge(milkPasteurize, fermentationStart)
root.order.add_edge(fermentationStart, phLoop)
root.order.add_edge(phLoop,         curdCutting)
root.order.add_edge(curdCutting,    wheyDrain)
root.order.add_edge(wheyDrain,      moldingPress)
root.order.add_edge(moldingPress,   saltingStage)
root.order.add_edge(saltingStage,   initialAging)
root.order.add_edge(initialAging,   flipLoop)
root.order.add_edge(flipLoop,       sensoryTest)
root.order.add_edge(sensoryTest,    packagingPrep)
root.order.add_edge(packagingPrep,  orderFulfill)
root.order.add_edge(orderFulfill,   fbLoop)