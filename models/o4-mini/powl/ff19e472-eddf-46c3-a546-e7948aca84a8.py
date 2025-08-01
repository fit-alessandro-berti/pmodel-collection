# Generated from: ff19e472-eddf-46c3-a546-e7948aca84a8.json
# Description: This process outlines the establishment of an urban vertical farming operation within a multi-story building. It involves site assessment, modular system installation, climate control calibration, nutrient solution preparation, seed selection and germination, automated monitoring deployment, pest management strategy implementation, harvest scheduling, and waste recycling integration. The process ensures sustainable food production in dense urban environments by optimizing space, reducing water usage, and leveraging IoT technologies for real-time crop health analytics. Extensive coordination across engineering, horticulture, and logistics teams is required to maintain continuous yield and quality.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey       = Transition(label='Site Survey')
design_layout     = Transition(label='Design Layout')
install_modules   = Transition(label='Install Modules')
calibrate_climate = Transition(label='Calibrate Climate')
prepare_nutrients = Transition(label='Prepare Nutrients')
select_seeds      = Transition(label='Select Seeds')
start_germination = Transition(label='Start Germination')
deploy_sensors    = Transition(label='Deploy Sensors')
monitor_growth    = Transition(label='Monitor Growth')
manage_pests      = Transition(label='Manage Pests')
optimize_energy   = Transition(label='Optimize Energy')
update_records    = Transition(label='Update Records')
schedule_harvest  = Transition(label='Schedule Harvest')
process_waste     = Transition(label='Process Waste')
conduct_training  = Transition(label='Conduct Training')
review_performance= Transition(label='Review Performance')

# A silent transition to serve as the loop connector
skip = SilentTransition()

# Define the growth‐monitoring phase as concurrent tasks
growth_phase = StrictPartialOrder(
    nodes=[monitor_growth, manage_pests, optimize_energy, update_records]
)
# No edges inside growth_phase ⇒ fully concurrent

# Loop over the growth_phase until we decide to harvest
loop_growth = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_phase, skip]
)

# Build the main partial‐order workflow
root = StrictPartialOrder(
    nodes=[
        site_survey, design_layout, install_modules,
        calibrate_climate, prepare_nutrients, select_seeds,
        start_germination, deploy_sensors, loop_growth,
        schedule_harvest, process_waste, conduct_training,
        review_performance
    ]
)

# Define the sequencing constraints
o = root.order
o.add_edge(site_survey,    design_layout)
o.add_edge(design_layout,  install_modules)
o.add_edge(install_modules,calibrate_climate)
o.add_edge(calibrate_climate, prepare_nutrients)
o.add_edge(prepare_nutrients, select_seeds)
o.add_edge(select_seeds,     start_germination)
o.add_edge(start_germination, deploy_sensors)
o.add_edge(deploy_sensors,    loop_growth)
o.add_edge(loop_growth,       schedule_harvest)
o.add_edge(schedule_harvest,  process_waste)
o.add_edge(process_waste,     conduct_training)
o.add_edge(conduct_training,  review_performance)