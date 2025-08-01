# Generated from: 1f302578-f9c7-4e3c-a770-87b900af274f.json
# Description: This process outlines the complete cycle of an urban vertical farming operation integrating IoT sensors, AI-driven growth optimization, and sustainable resource management. Starting from seed selection, the process covers climate control adjustments, nutrient delivery, and pest monitoring through automated drones. It includes real-time data analysis to optimize lighting and watering schedules, followed by harvesting, quality inspection, and packaging. The cycle concludes with waste recycling and energy consumption reporting, ensuring minimal environmental impact and maximum crop yield within a constrained urban footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Seed_Selection = Transition(label='Seed Selection')
Climate_Setup = Transition(label='Climate Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Sensor_Calibration = Transition(label='Sensor Calibration')
Lighting_Adjust = Transition(label='Lighting Adjust')
Watering_Cycle = Transition(label='Watering Cycle')
Pest_Scan = Transition(label='Pest Scan')
Drone_Patrol = Transition(label='Drone Patrol')
Data_Analysis = Transition(label='Data Analysis')
Growth_Forecast = Transition(label='Growth Forecast')
Harvest_Prep = Transition(label='Harvest Prep')
Quality_Check = Transition(label='Quality Check')
Packaging_Done = Transition(label='Packaging Done')
Waste_Sorting = Transition(label='Waste Sorting')
Energy_Report = Transition(label='Energy Report')

# Build partial order for the process as described:

# Start: Seed Selection --> Climate Setup --> Nutrient Mix
# After Nutrient Mix, Sensor Calibration
# Then Lighting Adjust and Watering Cycle in parallel (concurrent)
# Then Pest Scan and Drone Patrol in parallel (concurrent)
# Then Data Analysis --> Growth Forecast
# Then Harvest Prep --> Quality Check --> Packaging Done
# Then Waste Sorting --> Energy Report

# Represent Lighting Adjust and Watering Cycle concurrent: no edge between them, both after Sensor Calibration
# Represent Pest Scan and Drone Patrol concurrent: no edge between them, both after Lighting Adjust and Watering Cycle

# Create the main workflow with all nodes
nodes = [
    Seed_Selection,
    Climate_Setup,
    Nutrient_Mix,
    Sensor_Calibration,
    Lighting_Adjust,
    Watering_Cycle,
    Pest_Scan,
    Drone_Patrol,
    Data_Analysis,
    Growth_Forecast,
    Harvest_Prep,
    Quality_Check,
    Packaging_Done,
    Waste_Sorting,
    Energy_Report
]

root = StrictPartialOrder(nodes=nodes)

# Add edges following the described flow

# Seed Selection --> Climate Setup --> Nutrient Mix --> Sensor Calibration
root.order.add_edge(Seed_Selection, Climate_Setup)
root.order.add_edge(Climate_Setup, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Sensor_Calibration)

# Sensor Calibration --> Lighting Adjust and Watering Cycle (concurrent)
root.order.add_edge(Sensor_Calibration, Lighting_Adjust)
root.order.add_edge(Sensor_Calibration, Watering_Cycle)

# Lighting Adjust and Watering Cycle --> Pest Scan and Drone Patrol (concurrent)
root.order.add_edge(Lighting_Adjust, Pest_Scan)
root.order.add_edge(Lighting_Adjust, Drone_Patrol)
root.order.add_edge(Watering_Cycle, Pest_Scan)
root.order.add_edge(Watering_Cycle, Drone_Patrol)

# Pest Scan and Drone Patrol --> Data Analysis (converge)
# Because Pest Scan and Drone Patrol are concurrent, and both precede Data Analysis, add edges from both to Data Analysis
root.order.add_edge(Pest_Scan, Data_Analysis)
root.order.add_edge(Drone_Patrol, Data_Analysis)

# Data Analysis --> Growth Forecast
root.order.add_edge(Data_Analysis, Growth_Forecast)

# Growth Forecast --> Harvest Prep --> Quality Check --> Packaging Done
root.order.add_edge(Growth_Forecast, Harvest_Prep)
root.order.add_edge(Harvest_Prep, Quality_Check)
root.order.add_edge(Quality_Check, Packaging_Done)

# Packaging Done --> Waste Sorting --> Energy Report
root.order.add_edge(Packaging_Done, Waste_Sorting)
root.order.add_edge(Waste_Sorting, Energy_Report)