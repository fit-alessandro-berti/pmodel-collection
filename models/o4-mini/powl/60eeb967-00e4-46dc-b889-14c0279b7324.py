# Generated from: 60eeb967-00e4-46dc-b889-14c0279b7324.json
# Description: This process outlines the complex establishment of an urban vertical farm within a repurposed industrial building. It involves assessing structural integrity, designing modular growth units, integrating IoT sensors for environmental control, sourcing sustainable water and nutrient supplies, and implementing energy-efficient LED lighting systems. The process also includes staff training on crop management, scheduling automated harvesting, and establishing supply chain logistics for local distribution. Continuous monitoring and iterative optimization ensure maximum yield and minimal resource waste, adapting to seasonal and market variations in an urban context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey      = Transition(label='Site Survey')
structural_check = Transition(label='Structural Check')
unit_design      = Transition(label='Unit Design')
sensor_setup     = Transition(label='Sensor Setup')
water_sourcing   = Transition(label='Water Sourcing')
nutrient_prep    = Transition(label='Nutrient Prep')
lighting_install = Transition(label='Lighting Install')
system_integrate = Transition(label='System Integrate')
staff_train      = Transition(label='Staff Train')
crop_plan        = Transition(label='Crop Plan')
automation_setup = Transition(label='Automation Setup')
harvest_schedule = Transition(label='Harvest Schedule')
supply_chain     = Transition(label='Supply Chain')
yield_monitor    = Transition(label='Yield Monitor')
optimize_process = Transition(label='Optimize Process')
waste_manage     = Transition(label='Waste Manage')
market_adapt     = Transition(label='Market Adapt')

# Loop body: optimize → waste management → market adaptation
body = StrictPartialOrder(nodes=[optimize_process, waste_manage, market_adapt])
body.order.add_edge(optimize_process, waste_manage)
body.order.add_edge(waste_manage, market_adapt)

# Loop: monitor yield, then optionally repeat optimize/waste/market
loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_monitor, body])

# Root partial order
root = StrictPartialOrder(nodes=[
    site_survey, structural_check, unit_design, sensor_setup,
    water_sourcing, nutrient_prep, lighting_install, system_integrate,
    staff_train, crop_plan, automation_setup, harvest_schedule,
    supply_chain, loop
])

# Define the control-flow dependencies
root.order.add_edge(site_survey,      structural_check)
root.order.add_edge(structural_check, unit_design)
root.order.add_edge(unit_design,      sensor_setup)
root.order.add_edge(sensor_setup,     water_sourcing)
root.order.add_edge(sensor_setup,     nutrient_prep)
root.order.add_edge(water_sourcing,   lighting_install)
root.order.add_edge(nutrient_prep,    lighting_install)
root.order.add_edge(lighting_install, system_integrate)
root.order.add_edge(system_integrate, staff_train)
root.order.add_edge(system_integrate, crop_plan)
root.order.add_edge(crop_plan,        automation_setup)
root.order.add_edge(automation_setup, harvest_schedule)
root.order.add_edge(harvest_schedule, supply_chain)
root.order.add_edge(supply_chain,     loop)