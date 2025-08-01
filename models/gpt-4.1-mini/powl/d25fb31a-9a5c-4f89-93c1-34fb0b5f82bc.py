# Generated from: d25fb31a-9a5c-4f89-93c1-34fb0b5f82bc.json
# Description: This process outlines the steps required to establish a sustainable urban rooftop farming system on a commercial building. It begins with structural assessment to ensure roof load capacity, followed by environmental analysis for sunlight and wind exposure. Next, modular planting bed design is customized to optimize space and irrigation efficiency. After procurement of soil and organic nutrients, installation of automated drip irrigation and sensor systems takes place. Seed selection is tailored to microclimate conditions and market demand. Planting is scheduled in phases to maximize yield throughout the year. Continuous monitoring involves data collection on moisture, temperature, and pest activity, triggering adaptive maintenance interventions. Harvesting is coordinated with local vendors and community programs. Finally, waste composting and system feedback loops are implemented to ensure sustainability and scalability for future expansion.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
assess = Transition(label='Assess Structure')
analyze = Transition(label='Analyze Environment')
design = Transition(label='Design Modules')
procure = Transition(label='Procure Materials')
install_irrigation = Transition(label='Install Irrigation')
set_sensors = Transition(label='Set Sensors')
select_seeds = Transition(label='Select Seeds')
schedule = Transition(label='Schedule Planting')
monitor = Transition(label='Monitor Growth')
collect_data = Transition(label='Collect Data')
manage_pests = Transition(label='Manage Pests')
harvest = Transition(label='Harvest Crops')
coordinate = Transition(label='Coordinate Sales')
compost = Transition(label='Compost Waste')
review = Transition(label='Review Feedback')

# Compose partial orders

# Installation steps: Procure -> (Install Irrigation AND Set Sensors) in parallel
install_parallel = StrictPartialOrder(nodes=[install_irrigation, set_sensors])
# No order between install_irrigation and set_sensors => concurrent

procure_to_install = StrictPartialOrder(nodes=[procure, install_parallel])
procure_to_install.order.add_edge(procure, install_parallel)

# Monitoring steps: Monitor Growth -> Collect Data -> Manage Pests (sequential)
monitor_po = StrictPartialOrder(nodes=[monitor, collect_data, manage_pests])
monitor_po.order.add_edge(monitor, collect_data)
monitor_po.order.add_edge(collect_data, manage_pests)

# Harvest and coordinate sales sequential
harvest_coord = StrictPartialOrder(nodes=[harvest, coordinate])
harvest_coord.order.add_edge(harvest, coordinate)

# Compost and review feedback sequential
compost_review = StrictPartialOrder(nodes=[compost, review])
compost_review.order.add_edge(compost, review)

# Compose main flow
# Start: Assess -> Analyze -> Design -> Procure/Install -> Select Seeds -> Schedule -> Monitor -> Harvest/Coordinate -> Compost/Review

# Group Assess, Analyze, Design sequentially
start_seq = StrictPartialOrder(nodes=[assess, analyze, design])
start_seq.order.add_edge(assess, analyze)
start_seq.order.add_edge(analyze, design)

# Install steps embedded in procure_to_install with edges already added

# After design, go to procure_to_install
start_to_procure = StrictPartialOrder(nodes=[start_seq, procure_to_install])
start_to_procure.order.add_edge(start_seq, procure_to_install)

# After install, select seeds
procure_install_to_select = StrictPartialOrder(nodes=[start_to_procure, select_seeds])
procure_install_to_select.order.add_edge(start_to_procure, select_seeds)

# Then schedule planting
select_to_schedule = StrictPartialOrder(nodes=[procure_install_to_select, schedule])
select_to_schedule.order.add_edge(procure_install_to_select, schedule)

# Then monitoring (which itself is sequential monitor_po)
sched_to_monitor = StrictPartialOrder(nodes=[select_to_schedule, monitor_po])
sched_to_monitor.order.add_edge(select_to_schedule, monitor_po)

# Then harvest and coordinate sales
monitor_to_harvest = StrictPartialOrder(nodes=[sched_to_monitor, harvest_coord])
monitor_to_harvest.order.add_edge(sched_to_monitor, harvest_coord)

# Then compost and review
harvest_to_compost = StrictPartialOrder(nodes=[monitor_to_harvest, compost_review])
harvest_to_compost.order.add_edge(monitor_to_harvest, compost_review)

# This is the root model
root = harvest_to_compost