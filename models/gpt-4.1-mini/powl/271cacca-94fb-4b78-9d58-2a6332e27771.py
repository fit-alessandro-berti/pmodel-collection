# Generated from: 271cacca-94fb-4b78-9d58-2a6332e27771.json
# Description: This process involves the integrated management of an urban vertical farm, combining hydroponics, climate control, and automated harvesting to optimize crop yield within a limited city space. It begins with seed selection and conditioning, followed by nutrient solution preparation and precise environmental calibration. Continuous monitoring through IoT sensors enables adaptive adjustments to light intensity, humidity, and temperature. Harvesting robots collect mature produce, which is then quality-checked and packaged onsite. Waste materials are recycled into compost to sustain the growth cycle, while data analytics provide insights for future crop planning. The entire cycle emphasizes sustainability, efficiency, and minimal resource usage, making it an innovative model for urban agriculture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Seed_Prep = Transition(label='Seed Prep')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Set = Transition(label='Climate Set')
Sensor_Install = Transition(label='Sensor Install')
Light_Adjust = Transition(label='Light Adjust')
Humidity_Control = Transition(label='Humidity Control')
Temperature_Tune = Transition(label='Temperature Tune')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Inspect = Transition(label='Pest Inspect')
Harvest_Collect = Transition(label='Harvest Collect')
Quality_Check = Transition(label='Quality Check')
Packaging = Transition(label='Packaging')
Waste_Sort = Transition(label='Waste Sort')
Compost_Create = Transition(label='Compost Create')
Data_Analyze = Transition(label='Data Analyze')

# Setup environmental calibration as partial order of Light, Humidity and Temperature controls
env_calibration = StrictPartialOrder(nodes=[Light_Adjust, Humidity_Control, Temperature_Tune])
# No order edges: these 3 are concurrent adjustments

# Monitoring node: concurrent Growth Monitor and Pest Inspect (assumed concurrent sensors/inspections)
monitoring = StrictPartialOrder(nodes=[Growth_Monitor, Pest_Inspect])
# No order edges to allow concurrency

# Waste recycle subtree as partial order
waste_recycle = StrictPartialOrder(nodes=[Waste_Sort, Compost_Create])
waste_recycle.order.add_edge(Waste_Sort, Compost_Create)

# Harvest and packaging partial order
harvest_pack = StrictPartialOrder(nodes=[Harvest_Collect, Quality_Check, Packaging])
harvest_pack.order.add_edge(Harvest_Collect, Quality_Check)
harvest_pack.order.add_edge(Quality_Check, Packaging)

# Sequence for initial preparation: Seed Prep -> Nutrient Mix -> Climate Set -> Sensor Install -> (env calibration)
prep_po = StrictPartialOrder(nodes=[Seed_Prep, Nutrient_Mix, Climate_Set, Sensor_Install, env_calibration])
prep_po.order.add_edge(Seed_Prep, Nutrient_Mix)
prep_po.order.add_edge(Nutrient_Mix, Climate_Set)
prep_po.order.add_edge(Climate_Set, Sensor_Install)
prep_po.order.add_edge(Sensor_Install, env_calibration)

# Loop: growth monitoring loop controlling adaptive adjustments
# Loop node (* (Growth Monitor + Pest Inspect, (env calibration + data analyze)))
# Here, B = choice between Data Analyze and silent (exit),
# with env_calibration happening each loop cycle afterwards

# Define choice in loop body after Growth Monitor & Pest Inspect: 
# either analyze data or skip analysis (silent) => gives condition to exit loop or enter again
skip = SilentTransition()
analyze_choice = OperatorPOWL(operator=Operator.XOR, children=[Data_Analyze, skip])

# Loop children:
# A = monitoring (Growth Monitor + Pest Inspect)
# B = sequence env_calibration then analyze_choice
loop_B = StrictPartialOrder(nodes=[env_calibration, analyze_choice])
loop_B.order.add_edge(env_calibration, analyze_choice)

loop = OperatorPOWL(operator=Operator.LOOP, children=[monitoring, loop_B])

# Compose final process partial order:
# prep_po --> loop --> harvest_pack --> waste_recycle

root = StrictPartialOrder(nodes=[prep_po, loop, harvest_pack, waste_recycle])
root.order.add_edge(prep_po, loop)
root.order.add_edge(loop, harvest_pack)
root.order.add_edge(harvest_pack, waste_recycle)