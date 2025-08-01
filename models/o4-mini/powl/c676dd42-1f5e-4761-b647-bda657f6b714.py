# Generated from: c676dd42-1f5e-4761-b647-bda657f6b714.json
# Description: This process outlines the complex establishment of an urban vertical farming facility integrating hydroponics and IoT technology. It involves site analysis, modular design, nutrient solution management, sensor calibration, climate control optimization, waste recycling, and automated harvesting. The goal is to maximize crop yield in a limited space while maintaining sustainability through energy-efficient systems, data-driven growth monitoring, and community engagement programs. This atypical process requires coordination between agricultural scientists, engineers, software developers, and urban planners to create a self-sustaining ecosystem within a city environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey       = Transition(label='Site Survey')
design_layout     = Transition(label='Design Layout')
material_sourcing = Transition(label='Material Sourcing')
system_assembly   = Transition(label='System Assembly')
sensor_install    = Transition(label='Sensor Install')
nutrient_prep     = Transition(label='Nutrient Prep')
water_testing     = Transition(label='Water Testing')
climate_setup     = Transition(label='Climate Setup')
# The loop will include these two activities:
growth_monitoring = Transition(label='Growth Monitoring')
data_integration  = Transition(label='Data Integration')
pest_control      = Transition(label='Pest Control')
waste_sorting     = Transition(label='Waste Sorting')
harvest_plan      = Transition(label='Harvest Plan')
produce_pack      = Transition(label='Produce Pack')
energy_audit      = Transition(label='Energy Audit')
community_setup   = Transition(label='Community Setup')

# Build the monitoring loop: 
#   A = sequence Growth Monitoring -> Data Integration
#   B = choice {Pest Control, Waste Sorting}
cycle = StrictPartialOrder(nodes=[growth_monitoring, data_integration])
cycle.order.add_edge(growth_monitoring, data_integration)
cleanup_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, waste_sorting])
monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[cycle, cleanup_choice])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    material_sourcing,
    system_assembly,
    sensor_install,
    nutrient_prep,
    water_testing,
    climate_setup,
    monitoring_loop,
    harvest_plan,
    produce_pack,
    energy_audit,
    community_setup
])

# Define the control-flow dependencies
root.order.add_edge(site_survey,       design_layout)
root.order.add_edge(design_layout,     material_sourcing)
root.order.add_edge(design_layout,     system_assembly)
root.order.add_edge(material_sourcing, system_assembly)
root.order.add_edge(system_assembly,   sensor_install)
root.order.add_edge(sensor_install,    nutrient_prep)
root.order.add_edge(nutrient_prep,     water_testing)
root.order.add_edge(water_testing,     climate_setup)
root.order.add_edge(climate_setup,     monitoring_loop)
root.order.add_edge(monitoring_loop,   harvest_plan)
root.order.add_edge(harvest_plan,      produce_pack)
# After packing, energy audit and community setup can proceed in parallel
root.order.add_edge(produce_pack,      energy_audit)
root.order.add_edge(produce_pack,      community_setup)