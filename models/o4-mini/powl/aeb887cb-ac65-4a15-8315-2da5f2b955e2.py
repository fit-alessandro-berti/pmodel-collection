# Generated from: aeb887cb-ac65-4a15-8315-2da5f2b955e2.json
# Description: This process involves establishing an urban vertical farm within a repurposed city warehouse. It starts with site evaluation and structural assessment, followed by climate control system design. Next, hydroponic system installation occurs alongside LED lighting setup. Seed selection and germination testing are performed to ensure optimal crop yield. Nutrient solution formulation and automated delivery configuration are conducted. Continuous environmental monitoring and pest management protocols are established. Harvest scheduling and post-harvest processing are integrated, followed by packaging design tailored for urban retail. Finally, logistics planning ensures timely distribution to local markets while maintaining product freshness. The process requires cross-disciplinary coordination between agronomists, engineers, and supply chain experts to optimize productivity in a confined urban space.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_eval      = Transition(label='Site Eval')
structure_chk  = Transition(label='Structure Check')
climate_plan   = Transition(label='Climate Plan')
hydro_fit      = Transition(label='Hydroponic Fit')
led_setup      = Transition(label='LED Setup')
seed_test      = Transition(label='Seed Test')
nutrient_mix   = Transition(label='Nutrient Mix')
delivery_setup = Transition(label='Delivery Setup')
env_monitor    = Transition(label='Env Monitoring')
pest_control   = Transition(label='Pest Control')
harvest_plan   = Transition(label='Harvest Plan')
post_harvest   = Transition(label='Post-Harvest')
pack_design    = Transition(label='Package Design')
logistics_map  = Transition(label='Logistics Map')
market_sync    = Transition(label='Market Sync')

# Create the partial‐order model
root = StrictPartialOrder(nodes=[
    site_eval, structure_chk, climate_plan,
    hydro_fit, led_setup, seed_test,
    nutrient_mix, delivery_setup,
    env_monitor, pest_control,
    harvest_plan, post_harvest,
    pack_design, logistics_map, market_sync
])

# Define the control‐flow relations
root.order.add_edge(site_eval,  structure_chk)
root.order.add_edge(structure_chk, climate_plan)

# After climate design, installation and lighting happen in parallel
root.order.add_edge(climate_plan, hydro_fit)
root.order.add_edge(climate_plan, led_setup)

# Seed testing follows both installation tasks
root.order.add_edge(hydro_fit,  seed_test)
root.order.add_edge(led_setup,  seed_test)

# Nutrient mix and delivery setup in parallel after seed test
root.order.add_edge(seed_test,   nutrient_mix)
root.order.add_edge(seed_test,   delivery_setup)

# Environmental monitoring and pest control in parallel after both setups
root.order.add_edge(nutrient_mix,   env_monitor)
root.order.add_edge(nutrient_mix,   pest_control)
root.order.add_edge(delivery_setup, env_monitor)
root.order.add_edge(delivery_setup, pest_control)

# Harvest planning follows monitoring and pest management
root.order.add_edge(env_monitor,  harvest_plan)
root.order.add_edge(pest_control, harvest_plan)

# Post‐harvest processing after harvest planning
root.order.add_edge(harvest_plan, post_harvest)

# Packaging, then logistics planning, then market synchronization
root.order.add_edge(post_harvest,  pack_design)
root.order.add_edge(pack_design,   logistics_map)
root.order.add_edge(logistics_map, market_sync)