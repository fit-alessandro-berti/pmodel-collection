# Generated from: b8fe8e8d-1b06-4a0e-8812-a729b87f69db.json
# Description: This process describes the comprehensive operational cycle of an urban vertical farming facility specializing in multi-layer hydroponic vegetable production. It begins with nutrient solution preparation, followed by seed germination under controlled LED lighting. The seedlings are then transplanted into vertical racks where climate control systems optimize temperature, humidity, and CO2 levels. Automated sensors monitor plant health and growth metrics, triggering targeted nutrient adjustments. Periodic pest management employs integrated biological controls instead of chemicals. Harvesting is synchronized with market demand forecasts, while waste biomass is processed via onsite composting units. Finally, produce is packaged in eco-friendly materials and distributed through urban logistics channels, closing the loop with data-driven yield analysis for continuous improvement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
nutrient_prep = Transition(label='Nutrient Prep')
seed_germinate = Transition(label='Seed Germinate')
light_control = Transition(label='Light Control')
transplant_seedlings = Transition(label='Transplant Seedlings')
climate_adjust = Transition(label='Climate Adjust')
co2_monitor = Transition(label='CO2 Monitor')
sensor_scan = Transition(label='Sensor Scan')
nutrient_adjust = Transition(label='Nutrient Adjust')
pest_control = Transition(label='Pest Control')
growth_record = Transition(label='Growth Record')
harvest_schedule = Transition(label='Harvest Schedule')
waste_compost = Transition(label='Waste Compost')
eco_package = Transition(label='Eco Package')
urban_dispatch = Transition(label='Urban Dispatch')
yield_analyze = Transition(label='Yield Analyze')

# Nutrient Adjust depends on Sensor Scan, modeled as a loop:
# LOOP(sensor_scan, nutrient_adjust): sensor_scan then either exit or (nutrient_adjust then sensor_scan again)
nutrient_adjust_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_scan, nutrient_adjust])

# Concurrent climate control related tasks: Climate Adjust and CO2 Monitor
climate_co2_po = StrictPartialOrder(nodes=[climate_adjust, co2_monitor],)

# After Transplant Seedlings, these monitoring/adjustment tasks occur in partial order:
# Climate Adjust and CO2 Monitor run concurrently
# Sensor Scan with Nutrient Adjust in a loop runs after Climate Adjust and CO2 Monitor
# Pest Control and Growth Record happen after nutrient adjust loop concurrently
post_transplant_nodes = [climate_co2_po, nutrient_adjust_loop, pest_control, growth_record]

# Pest Control and Growth Record can be done concurrently:
pest_growth_po = StrictPartialOrder(nodes=[pest_control, growth_record],)

# Combining after Climate/CO2 and before Pest/Growth with edges
after_transplant_po = StrictPartialOrder(nodes=[climate_co2_po, nutrient_adjust_loop, pest_control, growth_record])

# Partial order edges:
# Climate Co2 and Nutrient Adjust Loop happen after Transplant Seedlings
# Pest Control and Growth Record happen after Nutrient Adjust Loop
after_transplant_po = StrictPartialOrder(nodes=[climate_co2_po, nutrient_adjust_loop, pest_control, growth_record])
after_transplant_po.order.add_edge(climate_co2_po, nutrient_adjust_loop)
after_transplant_po.order.add_edge(nutrient_adjust_loop, pest_control)
after_transplant_po.order.add_edge(nutrient_adjust_loop, growth_record)

# Waste Compost after Pest Control and Growth Record
# Partial order: Pest Control --> Waste Compost, Growth Record --> Waste Compost
waste_follow = StrictPartialOrder(nodes=[pest_control, growth_record, waste_compost])
waste_follow.order.add_edge(pest_control, waste_compost)
waste_follow.order.add_edge(growth_record, waste_compost)

# Harvest Schedule happens after Growth Record (reasonable assumption)
harvest_schedule_po = StrictPartialOrder(nodes=[growth_record, harvest_schedule])
harvest_schedule_po.order.add_edge(growth_record, harvest_schedule)

# Packaging and Urban Dispatch follow Harvest Schedule and Waste Compost in parallel (can be concurrent)
pack_dispatch_po = StrictPartialOrder(nodes=[eco_package, urban_dispatch])

# Packaging and Dispatch both occur after Harvest Schedule and Waste Compost
harvest_waste_pack_dispatch = StrictPartialOrder(nodes=[harvest_schedule, waste_compost, eco_package, urban_dispatch])
harvest_waste_pack_dispatch.order.add_edge(harvest_schedule, eco_package)
harvest_waste_pack_dispatch.order.add_edge(harvest_schedule, urban_dispatch)
harvest_waste_pack_dispatch.order.add_edge(waste_compost, eco_package)
harvest_waste_pack_dispatch.order.add_edge(waste_compost, urban_dispatch)

# Yield Analyze is last
yield_analyze_po = StrictPartialOrder(nodes=[eco_package, urban_dispatch, yield_analyze])
yield_analyze_po.order.add_edge(eco_package, yield_analyze)
yield_analyze_po.order.add_edge(urban_dispatch, yield_analyze)

# Entire after-transplant to final sequence combined
final_section = StrictPartialOrder(
    nodes=[after_transplant_po, waste_compost, harvest_schedule, eco_package, urban_dispatch, yield_analyze]
)
final_section.order.add_edge(after_transplant_po, waste_compost)
final_section.order.add_edge(waste_compost, harvest_schedule)
final_section.order.add_edge(harvest_schedule, eco_package)
final_section.order.add_edge(harvest_schedule, urban_dispatch)
final_section.order.add_edge(eco_package, yield_analyze)
final_section.order.add_edge(urban_dispatch, yield_analyze)

# Initial sequence: Nutrient Prep --> Seed Germinate --> Light Control --> Transplant Seedlings --> final_section
root = StrictPartialOrder(
    nodes=[nutrient_prep, seed_germinate, light_control, transplant_seedlings, final_section]
)
root.order.add_edge(nutrient_prep, seed_germinate)
root.order.add_edge(seed_germinate, light_control)
root.order.add_edge(light_control, transplant_seedlings)
root.order.add_edge(transplant_seedlings, final_section)