# Generated from: 1824902b-6f81-4668-bb0b-e48305790a17.json
# Description: This process outlines the complex steps involved in establishing a vertical farming system within an urban environment. It includes site assessment, modular design adaptation for limited spaces, climate control integration, nutrient delivery system setup, and automation programming. The process requires coordination between agricultural experts, engineers, and local authorities to ensure compliance with zoning laws and sustainability standards. Continuous monitoring and adjustment phases optimize plant growth cycles, energy consumption, and resource recycling, enabling a scalable, high-yield indoor farming operation that meets urban food demand while minimizing environmental impact and operational costs.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_survey      = Transition(label='Site Survey')
design_draft     = Transition(label='Design Draft')
compliance_check = Transition(label='Compliance Check')
modular_build    = Transition(label='Modular Build')
climate_setup    = Transition(label='Climate Setup')
nutrient_mix     = Transition(label='Nutrient Mix')
irrigation_install = Transition(label='Irrigation Install')
sensor_deploy    = Transition(label='Sensor Deploy')
automation_code  = Transition(label='Automation Code')
power_connect    = Transition(label='Power Connect')
trial_grow       = Transition(label='Trial Grow')
data_analysis    = Transition(label='Data Analysis')
adjust_settings  = Transition(label='Adjust Settings')
harvest_plan     = Transition(label='Harvest Plan')
waste_recycle    = Transition(label='Waste Recycle')
market_launch    = Transition(label='Market Launch')

# Build the loop for continuous monitoring and adjustment:
#   1) Trial Grow  (A)
#   2) then optionally repeat (Data Analysis -> Adjust Settings) (B) and go back to Trial Grow
loop_body = StrictPartialOrder(nodes=[data_analysis, adjust_settings])
loop_body.order.add_edge(data_analysis, adjust_settings)

growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[trial_grow, loop_body])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_draft,
    compliance_check,
    modular_build,
    climate_setup,
    nutrient_mix,
    irrigation_install,
    sensor_deploy,
    automation_code,
    power_connect,
    growth_loop,
    harvest_plan,
    waste_recycle,
    market_launch
])

# Add the control‐flow edges
root.order.add_edge(site_survey, design_draft)
root.order.add_edge(design_draft, compliance_check)
root.order.add_edge(compliance_check, modular_build)
root.order.add_edge(modular_build, climate_setup)
root.order.add_edge(climate_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, irrigation_install)
root.order.add_edge(irrigation_install, sensor_deploy)
root.order.add_edge(sensor_deploy, automation_code)
root.order.add_edge(automation_code, power_connect)
root.order.add_edge(power_connect, growth_loop)
root.order.add_edge(growth_loop, harvest_plan)
root.order.add_edge(harvest_plan, waste_recycle)
root.order.add_edge(waste_recycle, market_launch)