# Generated from: 0b228e6d-ce47-4277-99d2-b29b0c68045c.json
# Description: This process outlines the complex, cyclical operations of an urban vertical farm that integrates renewable energy management, waste recycling, and community engagement. It starts with seed selection based on predictive analytics, moves through automated nutrient delivery and environmental adjustments using IoT sensors, incorporates waste-to-compost conversion onsite, and ends with dynamic crop harvesting schedules adjusted by market demand and weather forecasts. Additionally, it involves coordinating volunteer shifts, educational workshops, and direct-to-consumer distribution, ensuring sustainability both economically and environmentally in a densely populated urban setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions with given labels
Seed_Selection = Transition(label='Seed Selection')
Soil_Prep = Transition(label='Soil Prep')
Nutrient_Mix = Transition(label='Nutrient Mix')
Planting_Cycle = Transition(label='Planting Cycle')
Sensor_Check = Transition(label='Sensor Check')
Env_Adjust = Transition(label='Env Adjust')
Waste_Collect = Transition(label='Waste Collect')
Compost_Turn = Transition(label='Compost Turn')
Energy_Monitor = Transition(label='Energy Monitor')
Water_Reuse = Transition(label='Water Reuse')
Volunteer_Coord = Transition(label='Volunteer Coord')
Workshop_Plan = Transition(label='Workshop Plan')
Market_Forecast = Transition(label='Market Forecast')
Harvest_Schedule = Transition(label='Harvest Schedule')
Delivery_Pack = Transition(label='Delivery Pack')
Customer_Notify = Transition(label='Customer Notify')
Feedback_Gather = Transition(label='Feedback Gather')

# Build partial orders for some subprocesses

# Waste recycling subprocess: Waste Collect --> Compost Turn --> Water Reuse (concurrent with Energy Monitor)
waste_po = StrictPartialOrder(nodes=[Waste_Collect, Compost_Turn, Water_Reuse, Energy_Monitor])
waste_po.order.add_edge(Waste_Collect, Compost_Turn)
waste_po.order.add_edge(Compost_Turn, Water_Reuse)
# Energy Monitor concurrent (no edges to others)

# Community engagement subprocess with choice: Volunteer Coord XOR Workshop Plan
community_xor = OperatorPOWL(operator=Operator.XOR, children=[Volunteer_Coord, Workshop_Plan])

# Delivery subprocess: Delivery Pack --> Customer Notify --> Feedback Gather
delivery_po = StrictPartialOrder(nodes=[Delivery_Pack, Customer_Notify, Feedback_Gather])
delivery_po.order.add_edge(Delivery_Pack, Customer_Notify)
delivery_po.order.add_edge(Customer_Notify, Feedback_Gather)

# Environmental adjustment subprocess: Sensor Check --> Env Adjust
env_adj_po = StrictPartialOrder(nodes=[Sensor_Check, Env_Adjust])
env_adj_po.order.add_edge(Sensor_Check, Env_Adjust)

# Nutrient delivery subprocess: Soil Prep --> Nutrient Mix
nutrient_po = StrictPartialOrder(nodes=[Soil_Prep, Nutrient_Mix])
nutrient_po.order.add_edge(Soil_Prep, Nutrient_Mix)

# Harvesting subprocess: Market Forecast --> Harvest Schedule
harvest_po = StrictPartialOrder(nodes=[Market_Forecast, Harvest_Schedule])
harvest_po.order.add_edge(Market_Forecast, Harvest_Schedule)

# Loop for Planting Cycle with Sensor Check + Env Adjust as body of loop 
# LOOP(A=Planting_Cycle, B=env_adj_po)
loop_env = OperatorPOWL(operator=Operator.LOOP, children=[Planting_Cycle, env_adj_po])

# Assemble main flow partial order:
# Seed Selection --> Soil Prep --> Nutrient Mix --> loop_env --> waste_po --> harvest_po --> community_xor --> delivery_po

main_nodes = [
    Seed_Selection, Soil_Prep, Nutrient_Mix,
    loop_env,
    waste_po,
    harvest_po,
    community_xor,
    delivery_po
]

root = StrictPartialOrder(nodes=main_nodes)

root.order.add_edge(Seed_Selection, Soil_Prep)
root.order.add_edge(Soil_Prep, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, loop_env)
root.order.add_edge(loop_env, waste_po)
root.order.add_edge(waste_po, harvest_po)
root.order.add_edge(harvest_po, community_xor)
root.order.add_edge(community_xor, delivery_po)