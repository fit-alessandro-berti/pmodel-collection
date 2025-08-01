# Generated from: 83f22022-8788-40bb-b79d-3c95edb1804a.json
# Description: This process outlines the complex steps required to establish an urban vertical farming system within a high-density city environment. It involves site assessment, environmental analysis, modular unit design, resource integration including water recycling and renewable energy, plant species selection based on local climate, installation of automated monitoring systems, and community engagement for sustainable food distribution. Coordination between architects, agronomists, engineers, and local authorities ensures compliance with regulations and maximizes yield efficiency while minimizing ecological footprint. The process further includes continuous maintenance protocols, data-driven growth optimization, and adaptive marketing strategies tailored for urban consumers seeking fresh, locally grown produce.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_assess = Transition(label='Site Assess')
climate_study = Transition(label='Climate Study')
unit_design = Transition(label='Unit Design')
resource_plan = Transition(label='Resource Plan')
water_setup = Transition(label='Water Setup')
energy_integrate = Transition(label='Energy Integrate')
plant_select = Transition(label='Plant Select')
sensor_install = Transition(label='Sensor Install')
automation_config = Transition(label='Automation Config')
regulation_check = Transition(label='Regulation Check')
stakeholder_meet = Transition(label='Stakeholder Meet')
growth_monitor = Transition(label='Growth Monitor')
maintenance_plan = Transition(label='Maintenance Plan')
data_analyze = Transition(label='Data Analyze')
market_launch = Transition(label='Market Launch')
community_outreach = Transition(label='Community Outreach')

# Define the loop body: Maintenance Plan -> Data Analyze
loop_body = StrictPartialOrder(nodes=[maintenance_plan, data_analyze])
loop_body.order.add_edge(maintenance_plan, data_analyze)

# Define the monitoring loop: (Growth Monitor) then optionally (maintenance->analyze) and repeat
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, loop_body])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    site_assess,
    climate_study,
    unit_design,
    resource_plan,
    water_setup,
    energy_integrate,
    plant_select,
    sensor_install,
    automation_config,
    regulation_check,
    stakeholder_meet,
    monitor_loop,
    market_launch,
    community_outreach
])

# Sequential and concurrent dependencies
root.order.add_edge(site_assess, climate_study)
root.order.add_edge(climate_study, unit_design)
root.order.add_edge(unit_design, resource_plan)

# Resource setup can be done in parallel
root.order.add_edge(resource_plan, water_setup)
root.order.add_edge(resource_plan, energy_integrate)

# After both setups, proceed to plant selection
root.order.add_edge(water_setup, plant_select)
root.order.add_edge(energy_integrate, plant_select)

# Continue sequentially through installation and compliance
root.order.add_edge(plant_select, sensor_install)
root.order.add_edge(sensor_install, automation_config)
root.order.add_edge(automation_config, regulation_check)
root.order.add_edge(regulation_check, stakeholder_meet)

# After stakeholder meeting, enter the monitoring loop
root.order.add_edge(stakeholder_meet, monitor_loop)

# Upon exit from the loop, launch market and outreach in parallel
root.order.add_edge(monitor_loop, market_launch)
root.order.add_edge(monitor_loop, community_outreach)