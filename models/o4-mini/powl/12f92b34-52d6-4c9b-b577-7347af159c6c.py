# Generated from: 12f92b34-52d6-4c9b-b577-7347af159c6c.json
# Description: This process outlines the comprehensive setup of an urban vertical farming system within a repurposed industrial building. It involves site assessment, modular structure assembly, climate control integration, nutrient solution preparation, automated seeding, growth monitoring via IoT sensors, pest management using biological agents, harvesting automation, waste recycling, and distribution logistics. The process ensures sustainability by incorporating renewable energy sources and water recirculation systems while maintaining compliance with urban agricultural regulations and community engagement for social acceptance.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
structure_build  = Transition(label='Structure Build')
climate_setup    = Transition(label='Climate Setup')
nutrient_prep    = Transition(label='Nutrient Prep')
seed_automation  = Transition(label='Seed Automation')
sensor_install   = Transition(label='Sensor Install')
growth_monitor   = Transition(label='Growth Monitor')
pest_control     = Transition(label='Pest Control')
harvest_auto     = Transition(label='Harvest Automate')
waste_recycle    = Transition(label='Waste Recycle')
energy_integrate = Transition(label='Energy Integrate')
water_recirc     = Transition(label='Water Recirc')
compliance_check = Transition(label='Compliance Check')
community_engage = Transition(label='Community Engage')
logistics_plan   = Transition(label='Logistics Plan')

# Loop for repeated monitoring and pest control
monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, pest_control])

# Build the partial order model
root = StrictPartialOrder(nodes=[
    site_survey,
    structure_build,
    climate_setup,
    nutrient_prep,
    seed_automation,
    sensor_install,
    monitoring_loop,
    harvest_auto,
    waste_recycle,
    energy_integrate,
    water_recirc,
    compliance_check,
    community_engage,
    logistics_plan
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, structure_build)
root.order.add_edge(site_survey, compliance_check)
root.order.add_edge(site_survey, community_engage)

root.order.add_edge(structure_build, climate_setup)
root.order.add_edge(structure_build, energy_integrate)

root.order.add_edge(climate_setup, nutrient_prep)
root.order.add_edge(climate_setup, water_recirc)

root.order.add_edge(nutrient_prep, seed_automation)
root.order.add_edge(nutrient_prep, sensor_install)

root.order.add_edge(seed_automation, monitoring_loop)
root.order.add_edge(sensor_install, monitoring_loop)

root.order.add_edge(monitoring_loop, harvest_auto)
root.order.add_edge(harvest_auto, waste_recycle)
root.order.add_edge(waste_recycle, logistics_plan)

root.order.add_edge(energy_integrate, logistics_plan)
root.order.add_edge(water_recirc, logistics_plan)
root.order.add_edge(compliance_check, logistics_plan)
root.order.add_edge(community_engage, logistics_plan)