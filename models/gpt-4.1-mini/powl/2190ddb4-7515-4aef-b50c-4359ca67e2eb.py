# Generated from: 2190ddb4-7515-4aef-b50c-4359ca67e2eb.json
# Description: This process outlines the complex cycle of managing an urban vertical farm, integrating advanced hydroponics and AI-driven environmental controls. It involves seed selection, nutrient blending, automated planting, continuous monitoring of microclimates, pest detection through computer vision, adaptive lighting adjustments, precision harvesting, and waste recycling. The process ensures optimal crop yield while minimizing water and energy consumption. Additionally, it includes data analytics to forecast demand and adjust production schedules dynamically, combined with logistics coordination for just-in-time delivery to local markets. This atypical business process leverages technology and sustainability principles to revolutionize urban agriculture in confined spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions corresponding to the activities
Seed_Selection = Transition(label='Seed Selection')
Nutrient_Blend = Transition(label='Nutrient Blend')
Automated_Planting = Transition(label='Automated Planting')

Microclimate_Scan = Transition(label='Microclimate Scan')
Pest_Detection = Transition(label='Pest Detection')
Light_Adjustment = Transition(label='Light Adjustment')
Growth_Monitoring = Transition(label='Growth Monitoring')

Water_Recycling = Transition(label='Water Recycling')

Harvest_Planning = Transition(label='Harvest Planning')
Precision_Harvest = Transition(label='Precision Harvest')
Waste_Processing = Transition(label='Waste Processing')

Yield_Forecast = Transition(label='Yield Forecast')
Demand_Analysis = Transition(label='Demand Analysis')
Schedule_Update = Transition(label='Schedule Update')

Logistics_Sync = Transition(label='Logistics Sync')
Market_Delivery = Transition(label='Market Delivery')

# Build partial order for the initial crop setup:
# Seed Selection --> Nutrient Blend --> Automated Planting
setup = StrictPartialOrder(nodes=[Seed_Selection, Nutrient_Blend, Automated_Planting])
setup.order.add_edge(Seed_Selection, Nutrient_Blend)
setup.order.add_edge(Nutrient_Blend, Automated_Planting)

# Monitoring cycle loop: loop(
#    A = monitoring group (Microclimate Scan, Pest Detection, Light Adjustment, Growth Monitoring) in parallel,
#    B = Water Recycling
# )
monitoring_nodes = [Microclimate_Scan, Pest_Detection, Light_Adjustment, Growth_Monitoring]
monitoring = StrictPartialOrder(nodes=monitoring_nodes)  # all concurrent, no order edges

monitoring_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitoring, Water_Recycling]
)

# Harvest phase: Harvest Planning --> Precision Harvest --> Waste Processing
harvest = StrictPartialOrder(nodes=[Harvest_Planning, Precision_Harvest, Waste_Processing])
harvest.order.add_edge(Harvest_Planning, Precision_Harvest)
harvest.order.add_edge(Precision_Harvest, Waste_Processing)

# Analytics phase: Yield Forecast --> Demand Analysis --> Schedule Update
analytics = StrictPartialOrder(nodes=[Yield_Forecast, Demand_Analysis, Schedule_Update])
analytics.order.add_edge(Yield_Forecast, Demand_Analysis)
analytics.order.add_edge(Demand_Analysis, Schedule_Update)

# Logistics phase: Logistics Sync --> Market Delivery
logistics = StrictPartialOrder(nodes=[Logistics_Sync, Market_Delivery])
logistics.order.add_edge(Logistics_Sync, Market_Delivery)

# Compose all main phases into one big StrictPartialOrder with dependencies:
# setup --> monitoring_loop --> harvest --> analytics --> logistics

root = StrictPartialOrder(
    nodes=[setup, monitoring_loop, harvest, analytics, logistics]
)
root.order.add_edge(setup, monitoring_loop)
root.order.add_edge(monitoring_loop, harvest)
root.order.add_edge(harvest, analytics)
root.order.add_edge(analytics, logistics)