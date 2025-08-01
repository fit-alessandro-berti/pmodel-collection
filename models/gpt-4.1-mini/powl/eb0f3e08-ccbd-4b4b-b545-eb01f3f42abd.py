# Generated from: eb0f3e08-ccbd-4b4b-b545-eb01f3f42abd.json
# Description: This process manages an adaptive urban farming system integrating IoT sensor data, local weather forecasts, and community input to optimize crop growth cycles in constrained city environments. It involves real-time monitoring, dynamic resource allocation, pest detection with AI, nutrient adjustment, and community-driven crop selection. The system adapts to sudden environmental changes and market demand fluctuations by recalibrating planting schedules and harvesting plans, ensuring sustainable yield and waste minimization while promoting local engagement and education.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Sensor_Setup = Transition(label='Sensor Setup')
Data_Collection = Transition(label='Data Collection')
Weather_Check = Transition(label='Weather Check')
Soil_Testing = Transition(label='Soil Testing')
Crop_Selection = Transition(label='Crop Selection')
Resource_Assign = Transition(label='Resource Assign')
Irrigation_Adjust = Transition(label='Irrigation Adjust')
Pest_Scan = Transition(label='Pest Scan')
Nutrient_Mix = Transition(label='Nutrient Mix')
Growth_Monitor = Transition(label='Growth Monitor')
Community_Poll = Transition(label='Community Poll')
Schedule_Update = Transition(label='Schedule Update')
Harvest_Plan = Transition(label='Harvest Plan')
Waste_Sort = Transition(label='Waste Sort')
Yield_Report = Transition(label='Yield Report')

# The process: 
# Initial setup and data gathering (Sensor Setup --> Data Collection --> Weather Check & Soil Testing concur)
init_PO = StrictPartialOrder(nodes=[Sensor_Setup, Data_Collection, Weather_Check, Soil_Testing])
init_PO.order.add_edge(Sensor_Setup, Data_Collection)
init_PO.order.add_edge(Data_Collection, Weather_Check)
init_PO.order.add_edge(Data_Collection, Soil_Testing)  # Weather Check and Soil Testing concurrent after Data Collection

# Crop Selection and Resource Assign after data collection and environment checks (concurrently Weather Check & Soil Testing)
crop_resource_PO = StrictPartialOrder(nodes=[Crop_Selection, Resource_Assign])
# No explicit order - after Weather Check and Soil Testing (modeled in outer PO)

# Adjustments cycle: IRRIGATION_ADJUST, PEST_SCAN, NUTRIENT_MIX all partially ordered (can overlap)
adjust_nodes = [Irrigation_Adjust, Pest_Scan, Nutrient_Mix]
adjust_PO = StrictPartialOrder(nodes=adjust_nodes)
# No order edges - partially concurrent activities

# Growth monitoring with community input and schedule update loop:
# Loop: Growth Monitor --> choice(exit or (Community Poll --> Schedule Update --> Growth Monitor))
community_schedule_loop_body = StrictPartialOrder(nodes=[Community_Poll, Schedule_Update])
community_schedule_loop_body.order.add_edge(Community_Poll, Schedule_Update)

loop = OperatorPOWL(operator=Operator.LOOP, children=[Growth_Monitor, community_schedule_loop_body])

# Harvesting and reporting steps follow after the loop ends
harvest_PO = StrictPartialOrder(nodes=[Harvest_Plan, Waste_Sort, Yield_Report])
harvest_PO.order.add_edge(Harvest_Plan, Waste_Sort)
harvest_PO.order.add_edge(Waste_Sort, Yield_Report)

# Now combine all parts in partial order form

# Combine crop/resource with adjustments - these can be after Weather Check & Soil Testing, crop selection before adjustments makes sense
crop_adjust_PO = StrictPartialOrder(
    nodes=[crop_resource_PO, adjust_PO]
)
# Resource Assign most likely precedes adjustments to allocate resources
crop_adjust_PO.order.add_edge(crop_resource_PO, adjust_PO)  # Depend on crop_selection/resource assign before adjustments

# Top-level PO combining initial data gathering, crop/adjust, loop, and harvest/report
root = StrictPartialOrder(
    nodes=[init_PO, crop_adjust_PO, loop, harvest_PO]
)
# Edges defining order across these nodes:
# Initial data gathering before crop/resource assign
root.order.add_edge(init_PO, crop_adjust_PO)
# Adjustments finish before starting loop (growth monitoring loop)
root.order.add_edge(crop_adjust_PO, loop)
# Loop terminates before harvest/report
root.order.add_edge(loop, harvest_PO)