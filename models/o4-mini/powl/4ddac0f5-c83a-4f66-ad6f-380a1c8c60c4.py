# Generated from: 4ddac0f5-c83a-4f66-ad6f-380a1c8c60c4.json
# Description: This process outlines the comprehensive cycle of managing an urban vertical farm designed for sustainable, year-round crop production in a controlled environment. It includes initial site analysis, structural setup, nutrient formulation, seed selection, climate regulation, automated planting, continuous monitoring, pest control using biological agents, hydroponic nutrient adjustments, light spectrum tuning, harvesting schedules, waste recycling, data analytics for yield optimization, and distribution logistics. The process ensures minimal resource use while maximizing output through integration of IoT sensors and AI-driven decision making, all adapted to urban constraints and consumer demand fluctuations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey     = Transition(label="Site Survey")
structure_build = Transition(label="Structure Build")
nutrient_mix    = Transition(label="Nutrient Mix")
seed_selection  = Transition(label="Seed Selection")
climate_set     = Transition(label="Climate Set")
sensor_install  = Transition(label="Sensor Install")
planting_auto   = Transition(label="Planting Auto")
growth_monitor  = Transition(label="Growth Monitor")
data_sync       = Transition(label="Data Sync")
yield_analyze   = Transition(label="Yield Analyze")
pest_control    = Transition(label="Pest Control")
water_adjust    = Transition(label="Water Adjust")
light_tune      = Transition(label="Light Tune")
harvest_plan    = Transition(label="Harvest Plan")
waste_recycle   = Transition(label="Waste Recycle")
logistics_prep  = Transition(label="Logistics Prep")

# Define the choice among adjustment activities
adjustment_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[pest_control, water_adjust, light_tune]
)

# Pack Data Sync -> Yield Analyze -> Adjustment Choice into a partial order B
B = StrictPartialOrder(nodes=[data_sync, yield_analyze, adjustment_choice])
B.order.add_edge(data_sync, yield_analyze)
B.order.add_edge(yield_analyze, adjustment_choice)

# Define the loop: Growth Monitor is A; B is the body for adjustments
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitor, B]
)

# Build the top‐level sequence as a strict partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    structure_build,
    nutrient_mix,
    seed_selection,
    climate_set,
    sensor_install,
    planting_auto,
    monitor_loop,
    harvest_plan,
    waste_recycle,
    logistics_prep
])

# Add the control‐flow edges
root.order.add_edge(site_survey,     structure_build)
root.order.add_edge(structure_build, nutrient_mix)
root.order.add_edge(nutrient_mix,    seed_selection)
root.order.add_edge(seed_selection,  climate_set)
root.order.add_edge(climate_set,     sensor_install)
root.order.add_edge(sensor_install,  planting_auto)
root.order.add_edge(planting_auto,   monitor_loop)
root.order.add_edge(monitor_loop,    harvest_plan)
root.order.add_edge(harvest_plan,    waste_recycle)
root.order.add_edge(waste_recycle,   logistics_prep)