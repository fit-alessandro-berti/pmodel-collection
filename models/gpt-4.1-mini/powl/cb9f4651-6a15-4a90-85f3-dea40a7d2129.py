# Generated from: cb9f4651-6a15-4a90-85f3-dea40a7d2129.json
# Description: This process outlines the end-to-end supply chain for artisan cheese production, starting from selecting rare milk sources and managing microbial cultures to aging, quality testing, and niche market distribution. It involves coordinating small-scale farmers, custom fermentation, manual aging conditions, rigorous sensory evaluation, and targeted logistics to specialty retailers and gourmet restaurants. The process emphasizes traceability, batch uniqueness, and maintaining optimal conditions for flavor development while handling fluctuating seasonal inputs and demand forecasts.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transition nodes
Milk_Sourcing = Transition(label='Milk Sourcing')
Culture_Prep = Transition(label='Culture Prep')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Milk_Inoculate = Transition(label='Milk Inoculate')
Curd_Formation = Transition(label='Curd Formation')
Curd_Cut = Transition(label='Curd Cut')
Whey_Drain = Transition(label='Whey Drain')
Mold_Inoculate = Transition(label='Mold Inoculate')
Press_Cheese = Transition(label='Press Cheese')
Aging_Setup = Transition(label='Aging Setup')
Humidity_Control = Transition(label='Humidity Control')
Temperature_Monitor = Transition(label='Temperature Monitor')
Quality_Test = Transition(label='Quality Test')
Packaging = Transition(label='Packaging')
Order_Fulfill = Transition(label='Order Fulfill')
Retail_Deliver = Transition(label='Retail Deliver')
Feedback_Collect = Transition(label='Feedback Collect')

# Modeling Aging conditions (Humidity Control and Temperature Monitor) as concurrent partial order
aging_conditions = StrictPartialOrder(nodes=[Humidity_Control, Temperature_Monitor])
# No order between Humidity_Control and Temperature_Monitor (concurrent)

# Modeling Aging Setup followed by aging conditions
aging_phase = StrictPartialOrder(nodes=[Aging_Setup, aging_conditions])
aging_phase.order.add_edge(Aging_Setup, aging_conditions)

# Sensory evaluation includes Quality Test
sensory_eval = Quality_Test

# Modeling the initial Milk Processing sequential steps:
# Milk Sourcing -> Culture Prep -> Milk Pasteurize -> Milk Inoculate -> Curd Formation -> Curd Cut -> Whey Drain
milk_processing = StrictPartialOrder(nodes=[Milk_Sourcing, Culture_Prep, Milk_Pasteurize, Milk_Inoculate,
                                            Curd_Formation, Curd_Cut, Whey_Drain])
milk_processing.order.add_edge(Milk_Sourcing, Culture_Prep)
milk_processing.order.add_edge(Culture_Prep, Milk_Pasteurize)
milk_processing.order.add_edge(Milk_Pasteurize, Milk_Inoculate)
milk_processing.order.add_edge(Milk_Inoculate, Curd_Formation)
milk_processing.order.add_edge(Curd_Formation, Curd_Cut)
milk_processing.order.add_edge(Curd_Cut, Whey_Drain)

# After Whey Drain, Mold Inoculate and Press Cheese in sequence
mold_press = StrictPartialOrder(nodes=[Mold_Inoculate, Press_Cheese])
mold_press.order.add_edge(Mold_Inoculate, Press_Cheese)

# Linking milk_processing -> mold_press
processing_phase = StrictPartialOrder(nodes=[milk_processing, mold_press])
processing_phase.order.add_edge(milk_processing, mold_press)

# Aging phase happens after pressing cheese
processing_to_aging = StrictPartialOrder(nodes=[processing_phase, aging_phase])
processing_to_aging.order.add_edge(processing_phase, aging_phase)

# Order fulfillment chain: Packaging -> Order Fulfill -> Retail Deliver
order_chain = StrictPartialOrder(nodes=[Packaging, Order_Fulfill, Retail_Deliver])
order_chain.order.add_edge(Packaging, Order_Fulfill)
order_chain.order.add_edge(Order_Fulfill, Retail_Deliver)

# Packaging happens after Quality Test and after aging phase (i.e., after sensory eval and aging)
quality_and_aging = StrictPartialOrder(nodes=[sensory_eval, processing_to_aging])
# Sensory evaluation Quality Test depends on aging phase completion
quality_and_aging.order.add_edge(processing_to_aging, sensory_eval)

# Packaging depends on Quality Test
packaging_phase = StrictPartialOrder(nodes=[quality_and_aging, Packaging])
packaging_phase.order.add_edge(quality_and_aging, Packaging)

# Full later chain: packaging_phase -> order_chain
final_chain = StrictPartialOrder(nodes=[packaging_phase, order_chain])
final_chain.order.add_edge(packaging_phase, order_chain)

# Feedback Collect can happen after Retail Deliver, but not necessarily immediately; treat it optionally concurrent with order_chain end
# To model optional feedback, we use choice: either Feedback_Collect or silent skip
skip = SilentTransition()
feedback_choice = OperatorPOWL(operator=Operator.XOR, children=[Feedback_Collect, skip])

# Feedback happens after Retail Deliver
feedback_phase = StrictPartialOrder(nodes=[Retail_Deliver, feedback_choice])
feedback_phase.order.add_edge(Retail_Deliver, feedback_choice)

# Integrate feedback into the final chain replacing Retail Deliver with feedback_phase
# We substitute final_chain nodes to replace Retail_Deliver with feedback_phase - or create new PO with feedback_phase in place of Retail_Deliver

# First, get all nodes from final_chain except Retail_Deliver; introduce feedback_phase instead of Retail_Deliver

# final_chain nodes are [packaging_phase, order_chain]
# order_chain nodes: Packaging, Order Fulfill, Retail Deliver
# Replace Retail_Deliver by feedback_phase in order_chain nodes

# Create order_chain_with_feedback nodes:
packaging_node = Packaging
order_fulfill_node = Order_Fulfill
# Remove Retail_Deliver from order_chain, add feedback_phase
order_chain_nodes_with_feedback = [Packaging, Order_Fulfill, feedback_phase]

order_chain_with_feedback = StrictPartialOrder(nodes=order_chain_nodes_with_feedback)
order_chain_with_feedback.order.add_edge(Packaging, Order_Fulfill)
order_chain_with_feedback.order.add_edge(Order_Fulfill, feedback_phase)

# packaging_phase includes quality_and_aging and Packaging - but Packaging is now in order_chain_with_feedback,
# so we should separate Packaging from packaging_phase to avoid duplication:
# Define quality_and_aging_only = strict PO with sensory_eval and processing_to_aging

quality_and_aging_only = StrictPartialOrder(nodes=[sensory_eval, processing_to_aging])
quality_and_aging_only.order.add_edge(processing_to_aging, sensory_eval)

# packaging_phase is then a strict PO of quality_and_aging_only and Packaging removed:
# We remove Packaging from packaging_phase nodes, so packaging_phase = quality_and_aging_only only now.

# Now final process is quality_and_aging_only -> Packaging -> Order Fulfill -> feedback_phase

# Build final model as StrictPartialOrder with nodes:
# quality_and_aging_only, Packaging, Order_Fulfill, feedback_phase
root_nodes = [quality_and_aging_only, Packaging, Order_Fulfill, feedback_phase]

root = StrictPartialOrder(nodes=root_nodes)
root.order.add_edge(quality_and_aging_only, Packaging)
root.order.add_edge(Packaging, Order_Fulfill)
root.order.add_edge(Order_Fulfill, feedback_phase)