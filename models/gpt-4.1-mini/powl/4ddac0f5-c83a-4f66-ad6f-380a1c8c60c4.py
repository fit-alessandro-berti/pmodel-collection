# Generated from: 4ddac0f5-c83a-4f66-ad6f-380a1c8c60c4.json
# Description: This process outlines the comprehensive cycle of managing an urban vertical farm designed for sustainable, year-round crop production in a controlled environment. It includes initial site analysis, structural setup, nutrient formulation, seed selection, climate regulation, automated planting, continuous monitoring, pest control using biological agents, hydroponic nutrient adjustments, light spectrum tuning, harvesting schedules, waste recycling, data analytics for yield optimization, and distribution logistics. The process ensures minimal resource use while maximizing output through integration of IoT sensors and AI-driven decision making, all adapted to urban constraints and consumer demand fluctuations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition, OperatorPOWL
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Survey = Transition(label='Site Survey')
Structure_Build = Transition(label='Structure Build')
Nutrient_Mix = Transition(label='Nutrient Mix')
Seed_Selection = Transition(label='Seed Selection')
Climate_Set = Transition(label='Climate Set')
Planting_Auto = Transition(label='Planting Auto')
Sensor_Install = Transition(label='Sensor Install')
Pest_Control = Transition(label='Pest Control')
Water_Adjust = Transition(label='Water Adjust')
Light_Tune = Transition(label='Light Tune')
Growth_Monitor = Transition(label='Growth Monitor')
Harvest_Plan = Transition(label='Harvest Plan')
Waste_Recycle = Transition(label='Waste Recycle')
Yield_Analyze = Transition(label='Yield Analyze')
Logistics_Prep = Transition(label='Logistics Prep')
Data_Sync = Transition(label='Data Sync')

# Model pest control interventions loop: Pest_Control, then Water_Adjust, then Light_Tune repeatedly
# Loop body B = sequence Pest_Control -> Water_Adjust -> Light_Tune
pest_loop_body = StrictPartialOrder(nodes=[Pest_Control, Water_Adjust, Light_Tune])
pest_loop_body.order.add_edge(Pest_Control, Water_Adjust)
pest_loop_body.order.add_edge(Water_Adjust, Light_Tune)

# Construct the loop node: Execute Growth_Monitor, then choose to exit or do pest_loop_body and repeat
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[Growth_Monitor, pest_loop_body])

# Build the main workflow partial order
root = StrictPartialOrder(nodes=[
    Site_Survey,
    Structure_Build,
    Nutrient_Mix,
    Seed_Selection,
    Climate_Set,
    Planting_Auto,
    Sensor_Install,
    pest_loop,
    Harvest_Plan,
    Waste_Recycle,
    Yield_Analyze,
    Logistics_Prep,
    Data_Sync
])

# Define ordering according to process description:

# Start: Site Survey -> Structure Build -> Nutrient Mix -> Seed Selection -> Climate Set -> Planting Auto -> Sensor Install
root.order.add_edge(Site_Survey, Structure_Build)
root.order.add_edge(Structure_Build, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Seed_Selection)
root.order.add_edge(Seed_Selection, Climate_Set)
root.order.add_edge(Climate_Set, Planting_Auto)
root.order.add_edge(Planting_Auto, Sensor_Install)

# Sensor Install -> Growth Monitor (part of pest_loop children[0])
root.order.add_edge(Sensor_Install, pest_loop)

# pest_loop is a loop starting with Growth Monitor, then loops pest control activities

# After pest_loop finishes -> Harvest Plan -> Waste Recycle -> Yield Analyze -> Logistics Prep -> Data Sync
root.order.add_edge(pest_loop, Harvest_Plan)
root.order.add_edge(Harvest_Plan, Waste_Recycle)
root.order.add_edge(Waste_Recycle, Yield_Analyze)
root.order.add_edge(Yield_Analyze, Logistics_Prep)
root.order.add_edge(Logistics_Prep, Data_Sync)