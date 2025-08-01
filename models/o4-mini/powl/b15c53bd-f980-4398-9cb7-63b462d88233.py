# Generated from: b15c53bd-f980-4398-9cb7-63b462d88233.json
# Description: This process involves curating a rotating exhibition of emerging digital and physical artworks in a hybrid gallery space. The curator must identify trending artists through social media sentiment analysis, negotiate with international artists remotely, coordinate logistics for fragile shipments, install augmented reality overlays, and manage both physical and virtual visitor engagement. The process requires iterative feedback from diverse audiences, adaptive scheduling for interactive workshops, and real-time adjustments to lighting and display settings based on visitor behavior and environmental conditions. Additionally, it includes post-exhibition data collection for sales forecasting and artist promotion, ensuring sustainability and innovation in contemporary art presentation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
trend_scan        = Transition(label='Trend Scan')
artist_outreach   = Transition(label='Artist Outreach')
contract_draft    = Transition(label='Contract Draft')
shipment_plan     = Transition(label='Shipment Plan')
customs_clear     = Transition(label='Customs Clear')
artwork_install   = Transition(label='Artwork Install')
ar_overlay        = Transition(label='AR Overlay')
visitor_monitor   = Transition(label='Visitor Monitor')
feedback_collect  = Transition(label='Feedback Collect')
workshop_setup    = Transition(label='Workshop Setup')
light_adjust      = Transition(label='Light Adjust')
display_calibrate = Transition(label='Display Calibrate')
sales_forecast    = Transition(label='Sales Forecast')
promo_launch      = Transition(label='Promo Launch')
data_archive      = Transition(label='Data Archive')

# Inner partial order for concurrent adjustments and feedback
inner_PO = StrictPartialOrder(
    nodes=[
        feedback_collect,
        workshop_setup,
        light_adjust,
        display_calibrate
    ]
)
# No edges in inner_PO => these four run concurrently

# Loop: monitor visitors, then do adjustments & feedback, repeat until exit
exhibition_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[visitor_monitor, inner_PO]
)

# Root workflow: sequential setup, installation, looped exhibition, and teardown
root = StrictPartialOrder(
    nodes=[
        trend_scan,
        artist_outreach,
        contract_draft,
        shipment_plan,
        customs_clear,
        artwork_install,
        ar_overlay,
        exhibition_loop,
        sales_forecast,
        promo_launch,
        data_archive
    ]
)

# Define the partial order (strict sequence)
root.order.add_edge(trend_scan, artist_outreach)
root.order.add_edge(artist_outreach, contract_draft)
root.order.add_edge(contract_draft, shipment_plan)
root.order.add_edge(shipment_plan, customs_clear)
root.order.add_edge(customs_clear, artwork_install)
root.order.add_edge(artwork_install, ar_overlay)
root.order.add_edge(ar_overlay, exhibition_loop)
root.order.add_edge(exhibition_loop, sales_forecast)
root.order.add_edge(sales_forecast, promo_launch)
root.order.add_edge(promo_launch, data_archive)