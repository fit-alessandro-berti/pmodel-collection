# Generated from: 7f82ce14-b488-406a-af93-879ccab2b73d.json
# Description: This process outlines the establishment of an urban vertical farm within a densely populated city environment. It involves specialized steps including site assessment for structural integrity, climate control system design tailored to microclimates, modular hydroponic installation, custom nutrient formula development, and integration of AI-driven crop monitoring. The process further incorporates community engagement for sustainable sourcing, waste recycling through bio-composting, and adaptive lighting schedules to optimize growth cycles. Each activity ensures the farm operates efficiently while minimizing environmental impact and maximizing yield in limited urban space.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_assess      = Transition(label='Site Assess')
structure_check  = Transition(label='Structure Check')
climate_design   = Transition(label='Climate Design')
hydroponic_setup = Transition(label='Hydroponic Setup')
nutrient_mix     = Transition(label='Nutrient Mix')
ai_integration   = Transition(label='AI Integration')
seed_selection   = Transition(label='Seed Selection')
community_meet   = Transition(label='Community Meet')
yield_forecast   = Transition(label='Yield Forecast')

crop_monitor     = Transition(label='Crop Monitor')
lighting_adjust  = Transition(label='Lighting Adjust')
waste_recycle    = Transition(label='Waste Recycle')
bio_compost      = Transition(label='Bio-Compost')
water_testing    = Transition(label='Water Testing')
energy_audit     = Transition(label='Energy Audit')

# Define a loop for ongoing monitoring and maintenance
cycle = StrictPartialOrder(nodes=[
    crop_monitor, lighting_adjust,
    waste_recycle, bio_compost,
    water_testing, energy_audit
])
cycle.order.add_edge(crop_monitor, lighting_adjust)
cycle.order.add_edge(lighting_adjust, waste_recycle)
cycle.order.add_edge(waste_recycle, bio_compost)
cycle.order.add_edge(bio_compost, water_testing)
cycle.order.add_edge(water_testing, energy_audit)

skip = SilentTransition()
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[cycle, skip])

# Assemble the full workflow as a partial order
root = StrictPartialOrder(nodes=[
    site_assess, structure_check, climate_design,
    hydroponic_setup, nutrient_mix, ai_integration,
    seed_selection, monitor_loop, community_meet,
    yield_forecast
])
# Define the control-flow order
root.order.add_edge(site_assess, structure_check)
root.order.add_edge(structure_check, climate_design)
root.order.add_edge(climate_design, hydroponic_setup)
root.order.add_edge(hydroponic_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, ai_integration)
root.order.add_edge(ai_integration, seed_selection)
root.order.add_edge(seed_selection, monitor_loop)
root.order.add_edge(monitor_loop, community_meet)
root.order.add_edge(community_meet, yield_forecast)