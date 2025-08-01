# Generated from: 400cc8be-6a9d-4688-995b-6dc5c5e90a4d.json
# Description: This process outlines the intricate steps involved in establishing a fully operational urban vertical farm within a repurposed industrial building. It includes site assessment, modular system design, environmental control calibration, crop selection based on microclimates, nutrient cycling optimization, automated harvesting integration, waste repurposing, and community engagement to ensure sustainability and scalability in constrained urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_survey    = Transition(label='Site Survey')
design_layout  = Transition(label='Design Layout')
system_build   = Transition(label='System Build')
climate_setup  = Transition(label='Climate Setup')
crop_select    = Transition(label='Crop Select')
nutrient_mix   = Transition(label='Nutrient Mix')
water_cycle    = Transition(label='Water Cycle')
lighting_adjust= Transition(label='Lighting Adjust')
sensor_deploy  = Transition(label='Sensor Deploy')
growth_monitor = Transition(label='Growth Monitor')
pest_control   = Transition(label='Pest Control')
data_analyze   = Transition(label='Data Analyze')
harvest_plan   = Transition(label='Harvest Plan')
waste_process  = Transition(label='Waste Process')
community_meet = Transition(label='Community Meet')
scale_review   = Transition(label='Scale Review')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_survey, design_layout, system_build,
    climate_setup, crop_select, nutrient_mix,
    water_cycle, lighting_adjust, sensor_deploy,
    growth_monitor, pest_control,
    data_analyze, harvest_plan,
    waste_process, community_meet, scale_review
])

# Sequential dependencies
root.order.add_edge(site_survey,   design_layout)
root.order.add_edge(design_layout, system_build)
root.order.add_edge(system_build,  climate_setup)
root.order.add_edge(climate_setup, crop_select)
root.order.add_edge(crop_select,   nutrient_mix)

# After nutrient mixing, three calibration tasks can run in parallel
root.order.add_edge(nutrient_mix, water_cycle)
root.order.add_edge(nutrient_mix, lighting_adjust)
root.order.add_edge(nutrient_mix, sensor_deploy)

# Monitoring and pest control depend on all three calibration tasks
for src in (water_cycle, lighting_adjust, sensor_deploy):
    root.order.add_edge(src, growth_monitor)
    root.order.add_edge(src, pest_control)

# Analysis after monitoring and pest control
root.order.add_edge(growth_monitor, data_analyze)
root.order.add_edge(pest_control,   data_analyze)

# Final sequence: harvesting, waste, community, scale‐up review
root.order.add_edge(data_analyze,  harvest_plan)
root.order.add_edge(harvest_plan,  waste_process)
root.order.add_edge(waste_process, community_meet)
root.order.add_edge(community_meet, scale_review)