# Generated from: d25fb31a-9a5c-4f89-93c1-34fb0b5f82bc.json
# Description: This process outlines the steps required to establish a sustainable urban rooftop farming system on a commercial building. It begins with structural assessment to ensure roof load capacity, followed by environmental analysis for sunlight and wind exposure. Next, modular planting bed design is customized to optimize space and irrigation efficiency. After procurement of soil and organic nutrients, installation of automated drip irrigation and sensor systems takes place. Seed selection is tailored to microclimate conditions and market demand. Planting is scheduled in phases to maximize yield throughout the year. Continuous monitoring involves data collection on moisture, temperature, and pest activity, triggering adaptive maintenance interventions. Harvesting is coordinated with local vendors and community programs. Finally, waste composting and system feedback loops are implemented to ensure sustainability and scalability for future expansion.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
assess = Transition(label='Assess Structure')
analyze = Transition(label='Analyze Environment')
design = Transition(label='Design Modules')
procure = Transition(label='Procure Materials')
install = Transition(label='Install Irrigation')
set_sensors = Transition(label='Set Sensors')
select_seeds = Transition(label='Select Seeds')
schedule = Transition(label='Schedule Planting')
monitor_growth = Transition(label='Monitor Growth')
collect_data = Transition(label='Collect Data')
manage_pests = Transition(label='Manage Pests')
harvest = Transition(label='Harvest Crops')
coordinate = Transition(label='Coordinate Sales')
compost = Transition(label='Compost Waste')
review_feedback = Transition(label='Review Feedback')
skip = SilentTransition()

# Monitoring loop: Monitor Growth, Collect Data, Manage Pests concurrently
mon_body = StrictPartialOrder(nodes=[monitor_growth, collect_data, manage_pests])
# no internal order => fully concurrent
mon_loop = OperatorPOWL(operator=Operator.LOOP, children=[mon_body, skip])

# Feedback loop: Compost Waste -> Review Feedback, then repeat
fb_body = StrictPartialOrder(nodes=[compost, review_feedback])
fb_body.order.add_edge(compost, review_feedback)
fb_loop = OperatorPOWL(operator=Operator.LOOP, children=[fb_body, skip])

# Root partial order
root = StrictPartialOrder(nodes=[
    assess, analyze, design, procure, install, set_sensors,
    select_seeds, schedule, mon_loop, harvest, coordinate, fb_loop
])

# Define the overall sequence
root.order.add_edge(assess, analyze)
root.order.add_edge(analyze, design)
root.order.add_edge(design, procure)
root.order.add_edge(procure, install)
root.order.add_edge(install, set_sensors)
root.order.add_edge(set_sensors, select_seeds)
root.order.add_edge(select_seeds, schedule)
root.order.add_edge(schedule, mon_loop)
root.order.add_edge(mon_loop, harvest)
root.order.add_edge(harvest, coordinate)
root.order.add_edge(coordinate, fb_loop)