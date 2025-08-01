# Generated from: 61002564-02e9-43ca-8a29-ee1bd7d81e06.json
# Description: This process outlines the comprehensive operational cycle of an urban vertical farm integrating automated hydroponics, AI-driven climate control, and real-time crop health analytics. Starting from seed selection, the farm leverages sensor networks and robotic systems to optimize nutrient delivery and light exposure. Periodic data analysis guides pruning and harvesting schedules, while waste is recycled through on-site composting. Market demand forecasts inform planting decisions, and harvested produce undergoes quality checks before distribution. The cycle also includes maintenance of mechanical systems and continuous improvement protocols based on yield performance and resource efficiency metrics, ensuring sustainable urban agriculture within limited city spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Seed_Selection = Transition(label='Seed Selection')
Nutrient_Mixing = Transition(label='Nutrient Mixing')
Planting_Setup = Transition(label='Planting Setup')
Climate_Control = Transition(label='Climate Control')
Sensor_Calibration = Transition(label='Sensor Calibration')
Data_Collection = Transition(label='Data Collection')
Growth_Monitoring = Transition(label='Growth Monitoring')
Pruning_Schedule = Transition(label='Pruning Schedule')
Pest_Detection = Transition(label='Pest Detection')
Harvest_Planning = Transition(label='Harvest Planning')
Quality_Check = Transition(label='Quality Check')
Waste_Recycling = Transition(label='Waste Recycling')
Market_Forecast = Transition(label='Market Forecast')
Distribution_Prep = Transition(label='Distribution Prep')
System_Maintenance = Transition(label='System Maintenance')
Yield_Analysis = Transition(label='Yield Analysis')

# Model loop: Daily or periodic growth & maintenance cycle
# Loop body: Growth Monitoring -> Pruning Schedule and Pest Detection (concurrent) -> Harvest Planning
# Choice in pruning and pest detection scheduling (could be concurrent, so use PO)
growth_maintenance_PO = StrictPartialOrder(nodes=[Growth_Monitoring, Pruning_Schedule, Pest_Detection])
growth_maintenance_PO.order.add_edge(Growth_Monitoring, Pruning_Schedule)
growth_maintenance_PO.order.add_edge(Growth_Monitoring, Pest_Detection)

loop_body = StrictPartialOrder(
    nodes=[growth_maintenance_PO, Harvest_Planning]
)
loop_body.order.add_edge(growth_maintenance_PO, Harvest_Planning)

# Construct the main loop:
# Execute loop_body, then choose to exit or continue after Yield_Analysis
# So loop = * (loop_body + Quality_Check + Waste_Recycling + Yield_Analysis, Market_Forecast + Distribution_Prep + System_Maintenance)
# But per structure: loop has (A, B) with A executed first, then either exit or execute B then A again

# Let's define A as:
# loop body: Growth & pruning & pest detection -> Harvest Planning -> Quality Check -> Waste Recycling -> Yield Analysis
A = StrictPartialOrder(nodes=[
    growth_maintenance_PO,
    Harvest_Planning,
    Quality_Check,
    Waste_Recycling,
    Yield_Analysis
])
A.order.add_edge(growth_maintenance_PO, Harvest_Planning)
A.order.add_edge(Harvest_Planning, Quality_Check)
A.order.add_edge(Quality_Check, Waste_Recycling)
A.order.add_edge(Waste_Recycling, Yield_Analysis)

# B as concurrency between Market Forecast, Distribution Prep and System Maintenance - all concurrent
B = StrictPartialOrder(nodes=[Market_Forecast, Distribution_Prep, System_Maintenance])

# Loop operator: execute A then choose exit or B then A again
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Initial sequence before loop:
# Seed Selection -> Nutrient Mixing -> Planting Setup -> Sensor Calibration -> Climate Control -> Data Collection -> loop
initial_sequence = StrictPartialOrder(nodes=[
    Seed_Selection,
    Nutrient_Mixing,
    Planting_Setup,
    Sensor_Calibration,
    Climate_Control,
    Data_Collection,
    loop
])
initial_sequence.order.add_edge(Seed_Selection, Nutrient_Mixing)
initial_sequence.order.add_edge(Nutrient_Mixing, Planting_Setup)
initial_sequence.order.add_edge(Planting_Setup, Sensor_Calibration)
initial_sequence.order.add_edge(Sensor_Calibration, Climate_Control)
initial_sequence.order.add_edge(Climate_Control, Data_Collection)
initial_sequence.order.add_edge(Data_Collection, loop)

root = initial_sequence