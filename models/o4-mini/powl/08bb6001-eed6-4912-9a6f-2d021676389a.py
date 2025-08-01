# Generated from: 08bb6001-eed6-4912-9a6f-2d021676389a.json
# Description: This process details the comprehensive operational cycle of an urban vertical farm that integrates hydroponics, automated climate control, and AI-driven crop optimization. It begins with seed selection based on market trends and genetic traits, followed by nutrient solution preparation and precise planting. Environmental sensors continuously monitor temperature, humidity, and light, triggering climate adjustments. AI algorithms analyze growth data to optimize resource use and predict harvest times. Concurrently, pest detection systems activate targeted biocontrol measures. Harvested crops undergo quality sorting and packaging before distribution. Waste biomass is composted or converted to bioenergy, closing the sustainability loop. The process culminates with performance analysis and strategic planning for the next cycle, ensuring efficiency and minimal environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed_select   = Transition(label='Seed Select')
nutrient_prep = Transition(label='Nutrient Prep')
plant_setup   = Transition(label='Plant Setup')
sensor_monitor = Transition(label='Sensor Monitor')
climate_adjust = Transition(label='Climate Adjust')
growth_track   = Transition(label='Growth Track')
ai_analyze     = Transition(label='AI Analyze')
pest_detect    = Transition(label='Pest Detect')
bio_control    = Transition(label='Bio Control')
harvest_crop   = Transition(label='Harvest Crop')
quality_sort   = Transition(label='Quality Sort')
package_goods  = Transition(label='Package Goods')
distribute     = Transition(label='Distribute')
waste_process  = Transition(label='Waste Process')
cycle_review   = Transition(label='Cycle Review')

# Define looping subprocesses
loop_sensors = OperatorPOWL(
    operator=Operator.LOOP,
    children=[sensor_monitor, climate_adjust]
)
loop_growth = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_track, ai_analyze]
)
loop_pest = OperatorPOWL(
    operator=Operator.LOOP,
    children=[pest_detect, bio_control]
)

# Build the overall partial order model
root = StrictPartialOrder(nodes=[
    seed_select,
    nutrient_prep,
    plant_setup,
    loop_sensors,
    loop_growth,
    loop_pest,
    harvest_crop,
    quality_sort,
    package_goods,
    distribute,
    waste_process,
    cycle_review
])

# Initial sequence: Seed Select -> Nutrient Prep -> Plant Setup
root.order.add_edge(seed_select, nutrient_prep)
root.order.add_edge(nutrient_prep, plant_setup)

# After planting, the three loops run (concurrently)
root.order.add_edge(plant_setup, loop_sensors)
root.order.add_edge(plant_setup, loop_growth)
root.order.add_edge(plant_setup, loop_pest)

# After all loops complete, proceed to harvest and downstream steps
root.order.add_edge(loop_sensors, harvest_crop)
root.order.add_edge(loop_growth, harvest_crop)
root.order.add_edge(loop_pest, harvest_crop)

# Final linear sequence: Harvest -> Quality Sort -> Package -> Distribute -> Waste -> Review
root.order.add_edge(harvest_crop, quality_sort)
root.order.add_edge(quality_sort, package_goods)
root.order.add_edge(package_goods, distribute)
root.order.add_edge(distribute, waste_process)
root.order.add_edge(waste_process, cycle_review)