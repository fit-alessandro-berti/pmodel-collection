# Generated from: 9191dea9-79c3-4264-9d13-ddac1adc5493.json
# Description: This process outlines the establishment of an urban vertical farming system aimed at maximizing crop yield in limited city spaces through multi-layer hydroponic techniques. It involves initial site assessment, structural design, climate control integration, nutrient management, and automation installation. The process also includes crop selection based on local demand and environmental factors, supplier negotiations for seeds and materials, installation of lighting and irrigation systems, routine system testing, staff training on maintenance and harvesting protocols, and finally, marketing the farm produce to urban retailers and consumers. Continuous monitoring and iterative system optimization ensure sustainability and profitability in a competitive market.

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
seed_selection    = Transition(label='Seed Selection')
structural_build  = Transition(label='Structural Build')
climate_setup     = Transition(label='Climate Setup')
hydroponic_install= Transition(label='Hydroponic Install')
lighting_setup    = Transition(label='Lighting Setup')
irrigation_setup  = Transition(label='Irrigation Setup')
sensor_deploy     = Transition(label='Sensor Deploy')
nutrient_mix      = Transition(label='Nutrient Mix')
system_testing    = Transition(label='System Testing')
staff_training    = Transition(label='Staff Training')
harvest_plan      = Transition(label='Harvest Plan')
market_launch     = Transition(label='Market Launch')
performance_review= Transition(label='Performance Review')

# Main process (A)
A = StrictPartialOrder(nodes=[
    site_survey, design_layout, material_sourcing, seed_selection,
    structural_build, climate_setup, hydroponic_install,
    lighting_setup, irrigation_setup, sensor_deploy,
    nutrient_mix, system_testing, staff_training,
    harvest_plan, market_launch
])

# Define the partial‐order dependencies
A.order.add_edge(site_survey,   design_layout)
A.order.add_edge(design_layout, material_sourcing)
A.order.add_edge(design_layout, seed_selection)
A.order.add_edge(material_sourcing, structural_build)
A.order.add_edge(material_sourcing, nutrient_mix)
A.order.add_edge(structural_build,  climate_setup)
A.order.add_edge(structural_build,  hydroponic_install)
A.order.add_edge(climate_setup,     hydroponic_install)
A.order.add_edge(hydroponic_install, lighting_setup)
A.order.add_edge(hydroponic_install, irrigation_setup)
A.order.add_edge(hydroponic_install, sensor_deploy)
A.order.add_edge(nutrient_mix,      system_testing)
A.order.add_edge(lighting_setup,    system_testing)
A.order.add_edge(irrigation_setup,  system_testing)
A.order.add_edge(sensor_deploy,     system_testing)
A.order.add_edge(system_testing,    staff_training)
A.order.add_edge(staff_training,    harvest_plan)
A.order.add_edge(harvest_plan,      market_launch)

# Loop for continuous monitoring and optimization
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[A, performance_review]
)