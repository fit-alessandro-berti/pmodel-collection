# Generated from: 3fa3435c-0f0e-4f99-8f5b-8ceca61852b3.json
# Description: This process describes the detailed steps involved in producing and distributing artisanal cheese from farm to consumer. It begins with sourcing rare milk varieties from select farms, followed by specialized fermentation and aging techniques in controlled environments. Quality inspections occur at multiple stages to ensure flavor consistency and safety. Packaging is done using eco-friendly materials with custom labeling. The process also includes coordinating niche marketing campaigns targeting gourmet retailers and direct consumer subscriptions. Logistics are managed with temperature-controlled transport and real-time tracking to preserve product integrity, culminating in customer feedback analysis to refine future batches and supply strategies.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
ms           = Transition(label='Milk Sourcing')
qt1          = Transition(label='Quality Testing')
pasteurize   = Transition(label='Milk Pasteurize')
starter      = Transition(label='Starter Culture')
curd         = Transition(label='Curd Cutting')
whey         = Transition(label='Whey Drain')
mold         = Transition(label='Mold Inoculate')
press        = Transition(label='Press Cheese')
aging        = Transition(label='Aging Control')
humidity     = Transition(label='Humidity Check')
tasting      = Transition(label='Flavor Tasting')
pack         = Transition(label='Eco Packaging')
label        = Transition(label='Label Design')
market       = Transition(label='Market Targeting')
setup        = Transition(label='Transport Setup')
temp         = Transition(label='Temp Monitor')
delivery     = Transition(label='Retail Delivery')
survey       = Transition(label='Customer Survey')

# Fermentation sequence: Pasteurize -> Starter -> Curd -> Whey -> Mold -> Press
fermentation = StrictPartialOrder(nodes=[pasteurize, starter, curd, whey, mold, press])
fermentation.order.add_edge(pasteurize, starter)
fermentation.order.add_edge(starter, curd)
fermentation.order.add_edge(curd, whey)
fermentation.order.add_edge(whey, mold)
fermentation.order.add_edge(mold, press)

# Aging-inspection sub-process: Humidity Check -> Flavor Tasting
aging_inspection = StrictPartialOrder(nodes=[humidity, tasting])
aging_inspection.order.add_edge(humidity, tasting)

# Loop: do Aging Control, then either exit or run inspections then age again
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging, aging_inspection])

# Packaging: Eco Packaging -> Label Design
packaging = StrictPartialOrder(nodes=[pack, label])
packaging.order.add_edge(pack, label)

# Marketing branch
marketing = StrictPartialOrder(nodes=[market])

# Logistics branch: Setup -> Temp Monitor -> Delivery
logistics = StrictPartialOrder(nodes=[setup, temp, delivery])
logistics.order.add_edge(setup, temp)
logistics.order.add_edge(temp, delivery)

# Assemble the overall model
root = StrictPartialOrder(nodes=[
    ms,
    qt1,
    fermentation,
    aging_loop,
    packaging,
    marketing,
    logistics,
    survey
])
# Define the control-flow edges
root.order.add_edge(ms,        qt1)
root.order.add_edge(qt1,       fermentation)
root.order.add_edge(fermentation, aging_loop)
root.order.add_edge(aging_loop,   packaging)
root.order.add_edge(packaging,    marketing)
root.order.add_edge(packaging,    logistics)
root.order.add_edge(marketing,     survey)
root.order.add_edge(logistics,     survey)