# Generated from: fb46e5c2-00d3-4d86-bf9c-326d5c813417.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm within a dense metropolitan area. It begins with site analysis and environmental impact assessment, followed by modular infrastructure design and integration of hydroponic systems. Subsequent activities include climate control calibration, nutrient solution optimization, and automated lighting configuration. The process also covers workforce training on advanced cultivation techniques, pest monitoring with AI drones, and real-time crop health analytics. Finally, it concludes with supply chain synchronization for local distribution and continuous system maintenance planning to ensure sustainable production and minimal ecological footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
Site_Analysis = Transition(label='Site Analysis')
Impact_Review = Transition(label='Impact Review')
Modular_Design = Transition(label='Modular Design')
System_Integration = Transition(label='System Integration')
Climate_Setup = Transition(label='Climate Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Light_Config = Transition(label='Light Config')
Staff_Training = Transition(label='Staff Training')
Pest_Monitor = Transition(label='Pest Monitor')
Drone_Deploy = Transition(label='Drone Deploy')
Health_Scan = Transition(label='Health Scan')
Data_Logging = Transition(label='Data Logging')
Supply_Sync = Transition(label='Supply Sync')
Maintenance_Plan = Transition(label='Maintenance Plan')
Waste_Manage = Transition(label='Waste Manage')

# Step 1: Site analysis and environmental impact assessment in sequence
analysis_and_review = StrictPartialOrder(nodes=[Site_Analysis, Impact_Review])
analysis_and_review.order.add_edge(Site_Analysis, Impact_Review)

# Step 2: Modular infrastructure design and integration in sequence
design_and_integration = StrictPartialOrder(nodes=[Modular_Design, System_Integration])
design_and_integration.order.add_edge(Modular_Design, System_Integration)

# Step 3: Climate control calibration, nutrient solution optimization, and automated lighting configuration
# sequence: Climate Setup --> Nutrient Mix --> Light Config
climate_nutrient_light = StrictPartialOrder(nodes=[Climate_Setup, Nutrient_Mix, Light_Config])
climate_nutrient_light.order.add_edge(Climate_Setup, Nutrient_Mix)
climate_nutrient_light.order.add_edge(Nutrient_Mix, Light_Config)

# Step 4: Workforce training on advanced cultivation techniques
# Staff Training is independent of above but logically after setup
# Step 5 & 6: Pest monitoring with AI drones and real-time crop health analytics.
# Pest Monitor -> Drone Deploy (drone supports pest monitoring)
pest_and_drone = StrictPartialOrder(nodes=[Pest_Monitor, Drone_Deploy])
pest_and_drone.order.add_edge(Pest_Monitor, Drone_Deploy)

# Health Scan and Data Logging together (concurrent)
health_and_logging = StrictPartialOrder(nodes=[Health_Scan, Data_Logging])

# Sequence pest_and_drone --> health_and_logging
pest_and_health = StrictPartialOrder(nodes=[pest_and_drone, health_and_logging])
pest_and_health.order.add_edge(pest_and_drone, health_and_logging)

# Step 7 & 8: Supply chain synchronization and continuous maintenance planning
# With Waste Management concurrent with Maintenance Plan
maintenance_and_waste = StrictPartialOrder(nodes=[Maintenance_Plan, Waste_Manage])

# Supply Sync before maintenance_and_waste
final_steps = StrictPartialOrder(nodes=[Supply_Sync, maintenance_and_waste])
final_steps.order.add_edge(Supply_Sync, maintenance_and_waste)

# Build entire process as partial orders with edges:
# Overall sequence:
# (analysis_and_review) --> (design_and_integration) --> (climate_nutrient_light) --> Staff_Training in parallel with pest_and_health --> final_steps

# Staff Training concurrent with pest_and_health
training_and_pest_block = StrictPartialOrder(nodes=[Staff_Training, pest_and_health])

# No order between Staff_Training and pest_and_health, concurrent

# Now sequential chaining of blocks:

root = StrictPartialOrder(
    nodes=[analysis_and_review, design_and_integration, climate_nutrient_light, training_and_pest_block, final_steps]
)

root.order.add_edge(analysis_and_review, design_and_integration)
root.order.add_edge(design_and_integration, climate_nutrient_light)
root.order.add_edge(climate_nutrient_light, training_and_pest_block)
root.order.add_edge(training_and_pest_block, final_steps)