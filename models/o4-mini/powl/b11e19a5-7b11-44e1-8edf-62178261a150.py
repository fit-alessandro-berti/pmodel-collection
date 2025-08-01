# Generated from: b11e19a5-7b11-44e1-8edf-62178261a150.json
# Description: This process outlines the complex and multi-disciplinary steps required to establish a sustainable urban rooftop farm on a commercial building. It involves assessing structural integrity, securing permits, designing modular planting systems, integrating smart irrigation, sourcing organic seeds, coordinating with local suppliers, training staff, and establishing distribution channels for fresh produce. The process also includes continuous monitoring of plant health using IoT sensors, adjusting nutrient delivery, managing waste composting, and engaging the community through workshops and events. This atypical but increasingly relevant business process combines agriculture, technology, and urban planning to transform unused rooftop spaces into productive green areas that contribute to local food security and environmental sustainability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey      = Transition(label='Site Survey')
struct_check     = Transition(label='Structural Check')
permit_review    = Transition(label='Permit Review')
design_layout    = Transition(label='Design Layout')
system_sourcing  = Transition(label='System Sourcing')
seed_selection   = Transition(label='Seed Selection')
supplier_contact = Transition(label='Supplier Contact')
staff_training   = Transition(label='Staff Training')
irrigation_setup = Transition(label='Irrigation Setup')
sensor_install   = Transition(label='Sensor Install')
planting_phase   = Transition(label='Planting Phase')
health_monitor   = Transition(label='Health Monitor')
nutrient_adjust  = Transition(label='Nutrient Adjust')
waste_compost    = Transition(label='Waste Compost')
community_event  = Transition(label='Community Event')
harvest_plan     = Transition(label='Harvest Plan')
distribution     = Transition(label='Distribution')
feedback_collect = Transition(label='Feedback Collect')

# Define the loop body for continuous monitoring activities
body = StrictPartialOrder(nodes=[nutrient_adjust, waste_compost, community_event])
# No internal order: these can happen in any order (concurrent within the loop body)

# Define the monitoring loop: monitor -> (adjust|compost|event) -> monitor ...
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[health_monitor, body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    struct_check,
    permit_review,
    design_layout,
    system_sourcing,
    seed_selection,
    supplier_contact,
    staff_training,
    irrigation_setup,
    sensor_install,
    planting_phase,
    monitor_loop,
    harvest_plan,
    distribution,
    feedback_collect
])

# Initial assessment: survey -> structural check -> permit
root.order.add_edge(site_survey, struct_check)
root.order.add_edge(struct_check, permit_review)

# After permits, design
root.order.add_edge(permit_review, design_layout)

# After design, sourcing seeds and systems in parallel
root.order.add_edge(design_layout, system_sourcing)
root.order.add_edge(design_layout, seed_selection)
root.order.add_edge(design_layout, supplier_contact)

# System sourcing leads to staff training and irrigation setup
root.order.add_edge(system_sourcing, staff_training)
root.order.add_edge(system_sourcing, irrigation_setup)

# Supplier contact also needed for irrigation setup
root.order.add_edge(supplier_contact, irrigation_setup)

# Irrigation set up before sensor installation
root.order.add_edge(irrigation_setup, sensor_install)

# Seeds, sensors, and trained staff before planting
root.order.add_edge(seed_selection, planting_phase)
root.order.add_edge(sensor_install, planting_phase)
root.order.add_edge(staff_training, planting_phase)

# After planting, enter the continuous monitoring loop
root.order.add_edge(planting_phase, monitor_loop)

# After exiting the loop, proceed to harvest and distribution
root.order.add_edge(monitor_loop, harvest_plan)
root.order.add_edge(harvest_plan, distribution)
root.order.add_edge(distribution, feedback_collect)