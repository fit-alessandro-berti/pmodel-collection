# Generated from: cecb614a-5f59-4f66-b359-da5c9b70a4b8.json
# Description: This process outlines the establishment of an urban rooftop farm on commercial buildings, integrating environmental assessments, resource logistics, and community engagement. It involves evaluating structural integrity, selecting crop varieties suited for microclimates, installing irrigation systems, and coordinating with local authorities for compliance. Continuous monitoring of soil health and pest control is combined with marketing strategies to promote farm-to-table initiatives. The process also includes training sessions for staff and residents, waste recycling protocols, and seasonal harvest planning to maximize yield while ensuring sustainability and social impact within densely populated urban areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey    = Transition(label='Site Survey')
load_testing   = Transition(label='Load Testing')
permits_acquire= Transition(label='Permits Acquire')
supplier_out   = Transition(label='Supplier Outreach')
crop_selection = Transition(label='Crop Selection')
soil_prep      = Transition(label='Soil Prep')
irrigation     = Transition(label='Irrigation Setup')
planting       = Transition(label='Planting Seedlings')
pest_monitor   = Transition(label='Pest Monitoring')
nutrient_test  = Transition(label='Nutrient Testing')
waste_sort     = Transition(label='Waste Sorting')
yield_track    = Transition(label='Yield Tracking')
staff_train    = Transition(label='Staff Training')
community_meet = Transition(label='Community Meet')
harvest_plan   = Transition(label='Harvest Planning')
market_launch  = Transition(label='Market Launch')

# Silent transition for loop exit
skip = SilentTransition()

# Loop body: continuous monitoring sub‐process
loop_body = StrictPartialOrder(nodes=[pest_monitor, nutrient_test, waste_sort, yield_track])
loop_body.order.add_edge(pest_monitor, nutrient_test)
loop_body.order.add_edge(nutrient_test, waste_sort)
loop_body.order.add_edge(waste_sort, yield_track)

# Define the monitoring loop: repeat the loop_body until exit
monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, skip])

# Build the overall process as a strict partial order
root = StrictPartialOrder(nodes=[
    site_survey, load_testing,
    permits_acquire, supplier_out,
    crop_selection, soil_prep, irrigation, planting,
    staff_train, community_meet,
    monitoring_loop,
    harvest_plan, market_launch
])

# Structural integrity checks
root.order.add_edge(site_survey, load_testing)

# Permits and supplier outreach in parallel after testing
root.order.add_edge(load_testing, permits_acquire)
root.order.add_edge(load_testing, supplier_out)

# Crop selection after both permits and suppliers are ready
root.order.add_edge(permits_acquire, crop_selection)
root.order.add_edge(supplier_out, crop_selection)

# Preparation steps
root.order.add_edge(crop_selection, soil_prep)
root.order.add_edge(soil_prep, irrigation)
root.order.add_edge(irrigation, planting)

# After planting: training, community engagement, and monitoring start concurrently
root.order.add_edge(planting, staff_train)
root.order.add_edge(planting, community_meet)
root.order.add_edge(planting, monitoring_loop)

# Harvest planning after training, community meet, and monitoring are done
root.order.add_edge(staff_train, harvest_plan)
root.order.add_edge(community_meet, harvest_plan)
root.order.add_edge(monitoring_loop, harvest_plan)

# Market launch follows harvest planning
root.order.add_edge(harvest_plan, market_launch)