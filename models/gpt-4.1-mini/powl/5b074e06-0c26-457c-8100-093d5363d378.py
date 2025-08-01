# Generated from: 5b074e06-0c26-457c-8100-093d5363d378.json
# Description: This process outlines the intricate steps involved in producing and distributing artisanal cheese from farm to boutique retail. It begins with selective milk sourcing from specific breeds of livestock, followed by precise milk testing and standardization. The milk is then cultured using unique bacterial blends before curdling and gentle cutting. After molding and initial aging, the cheese undergoes repeated washing and brushing to develop its rind. Quality control includes sensory evaluation and microbial testing. Packaging is customized to preserve flavor and texture, with cold chain logistics ensuring freshness during transport. Marketing targets niche markets emphasizing provenance and craftsmanship, culminating in boutique retail placement and consumer feedback collection to refine future batches.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
milk_sourcing = Transition(label='Milk Sourcing')
milk_testing = Transition(label='Milk Testing')
milk_standardization = Transition(label='Milk Standardization')
culture_preparation = Transition(label='Culture Preparation')
milk_culturing = Transition(label='Milk Culturing')
curd_cutting = Transition(label='Curd Cutting')
molding_cheese = Transition(label='Molding Cheese')
initial_aging = Transition(label='Initial Aging')
rind_washing = Transition(label='Rind Washing')
rind_brushing = Transition(label='Rind Brushing')
sensory_check = Transition(label='Sensory Check')
microbial_test = Transition(label='Microbial Test')
custom_packaging = Transition(label='Custom Packaging')
cold_transport = Transition(label='Cold Transport')
market_targeting = Transition(label='Market Targeting')
retail_placement = Transition(label='Retail Placement')
feedback_gathering = Transition(label='Feedback Gathering')

# Loop for repeated washing and brushing rind
rind_loop = OperatorPOWL(operator=Operator.LOOP, children=[rind_washing, rind_brushing])

# Quality control choices (both must be done, so in partial order)
qc = StrictPartialOrder(nodes=[sensory_check, microbial_test])
# no order between sensory_check and microbial_test, so concurrent

# Packaging and logistics partial order
pack_and_cold = StrictPartialOrder(nodes=[custom_packaging, cold_transport])
pack_and_cold.order.add_edge(custom_packaging, cold_transport)

# Marketing and retail partial order
market_and_retail = StrictPartialOrder(nodes=[market_targeting, retail_placement])
market_and_retail.order.add_edge(market_targeting, retail_placement)

# Overall ordering partial order
root = StrictPartialOrder(
    nodes=[
        milk_sourcing,
        milk_testing,
        milk_standardization,
        culture_preparation,
        milk_culturing,
        curd_cutting,
        molding_cheese,
        initial_aging,
        rind_loop,
        qc,
        pack_and_cold,
        market_and_retail,
        feedback_gathering
    ]
)

# Define needed orders (sequential steps)
root.order.add_edge(milk_sourcing, milk_testing)
root.order.add_edge(milk_testing, milk_standardization)
root.order.add_edge(milk_standardization, culture_preparation)
root.order.add_edge(culture_preparation, milk_culturing)
root.order.add_edge(milk_culturing, curd_cutting)
root.order.add_edge(curd_cutting, molding_cheese)
root.order.add_edge(molding_cheese, initial_aging)
root.order.add_edge(initial_aging, rind_loop)
root.order.add_edge(rind_loop, qc)
root.order.add_edge(qc, pack_and_cold)
root.order.add_edge(pack_and_cold, market_and_retail)
root.order.add_edge(market_and_retail, feedback_gathering)