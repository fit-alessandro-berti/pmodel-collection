# Generated from: 6809679e-1706-40b9-9ccb-eb658f721944.json
# Description: This process outlines the steps required to establish a sustainable urban rooftop farm in a dense city environment. It involves assessing rooftop structural integrity, designing modular planting systems, sourcing organic soil and seeds, installing automated irrigation and climate control, integrating renewable energy sources such as solar panels, and implementing pest control methods using natural predators. The process also includes community engagement for educational workshops, establishing distribution channels for local markets, and continuous monitoring through IoT sensors to optimize crop yield and resource usage. Finally, it covers maintenance routines and scalability planning for expanding the farm footprint across multiple rooftops in the city.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
load_testing = Transition(label='Load Testing')
design_layout = Transition(label='Design Layout')
material_sourcing = Transition(label='Material Sourcing')
soil_preparation = Transition(label='Soil Preparation')
seed_selection = Transition(label='Seed Selection')
irrigation_setup = Transition(label='Irrigation Setup')
climate_control = Transition(label='Climate Control')
energy_integration = Transition(label='Energy Integration')
pest_management = Transition(label='Pest Management')
community_outreach = Transition(label='Community Outreach')
market_setup = Transition(label='Market Setup')
sensor_installation = Transition(label='Sensor Installation')
data_monitoring = Transition(label='Data Monitoring')
routine_maintenance = Transition(label='Routine Maintenance')
expansion_planning = Transition(label='Expansion Planning')

# Structural assessment: Site Survey --> Load Testing
structural_assessment = StrictPartialOrder(nodes=[site_survey, load_testing])
structural_assessment.order.add_edge(site_survey, load_testing)

# Design and sourcing parallel: Design Layout -> Material Sourcing
# Soil Preparation and Seed Selection are parallel and start after Material Sourcing
design_and_sourcing = StrictPartialOrder(
    nodes=[design_layout, material_sourcing, soil_preparation, seed_selection]
)
design_and_sourcing.order.add_edge(design_layout, material_sourcing)
design_and_sourcing.order.add_edge(material_sourcing, soil_preparation)
design_and_sourcing.order.add_edge(material_sourcing, seed_selection)

# Installation parallel activities after design and sourcing:
# Irrigation Setup, Climate Control, Energy Integration
installation_parallel = StrictPartialOrder(
    nodes=[irrigation_setup, climate_control, energy_integration]
)
# no order among these three, fully concurrent

# Pest Management after installation setup
pest_and_community = StrictPartialOrder(
    nodes=[pest_management, community_outreach, market_setup]
)
# pest_management must precede community_outreach and market_setup, which are parallel
pest_and_community.order.add_edge(pest_management, community_outreach)
pest_and_community.order.add_edge(pest_management, market_setup)

# Sensor Installation and Data Monitoring parallel, sensor precedes monitoring
sensing = StrictPartialOrder(
    nodes=[sensor_installation, data_monitoring]
)
sensing.order.add_edge(sensor_installation, data_monitoring)

# Maintenance Loop: * (Routine Maintenance, Expansion Planning)
# This models the maintenance repeated with possible expansions
maintenance_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[routine_maintenance, expansion_planning]
)

# Compose main sequence with partial orders and concurrency:
# structural_assessment --> design_and_sourcing --> installation_parallel 
# --> pest_and_community --> sensing --> maintenance_loop

root = StrictPartialOrder(
    nodes=[structural_assessment,
           design_and_sourcing,
           installation_parallel,
           pest_and_community,
           sensing,
           maintenance_loop]
)

root.order.add_edge(structural_assessment, design_and_sourcing)
root.order.add_edge(design_and_sourcing, installation_parallel)
root.order.add_edge(installation_parallel, pest_and_community)
root.order.add_edge(pest_and_community, sensing)
root.order.add_edge(sensing, maintenance_loop)