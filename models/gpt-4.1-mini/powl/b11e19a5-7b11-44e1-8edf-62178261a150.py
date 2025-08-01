# Generated from: b11e19a5-7b11-44e1-8edf-62178261a150.json
# Description: This process outlines the complex and multi-disciplinary steps required to establish a sustainable urban rooftop farm on a commercial building. It involves assessing structural integrity, securing permits, designing modular planting systems, integrating smart irrigation, sourcing organic seeds, coordinating with local suppliers, training staff, and establishing distribution channels for fresh produce. The process also includes continuous monitoring of plant health using IoT sensors, adjusting nutrient delivery, managing waste composting, and engaging the community through workshops and events. This atypical but increasingly relevant business process combines agriculture, technology, and urban planning to transform unused rooftop spaces into productive green areas that contribute to local food security and environmental sustainability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Survey = Transition(label='Site Survey')
Permit_Review = Transition(label='Permit Review')
Structural_Check = Transition(label='Structural Check')
Design_Layout = Transition(label='Design Layout')
System_Sourcing = Transition(label='System Sourcing')
Seed_Selection = Transition(label='Seed Selection')
Supplier_Contact = Transition(label='Supplier Contact')
Staff_Training = Transition(label='Staff Training')
Irrigation_Setup = Transition(label='Irrigation Setup')
Sensor_Install = Transition(label='Sensor Install')
Planting_Phase = Transition(label='Planting Phase')
Health_Monitor = Transition(label='Health Monitor')
Nutrient_Adjust = Transition(label='Nutrient Adjust')
Waste_Compost = Transition(label='Waste Compost')
Community_Event = Transition(label='Community Event')
Harvest_Plan = Transition(label='Harvest Plan')
Distribution = Transition(label='Distribution')
Feedback_Collect = Transition(label='Feedback Collect')

# Step 1: Initial assessment partial order: Site Survey --> Permit Review and Structural Check (concurrent)
initial_assessment = StrictPartialOrder(nodes=[Site_Survey, Permit_Review, Structural_Check])
initial_assessment.order.add_edge(Site_Survey, Permit_Review)
initial_assessment.order.add_edge(Site_Survey, Structural_Check)
# Permit Review and Structural Check can be done in parallel after Site Survey

# Step 2: Design & sourcing (Design Layout --> System Sourcing)
design_sourcing = StrictPartialOrder(nodes=[Design_Layout, System_Sourcing])
design_sourcing.order.add_edge(Design_Layout, System_Sourcing)

# Step 3: Seed & supplier coordination (Seed Selection --> Supplier Contact)
seed_supplier = StrictPartialOrder(nodes=[Seed_Selection, Supplier_Contact])
seed_supplier.order.add_edge(Seed_Selection, Supplier_Contact)

# Step 4: Staff training and irrigation setup (concurrent)
training_irrigation = StrictPartialOrder(nodes=[Staff_Training, Irrigation_Setup])
# concurrent so no edges

# Step 5: Sensor installation before planting
sensor_planting = StrictPartialOrder(nodes=[Sensor_Install, Planting_Phase])
sensor_planting.order.add_edge(Sensor_Install, Planting_Phase)

# Step 6: Continuous monitoring loop:
# loop body: (Health Monitor --> Nutrient Adjust)
monitor_loop_body = StrictPartialOrder(nodes=[Health_Monitor, Nutrient_Adjust])
monitor_loop_body.order.add_edge(Health_Monitor, Nutrient_Adjust)

# loop loop body (B) = Waste Compost --> Community Event (in parallel)
waste_community = StrictPartialOrder(nodes=[Waste_Compost, Community_Event])
# concurrent in loop body B, no edges

# The loop node: execute monitor_loop_body (A), then choose exit OR execute waste_community (B) then loop again
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_loop_body, waste_community])

# Step 7: Harvest plan -> Distribution -> Feedback Collect (strict sequence)
harvest_dist_feedback = StrictPartialOrder(nodes=[Harvest_Plan, Distribution, Feedback_Collect])
harvest_dist_feedback.order.add_edge(Harvest_Plan, Distribution)
harvest_dist_feedback.order.add_edge(Distribution, Feedback_Collect)

# Compose Setup phase: initial_assessment -> design_sourcing -> seed_supplier -> training_irrigation -> sensor_planting
setup_phase = StrictPartialOrder(
    nodes=[initial_assessment, design_sourcing, seed_supplier, training_irrigation, sensor_planting]
)
setup_phase.order.add_edge(initial_assessment, design_sourcing)
setup_phase.order.add_edge(design_sourcing, seed_supplier)
setup_phase.order.add_edge(seed_supplier, training_irrigation)
setup_phase.order.add_edge(training_irrigation, sensor_planting)

# Final full model phase:
# setup_phase --> monitor_loop --> harvest_dist_feedback

root = StrictPartialOrder(
    nodes=[setup_phase, monitor_loop, harvest_dist_feedback]
)
root.order.add_edge(setup_phase, monitor_loop)
root.order.add_edge(monitor_loop, harvest_dist_feedback)