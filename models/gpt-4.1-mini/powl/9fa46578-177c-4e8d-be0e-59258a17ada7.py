# Generated from: 9fa46578-177c-4e8d-be0e-59258a17ada7.json
# Description: This process details the establishment of an urban rooftop farm in a densely populated city environment, integrating sustainable agriculture practices with modern technology. It begins with site assessment and structural analysis to ensure the rooftop can support the farm's weight. Subsequent steps include soil preparation and installation of hydroponic systems, followed by seed selection tailored to urban climate conditions. The process incorporates smart irrigation setup and renewable energy integration to optimize resource efficiency. Regular crop monitoring and pest management are conducted using IoT sensors and AI diagnostics. Finally, harvested produce undergoes quality checks before distribution to local markets, while continuous feedback is used to improve future crop cycles and sustainability metrics.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
site_assess = Transition(label='Site Assess')
structure_check = Transition(label='Structure Check')
soil_prep = Transition(label='Soil Prep')
hydroponics_setup = Transition(label='Hydroponics Setup')
seed_select = Transition(label='Seed Select')
irrigation_install = Transition(label='Irrigation Install')
energy_integrate = Transition(label='Energy Integrate')
sensor_deploy = Transition(label='Sensor Deploy')
ai_diagnostics = Transition(label='AI Diagnostics')
crop_monitor = Transition(label='Crop Monitor')
pest_control = Transition(label='Pest Control')
harvest_collect = Transition(label='Harvest Collect')
quality_check = Transition(label='Quality Check')
market_deliver = Transition(label='Market Deliver')
feedback_review = Transition(label='Feedback Review')

# First stage: site assessment and structural analysis
stage1 = StrictPartialOrder(nodes=[site_assess, structure_check])
stage1.order.add_edge(site_assess, structure_check)

# Second stage: soil prep and hydroponics setup occur sequentially
stage2 = StrictPartialOrder(nodes=[soil_prep, hydroponics_setup])
stage2.order.add_edge(soil_prep, hydroponics_setup)

# Third stage: seed selection
stage3 = seed_select

# Fourth stage: irrigation install and energy integration can be in parallel
stage4 = StrictPartialOrder(nodes=[irrigation_install, energy_integrate])
# no edges -> concurrent

# Fifth stage: sensor deploy and AI diagnostics sequentially
stage5 = StrictPartialOrder(nodes=[sensor_deploy, ai_diagnostics])
stage5.order.add_edge(sensor_deploy, ai_diagnostics)

# Sixth stage: crop monitor and pest control can be parallel
stage6 = StrictPartialOrder(nodes=[crop_monitor, pest_control])
# no edges -> concurrent

# Seventh stage: harvest collect then quality check sequentially
stage7 = StrictPartialOrder(nodes=[harvest_collect, quality_check])
stage7.order.add_edge(harvest_collect, quality_check)

# Eighth stage: market deliver
stage8 = market_deliver

# Ninth stage: feedback review
stage9 = feedback_review

# Combine all stages in strict partial order
root = StrictPartialOrder(nodes=[stage1, stage2, stage3, stage4, stage5, stage6, stage7, stage8, stage9])

root.order.add_edge(stage1, stage2)
root.order.add_edge(stage2, stage3)
root.order.add_edge(stage3, stage4)
root.order.add_edge(stage4, stage5)
root.order.add_edge(stage5, stage6)
root.order.add_edge(stage6, stage7)
root.order.add_edge(stage7, stage8)
root.order.add_edge(stage8, stage9)