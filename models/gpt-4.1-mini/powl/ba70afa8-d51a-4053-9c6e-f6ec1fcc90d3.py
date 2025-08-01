# Generated from: ba70afa8-d51a-4053-9c6e-f6ec1fcc90d3.json
# Description: This process manages the end-to-end supply chain of an urban vertical farming operation specializing in microgreens and specialty herbs. It includes seed sourcing from niche suppliers, controlled environment planting, automated growth monitoring with AI sensors, nutrient solution adjustments, and on-demand harvesting schedules. Post-harvest, the process incorporates rapid packaging in eco-friendly materials, cold chain logistics with real-time tracking, dynamic order allocation for local markets and restaurants, and feedback loops from clients to optimize crop varieties. The system uniquely integrates waste recycling by converting plant residues into biofertilizers used internally, closing the sustainability loop while maintaining high product quality and minimizing urban footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Seed_Sourcing = Transition(label='Seed Sourcing')
Planting_Setup = Transition(label='Planting Setup')
Growth_Monitoring = Transition(label='Growth Monitoring')
Nutrient_Mixing = Transition(label='Nutrient Mixing')
Climate_Control = Transition(label='Climate Control')
Pest_Scanning = Transition(label='Pest Scanning')
Harvest_Planning = Transition(label='Harvest Planning')
Selective_Picking = Transition(label='Selective Picking')
Waste_Sorting = Transition(label='Waste Sorting')
Biofertilizer_Prep = Transition(label='Biofertilizer Prep')
Packaging_Prep = Transition(label='Packaging Prep')
Cold_Storage = Transition(label='Cold Storage')
Order_Allocation = Transition(label='Order Allocation')
Delivery_Routing = Transition(label='Delivery Routing')
Client_Feedback = Transition(label='Client Feedback')
Data_Analysis = Transition(label='Data Analysis')

# Waste recycling partial order: Waste Sorting --> Biofertilizer Prep
waste_PO = StrictPartialOrder(nodes=[Waste_Sorting, Biofertilizer_Prep])
waste_PO.order.add_edge(Waste_Sorting, Biofertilizer_Prep)

# Growth and monitoring partial order (concurrent where possible)
# Nutrient Mixing, Climate Control, Pest Scanning occur in parallel after Growth Monitoring
growth_PO = StrictPartialOrder(nodes=[Growth_Monitoring, Nutrient_Mixing, Climate_Control, Pest_Scanning])
growth_PO.order.add_edge(Growth_Monitoring, Nutrient_Mixing)
growth_PO.order.add_edge(Growth_Monitoring, Climate_Control)
growth_PO.order.add_edge(Growth_Monitoring, Pest_Scanning)

# Harvest partial order: Harvest Planning --> Selective Picking
harvest_PO = StrictPartialOrder(nodes=[Harvest_Planning, Selective_Picking])
harvest_PO.order.add_edge(Harvest_Planning, Selective_Picking)

# Packaging and cold storage partial order: Packaging Prep --> Cold Storage
package_PO = StrictPartialOrder(nodes=[Packaging_Prep, Cold_Storage])
package_PO.order.add_edge(Packaging_Prep, Cold_Storage)

# Delivery partial order: Order Allocation --> Delivery Routing
delivery_PO = StrictPartialOrder(nodes=[Order_Allocation, Delivery_Routing])
delivery_PO.order.add_edge(Order_Allocation, Delivery_Routing)

# Client feedback and data analysis partial order: Client Feedback --> Data Analysis
feedback_PO = StrictPartialOrder(nodes=[Client_Feedback, Data_Analysis])
feedback_PO.order.add_edge(Client_Feedback, Data_Analysis)

# Loop for growth monitoring and adjustment, i.e. after monitoring we optionally do nutrient mixing,
# climate control, pest scanning again before harvesting. We model the loop as:
# LOOP body: growth_PO (Growth Monitoring + adjustments)
# LOOP redo: Nutrient_Mixing, Climate_Control and Pest_Scanning as a parallel sub PO inside loop's B child
# We'll create a partial order for loop's B child consisting of Nutrient_Mixing, Climate_Control, Pest_Scanning,
# then loop back to the full growth_PO

adjustments = StrictPartialOrder(nodes=[Nutrient_Mixing, Climate_Control, Pest_Scanning])
# No order edges as they are parallel inside adjustments node

loop_growth = OperatorPOWL(operator=Operator.LOOP, children=[growth_PO, adjustments])

# Root PO nodes and ordering:
# Seed Sourcing --> Planting Setup --> loop_growth --> Harvest Planning --> Selective Picking
# Waste sorting and biofertilizer prep run in parallel with harvest and packaging
# Packaging Prep --> Cold Storage
# Cold Storage --> Order Allocation --> Delivery Routing
# Delivery Routing --> Client Feedback --> Data Analysis
# Waste recycling loop closes sustainability loop internally

root = StrictPartialOrder(
    nodes=[
        Seed_Sourcing,
        Planting_Setup,
        loop_growth,
        Harvest_Planning,
        Selective_Picking,
        waste_PO,
        package_PO,
        delivery_PO,
        feedback_PO
    ]
)

# Add ordering edges for main flow
root.order.add_edge(Seed_Sourcing, Planting_Setup)
root.order.add_edge(Planting_Setup, loop_growth)
root.order.add_edge(loop_growth, Harvest_Planning)
root.order.add_edge(Harvest_Planning, Selective_Picking)

# Waste sorting can start after Selective Picking (post-harvest)
root.order.add_edge(Selective_Picking, waste_PO)

# After harvesting and waste sorting, packaging starts
root.order.add_edge(Selective_Picking, package_PO)
root.order.add_edge(waste_PO, package_PO)  # Waste recycling feeds packaging/prep loop internally

# After packaging, cold storage done, then order allocation etc.
root.order.add_edge(package_PO, delivery_PO)

# Delivery leads to feedback and analysis
root.order.add_edge(delivery_PO, feedback_PO)

# The model thus captures concurrency of waste processing and packaging with harvesting,
# as well as the feedback loop at the end.
