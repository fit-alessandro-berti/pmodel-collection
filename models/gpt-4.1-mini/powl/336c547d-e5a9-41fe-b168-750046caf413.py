# Generated from: 336c547d-e5a9-41fe-b168-750046caf413.json
# Description: This process outlines the complex and interdisciplinary steps required to establish a sustainable urban rooftop farm in a dense city environment. It involves initial site assessment, structural integrity analysis, microclimate evaluation, soil substrate preparation, irrigation system design, plant species selection optimized for urban conditions, installation of renewable energy sources, pest control planning with eco-friendly methods, community engagement and education programs, real-time environmental monitoring setup, harvest scheduling, waste composting integration, and finally, distribution logistics tailored to local markets and restaurants. Each activity requires careful coordination between architects, agronomists, engineers, and community stakeholders to ensure the project’s viability and long-term impact on urban food security and green space enhancement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Survey = Transition(label='Site Survey')
Load_Testing = Transition(label='Load Testing')
Climate_Study = Transition(label='Climate Study')
Soil_Mix = Transition(label='Soil Mix')
Irrigation_Plan = Transition(label='Irrigation Plan')
Crop_Choice = Transition(label='Crop Choice')
Energy_Install = Transition(label='Energy Install')
Pest_Monitor = Transition(label='Pest Monitor')
Community_Meet = Transition(label='Community Meet')
Sensor_Setup = Transition(label='Sensor Setup')
Harvest_Plan = Transition(label='Harvest Plan')
Waste_Cycle = Transition(label='Waste Cycle')
Market_Link = Transition(label='Market Link')
Training_Day = Transition(label='Training Day')
Report_Review = Transition(label='Report Review')

# Structure the process as partial orders with dependencies representing logical flow
# Step 1: Initial site assessment sequence
step1 = StrictPartialOrder(nodes=[Site_Survey, Load_Testing, Climate_Study])
step1.order.add_edge(Site_Survey, Load_Testing)
step1.order.add_edge(Load_Testing, Climate_Study)

# Step 2: Soil substrate preparation, irrigation design, crop choice can happen concurrently but after site assessment
step2 = StrictPartialOrder(nodes=[Soil_Mix, Irrigation_Plan, Crop_Choice])
# Concurrent, so no order edges among step2 nodes

# Step 3: Renewable energy installation and pest monitoring can be concurrent, after soil and irrigation and crop choice
step3 = StrictPartialOrder(nodes=[Energy_Install, Pest_Monitor])
# Concurrent internally

# Step 4: Community engagement and training can happen concurrently, after pest monitoring
step4 = StrictPartialOrder(nodes=[Community_Meet, Training_Day])

# Step 5: Sensor setup for monitoring, after energy install and community engagement & training
step5 = StrictPartialOrder(nodes=[Sensor_Setup])

# Step 6: Harvest plan and waste cycle after sensor setup
step6 = StrictPartialOrder(nodes=[Harvest_Plan, Waste_Cycle])
# concurrent internally

# Step 7: Market link and report review after harvest and waste cycle
step7 = StrictPartialOrder(nodes=[Market_Link, Report_Review])
# concurrent internally

# Build top-level partial order with all steps and the appropriate order edges between steps

# Collect all step nodes as submodels
# We'll create a StrictPartialOrder with nodes=step1, step2, step3, step4, step5, step6, step7
# Then order edges link these steps in sequence, with some concurrency inside steps as defined

root = StrictPartialOrder(nodes=[step1, step2, step3, step4, step5, step6, step7])

# Add edges between steps to represent flow/dependency:
# step1 --> step2
root.order.add_edge(step1, step2)

# step2 --> step3
root.order.add_edge(step2, step3)

# step3 --> step4
root.order.add_edge(step3, step4)

# step4 --> step5
root.order.add_edge(step4, step5)

# step5 --> step6
root.order.add_edge(step5, step6)

# step6 --> step7
root.order.add_edge(step6, step7)