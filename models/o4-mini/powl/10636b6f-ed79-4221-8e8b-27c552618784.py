# Generated from: 10636b6f-ed79-4221-8e8b-27c552618784.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farm within a repurposed industrial building. It begins with site evaluation considering sunlight exposure and structural integrity, followed by modular rack installation optimized for hydroponic systems. Subsequent activities include nutrient solution formulation, LED light calibration, and climate control automation setup. The process also incorporates seed selection based on local market demand, pest management protocols adapted to enclosed environments, and workforce training in specialized agricultural techniques. Final stages involve integration of IoT sensors for real-time monitoring, data analytics for yield prediction, and compliance verification with urban agricultural regulations. This atypical yet realistic process merges urban planning, advanced agriculture, and technology implementation to create sustainable food production in city settings.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey    = Transition(label='Site Survey')
rack_install   = Transition(label='Rack Install')
solution_mix   = Transition(label='Solution Mix')
light_setup    = Transition(label='Light Setup')
climate_tune   = Transition(label='Climate Tune')
seed_select    = Transition(label='Seed Select')
iot_deploy     = Transition(label='IoT Deploy')
system_test    = Transition(label='System Test')
pest_control   = Transition(label='Pest Control')
staff_train    = Transition(label='Staff Train')
water_cycle    = Transition(label='Water Cycle')
data_analyze   = Transition(label='Data Analyze')
yield_monitor  = Transition(label='Yield Monitor')
harvest_plan   = Transition(label='Harvest Plan')
market_sync    = Transition(label='Market Sync')
regulate_check = Transition(label='Regulate Check')

# Define loop over the growth & analysis cycle
growth_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[water_cycle, data_analyze]
)

# Assemble the partial order model
root = StrictPartialOrder(nodes=[
    site_survey, rack_install,
    solution_mix, light_setup, climate_tune, seed_select,
    iot_deploy, system_test,
    pest_control, staff_train,
    water_cycle, data_analyze, growth_loop,
    yield_monitor, harvest_plan,
    market_sync, regulate_check
])

# Add control-flow edges
root.order.add_edge(site_survey,  rack_install)

# Parallel setup steps after rack installation
root.order.add_edge(rack_install, solution_mix)
root.order.add_edge(rack_install, light_setup)
root.order.add_edge(rack_install, climate_tune)
root.order.add_edge(rack_install, seed_select)

# IoT deployment requires all calibrations
root.order.add_edge(solution_mix, iot_deploy)
root.order.add_edge(light_setup,   iot_deploy)
root.order.add_edge(climate_tune,  iot_deploy)

# System test follows IoT deployment
root.order.add_edge(iot_deploy, system_test)

# After system test we prepare for production
root.order.add_edge(system_test, pest_control)
root.order.add_edge(system_test, staff_train)

# All preconditions must hold before entering the growth loop
root.order.add_edge(system_test,   growth_loop)
root.order.add_edge(seed_select,   growth_loop)
root.order.add_edge(pest_control,  growth_loop)
root.order.add_edge(staff_train,   growth_loop)

# After finishing the loop we monitor yield and plan harvest
root.order.add_edge(growth_loop,    yield_monitor)
root.order.add_edge(yield_monitor,  harvest_plan)

# Finalization steps in parallel
root.order.add_edge(harvest_plan, market_sync)
root.order.add_edge(harvest_plan, regulate_check)