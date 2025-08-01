# Generated from: 1bba2009-03b1-4712-8021-3d9757dc9351.json
# Description: This process outlines the establishment of an urban vertical farm inside a repurposed high-rise building. It involves initial site evaluation, structural adaptation for hydroponic systems, environmental controls installation, crop selection based on urban microclimates, seedling propagation, nutrient solution preparation, automated monitoring setup, pest control strategies, harvesting schedules, post-harvest processing, packaging optimization for local distribution, waste recycling protocols, energy consumption tracking, and continuous improvement cycles to maximize yield and sustainability in a confined urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey = Transition(label='Site Survey')
structure_retrofit = Transition(label='Structure Retrofit')
system_install = Transition(label='System Install')
crop_select = Transition(label='Crop Select')
seedling_prep = Transition(label='Seedling Prep')
nutrient_mix = Transition(label='Nutrient Mix')
sensor_setup = Transition(label='Sensor Setup')
pest_control = Transition(label='Pest Control')
water_cycle = Transition(label='Water Cycle')
lighting_adjust = Transition(label='Lighting Adjust')
harvest_plan = Transition(label='Harvest Plan')
post_harvest = Transition(label='Post Harvest')
packaging = Transition(label='Packaging')
waste_process = Transition(label='Waste Process')
energy_audit = Transition(label='Energy Audit')
skip = SilentTransition()  # use for optional or exit in loops if needed

# Partial order segment 1:
# Initial site evaluation -> structure retrofit -> system install
po1 = StrictPartialOrder(nodes=[site_survey, structure_retrofit, system_install])
po1.order.add_edge(site_survey, structure_retrofit)
po1.order.add_edge(structure_retrofit, system_install)

# Partial order segment 2:
# Crop select -> seedling prep & nutrient mix concurrent -> sensor setup
# seedling prep and nutrient mix concurrent means no edges between them
po2 = StrictPartialOrder(nodes=[crop_select, seedling_prep, nutrient_mix, sensor_setup])
po2.order.add_edge(crop_select, seedling_prep)
po2.order.add_edge(crop_select, nutrient_mix)
po2.order.add_edge(seedling_prep, sensor_setup)
po2.order.add_edge(nutrient_mix, sensor_setup)

# Partial order segment 3:
# Pest control -> water cycle -> lighting adjust
po3 = StrictPartialOrder(nodes=[pest_control, water_cycle, lighting_adjust])
po3.order.add_edge(pest_control, water_cycle)
po3.order.add_edge(water_cycle, lighting_adjust)

# Partial order segment 4:
# Harvest plan -> post harvest -> packaging
po4 = StrictPartialOrder(nodes=[harvest_plan, post_harvest, packaging])
po4.order.add_edge(harvest_plan, post_harvest)
po4.order.add_edge(post_harvest, packaging)

# Partial order segment 5:
# Waste process & energy audit concurrent
po5 = StrictPartialOrder(nodes=[waste_process, energy_audit])
# no order edges => concurrent

# Loop representing continuous improvement cycle:
# Loop(harvest_plan to packaging, waste_process & energy_audit then restart)

# The replenishment and improvement cycle after packaging before harvest plan again:
# For the cycle body B, combine Waste Process and Energy Audit as partial order (po5)
loop_body = po5
loop = OperatorPOWL(operator=Operator.LOOP, children=[po4, loop_body])
# where:
# A = po4 (harvest_plan->post_harvest->packaging)
# B = po5 (waste_process, energy_audit concurrent)

# Now combine main sequence:
# 1) po1 -> 2) po2 -> 3) po3 -> 4) loop (harvest + improvements cycles)
root = StrictPartialOrder(nodes=[po1, po2, po3, loop])
root.order.add_edge(po1, po2)
root.order.add_edge(po2, po3)
root.order.add_edge(po3, loop)