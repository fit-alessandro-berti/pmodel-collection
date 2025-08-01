# Generated from: 858a26ca-f0b6-455a-8f0b-0007f2e65951.json
# Description: This process involves the establishment of a vertical farm within an urban environment, focusing on maximizing limited space for sustainable food production. It includes selecting an appropriate building, designing modular grow units, installing hydroponic systems, integrating IoT sensors for climate control, and establishing nutrient delivery methods. The process also covers securing necessary permits, sourcing organic seeds, training staff in urban agriculture techniques, and setting up a distribution network tailored for local markets. Additionally, ongoing monitoring and iterative optimization are essential to ensure crop health and yield efficiency in a controlled urban setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
site_survey     = Transition(label='Site Survey')
permit_check    = Transition(label='Permit Check')
design_layout   = Transition(label='Design Layout')
modular_build   = Transition(label='Modular Build')
install_hydro   = Transition(label='Install Hydroponics')
sensor_setup    = Transition(label='Sensor Setup')
climate_config  = Transition(label='Climate Config')
seed_sourcing   = Transition(label='Seed Sourcing')
nutrient_mix    = Transition(label='Nutrient Mix')
staff_training  = Transition(label='Staff Training')
trial_growth    = Transition(label='Trial Growth')
pest_control    = Transition(label='Pest Control')
data_monitoring = Transition(label='Data Monitoring')
harvest_plan    = Transition(label='Harvest Plan')
market_setup    = Transition(label='Market Setup')
waste_recycle   = Transition(label='Waste Recycle')

# Define the body of the loop: concurrent monitoring & pest control
loop_body = StrictPartialOrder(nodes=[data_monitoring, pest_control])

# Define the loop: run Trial Growth, then choose to exit or do (monitor & pest) and loop again
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[trial_growth, loop_body])

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    site_survey, permit_check, design_layout, modular_build,
    install_hydro, sensor_setup, climate_config, seed_sourcing,
    nutrient_mix, staff_training, growth_loop,
    harvest_plan, market_setup, waste_recycle
])

# Add sequencing edges
o = root.order
o.add_edge(site_survey,    permit_check)
o.add_edge(permit_check,   design_layout)
o.add_edge(design_layout,  modular_build)
o.add_edge(modular_build,  install_hydro)
o.add_edge(install_hydro,  sensor_setup)
o.add_edge(sensor_setup,   climate_config)
o.add_edge(climate_config, seed_sourcing)
o.add_edge(seed_sourcing,  nutrient_mix)
o.add_edge(nutrient_mix,   staff_training)
o.add_edge(staff_training, growth_loop)
o.add_edge(growth_loop,    harvest_plan)
o.add_edge(harvest_plan,   market_setup)
o.add_edge(market_setup,   waste_recycle)