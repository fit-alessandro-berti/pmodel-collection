# Generated from: a5f53b4b-e80a-49e2-9280-c4ba6a82d6cd.json
# Description: This process involves establishing an urban vertical farm that maximizes limited city space for sustainable agriculture. It begins with site analysis and structural assessment, followed by modular system design and climate control integration. The process includes nutrient solution formulation, automated seeding, and crop monitoring using IoT sensors. Maintenance planning ensures pest control and lighting optimization, while harvest scheduling and yield analysis optimize production cycles. Finally, distribution logistics coordinate fresh produce delivery to local markets, completing a complex cycle of urban food production that integrates technology, infrastructure, and sustainability in a confined environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
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

# Begin with site analysis and structural check sequentially
po_init = StrictPartialOrder(nodes=[site_analysis, structural_check])
po_init.order.add_edge(site_analysis, structural_check)

# Then system design and climate setup sequentially
po_design = StrictPartialOrder(nodes=[system_design, climate_setup])
po_design.order.add_edge(system_design, climate_setup)

# Nutrient mix and seed automation in sequence
po_nutrient_seed = StrictPartialOrder(nodes=[nutrient_mix, seed_automation])
po_nutrient_seed.order.add_edge(nutrient_mix, seed_automation)

# Sensor install and crop monitor sequentially
po_sensors = StrictPartialOrder(nodes=[sensor_install, crop_monitor])
po_sensors.order.add_edge(sensor_install, crop_monitor)

# Pest control and lighting adjust concurrent with water recycling and growth tracking (maintenance tasks)
po_maintenance1 = StrictPartialOrder(nodes=[pest_control, lighting_adjust])
po_maintenance2 = StrictPartialOrder(nodes=[water_recycling, growth_tracking])
# Merge the two maintenance parts as concurrent nodes
maintenance_nodes = [po_maintenance1, po_maintenance2]

# Harvest plan and yield review sequentially
po_harvest = StrictPartialOrder(nodes=[harvest_plan, yield_review])
po_harvest.order.add_edge(harvest_plan, yield_review)

# The final activity market delivery
market = market_delivery

# Compose complex POWL model using explicit partial orders and operators to represent partial ordering

# Step 1: Combine site analysis & structural check, then system design & climate setup, sequentially
po_step1 = StrictPartialOrder(
    nodes=[po_init, po_design]
)
po_step1.order.add_edge(po_init, po_design)

# Step 2: Nutrient mix & seed automation
po_step2 = po_nutrient_seed

# Step 3: Sensor install & crop monitor
po_step3 = po_sensors

# Step 4: Maintenance is parallel of two POs, use partial order with both nodes as concurrent
po_step4 = StrictPartialOrder(nodes=maintenance_nodes)

# Step 5: Harvest plan & yield review
po_step5 = po_harvest

# Step 6: Market delivery as last

# Now combine step 2 and 3 in parallel (nutrient/seed and sensor steps are concurrent)
po_23 = StrictPartialOrder(nodes=[po_step2, po_step3])  # no order edges, concurrent

# Combine step 4 maintenance concurrently as well
po_234 = StrictPartialOrder(nodes=[po_23, po_step4])  # concurrent nodes

# Now combine step1 with po_234 sequentially (setup steps then operational steps)
po_1234 = StrictPartialOrder(nodes=[po_step1, po_234])
po_1234.order.add_edge(po_step1, po_234)

# Combine step5 (harvest plan/yield review) after operational steps
po_12345 = StrictPartialOrder(nodes=[po_1234, po_step5])
po_12345.order.add_edge(po_1234, po_step5)

# Final market delivery sequentially last
root = StrictPartialOrder(nodes=[po_12345, market])
root.order.add_edge(po_12345, market)