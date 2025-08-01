# Generated from: a5f53b4b-e80a-49e2-9280-c4ba6a82d6cd.json
# Description: This process involves establishing an urban vertical farm that maximizes limited city space for sustainable agriculture. It begins with site analysis and structural assessment, followed by modular system design and climate control integration. The process includes nutrient solution formulation, automated seeding, and crop monitoring using IoT sensors. Maintenance planning ensures pest control and lighting optimization, while harvest scheduling and yield analysis optimize production cycles. Finally, distribution logistics coordinate fresh produce delivery to local markets, completing a complex cycle of urban food production that integrates technology, infrastructure, and sustainability in a confined environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

site_analysis = Transition(label='Site Analysis')
structural_check = Transition(label='Structural Check')
system_design = Transition(label='System Design')
climate_setup = Transition(label='Climate Setup')
nutrient_mix = Transition(label='Nutrient Mix')
seed_automation = Transition(label='Seed Automation')
sensor_install = Transition(label='Sensor Install')
crop_monitor = Transition(label='Crop Monitor')
pest_control = Transition(label='Pest Control')
lighting_adjust = Transition(label='Lighting Adjust')
water_recycling = Transition(label='Water Recycling')
growth_tracking = Transition(label='Growth Tracking')
harvest_plan = Transition(label='Harvest Plan')
yield_review = Transition(label='Yield Review')
market_delivery = Transition(label='Market Delivery')

root = StrictPartialOrder(nodes=[
    site_analysis, structural_check, system_design, climate_setup,
    nutrient_mix, seed_automation, sensor_install, crop_monitor,
    pest_control, lighting_adjust, water_recycling, growth_tracking,
    harvest_plan, yield_review, market_delivery
])

# sequence up to crop monitoring
root.order.add_edge(site_analysis, structural_check)
root.order.add_edge(structural_check, system_design)
root.order.add_edge(system_design, climate_setup)
root.order.add_edge(climate_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, seed_automation)
root.order.add_edge(seed_automation, sensor_install)
root.order.add_edge(sensor_install, crop_monitor)

# parallel maintenance tasks after crop monitoring
root.order.add_edge(crop_monitor, pest_control)
root.order.add_edge(crop_monitor, lighting_adjust)
root.order.add_edge(crop_monitor, water_recycling)
root.order.add_edge(crop_monitor, growth_tracking)

# join before harvest planning
for tbl in [pest_control, lighting_adjust, water_recycling, growth_tracking]:
    root.order.add_edge(tbl, harvest_plan)

# final sequence
root.order.add_edge(harvest_plan, yield_review)
root.order.add_edge(yield_review, market_delivery)