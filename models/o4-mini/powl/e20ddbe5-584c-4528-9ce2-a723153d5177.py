# Generated from: e20ddbe5-584c-4528-9ce2-a723153d5177.json
# Description: This process outlines the establishment of a sustainable urban rooftop farm in a metropolitan environment. It begins with site analysis and structural assessment to ensure roof load capacity and sunlight exposure. Next, soil-less medium selection and hydroponic system design are conducted to optimize water and nutrient delivery. Procurement involves sourcing organic seeds and eco-friendly materials, followed by installation of irrigation and climate control systems. Planting schedules are created based on seasonal cycles, alongside pest management planning using integrated pest management strategies. Regular monitoring includes data collection on plant growth, moisture levels, and system performance, while adapting to weather fluctuations through automated controls. Harvesting and packaging protocols prioritize freshness and minimal waste. Finally, community engagement and educational workshops are organized to promote urban agriculture awareness and sustainability practices.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_analysis     = Transition(label='Site Analysis')
load_test         = Transition(label='Load Test')
sunlight_map      = Transition(label='Sunlight Map')
medium_select     = Transition(label='Medium Select')
hydro_design      = Transition(label='Hydro Design')
procure_seeds     = Transition(label='Procure Seeds')
install_irrigation= Transition(label='Install Irrigation')
setup_climate     = Transition(label='Setup Climate')
create_schedule   = Transition(label='Create Schedule')
pest_control      = Transition(label='Pest Control')
monitor_growth    = Transition(label='Monitor Growth')
adjust_systems    = Transition(label='Adjust Systems')
harvest_crops     = Transition(label='Harvest Crops')
package_produce   = Transition(label='Package Produce')
engage_community  = Transition(label='Engage Community')
host_workshops    = Transition(label='Host Workshops')

# Create a LOOP node for regular monitoring and adjustment
monitor_loop = OperatorPOWL(operator=Operator.LOOP,
                           children=[monitor_growth, adjust_systems])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    site_analysis, load_test, sunlight_map,
    medium_select, hydro_design,
    procure_seeds, install_irrigation, setup_climate,
    create_schedule, pest_control,
    monitor_loop,
    harvest_crops, package_produce,
    engage_community, host_workshops
])

# Site analysis splits into load test and sunlight mapping (concurrent)
root.order.add_edge(site_analysis, load_test)
root.order.add_edge(site_analysis, sunlight_map)

# Structural results lead to medium selection
root.order.add_edge(load_test, medium_select)
root.order.add_edge(sunlight_map, medium_select)

# Medium selection then hydroponic design
root.order.add_edge(medium_select, hydro_design)

# Hydro design then procurement
root.order.add_edge(hydro_design, procure_seeds)

# Procurement then installation tasks (concurrent)
root.order.add_edge(procure_seeds, install_irrigation)
root.order.add_edge(procure_seeds, setup_climate)

# Installation then scheduling and pest control (concurrent)
root.order.add_edge(install_irrigation, create_schedule)
root.order.add_edge(setup_climate, create_schedule)
root.order.add_edge(install_irrigation, pest_control)
root.order.add_edge(setup_climate, pest_control)

# Scheduling & pest control lead into the monitoring loop
root.order.add_edge(create_schedule, monitor_loop)
root.order.add_edge(pest_control, monitor_loop)

# After loop exit, harvesting, packaging, then community activities (concurrent)
root.order.add_edge(monitor_loop, harvest_crops)
root.order.add_edge(harvest_crops, package_produce)
root.order.add_edge(package_produce, engage_community)
root.order.add_edge(package_produce, host_workshops)