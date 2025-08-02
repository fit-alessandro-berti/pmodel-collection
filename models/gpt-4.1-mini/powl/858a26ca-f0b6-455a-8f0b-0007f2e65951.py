# Generated from: 858a26ca-f0b6-455a-8f0b-0007f2e65951.json
# Description: This process involves the establishment of a vertical farm within an urban environment, focusing on maximizing limited space for sustainable food production. It includes selecting an appropriate building, designing modular grow units, installing hydroponic systems, integrating IoT sensors for climate control, and establishing nutrient delivery methods. The process also covers securing necessary permits, sourcing organic seeds, training staff in urban agriculture techniques, and setting up a distribution network tailored for local markets. Additionally, ongoing monitoring and iterative optimization are essential to ensure crop health and yield efficiency in a controlled urban setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
site_survey = Transition(label='Site Survey')
permit_check = Transition(label='Permit Check')
design_layout = Transition(label='Design Layout')
modular_build = Transition(label='Modular Build')
install_hydroponics = Transition(label='Install Hydroponics')
sensor_setup = Transition(label='Sensor Setup')
climate_config = Transition(label='Climate Config')
seed_sourcing = Transition(label='Seed Sourcing')
nutrient_mix = Transition(label='Nutrient Mix')
staff_training = Transition(label='Staff Training')
trial_growth = Transition(label='Trial Growth')
pest_control = Transition(label='Pest Control')
data_monitoring = Transition(label='Data Monitoring')
harvest_plan = Transition(label='Harvest Plan')
market_setup = Transition(label='Market Setup')
waste_recycle = Transition(label='Waste Recycle')

# Build partial order of the main process

# Phase 1: Site survey and permits
phase1 = StrictPartialOrder(nodes=[site_survey, permit_check])
phase1.order.add_edge(site_survey, permit_check)

# Phase 2: Design and build modular grow units
phase2 = StrictPartialOrder(
    nodes=[design_layout, modular_build, install_hydroponics, sensor_setup, climate_config]
)
phase2.order.add_edge(design_layout, modular_build)
phase2.order.add_edge(modular_build, install_hydroponics)
phase2.order.add_edge(install_hydroponics, sensor_setup)
phase2.order.add_edge(sensor_setup, climate_config)

# Phase 3: Seed and nutrient preparation concurrently with staff training
phase3 = StrictPartialOrder(
    nodes=[seed_sourcing, nutrient_mix, staff_training]
)
# seed sourcing and nutrient mix can be concurrent
# staff training runs in parallel but must finish before trial growth (enforced later)

# Phase 4: Trial growth with pest control, then data monitoring and iterative loop
# Construct loop: 
# Loop body: pest_control + data_monitoring
# Loop exit: harvest_plan

# We put pest_control then data_monitoring in partial order
monitoring_body = StrictPartialOrder(nodes=[pest_control, data_monitoring])
monitoring_body.order.add_edge(pest_control, data_monitoring)

# loop = * (trial_growth, monitoring_body)
# After trial_growth we loop:
# - either exit (harvest_plan)
# - or execute monitoring_body then trial_growth again
loop_body = StrictPartialOrder(nodes=[trial_growth, monitoring_body])
loop_body.order.add_edge(trial_growth, monitoring_body)

# define loop with:
# A=trial_growth
# B = monitoring_body (pest_control -> data_monitoring)
loop = OperatorPOWL(operator=Operator.LOOP,
                    children=[trial_growth, monitoring_body])

# Phase 5: harvest_plan then market_setup
phase5 = StrictPartialOrder(nodes=[harvest_plan, market_setup])
phase5.order.add_edge(harvest_plan, market_setup)

# Phase 6: waste_recycle concurrent after or with market_setup
# Let's add order market_setup --> waste_recycle
# i.e., waste recycle follows market setup

# Assemble final process partial order with all phases and edges

# Node list
nodes = [
    phase1,    # Phase1 partial order
    phase2,    # Phase2 partial order
    phase3,    # Phase3 partial order
    loop,     # loop over trial growth and monitoring
    phase5,   # harvest and market setup
    waste_recycle
]

root = StrictPartialOrder(nodes=nodes)

# Define order edges between phases

# Phase1 --> Phase2
root.order.add_edge(phase1, phase2)

# Phase2 --> Phase3 (design/build done before sourcing/training)
root.order.add_edge(phase2, phase3)

# Phase3 --> loop (trial growth starts after seed, nutrients and training)
root.order.add_edge(phase3, loop)

# loop --> phase5 (harvest and market)
root.order.add_edge(loop, phase5)

# phase5 --> waste_recycle
root.order.add_edge(phase5, waste_recycle)