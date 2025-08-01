# Generated from: 1f302578-f9c7-4e3c-a770-87b900af274f.json
# Description: This process outlines the complete cycle of an urban vertical farming operation integrating IoT sensors, AI-driven growth optimization, and sustainable resource management. Starting from seed selection, the process covers climate control adjustments, nutrient delivery, and pest monitoring through automated drones. It includes real-time data analysis to optimize lighting and watering schedules, followed by harvesting, quality inspection, and packaging. The cycle concludes with waste recycling and energy consumption reporting, ensuring minimal environmental impact and maximum crop yield within a constrained urban footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
seed_selection    = Transition(label='Seed Selection')
climate_setup     = Transition(label='Climate Setup')
nutrient_mix      = Transition(label='Nutrient Mix')
sensor_calibration= Transition(label='Sensor Calibration')
lighting_adjust   = Transition(label='Lighting Adjust')
watering_cycle    = Transition(label='Watering Cycle')
pest_scan         = Transition(label='Pest Scan')
drone_patrol      = Transition(label='Drone Patrol')
data_analysis     = Transition(label='Data Analysis')
growth_forecast   = Transition(label='Growth Forecast')
harvest_prep      = Transition(label='Harvest Prep')
quality_check     = Transition(label='Quality Check')
packaging_done    = Transition(label='Packaging Done')
waste_sorting     = Transition(label='Waste Sorting')
energy_report     = Transition(label='Energy Report')

# Partial order for the intra-loop cycle
cycle_po = StrictPartialOrder(nodes=[
    lighting_adjust, watering_cycle, pest_scan, drone_patrol, data_analysis, growth_forecast
])
cycle_po.order.add_edge(lighting_adjust, watering_cycle)
cycle_po.order.add_edge(watering_cycle, pest_scan)
cycle_po.order.add_edge(pest_scan, drone_patrol)
cycle_po.order.add_edge(drone_patrol, data_analysis)
cycle_po.order.add_edge(data_analysis, growth_forecast)

# Loop: sensor calibration then repeat the cycle until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_calibration, cycle_po])

# Build the overall process partial order
root = StrictPartialOrder(nodes=[
    seed_selection, climate_setup, nutrient_mix, loop,
    harvest_prep, quality_check, packaging_done,
    waste_sorting, energy_report
])
root.order.add_edge(seed_selection, climate_setup)
root.order.add_edge(climate_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, loop)
root.order.add_edge(loop, harvest_prep)
root.order.add_edge(harvest_prep, quality_check)
root.order.add_edge(quality_check, packaging_done)
root.order.add_edge(packaging_done, waste_sorting)
root.order.add_edge(packaging_done, energy_report)