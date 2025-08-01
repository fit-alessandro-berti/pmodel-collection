# Generated from: 0ab6f23e-f081-4f9e-a6b9-f665a0b8cbf6.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farming system in a repurposed industrial building. It involves site analysis, environmental control design, modular system installation, nutrient solution calibration, and continuous monitoring. The process integrates IoT sensor deployment for real-time data collection, adaptive lighting adjustments, and automated pest management to optimize plant growth. Additionally, it incorporates community engagement for local sourcing, waste recycling strategies, and a scalable business model to ensure sustainable urban food production. Each activity ensures operational efficiency, resource conservation, and product quality in a complex, space-constrained urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
structural_check = Transition(label='Structural Check')
layout_design    = Transition(label='Layout Design')
env_control      = Transition(label='Env Control')
module_build     = Transition(label='Module Build')
sensor_install   = Transition(label='Sensor Install')
nutrient_mix     = Transition(label='Nutrient Mix')
lighting_setup   = Transition(label='Lighting Setup')
irrigation_test  = Transition(label='Irrigation Test')
pest_scan        = Transition(label='Pest Scan')
data_sync        = Transition(label='Data Sync')
growth_audit     = Transition(label='Growth Audit')
waste_sort       = Transition(label='Waste Sort')
community_meet   = Transition(label='Community Meet')
market_plan      = Transition(label='Market Plan')
scale_review     = Transition(label='Scale Review')

# Monitoring loop: Data Sync then Growth Audit, repeat until exit
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_sync, growth_audit])

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    structural_check,
    layout_design,
    env_control,
    module_build,
    sensor_install,
    nutrient_mix,
    lighting_setup,
    irrigation_test,
    pest_scan,
    monitor_loop,
    waste_sort,
    community_meet,
    market_plan,
    scale_review
])

# Define the control-flow dependencies
root.order.add_edge(site_survey,      structural_check)
root.order.add_edge(structural_check, layout_design)
root.order.add_edge(layout_design,    env_control)
root.order.add_edge(env_control,      module_build)
root.order.add_edge(module_build,     sensor_install)
root.order.add_edge(sensor_install,   nutrient_mix)
root.order.add_edge(nutrient_mix,     lighting_setup)
root.order.add_edge(lighting_setup,   irrigation_test)
root.order.add_edge(irrigation_test,  pest_scan)
root.order.add_edge(pest_scan,        monitor_loop)
root.order.add_edge(monitor_loop,     waste_sort)
root.order.add_edge(waste_sort,       community_meet)
root.order.add_edge(community_meet,   market_plan)
root.order.add_edge(market_plan,      scale_review)