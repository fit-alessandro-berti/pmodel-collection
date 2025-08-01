# Generated from: 3806d590-0c44-44e2-9b90-e11cf5433911.json
# Description: This process involves the integration of automated systems and human intervention to cultivate crops in a vertical farm within an urban environment. It starts with seed selection and preparation, followed by nutrient solution formulation and environmental calibration. Automated planting robots deposit seeds into hydroponic trays, while sensors continuously monitor air quality, humidity, and light exposure. Periodic manual inspections ensure plant health, and integrated pest management is applied selectively. Harvesting robots collect mature plants, which are then processed and packaged on-site. Waste materials are recycled into compost or bioenergy, completing a sustainable urban farming loop.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed_prep       = Transition(label='Seed Prep')
nutrient_mix    = Transition(label='Nutrient Mix')
env_set         = Transition(label='Env Set')
planting_bot    = Transition(label='Planting Bot')
sensor_check    = Transition(label='Sensor Check')
air_quality     = Transition(label='Air Quality')
humidity_control= Transition(label='Humidity Control')
light_adjust    = Transition(label='Light Adjust')
pest_scan       = Transition(label='Pest Scan')
manual_inspect  = Transition(label='Manual Inspect')
growth_log      = Transition(label='Growth Log')
harvest_bot     = Transition(label='Harvest Bot')
product_pack    = Transition(label='Product Pack')
waste_sort      = Transition(label='Waste Sort')
compost_feed    = Transition(label='Compost Feed')
skip            = SilentTransition()

# Maintenance start: sensor check leading to three concurrent sensor readings
maintenance_start = StrictPartialOrder(nodes=[sensor_check, air_quality, humidity_control, light_adjust])
maintenance_start.order.add_edge(sensor_check, air_quality)
maintenance_start.order.add_edge(sensor_check, humidity_control)
maintenance_start.order.add_edge(sensor_check, light_adjust)

# Maintenance body: optional pest scan, then manual inspect and growth log
choice_pest = OperatorPOWL(operator=Operator.XOR, children=[pest_scan, skip])
maintenance_body = StrictPartialOrder(nodes=[choice_pest, manual_inspect, growth_log])
# After choosing pest scan or skip, do the manual inspection and then log growth
maintenance_body.order.add_edge(choice_pest, manual_inspect)
maintenance_body.order.add_edge(manual_inspect, growth_log)

# Loop over maintenance until exit
maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[maintenance_start, maintenance_body])

# Top‐level process partial order
root = StrictPartialOrder(nodes=[
    seed_prep,
    nutrient_mix,
    env_set,
    planting_bot,
    maintenance_loop,
    harvest_bot,
    product_pack,
    waste_sort,
    compost_feed
])
# Sequence: seed prep -> nutrient mix -> environment setup -> planting -> maintenance loop -> harvest -> pack -> sort -> compost
root.order.add_edge(seed_prep,      nutrient_mix)
root.order.add_edge(nutrient_mix,   env_set)
root.order.add_edge(env_set,        planting_bot)
root.order.add_edge(planting_bot,   maintenance_loop)
root.order.add_edge(maintenance_loop, harvest_bot)
root.order.add_edge(harvest_bot,    product_pack)
root.order.add_edge(product_pack,   waste_sort)
root.order.add_edge(waste_sort,     compost_feed)