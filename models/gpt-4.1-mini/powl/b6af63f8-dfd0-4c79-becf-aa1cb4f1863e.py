# Generated from: b6af63f8-dfd0-4c79-becf-aa1cb4f1863e.json
# Description: This process outlines the comprehensive operational cycle of an urban vertical farm that integrates advanced hydroponic systems, AI-driven climate controls, and automated harvesting robots. Starting from seed selection optimized for urban microclimates, it progresses through nutrient blending, growth monitoring via IoT sensors, and pest management using biocontrol agents. The process also includes energy recycling from waste biomass, real-time yield prediction algorithms, and adaptive lighting schedules to maximize photosynthesis efficiency. Finally, harvested crops undergo quality scanning, packaging with smart labels for traceability, and urban distribution logistics optimized for minimal carbon footprint. This atypical but realistic process blends agriculture, technology, and sustainability into a continuous loop designed for dense metropolitan environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Seed_Select = Transition(label='Seed Select')
Nutrient_Mix = Transition(label='Nutrient Mix')
Planting_Setup = Transition(label='Planting Setup')
Climate_Adjust = Transition(label='Climate Adjust')
IoT_Monitor = Transition(label='IoT Monitor')
Pest_Control = Transition(label='Pest Control')
Growth_Analyze = Transition(label='Growth Analyze')
Light_Schedule = Transition(label='Light Schedule')
Water_Recycle = Transition(label='Water Recycle')
Energy_Capture = Transition(label='Energy Capture')
Robot_Harvest = Transition(label='Robot Harvest')
Quality_Scan = Transition(label='Quality Scan')
Smart_Label = Transition(label='Smart Label')
Pack_Produce = Transition(label='Pack Produce')
Urban_Dispatch = Transition(label='Urban Dispatch')
Waste_Process = Transition(label='Waste Process')
Yield_Predict = Transition(label='Yield Predict')

# Partial order for the initial growth setup and monitoring:
# Seed Select -> Nutrient Mix -> Planting Setup -> Climate Adjust
# Then IoT Monitor -> Pest Control -> Growth Analyze -> Light Schedule

growth_setup = StrictPartialOrder(
    nodes=[Seed_Select, Nutrient_Mix, Planting_Setup, Climate_Adjust,
           IoT_Monitor, Pest_Control, Growth_Analyze, Light_Schedule]
)
growth_setup.order.add_edge(Seed_Select, Nutrient_Mix)
growth_setup.order.add_edge(Nutrient_Mix, Planting_Setup)
growth_setup.order.add_edge(Planting_Setup, Climate_Adjust)

growth_setup.order.add_edge(Climate_Adjust, IoT_Monitor)
growth_setup.order.add_edge(IoT_Monitor, Pest_Control)
growth_setup.order.add_edge(Pest_Control, Growth_Analyze)
growth_setup.order.add_edge(Growth_Analyze, Light_Schedule)

# Partial order for resource recycling - can run concurrently with growth monitoring
# Water Recycle and Energy Capture, Waste Process

recycling = StrictPartialOrder(
    nodes=[Water_Recycle, Energy_Capture, Waste_Process]
)
# No order constraints between these three; they run concurrently

# Yield prediction happens after growth analysis (depends on analysis)
# We'll link it later in the main PO

# After growth and recycling, harvesting and packaging flow:
# Robot Harvest -> Quality Scan -> Smart Label -> Pack Produce -> Urban Dispatch

harvest_packaging = StrictPartialOrder(
    nodes=[Robot_Harvest, Quality_Scan, Smart_Label, Pack_Produce, Urban_Dispatch]
)
harvest_packaging.order.add_edge(Robot_Harvest, Quality_Scan)
harvest_packaging.order.add_edge(Quality_Scan, Smart_Label)
harvest_packaging.order.add_edge(Smart_Label, Pack_Produce)
harvest_packaging.order.add_edge(Pack_Produce, Urban_Dispatch)

# Yield Predict depends on Growth Analyze and can run in parallel or concurrently with harvesting phases
# We incorporate it so it happens after Growth Analyze but concurrently with harvesting

# Partial order for Yield Predict just alone
yield_predict = StrictPartialOrder(nodes=[Yield_Predict])

# Now combine growth_setup, recycling, yield_predict and harvest_packaging into one partial order
# Order edges:
# Growth Setup -> Harvesting setup start (Robot Harvest)
# Growth Analyze -> Yield Predict
# Yield Predict concurrent with harvesting
# Recycling concurrent with harvesting and growth

root = StrictPartialOrder(
    nodes=[growth_setup, recycling, yield_predict, harvest_packaging]
)

# Add edges connecting the partial orders
root.order.add_edge(growth_setup, harvest_packaging)
root.order.add_edge(growth_setup, yield_predict)

# Loop the entire process with adaptive lighting and climate control in the loop

# Loop body:
# Body A: growth_setup, recycling, yield_predict, harvest_packaging
# Body B: adaptive steps that lead back to growth_setup (simulate continuous loop)
# We choose loop children as (A, B) where B models the loop continuation steps

# We can place Light_Schedule and Climate_Adjust as loop continuation activities,
# representing adaptations before next iteration.

loop_continuation = StrictPartialOrder(
    nodes=[Light_Schedule, Climate_Adjust]
)
# Adaptive lighting and climate adjustments: order Light_Schedule -> Climate_Adjust
loop_continuation.order.add_edge(Light_Schedule, Climate_Adjust)

# Build loop operator
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        root,            # A: main operational process
        loop_continuation # B: loop continuation adaptations
    ]
)

# Save final result in root
root = loop