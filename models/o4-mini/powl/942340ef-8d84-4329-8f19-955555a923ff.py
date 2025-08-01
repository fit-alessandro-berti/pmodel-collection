# Generated from: 942340ef-8d84-4329-8f19-955555a923ff.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban rooftop farm on a commercial building. It involves site analysis, structural assessment, environmental impact evaluation, crop selection based on microclimate, soil preparation with imported organic matter, installation of automated irrigation systems, pest control planning, integration of renewable energy sources, community engagement for training, regulatory compliance checks, and continuous monitoring of crop growth and resource usage to ensure optimal yield and sustainability within an urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey    = Transition(label='Site Survey')
load_test      = Transition(label='Load Test')
climate_study  = Transition(label='Climate Study')
crop_choose    = Transition(label='Crop Choose')
soil_prep      = Transition(label='Soil Prep')
irrigation_inst= Transition(label='Irrigation Install')
pest_plan      = Transition(label='Pest Plan')
energy_setup   = Transition(label='Energy Setup')
permits_acq    = Transition(label='Permits Acquire')
community_meet = Transition(label='Community Meet')
training_plan  = Transition(label='Training Plan')
plant_seed     = Transition(label='Plant Seed')
growth_mon     = Transition(label='Growth Monitor')
waste_manage   = Transition(label='Waste Manage')
yield_analyze  = Transition(label='Yield Analyze')
harvest_plan   = Transition(label='Harvest Plan')

# Loop body: concurrent monitoring, waste management, yield analysis
loop_body = StrictPartialOrder(nodes=[growth_mon, waste_manage, yield_analyze])

# Loop: Plant Seed once, then zero-or-more repetitions of the loop_body + Plant Seed
loop = OperatorPOWL(operator=Operator.LOOP, children=[plant_seed, loop_body])

# Root partial order
root = StrictPartialOrder(nodes=[
    site_survey, load_test, climate_study, crop_choose, soil_prep,
    irrigation_inst, pest_plan, energy_setup, permits_acq,
    community_meet, training_plan, loop, harvest_plan
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, climate_study)
root.order.add_edge(load_test, climate_study)
root.order.add_edge(climate_study, crop_choose)
root.order.add_edge(crop_choose, soil_prep)

root.order.add_edge(soil_prep, irrigation_inst)
root.order.add_edge(soil_prep, pest_plan)
root.order.add_edge(soil_prep, energy_setup)

root.order.add_edge(site_survey, permits_acq)
root.order.add_edge(load_test, permits_acq)
root.order.add_edge(climate_study, permits_acq)

root.order.add_edge(irrigation_inst, community_meet)
root.order.add_edge(pest_plan, community_meet)
root.order.add_edge(energy_setup, community_meet)
root.order.add_edge(permits_acq, community_meet)

root.order.add_edge(community_meet, training_plan)
root.order.add_edge(training_plan, loop)

root.order.add_edge(loop, harvest_plan)