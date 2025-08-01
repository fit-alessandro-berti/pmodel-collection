# Generated from: 3806d590-0c44-44e2-9b90-e11cf5433911.json
# Description: This process involves the integration of automated systems and human intervention to cultivate crops in a vertical farm within an urban environment. It starts with seed selection and preparation, followed by nutrient solution formulation and environmental calibration. Automated planting robots deposit seeds into hydroponic trays, while sensors continuously monitor air quality, humidity, and light exposure. Periodic manual inspections ensure plant health, and integrated pest management is applied selectively. Harvesting robots collect mature plants, which are then processed and packaged on-site. Waste materials are recycled into compost or bioenergy, completing a sustainable urban farming loop.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
Seed_Prep = Transition(label='Seed Prep')
Nutrient_Mix = Transition(label='Nutrient Mix')
Env_Set = Transition(label='Env Set')
Planting_Bot = Transition(label='Planting Bot')
Sensor_Check = Transition(label='Sensor Check')
Air_Quality = Transition(label='Air Quality')
Humidity_Control = Transition(label='Humidity Control')
Light_Adjust = Transition(label='Light Adjust')
Pest_Scan = Transition(label='Pest Scan')
Manual_Inspect = Transition(label='Manual Inspect')
Growth_Log = Transition(label='Growth Log')
Harvest_Bot = Transition(label='Harvest Bot')
Product_Pack = Transition(label='Product Pack')
Waste_Sort = Transition(label='Waste Sort')
Compost_Feed = Transition(label='Compost Feed')

# Partial order for Sensor sub-activities (Air Quality, Humidity Control, Light Adjust) are concurrent
sensor_sub_activities = StrictPartialOrder(nodes=[Air_Quality, Humidity_Control, Light_Adjust])
# No order edges added → concurrent monitoring

# Sensor Check encompasses the monitoring activities in parallel before continuing
sensor_monitoring = StrictPartialOrder(nodes=[Sensor_Check, sensor_sub_activities])
sensor_monitoring.order.add_edge(Sensor_Check, sensor_sub_activities)

# Pest Scan and Manual Inspect as a choice (since Integrated pest management applied selectively)
pest_or_manual = OperatorPOWL(operator=Operator.XOR, children=[Pest_Scan, Manual_Inspect])

# Loop structure: the Growth log and pest/manual inspections can repeat through growth phase
# After Pest/Manual, we log growth and then loop back to Sensor Check phase
# So Loop with:
#   A = Sensor_Check monitoring part + concurrent monitoring activities + "pest_or_manual"
#   B = Growth_Log before looping again

# Construct A: Sensor_Check then sensor_sub_activities then pest/manual choice partially ordered accordingly
A = StrictPartialOrder(nodes=[Sensor_Check, pest_or_manual, Growth_Log, Air_Quality, Humidity_Control, Light_Adjust])
# Sensor_Check before Air Quality, Humidity Control, Light Adjust (all three concurrent, so order from Sensor Check to each)
A.order.add_edge(Sensor_Check, Air_Quality)
A.order.add_edge(Sensor_Check, Humidity_Control)
A.order.add_edge(Sensor_Check, Light_Adjust)
# Pest or Manual choice after Sensor check & monitored activities
A.order.add_edge(Air_Quality, pest_or_manual)
A.order.add_edge(Humidity_Control, pest_or_manual)
A.order.add_edge(Light_Adjust, pest_or_manual)
# Growth Log after Pest/Manual
A.order.add_edge(pest_or_manual, Growth_Log)

# Loop between A and B with B being any additional step between iterations
# According to description: execute A, then choose to exit or execute B then A again repeated until exit
# Here B is empty (skip) because growth log is inside A with pest/manual inspections
# So we can model loop as execute A, then choose to exit or loop back
skip = SilentTransition()
loop_growth = OperatorPOWL(operator=Operator.LOOP, children=[A, skip])

# Build main process partial order:
# 1. Seed Prep -> Nutrient Mix -> Env Set -> Planting Bot
# 2. Then loop growth
# 3. Then Harvest Bot -> Product Pack
# 4. Then Waste Sort -> Compost Feed

root = StrictPartialOrder(nodes=[
    Seed_Prep,
    Nutrient_Mix,
    Env_Set,
    Planting_Bot,
    loop_growth,
    Harvest_Bot,
    Product_Pack,
    Waste_Sort,
    Compost_Feed
])

root.order.add_edge(Seed_Prep, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Env_Set)
root.order.add_edge(Env_Set, Planting_Bot)
root.order.add_edge(Planting_Bot, loop_growth)
root.order.add_edge(loop_growth, Harvest_Bot)
root.order.add_edge(Harvest_Bot, Product_Pack)
root.order.add_edge(Product_Pack, Waste_Sort)
root.order.add_edge(Waste_Sort, Compost_Feed)