# Generated from: 4ca0ed2b-c3f6-40b4-b6ab-0ec288ed8b5c.json
# Description: This process involves sourcing rare artisan cheeses from small-scale producers worldwide, verifying quality through expert tasting panels, and coordinating logistics for timely delivery to a centralized auction house. The auction includes online and in-person bidding, real-time price adjustments based on demand, and post-auction quality assurance. Successful bidders engage in customized packaging and expedited shipping while maintaining strict temperature controls. The process concludes with detailed feedback collection from buyers and producers to refine future auctions and enhance product offerings, ensuring the preservation of traditional cheese-making techniques and fostering a global community of connoisseurs.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Source_Cheeses = Transition(label='Source Cheeses')
Verify_Quality = Transition(label='Verify Quality')
Schedule_Tasting = Transition(label='Schedule Tasting')
Conduct_Tasting = Transition(label='Conduct Tasting')
Evaluate_Feedback = Transition(label='Evaluate Feedback')
Arrange_Logistics = Transition(label='Arrange Logistics')
Prepare_Auction = Transition(label='Prepare Auction')
Open_Bidding = Transition(label='Open Bidding')
Monitor_Prices = Transition(label='Monitor Prices')
Close_Auction = Transition(label='Close Auction')
Confirm_Winners = Transition(label='Confirm Winners')
Coordinate_Packaging = Transition(label='Coordinate Packaging')
Initiate_Shipping = Transition(label='Initiate Shipping')
Track_Delivery = Transition(label='Track Delivery')
Collect_Feedback = Transition(label='Collect Feedback')
Analyze_Results = Transition(label='Analyze Results')

# Partial order for sourcing and quality verification
source_quality_po = StrictPartialOrder(
    nodes=[Source_Cheeses, Verify_Quality, Schedule_Tasting, Conduct_Tasting]
)
source_quality_po.order.add_edge(Source_Cheeses, Verify_Quality)
source_quality_po.order.add_edge(Verify_Quality, Schedule_Tasting)
source_quality_po.order.add_edge(Schedule_Tasting, Conduct_Tasting)

# Partial order for logistics preparation before auction
logistics_prep_po = StrictPartialOrder(
    nodes=[Arrange_Logistics, Prepare_Auction]
)
logistics_prep_po.order.add_edge(Arrange_Logistics, Prepare_Auction)

# Loop for bidding: Open Bidding then looping Monitor Prices until Close Auction
bidding_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Open_Bidding, Monitor_Prices]
)

# Close auction then confirm winners
close_confirm_po = StrictPartialOrder(
    nodes=[Close_Auction, Confirm_Winners]
)
close_confirm_po.order.add_edge(Close_Auction, Confirm_Winners)

# Packaging and shipping in partial order
packaging_shipping_po = StrictPartialOrder(
    nodes=[Coordinate_Packaging, Initiate_Shipping, Track_Delivery]
)
packaging_shipping_po.order.add_edge(Coordinate_Packaging, Initiate_Shipping)
packaging_shipping_po.order.add_edge(Initiate_Shipping, Track_Delivery)

# Feedback collection and analysis partial order
feedback_po = StrictPartialOrder(
    nodes=[Collect_Feedback, Evaluate_Feedback, Analyze_Results]
)
feedback_po.order.add_edge(Collect_Feedback, Evaluate_Feedback)
feedback_po.order.add_edge(Evaluate_Feedback, Analyze_Results)

# Combine after sourcing and tasting: arrange logistics and prepare auction
pre_auction_po = StrictPartialOrder(
    nodes=[source_quality_po, logistics_prep_po]
)
pre_auction_po.order.add_edge(source_quality_po, logistics_prep_po)

# Combine post auction steps:
post_auction_po = StrictPartialOrder(
    nodes=[close_confirm_po, packaging_shipping_po, feedback_po]
)
post_auction_po.order.add_edge(close_confirm_po, packaging_shipping_po)
post_auction_po.order.add_edge(packaging_shipping_po, feedback_po)

# Root partial order combining the big stages:
root = StrictPartialOrder(
    nodes=[pre_auction_po, bidding_loop, post_auction_po]
)
root.order.add_edge(pre_auction_po, bidding_loop)
root.order.add_edge(bidding_loop, post_auction_po)