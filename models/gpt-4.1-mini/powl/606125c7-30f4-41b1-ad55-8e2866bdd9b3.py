# Generated from: 606125c7-30f4-41b1-ad55-8e2866bdd9b3.json
# Description: This process manages the entire lifecycle of an urban vertical farm, integrating automated crop cultivation with environmental controls and real-time data analytics. It starts with seed selection based on AI-driven market demand forecasts, followed by nutrient solution formulation tailored to each plant species. The system then initiates germination under controlled humidity and light conditions, transitioning to automated transplanting into vertical racks. Continuous monitoring via IoT sensors adjusts watering, lighting, and temperature dynamically. Crop health is assessed using drone-based multispectral imaging, triggering pest control measures or nutrient adjustments as needed. Harvest scheduling optimizes yield and freshness, while post-harvest processing includes automated packaging and cold storage. Finally, waste from plant residues is processed into bio-compost, closing the sustainability loop. This atypical agricultural process leverages advanced technology to maximize productivity in limited urban spaces, ensuring fresh produce availability with minimal environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# define activities
Seed_Select = Transition(label='Seed Select')
Demand_Forecast = Transition(label='Demand Forecast')
Nutrient_Mix = Transition(label='Nutrient Mix')
Germination_Start = Transition(label='Germination Start')
Humidity_Adjust = Transition(label='Humidity Adjust')
Light_Control = Transition(label='Light Control')
Transplant_Racks = Transition(label='Transplant Racks')
IoT_Monitor = Transition(label='IoT Monitor')
Watering_Adjust = Transition(label='Watering Adjust')
Temp_Control = Transition(label='Temp Control')
Drone_Scan = Transition(label='Drone Scan')
Pest_Control = Transition(label='Pest Control')
Harvest_Plan = Transition(label='Harvest Plan')
Auto_Package = Transition(label='Auto Package')
Cold_Storage = Transition(label='Cold Storage')
Waste_Process = Transition(label='Waste Process')
Bio_Compost = Transition(label='Bio-Compost')

# loop body represents continuous adjustments triggered by IoT monitoring:
# IoT Monitor -> choice( Pest Control or Watering/Temp Adjustments ) -> back to start of adjustments
watering_temp = StrictPartialOrder(nodes=[Watering_Adjust, Temp_Control])
watering_temp.order.add_edge(Watering_Adjust, Temp_Control)  # watering then temp control

# choice between pest control or watering/temperature adjustments after drone scan
pest_or_adjust = OperatorPOWL(operator=Operator.XOR, children=[Pest_Control, watering_temp])

# continuous environmental adjustments loop:
# execute IoT Monitor,
# then enter loop: (exit or execute (Drone Scan then pest_or_adjust) then IoT Monitor again)
loop_body = StrictPartialOrder(nodes=[Drone_Scan, pest_or_adjust])
loop_body.order.add_edge(Drone_Scan, pest_or_adjust)

env_loop = OperatorPOWL(operator=Operator.LOOP, children=[IoT_Monitor, loop_body])

# pre-loop sequence:
# Seed Select -> Demand Forecast -> Nutrient Mix -> Germination Start -> Humidity Adjust -> Light Control -> Transplant Racks
pre_loop_seq = StrictPartialOrder(nodes=[
    Seed_Select, Demand_Forecast, Nutrient_Mix,
    Germination_Start, Humidity_Adjust, Light_Control,
    Transplant_Racks
])
pre_loop_seq.order.add_edge(Seed_Select, Demand_Forecast)
pre_loop_seq.order.add_edge(Demand_Forecast, Nutrient_Mix)
pre_loop_seq.order.add_edge(Nutrient_Mix, Germination_Start)
pre_loop_seq.order.add_edge(Germination_Start, Humidity_Adjust)
pre_loop_seq.order.add_edge(Humidity_Adjust, Light_Control)
pre_loop_seq.order.add_edge(Light_Control, Transplant_Racks)

# post-loop sequence:
# Harvest Plan -> Auto Package -> Cold Storage -> Waste Process -> Bio Compost
post_seq = StrictPartialOrder(nodes=[
    Harvest_Plan, Auto_Package, Cold_Storage, Waste_Process, Bio_Compost
])
post_seq.order.add_edge(Harvest_Plan, Auto_Package)
post_seq.order.add_edge(Auto_Package, Cold_Storage)
post_seq.order.add_edge(Cold_Storage, Waste_Process)
post_seq.order.add_edge(Waste_Process, Bio_Compost)

# root process partial order with three parts:
# pre_loop_seq --> env_loop --> post_seq
root = StrictPartialOrder(nodes=[pre_loop_seq, env_loop, post_seq])
root.order.add_edge(pre_loop_seq, env_loop)
root.order.add_edge(env_loop, post_seq)