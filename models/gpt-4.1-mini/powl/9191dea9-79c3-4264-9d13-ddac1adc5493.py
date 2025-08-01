# Generated from: 9191dea9-79c3-4264-9d13-ddac1adc5493.json
# Description: This process outlines the establishment of an urban vertical farming system aimed at maximizing crop yield in limited city spaces through multi-layer hydroponic techniques. It involves initial site assessment, structural design, climate control integration, nutrient management, and automation installation. The process also includes crop selection based on local demand and environmental factors, supplier negotiations for seeds and materials, installation of lighting and irrigation systems, routine system testing, staff training on maintenance and harvesting protocols, and finally, marketing the farm produce to urban retailers and consumers. Continuous monitoring and iterative system optimization ensure sustainability and profitability in a competitive market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
material_sourcing = Transition(label='Material Sourcing')
structural_build = Transition(label='Structural Build')
climate_setup = Transition(label='Climate Setup')
hydroponic_install = Transition(label='Hydroponic Install')
lighting_setup = Transition(label='Lighting Setup')
irrigation_setup = Transition(label='Irrigation Setup')
sensor_deploy = Transition(label='Sensor Deploy')
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
system_testing = Transition(label='System Testing')
staff_training = Transition(label='Staff Training')
harvest_plan = Transition(label='Harvest Plan')
market_launch = Transition(label='Market Launch')
performance_review = Transition(label='Performance Review')

# Partial order nodes list
nodes = [
    site_survey,
    design_layout,
    material_sourcing,
    structural_build,
    climate_setup,
    hydroponic_install,
    lighting_setup,
    irrigation_setup,
    sensor_deploy,
    seed_selection,
    nutrient_mix,
    system_testing,
    staff_training,
    harvest_plan,
    market_launch,
    performance_review
]

root = StrictPartialOrder(nodes=nodes)

# Define the order relations as per process description:

# Initial sequence: Site Survey --> Design Layout
root.order.add_edge(site_survey, design_layout)

# Material sourcing can start after Design Layout
root.order.add_edge(design_layout, material_sourcing)

# Structural Build depends on Material Sourcing
root.order.add_edge(material_sourcing, structural_build)

# Climate Setup and Hydroponic Install depend on Structural Build; they can be concurrent
root.order.add_edge(structural_build, climate_setup)
root.order.add_edge(structural_build, hydroponic_install)

# Lighting Setup and Irrigation Setup depend on Hydroponic Install; concurrent
root.order.add_edge(hydroponic_install, lighting_setup)
root.order.add_edge(hydroponic_install, irrigation_setup)

# Sensor Deploy depends on Lighting Setup and Irrigation Setup (both must finish before deploying sensors)
root.order.add_edge(lighting_setup, sensor_deploy)
root.order.add_edge(irrigation_setup, sensor_deploy)

# Seed Selection and Nutrient Mix can start after Climate Setup and Sensor Deploy (both must finish before seed selection and nutrient mix start)
root.order.add_edge(climate_setup, seed_selection)
root.order.add_edge(sensor_deploy, seed_selection)
root.order.add_edge(climate_setup, nutrient_mix)
root.order.add_edge(sensor_deploy, nutrient_mix)

# System Testing depends on Seed Selection and Nutrient Mix
root.order.add_edge(seed_selection, system_testing)
root.order.add_edge(nutrient_mix, system_testing)

# Staff Training depends on System Testing
root.order.add_edge(system_testing, staff_training)

# Harvest Plan depends on Staff Training
root.order.add_edge(staff_training, harvest_plan)

# Market Launch depends on Harvest Plan
root.order.add_edge(harvest_plan, market_launch)

# Performance Review depends on Market Launch (continuous monitoring suggests loop but here modeled linearly)
root.order.add_edge(market_launch, performance_review)