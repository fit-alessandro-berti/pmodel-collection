# Generated from: b257e5c8-4a2f-4cc2-8f05-13ef95d911e0.json
# Description: This process outlines the complex steps involved in establishing an urban rooftop farm on a commercial building. It includes initial site evaluation, structural integrity checks, environmental impact assessments, securing permits from multiple authorities, designing modular planting systems, sourcing sustainable soil and water solutions, integrating IoT sensors for monitoring, training staff for urban agriculture techniques, marketing to local communities, and establishing supply chains for fresh produce distribution. The process ensures compliance with city regulations, maximizes yield in limited space, and promotes sustainable urban food production while addressing logistical and environmental challenges unique to rooftop farming.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as labeled transitions
Site_Survey = Transition(label='Site Survey')
Load_Test = Transition(label='Load Test')
Permit_Apply = Transition(label='Permit Apply')
Impact_Study = Transition(label='Impact Study')
Design_Layout = Transition(label='Design Layout')
Soil_Source = Transition(label='Soil Source')
Water_Setup = Transition(label='Water Setup')
Sensor_Install = Transition(label='Sensor Install')
Staff_Train = Transition(label='Staff Train')
Plant_Seed = Transition(label='Plant Seed')
Irrigation_Check = Transition(label='Irrigation Check')
Pest_Control = Transition(label='Pest Control')
Harvest_Plan = Transition(label='Harvest Plan')
Market_Launch = Transition(label='Market Launch')
Delivery_Route = Transition(label='Delivery Route')
Waste_Manage = Transition(label='Waste Manage')

# Step 1: Initial structural and site evaluation (Site Survey -> Load Test)
# These two activities are strictly ordered
evaluation = StrictPartialOrder(nodes=[Site_Survey, Load_Test])
evaluation.order.add_edge(Site_Survey, Load_Test)

# Step 2: Permit and environmental impact checks (Permit Apply and Impact Study in parallel after evaluation)
permits = StrictPartialOrder(nodes=[Permit_Apply, Impact_Study])

# evaluation strictly precedes permits
first_phase = StrictPartialOrder(nodes=[evaluation, permits])
first_phase.order.add_edge(evaluation, permits)

# Step 3: Design phase and sourcing materials concurrently:
# Design Layout -> Sensor Install -> Staff Train -> Plant Seed
# Soil Source and Water Setup can be done in parallel (concurrent)
design_nodes = [Design_Layout, Sensor_Install, Staff_Train, Plant_Seed]
design = StrictPartialOrder(nodes=design_nodes)
design.order.add_edge(Design_Layout, Sensor_Install)
design.order.add_edge(Sensor_Install, Staff_Train)
design.order.add_edge(Staff_Train, Plant_Seed)

soil_water = StrictPartialOrder(nodes=[Soil_Source, Water_Setup])  # concurrent

# design and soil_water are concurrent
material_and_design = StrictPartialOrder(nodes=[design, soil_water])

# Step 4: Planting validation and maintenance activities
# Plant_Seed precedes irrigation check and pest control in parallel
maint_nodes = [Irrigation_Check, Pest_Control]
maintenance = StrictPartialOrder(nodes=maint_nodes)

plant_and_maint = StrictPartialOrder(nodes=[Plant_Seed, maintenance])
plant_and_maint.order.add_edge(Plant_Seed, maintenance)

# Step 5: Harvest planning follows maintenance
harvest = Harvest_Plan

harvest_phase = StrictPartialOrder(nodes=[plant_and_maint, harvest])
harvest_phase.order.add_edge(plant_and_maint, harvest)

# Step 6: Marketing and delivery chains after harvest plan
marketing_delivery = StrictPartialOrder(nodes=[Market_Launch, Delivery_Route])
marketing_delivery.order.add_edge(Market_Launch, Delivery_Route)

# Step 7: Waste management concurrent with delivery route (cleanup can overlap)
cleanup_and_delivery = StrictPartialOrder(nodes=[Delivery_Route, Waste_Manage])  # concurrent

# Combine marketing and cleanup/delivery (Marketing precedes delivery, delivery concurrent with waste)
final_phase = StrictPartialOrder(nodes=[Market_Launch, cleanup_and_delivery])
final_phase.order.add_edge(Market_Launch, cleanup_and_delivery)  # Market_Launch -> cleanup_and_delivery

# Combine phases with their precedence:

# First phase (evaluation + permits)
# Second phase (material_and_design) after permits
# Third phase (harvest_phase) after material_and_design
# Fourth phase (final_phase) after harvest_phase

phase_2_after_permits = StrictPartialOrder(nodes=[permits, material_and_design])
phase_2_after_permits.order.add_edge(permits, material_and_design)

phase_3_after_design = StrictPartialOrder(nodes=[material_and_design, harvest_phase])
phase_3_after_design.order.add_edge(material_and_design, harvest_phase)

phase_4_after_harvest = StrictPartialOrder(nodes=[harvest_phase, final_phase])
phase_4_after_harvest.order.add_edge(harvest_phase, final_phase)

# Now combine all phases root
root = StrictPartialOrder(
    nodes=[evaluation, permits, material_and_design, harvest_phase, final_phase]
)
root.order.add_edge(evaluation, permits)
root.order.add_edge(permits, material_and_design)
root.order.add_edge(material_and_design, harvest_phase)
root.order.add_edge(harvest_phase, final_phase)