# Generated from: ff19e472-eddf-46c3-a546-e7948aca84a8.json
# Description: This process outlines the establishment of an urban vertical farming operation within a multi-story building. It involves site assessment, modular system installation, climate control calibration, nutrient solution preparation, seed selection and germination, automated monitoring deployment, pest management strategy implementation, harvest scheduling, and waste recycling integration. The process ensures sustainable food production in dense urban environments by optimizing space, reducing water usage, and leveraging IoT technologies for real-time crop health analytics. Extensive coordination across engineering, horticulture, and logistics teams is required to maintain continuous yield and quality.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as labeled transitions
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
install_modules = Transition(label='Install Modules')
calibrate_climate = Transition(label='Calibrate Climate')
prepare_nutrients = Transition(label='Prepare Nutrients')
select_seeds = Transition(label='Select Seeds')
start_germination = Transition(label='Start Germination')
deploy_sensors = Transition(label='Deploy Sensors')
monitor_growth = Transition(label='Monitor Growth')
manage_pests = Transition(label='Manage Pests')
schedule_harvest = Transition(label='Schedule Harvest')
process_waste = Transition(label='Process Waste')
optimize_energy = Transition(label='Optimize Energy')
conduct_training = Transition(label='Conduct Training')
update_records = Transition(label='Update Records')
review_performance = Transition(label='Review Performance')

# Construct the partial order reflecting reasonable sequencing and concurrency:
# 1. Site Survey --> Design Layout --> Install Modules --> Calibrate Climate (sequential)
# 2. Prepare Nutrients runs concurrently with calibration
# 3. Select Seeds --> Start Germination sequentially after nutrients prepared
# 4. Deploy Sensors depends on Modules installed and Germination started (parallel inputs)
# 5. Monitor Growth follows sensors deployed
# 6. Manage Pests and Schedule Harvest can proceed in parallel after monitoring started
# 7. Process Waste and Optimize Energy happen concurrently, after harvest scheduled
# 8. Conduct Training and Update Records can be done concurrently, after process waste and optimize energy
# 9. Finally, Review Performance after training and update records

# Concurrent starts:
# Prepare Nutrients starts after Design Layout (parallel with Calibrate Climate after Install Modules)
# Select Seeds depends on Prepare Nutrients

# Build nodes list
nodes = [
    site_survey,
    design_layout,
    install_modules,
    calibrate_climate,
    prepare_nutrients,
    select_seeds,
    start_germination,
    deploy_sensors,
    monitor_growth,
    manage_pests,
    schedule_harvest,
    process_waste,
    optimize_energy,
    conduct_training,
    update_records,
    review_performance
]

root = StrictPartialOrder(nodes=nodes)

# Define order edges:
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, install_modules)

root.order.add_edge(install_modules, calibrate_climate)
root.order.add_edge(design_layout, prepare_nutrients)
root.order.add_edge(prepare_nutrients, select_seeds)
root.order.add_edge(select_seeds, start_germination)

root.order.add_edge(install_modules, deploy_sensors)
root.order.add_edge(start_germination, deploy_sensors)

root.order.add_edge(deploy_sensors, monitor_growth)

root.order.add_edge(monitor_growth, manage_pests)
root.order.add_edge(monitor_growth, schedule_harvest)

root.order.add_edge(schedule_harvest, process_waste)
root.order.add_edge(schedule_harvest, optimize_energy)

root.order.add_edge(process_waste, conduct_training)
root.order.add_edge(optimize_energy, conduct_training)

root.order.add_edge(process_waste, update_records)
root.order.add_edge(optimize_energy, update_records)

root.order.add_edge(conduct_training, review_performance)
root.order.add_edge(update_records, review_performance)