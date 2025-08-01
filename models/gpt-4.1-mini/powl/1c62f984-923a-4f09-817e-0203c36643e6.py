# Generated from: 1c62f984-923a-4f09-817e-0203c36643e6.json
# Description: This process outlines the complex and atypical steps involved in establishing an urban vertical farming system within a repurposed industrial building. It includes site assessment, environmental simulation, modular installation, nutrient cycling optimization, and integration of AI-driven crop monitoring. The workflow also covers regulatory compliance, energy management, and community engagement to ensure sustainable and scalable food production in densely populated areas. Each activity is designed to address unique challenges of urban agriculture, such as limited space, resource efficiency, and real-time data analytics for yield maximization.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Survey = Transition(label='Site Survey')
Structural_Test = Transition(label='Structural Test')
Light_Setup = Transition(label='Light Setup')
Climate_Control = Transition(label='Climate Control')
Water_Loop = Transition(label='Water Loop')
Nutrient_Mix = Transition(label='Nutrient Mix')
Sensor_Install = Transition(label='Sensor Install')
AI_Integration = Transition(label='AI Integration')
Crop_Seeding = Transition(label='Crop Seeding')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Check = Transition(label='Pest Check')
Energy_Audit = Transition(label='Energy Audit')
Waste_Cycle = Transition(label='Waste Cycle')
Regulation_Review = Transition(label='Regulation Review')
Community_Meet = Transition(label='Community Meet')
Yield_Report = Transition(label='Yield Report')

# Structure:
# Core foundational work: Site Survey and Structural Test sequentially
foundational_PO = StrictPartialOrder(nodes=[Site_Survey, Structural_Test])
foundational_PO.order.add_edge(Site_Survey, Structural_Test)

# Setup environmental control: Light Setup and Climate Control concurrently after Structural Test
env_control_PO = StrictPartialOrder(nodes=[Light_Setup, Climate_Control])
# No order between Light_Setup and Climate_Control so they are concurrent

# After environmental control, install sensors and integrate AI concurrently
sensor_ai_PO = StrictPartialOrder(nodes=[Sensor_Install, AI_Integration])
# Concurrent nodes

# Crop seeding after sensor and AI integration
# Growth Monitoring (Growth Monitor) after Crop Seeding
# Pest Check after Growth Monitor
crop_PO = StrictPartialOrder(nodes=[Crop_Seeding, Growth_Monitor, Pest_Check])
crop_PO.order.add_edge(Crop_Seeding, Growth_Monitor)
crop_PO.order.add_edge(Growth_Monitor, Pest_Check)

# Nutrient and water loops modeled as a loop: Water Loop then Nutrient Mix in loop until exit
nutrient_loop = OperatorPOWL(operator=Operator.LOOP, children=[Water_Loop, Nutrient_Mix])

# Waste cycle and energy audit concurrently after nutrient loop and crop activities
post_growth_PO = StrictPartialOrder(nodes=[Waste_Cycle, Energy_Audit])
# concurrent, no edges

# Regulation Review and Community Meeting concurrently after foundational checks
compliance_PO = StrictPartialOrder(nodes=[Regulation_Review, Community_Meet])
# concurrent

# Final yield report after pest check, energy audit, waste cycle, regulation review, community meet
final_PO_nodes = [Yield_Report]
final_PO = StrictPartialOrder(nodes=final_PO_nodes)

# Now integrate all parts in correct order

# 1. foundational_PO --> env_control_PO --> sensor_ai_PO
part1 = StrictPartialOrder(nodes=[foundational_PO, env_control_PO, sensor_ai_PO])
part1.order.add_edge(foundational_PO, env_control_PO)
part1.order.add_edge(env_control_PO, sensor_ai_PO)

# 2. sensor_ai_PO --> crop_PO --> nutrient loop
part2 = StrictPartialOrder(nodes=[sensor_ai_PO, crop_PO, nutrient_loop])
part2.order.add_edge(sensor_ai_PO, crop_PO)
part2.order.add_edge(crop_PO, nutrient_loop)

# 3. nutrient_loop --> post_growth_PO
part3 = StrictPartialOrder(nodes=[nutrient_loop, post_growth_PO])
part3.order.add_edge(nutrient_loop, post_growth_PO)

# 4. foundational_PO --> compliance_PO
# annotate that compliance_PO depends on foundational_PO but can run concurrently with env_control_PO etc
# We'll integrate compliance_PO after foundational_PO in final PO
part4 = StrictPartialOrder(nodes=[foundational_PO, compliance_PO])
part4.order.add_edge(foundational_PO, compliance_PO)

# 5. Final join: everything prior converges to Yield_Report:

final_full = StrictPartialOrder(nodes=[
    foundational_PO, env_control_PO, sensor_ai_PO, crop_PO, nutrient_loop,
    post_growth_PO, compliance_PO, Yield_Report
])

# Add all edges for sequencing:
final_full.order.add_edge(foundational_PO, env_control_PO)
final_full.order.add_edge(env_control_PO, sensor_ai_PO)
final_full.order.add_edge(sensor_ai_PO, crop_PO)
final_full.order.add_edge(crop_PO, nutrient_loop)
final_full.order.add_edge(nutrient_loop, post_growth_PO)
final_full.order.add_edge(foundational_PO, compliance_PO)

# Yield_Report after pest check, energy audit, waste cycle, regulation review, community meet
final_full.order.add_edge(crop_PO, Yield_Report)          # pest check before Yield_Report
final_full.order.add_edge(post_growth_PO, Yield_Report)   # energy audit and waste cycle before Yield_Report
final_full.order.add_edge(compliance_PO, Yield_Report)    # regulation and community meet before Yield_Report

root = final_full