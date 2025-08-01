# Generated from: 0e544013-f632-4b0c-9203-060c9e06658b.json
# Description: This process outlines the complex and atypical steps required to establish an urban vertical farm within a repurposed industrial building. It involves site assessment, modular system design, environmental control integration, seed selection, and nutrient solution formulation. The process further includes automated planting, multi-tier crop monitoring using IoT sensors, adaptive lighting adjustments, pest management through biological controls, and dynamic harvesting schedules. Post-harvest, produce is cleaned, quality checked, packaged, and routed through a local distribution network optimized for freshness and minimal carbon footprint. Continuous data analysis and machine learning are applied to optimize growth cycles and resource consumption, ensuring sustainable urban agriculture operations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Site_Assess = Transition(label='Site Assess')
System_Design = Transition(label='System Design')
Env_Control = Transition(label='Env Control')
Seed_Select = Transition(label='Seed Select')
Nutrient_Prep = Transition(label='Nutrient Prep')
Auto_Plant = Transition(label='Auto Plant')
Sensor_Deploy = Transition(label='Sensor Deploy')
Light_Adjust = Transition(label='Light Adjust')
Pest_Control = Transition(label='Pest Control')
Growth_Monitor = Transition(label='Growth Monitor')
Harvest_Plan = Transition(label='Harvest Plan')
Produce_Clean = Transition(label='Produce Clean')
Quality_Check = Transition(label='Quality Check')
Package_Goods = Transition(label='Package Goods')
Local_Ship = Transition(label='Local Ship')
Data_Analyze = Transition(label='Data Analyze')
Cycle_Optimize = Transition(label='Cycle Optimize')

# Partial order for initial site assessment and system design steps (linear)
init_PO = StrictPartialOrder(nodes=[Site_Assess, System_Design, Env_Control, Seed_Select, Nutrient_Prep])
init_PO.order.add_edge(Site_Assess, System_Design)
init_PO.order.add_edge(System_Design, Env_Control)
init_PO.order.add_edge(Env_Control, Seed_Select)
init_PO.order.add_edge(Seed_Select, Nutrient_Prep)

# Partial order for planting and monitoring steps (some concurrency)
# Auto Plant -> Sensor Deploy -> Light Adjust -> Pest Control concurrent with Growth Monitor
plant_PO = StrictPartialOrder(
    nodes=[Auto_Plant, Sensor_Deploy, Light_Adjust, Pest_Control, Growth_Monitor]
)
plant_PO.order.add_edge(Auto_Plant, Sensor_Deploy)
plant_PO.order.add_edge(Sensor_Deploy, Light_Adjust)
plant_PO.order.add_edge(Light_Adjust, Pest_Control)
plant_PO.order.add_edge(Pest_Control, Growth_Monitor)

# Growth Monitor can run concurrently with Pest Control adjustments (already sequenced above) so no extra edges

# Harvest planning and post-harvest processing linear
harvest_PO = StrictPartialOrder(
    nodes=[Harvest_Plan, Produce_Clean, Quality_Check, Package_Goods, Local_Ship]
)
harvest_PO.order.add_edge(Harvest_Plan, Produce_Clean)
harvest_PO.order.add_edge(Produce_Clean, Quality_Check)
harvest_PO.order.add_edge(Quality_Check, Package_Goods)
harvest_PO.order.add_edge(Package_Goods, Local_Ship)

# Loop for continuous data analysis and cycle optimization after harvest/shipping
# * (Data Analyze, Cycle Optimize)
loop = OperatorPOWL(operator=Operator.LOOP, children=[Data_Analyze, Cycle_Optimize])

# Assemble main process as partial order
# init_PO -> plant_PO -> harvest_PO -> loop
root = StrictPartialOrder(nodes=[init_PO, plant_PO, harvest_PO, loop])
root.order.add_edge(init_PO, plant_PO)
root.order.add_edge(plant_PO, harvest_PO)
root.order.add_edge(harvest_PO, loop)