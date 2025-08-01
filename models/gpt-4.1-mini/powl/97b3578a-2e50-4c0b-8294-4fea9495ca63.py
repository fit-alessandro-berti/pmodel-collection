# Generated from: 97b3578a-2e50-4c0b-8294-4fea9495ca63.json
# Description: This process outlines the comprehensive management cycle of an urban vertical farming operation that integrates automated climate control, nutrient monitoring, and staggered crop harvesting to maximize yield in limited spaces. The process begins with seed selection based on market demand forecasts, followed by precision seeding using robotic planters. Continuous environmental monitoring adjusts humidity, light intensity, and temperature to optimize growth conditions. Nutrient delivery is automated and adapted in real-time through IoT sensors detecting plant health. Pest management employs integrated biological controls rather than chemicals, ensuring sustainability. Crop growth stages are tracked digitally, triggering staggered harvesting to maintain a steady supply chain. Post-harvest, produce undergoes rapid quality assessment, packaging, and cold storage before distribution. Data analytics feed back into operational adjustments, improving future cycles and reducing waste while aligning with urban food security goals.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Seed_Select = Transition(label='Seed Select')
Demand_Forecast = Transition(label='Demand Forecast')
Robotic_Planting = Transition(label='Robotic Planting')
Climate_Adjust = Transition(label='Climate Adjust')
Humidity_Control = Transition(label='Humidity Control')
Light_Modulate = Transition(label='Light Modulate')
Temp_Maintain = Transition(label='Temp Maintain')
Nutrient_Flow = Transition(label='Nutrient Flow')
Sensor_Check = Transition(label='Sensor Check')
Pest_Monitor = Transition(label='Pest Monitor')
Bio_Control = Transition(label='Bio Control')
Growth_Track = Transition(label='Growth Track')
Stagger_Harvest = Transition(label='Stagger Harvest')
Quality_Scan = Transition(label='Quality Scan')
Pack_Produce = Transition(label='Pack Produce')
Cold_Store = Transition(label='Cold Store')
Data_Analyze = Transition(label='Data Analyze')
Waste_Reduce = Transition(label='Waste Reduce')

# Build partial orders matching the process description

# Initial Seed Selection and Demand Forecast
init_PO = StrictPartialOrder(nodes=[Demand_Forecast, Seed_Select])
init_PO.order.add_edge(Demand_Forecast, Seed_Select)  # Demand Forecast before Seed Select

# Precision seeding using robotic planters after seed selection
planting_PO = StrictPartialOrder(nodes=[Seed_Select, Robotic_Planting])
planting_PO.order.add_edge(Seed_Select, Robotic_Planting)

# Climate adjustment consists of Humidity Control, Light Modulate, Temp Maintain running concurrently
climate_sub_PO = StrictPartialOrder(nodes=[Humidity_Control, Light_Modulate, Temp_Maintain])

# Climate Adjust depends on the 3 parallel controls completing? 
# Actually, the description says continuous environmental monitoring adjusts humidity, light intensity, temp.
# We interpret Climate Adjust as the coordination node, then the three activities concurrently.
# Let's model Climate Adjust first, then the three concurrently.

climate_PO = StrictPartialOrder(nodes=[Climate_Adjust, climate_sub_PO])
climate_PO.order.add_edge(Climate_Adjust, climate_sub_PO)

# Nutrient delivery automation with Sensor Check influencing Nutrient Flow
nutrient_PO = StrictPartialOrder(nodes=[Sensor_Check, Nutrient_Flow])
nutrient_PO.order.add_edge(Sensor_Check, Nutrient_Flow)

# Pest management: Pest Monitor then Bio Control
pest_PO = StrictPartialOrder(nodes=[Pest_Monitor, Bio_Control])
pest_PO.order.add_edge(Pest_Monitor, Bio_Control)

# Crop growth stages tracking and staggered harvesting
growth_harvest_PO = StrictPartialOrder(nodes=[Growth_Track, Stagger_Harvest])
growth_harvest_PO.order.add_edge(Growth_Track, Stagger_Harvest)

# Post-harvest: Quality Scan, Pack Produce, Cold Store sequentially
post_harvest_PO = StrictPartialOrder(nodes=[Quality_Scan, Pack_Produce, Cold_Store])
post_harvest_PO.order.add_edge(Quality_Scan, Pack_Produce)
post_harvest_PO.order.add_edge(Pack_Produce, Cold_Store)

# Data Analytics and Waste Reduce after post-harvest
data_waste_PO = StrictPartialOrder(nodes=[Data_Analyze, Waste_Reduce])
data_waste_PO.order.add_edge(Data_Analyze, Waste_Reduce)

# Overall partial order assembling main phases:
# (init_PO --> planting_PO --> climate_PO --> nutrient_PO --> pest_PO --> growth_harvest_PO --> post_harvest_PO --> data_waste_PO)

root = StrictPartialOrder(
    nodes=[init_PO, planting_PO, climate_PO, nutrient_PO, pest_PO, growth_harvest_PO, post_harvest_PO, data_waste_PO]
)
root.order.add_edge(init_PO, planting_PO)
root.order.add_edge(planting_PO, climate_PO)
root.order.add_edge(climate_PO, nutrient_PO)
root.order.add_edge(nutrient_PO, pest_PO)
root.order.add_edge(pest_PO, growth_harvest_PO)
root.order.add_edge(growth_harvest_PO, post_harvest_PO)
root.order.add_edge(post_harvest_PO, data_waste_PO)