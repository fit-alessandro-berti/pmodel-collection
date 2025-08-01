# Generated from: 3690f41d-e861-494b-bf4f-7a97e211c9c0.json
# Description: This process outlines the establishment of a commercial urban vertical farm that integrates advanced hydroponics, AI-driven climate control, and sustainable resource management. It begins with site evaluation, followed by modular rack installation and nutrient system calibration. Subsequent steps include AI sensor deployment to monitor plant health, automated seeding, and growth pattern analysis. The process also involves waste recycling integration and energy optimization. Harvest scheduling is dynamically adjusted based on real-time data, ensuring peak yield. Finally, the produce undergoes quality inspection before packaging and local distribution, emphasizing minimal environmental impact while maximizing urban space utilization and food security.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_eval     = Transition(label="Site Evaluate")
rack_install  = Transition(label="Rack Install")
nutrient_setup = Transition(label="Nutrient Setup")
sensor_deploy = Transition(label="Sensor Deploy")
seed_automate = Transition(label="Seed Automate")
growth_monitor = Transition(label="Growth Monitor")
data_analyze  = Transition(label="Data Analyze")
climate_adjust = Transition(label="Climate Adjust")
waste_recycle = Transition(label="Waste Recycle")
energy_optimize = Transition(label="Energy Optimize")
harvest_plan  = Transition(label="Harvest Plan")
quality_check = Transition(label="Quality Check")
produce_package = Transition(label="Produce Package")
local_dispatch  = Transition(label="Local Dispatch")
system_maintain = Transition(label="System Maintain")

# A silent transition for the LOOP exit
skip = SilentTransition()

# Define the body of the growth loop: Growth Monitor -> Data Analyze -> Climate Adjust
body = StrictPartialOrder(nodes=[growth_monitor, data_analyze, climate_adjust])
body.order.add_edge(growth_monitor, data_analyze)
body.order.add_edge(data_analyze, climate_adjust)

# The LOOP: execute the body, then choose to exit (skip) or go through skip then body again
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[body, skip])

# Assemble the top‐level partial order
root = StrictPartialOrder(nodes=[
    site_eval,
    rack_install,
    nutrient_setup,
    sensor_deploy,
    seed_automate,
    waste_recycle,
    energy_optimize,
    system_maintain,
    growth_loop,
    harvest_plan,
    quality_check,
    produce_package,
    local_dispatch
])

# Define the control‐flow ordering
# Setup sequence
root.order.add_edge(site_eval, rack_install)
root.order.add_edge(rack_install, nutrient_setup)
root.order.add_edge(nutrient_setup, sensor_deploy)
root.order.add_edge(sensor_deploy, seed_automate)

# After seeding, do waste recycling, energy optimization, and system maintenance in parallel
root.order.add_edge(seed_automate, waste_recycle)
root.order.add_edge(seed_automate, energy_optimize)
root.order.add_edge(seed_automate, system_maintain)

# Then enter the growth loop
root.order.add_edge(waste_recycle, growth_loop)
root.order.add_edge(energy_optimize, growth_loop)
root.order.add_edge(system_maintain, growth_loop)

# After the loop finishes, plan the harvest and close out
root.order.add_edge(growth_loop, harvest_plan)
root.order.add_edge(harvest_plan, quality_check)
root.order.add_edge(quality_check, produce_package)
root.order.add_edge(produce_package, local_dispatch)