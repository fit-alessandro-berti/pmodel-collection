# Generated from: ba56f93a-d936-479b-9294-0bcf3c15e37d.json
# Description: This process outlines the entire operational cycle of an urban vertical farming facility that integrates IoT sensors, AI-driven climate control, and automated harvesting systems. Starting from seed selection and nutrient calibration, it includes environmental monitoring, pest management via bio-controls, growth optimization through AI analytics, and automated packaging for local distribution. The process also incorporates waste recycling, energy usage tracking, and community engagement for crop feedback, ensuring sustainability and efficiency in a confined urban environment where space and resources are limited but demand for fresh produce is high.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transition instances
Seed_Selection = Transition(label='Seed Selection')
Nutrient_Mix = Transition(label='Nutrient Mix')
IoT_Setup = Transition(label='IoT Setup')
Climate_Adjust = Transition(label='Climate Adjust')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control = Transition(label='Pest Control')
AI_Analysis = Transition(label='AI Analysis')
Water_Recycle = Transition(label='Water Recycle')
Energy_Audit = Transition(label='Energy Audit')
Harvest_Prep = Transition(label='Harvest Prep')
Auto_Harvest = Transition(label='Auto Harvest')
Quality_Check = Transition(label='Quality Check')
Pack_Produce = Transition(label='Pack Produce')
Delivery_Plan = Transition(label='Delivery Plan')
Feedback_Loop = Transition(label='Feedback Loop')
Waste_Manage = Transition(label='Waste Manage')

# Define partial orders inside main process to capture dependencies and concurrency

# Part 1: Seed Selection --> Nutrient Mix --> IoT Setup --> Climate Adjust
so1 = StrictPartialOrder(nodes=[Seed_Selection, Nutrient_Mix, IoT_Setup, Climate_Adjust])
so1.order.add_edge(Seed_Selection, Nutrient_Mix)
so1.order.add_edge(Nutrient_Mix, IoT_Setup)
so1.order.add_edge(IoT_Setup, Climate_Adjust)

# Part 2: Environmental Monitoring & Pest Control (concurrent with Growth Monitoring and AI Analysis)
# Growth_Monitor and Pest_Control and AI_Analysis run concurrently after Climate_Adjust
# We'll join Climate_Adjust before them
# So create a PO with Climate_Adjust --> all three concurrent nodes

concurrent_monitor = StrictPartialOrder(nodes=[Growth_Monitor, Pest_Control, AI_Analysis])

so2 = StrictPartialOrder(nodes=[Climate_Adjust, concurrent_monitor])
so2.order.add_edge(Climate_Adjust, concurrent_monitor)

# Part 3: Waste and Energy related tasks run concurrently and can be started after Pest Control and AI Analysis
# Pest_Control and AI_Analysis --> Waste_Manage and Energy_Audit and Water_Recycle (these three concurrent)
# Wait for Pest_Control and AI_Analysis to finish before these three start

waste_energy = StrictPartialOrder(nodes=[Water_Recycle, Energy_Audit, Waste_Manage])

so3 = StrictPartialOrder(nodes=[Pest_Control, AI_Analysis, waste_energy])
so3.order.add_edge(Pest_Control, waste_energy)
so3.order.add_edge(AI_Analysis, waste_energy)

# Part 4: Harvesting process: Harvest_Prep --> Auto_Harvest --> Quality_Check --> Pack_Produce --> Delivery_Plan
harvest_po = StrictPartialOrder(nodes=[Harvest_Prep, Auto_Harvest, Quality_Check, Pack_Produce, Delivery_Plan])
harvest_po.order.add_edge(Harvest_Prep, Auto_Harvest)
harvest_po.order.add_edge(Auto_Harvest, Quality_Check)
harvest_po.order.add_edge(Quality_Check, Pack_Produce)
harvest_po.order.add_edge(Pack_Produce, Delivery_Plan)

# Part 5: Feedback_Loop is a loop with Delivery_Plan feedbacking to Growth_Monitor
# Model as a loop: (Growth_Monitor, Delivery_Plan and Feedback_Loop)
# This is challenging because Growth_Monitor is also in concurrent_monitor
# We'll model the loop around Growth_Monitor and Feedback_Loop with Delivery_Plan
# Loop body: Growth_Monitor
# Loop redo: Feedback_Loop --> Growth_Monitor
# Exit after Delivery_Plan without Feedback_Loop

# Make a loop where A=Growth_Monitor, B= sequence Feedback_Loop (->) Growth_Monitor
feedback_seq = StrictPartialOrder(nodes=[Feedback_Loop, Growth_Monitor])
feedback_seq.order.add_edge(Feedback_Loop, Growth_Monitor)

loop_feedback = OperatorPOWL(operator=Operator.LOOP, children=[Growth_Monitor, feedback_seq])

# Now replace Growth_Monitor in concurrent_monitor with loop_feedback to represent this looping behavior

concurrent_monitor_loop = StrictPartialOrder(nodes=[loop_feedback, Pest_Control, AI_Analysis])

# Update so2 accordingly, Climate_Adjust --> concurrent_monitor_loop
so2_loop = StrictPartialOrder(nodes=[Climate_Adjust, concurrent_monitor_loop])
so2_loop.order.add_edge(Climate_Adjust, concurrent_monitor_loop)

# Part 6: Connect everything in global PO

# After so1 finishes at Climate_Adjust, so2_loop starts
# After Pest_Control and AI_Analysis finish (in so2_loop), so3 starts
# Harvesting (harvest_po) can start after so3 finishes and Climate_Adjust and IoT_Setup (represent preparation done)
# To allow some concurrency:
# Let's assume Harvest prep depends on Nutrient_Mix and IoT_Setup, and Waste/Energy finished

root_nodes = [so1, so2_loop, so3, harvest_po]

root = StrictPartialOrder(nodes=root_nodes)

# Connect edges between these subPOs

# so1 ends at Climate_Adjust, so2_loop starts at Climate_Adjust node inside it
root.order.add_edge(so1, so2_loop)

# so2_loop ends after Pest_Control and AI_Analysis, so3 depends on them at least
root.order.add_edge(so2_loop, so3)

# harvest_po depends on Nutrient_Mix and IoT_Setup (in so1), and so3 finish

# so1 --> harvest_po
root.order.add_edge(so1, harvest_po)
# so3 --> harvest_po
root.order.add_edge(so3, harvest_po)