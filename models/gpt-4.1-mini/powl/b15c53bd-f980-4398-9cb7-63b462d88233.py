# Generated from: b15c53bd-f980-4398-9cb7-63b462d88233.json
# Description: This process involves curating a rotating exhibition of emerging digital and physical artworks in a hybrid gallery space. The curator must identify trending artists through social media sentiment analysis, negotiate with international artists remotely, coordinate logistics for fragile shipments, install augmented reality overlays, and manage both physical and virtual visitor engagement. The process requires iterative feedback from diverse audiences, adaptive scheduling for interactive workshops, and real-time adjustments to lighting and display settings based on visitor behavior and environmental conditions. Additionally, it includes post-exhibition data collection for sales forecasting and artist promotion, ensuring sustainability and innovation in contemporary art presentation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Trend_Scan = Transition(label='Trend Scan')
Artist_Outreach = Transition(label='Artist Outreach')
Contract_Draft = Transition(label='Contract Draft')
Shipment_Plan = Transition(label='Shipment Plan')
Customs_Clear = Transition(label='Customs Clear')
Artwork_Install = Transition(label='Artwork Install')
AR_Overlay = Transition(label='AR Overlay')
Visitor_Monitor = Transition(label='Visitor Monitor')
Feedback_Collect = Transition(label='Feedback Collect')
Workshop_Setup = Transition(label='Workshop Setup')
Light_Adjust = Transition(label='Light Adjust')
Display_Calibrate = Transition(label='Display Calibrate')
Sales_Forecast = Transition(label='Sales Forecast')
Promo_Launch = Transition(label='Promo Launch')
Data_Archive = Transition(label='Data Archive')

# We'll model the process roughly as:

# 1. Initial sequence: Trend Scan --> Artist Outreach --> Contract Draft
initial_seq = StrictPartialOrder(nodes=[Trend_Scan, Artist_Outreach, Contract_Draft])
initial_seq.order.add_edge(Trend_Scan, Artist_Outreach)
initial_seq.order.add_edge(Artist_Outreach, Contract_Draft)

# 2. Shipment logistics: Shipment Plan --> Customs Clear
shipment_seq = StrictPartialOrder(nodes=[Shipment_Plan, Customs_Clear])
shipment_seq.order.add_edge(Shipment_Plan, Customs_Clear)

# 3. Installation & AR overlay: Artwork Install --> AR Overlay
install_seq = StrictPartialOrder(nodes=[Artwork_Install, AR_Overlay])
install_seq.order.add_edge(Artwork_Install, AR_Overlay)

# 4. Visitor engagement partial order of concurrent activities:
#    Visitor Monitor || Feedback Collect || Workshop Setup
visitor_engagement = StrictPartialOrder(nodes=[Visitor_Monitor, Feedback_Collect, Workshop_Setup])
# no edges: concurrent

# 5. Adaptive adjustments partial order:
#    Light Adjust and Display Calibrate in parallel (no order)
adjustments = StrictPartialOrder(nodes=[Light_Adjust, Display_Calibrate])
# no edges

# 6. Post-exhibition data activities: Sales Forecast --> Promo Launch --> Data Archive
post_exhibit = StrictPartialOrder(nodes=[Sales_Forecast, Promo_Launch, Data_Archive])
post_exhibit.order.add_edge(Sales_Forecast, Promo_Launch)
post_exhibit.order.add_edge(Promo_Launch, Data_Archive)

# 7. Loop for iterative feedback and scheduling:
#    Loop body: Feedback Collect and Workshop Setup (concurrent)
feedback_and_workshop = StrictPartialOrder(nodes=[Feedback_Collect, Workshop_Setup])
# no edges inside

# The loop is: * (feedback_and_workshop, Visitor Monitor)
# Meaning: execute feedback_and_workshop once,
# then choose to exit, or execute Visitor Monitor and feedback_and_workshop again
loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_and_workshop, Visitor_Monitor])

# Assemble full process as partial order

# Combine shipment plans and installation parts in sequence after Contract Draft
logistics_and_install = StrictPartialOrder(
    nodes=[shipment_seq, install_seq]
)
logistics_and_install.order.add_edge(shipment_seq, install_seq)

# Combine visitor engagement and adjustments concurrent
visitor_and_adjust = StrictPartialOrder(
    nodes=[visitor_engagement, adjustments]
)
# no edges => concurrent

# Combine post exhibition after visitor and adjustments
post_after_engagement = StrictPartialOrder(
    nodes=[visitor_and_adjust, post_exhibit]
)
post_after_engagement.order.add_edge(visitor_and_adjust, post_exhibit)

# Combine loop into visitor engagement:

# Instead of visitor_engagement, replace Feedback Collect and Workshop Setup by the loop
# visitor_engagement was Visitor Monitor || Feedback Collect || Workshop Setup
# Now we have loop for Feedback Collect and Workshop Setup and Visitor Monitor inside loop as second child
# This matches the loop structure, but our loop is: * (feedback_and_workshop, Visitor Monitor)
# So actually Visitor Monitor is part of loop body through second child.

# Let's create top level model in sequence:
# initial_seq --> logistics_and_install --> loop --> adjustments & visitor monitor, but visitor monitor is in loop.

# After loop, post exhibit.

# Actually adjustments and visitor monitor are inside loop and visitor engagement, so we have:
# initial_seq --> logistics_and_install --> loop --> adjustments --> post_exhibit

# Assemble root:
root = StrictPartialOrder(
    nodes=[initial_seq, logistics_and_install, loop, adjustments, post_exhibit]
)
root.order.add_edge(initial_seq, logistics_and_install)
root.order.add_edge(logistics_and_install, loop)
root.order.add_edge(loop, adjustments)
root.order.add_edge(adjustments, post_exhibit)