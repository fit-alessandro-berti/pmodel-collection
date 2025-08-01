# Generated from: 4ca0ed2b-c3f6-40b4-b6ab-0ec288ed8b5c.json
# Description: This process involves sourcing rare artisan cheeses from small-scale producers worldwide, verifying quality through expert tasting panels, and coordinating logistics for timely delivery to a centralized auction house. The auction includes online and in-person bidding, real-time price adjustments based on demand, and post-auction quality assurance. Successful bidders engage in customized packaging and expedited shipping while maintaining strict temperature controls. The process concludes with detailed feedback collection from buyers and producers to refine future auctions and enhance product offerings, ensuring the preservation of traditional cheese-making techniques and fostering a global community of connoisseurs.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
source = Transition(label='Source Cheeses')
verify = Transition(label='Verify Quality')
schedule = Transition(label='Schedule Tasting')
conduct = Transition(label='Conduct Tasting')
eval_feedback = Transition(label='Evaluate Feedback')
arrange = Transition(label='Arrange Logistics')
prepare = Transition(label='Prepare Auction')
open_bid = Transition(label='Open Bidding')
monitor = Transition(label='Monitor Prices')
close = Transition(label='Close Auction')
confirm = Transition(label='Confirm Winners')
packaging = Transition(label='Coordinate Packaging')
shipping = Transition(label='Initiate Shipping')
tracking = Transition(label='Track Delivery')
collect = Transition(label='Collect Feedback')
analyze = Transition(label='Analyze Results')
tau = SilentTransition()

# Loop for real-time price monitoring during the auction
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor, tau])

# Build the partial order
root = StrictPartialOrder(nodes=[
    source, verify, schedule, conduct, eval_feedback,
    arrange, prepare, open_bid, monitor_loop,
    close, confirm, packaging, shipping, tracking, collect, analyze
])

# Define ordering constraints
root.order.add_edge(source, verify)
root.order.add_edge(verify, schedule)
root.order.add_edge(schedule, conduct)
root.order.add_edge(conduct, eval_feedback)
root.order.add_edge(verify, arrange)

root.order.add_edge(eval_feedback, prepare)
root.order.add_edge(arrange, prepare)

root.order.add_edge(prepare, open_bid)
root.order.add_edge(open_bid, monitor_loop)
root.order.add_edge(monitor_loop, close)

root.order.add_edge(close, confirm)
root.order.add_edge(confirm, packaging)
root.order.add_edge(packaging, shipping)
root.order.add_edge(shipping, tracking)

root.order.add_edge(tracking, collect)
root.order.add_edge(collect, analyze)