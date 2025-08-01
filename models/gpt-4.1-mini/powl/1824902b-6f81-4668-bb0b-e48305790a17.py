# Generated from: 1824902b-6f81-4668-bb0b-e48305790a17.json
# Description: This process outlines the complex steps involved in establishing a vertical farming system within an urban environment. It includes site assessment, modular design adaptation for limited spaces, climate control integration, nutrient delivery system setup, and automation programming. The process requires coordination between agricultural experts, engineers, and local authorities to ensure compliance with zoning laws and sustainability standards. Continuous monitoring and adjustment phases optimize plant growth cycles, energy consumption, and resource recycling, enabling a scalable, high-yield indoor farming operation that meets urban food demand while minimizing environmental impact and operational costs.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Create transitions for all activities
site_survey = Transition(label='Site Survey')
design_draft = Transition(label='Design Draft')
compliance_check = Transition(label='Compliance Check')
modular_build = Transition(label='Modular Build')
climate_setup = Transition(label='Climate Setup')
nutrient_mix = Transition(label='Nutrient Mix')
irrigation_install = Transition(label='Irrigation Install')
sensor_deploy = Transition(label='Sensor Deploy')
automation_code = Transition(label='Automation Code')
power_connect = Transition(label='Power Connect')
trial_grow = Transition(label='Trial Grow')
data_analysis = Transition(label='Data Analysis')
adjust_settings = Transition(label='Adjust Settings')
harvest_plan = Transition(label='Harvest Plan')
waste_recycle = Transition(label='Waste Recycle')
market_launch = Transition(label='Market Launch')

# Model the loop for continuous monitoring and adjustment:
# loop = *(trial_grow, seq(data_analysis, adjust_settings))
# i.e. execute trial_grow, then choose to exit or execute (data_analysis then adjust_settings) then trial_grow again
monitoring_cycle = StrictPartialOrder(
    nodes=[data_analysis, adjust_settings]
)
monitoring_cycle.order.add_edge(data_analysis, adjust_settings)

loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[trial_grow, monitoring_cycle]
)

# Core build steps sequence:
# Site Survey --> Design Draft --> Compliance Check --> Modular Build --> Climate Setup --> Nutrient Mix --> 
# Irrigation Install --> Sensor Deploy --> Automation Code --> Power Connect

core_build_steps = StrictPartialOrder(
    nodes=[site_survey, design_draft, compliance_check, modular_build,
           climate_setup, nutrient_mix, irrigation_install, sensor_deploy,
           automation_code, power_connect]
)

core_build_steps.order.add_edge(site_survey, design_draft)
core_build_steps.order.add_edge(design_draft, compliance_check)
core_build_steps.order.add_edge(compliance_check, modular_build)
core_build_steps.order.add_edge(modular_build, climate_setup)
core_build_steps.order.add_edge(climate_setup, nutrient_mix)
core_build_steps.order.add_edge(nutrient_mix, irrigation_install)
core_build_steps.order.add_edge(irrigation_install, sensor_deploy)
core_build_steps.order.add_edge(sensor_deploy, automation_code)
core_build_steps.order.add_edge(automation_code, power_connect)

# After core build and monitoring loop, harvest planning and waste recycle run in parallel:
# harvest_plan and waste_recycle concurrent; then both precede market_launch

post_build_parallel = StrictPartialOrder(
    nodes=[harvest_plan, waste_recycle]
)
# no order edges between these two => concurrent

# Market launch depends on both harvest_plan and waste_recycle
final_seq = StrictPartialOrder(
    nodes=[post_build_parallel, market_launch]
)
final_seq.order.add_edge(post_build_parallel, market_launch)

# Compose the whole model in sequence:
# core_build_steps --> loop --> post_build_parallel --> market_launch

# Because StrictPartialOrder nodes can only be transitions or operators,
# nest accordingly.

# First combine monitoring loop after core build:
core_and_monitoring = StrictPartialOrder(
    nodes=[core_build_steps, loop]
)
core_and_monitoring.order.add_edge(core_build_steps, loop)

# Then add post build parallel before market launch
post_build_plus_market = StrictPartialOrder(
    nodes=[post_build_parallel, market_launch]
)
post_build_plus_market.order.add_edge(post_build_parallel, market_launch)

# Now the entire flow:
# core_and_monitoring --> post_build_parallel --> market_launch
root = StrictPartialOrder(
    nodes=[core_and_monitoring, post_build_plus_market]
)
root.order.add_edge(core_and_monitoring, post_build_plus_market)