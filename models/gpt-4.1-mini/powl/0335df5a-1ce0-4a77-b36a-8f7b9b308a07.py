# Generated from: 0335df5a-1ce0-4a77-b36a-8f7b9b308a07.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban rooftop farm on a commercial building. It involves assessing structural integrity, securing permits, designing the layout for optimal sunlight and water usage, installing irrigation and hydroponic systems, sourcing organic seeds, training local staff, implementing pest control measures, monitoring crop growth using IoT sensors, coordinating harvest logistics, and marketing fresh produce directly to urban consumers. The process also includes waste recycling, seasonal crop rotation planning, integrating renewable energy sources, and continuous community engagement to promote urban agriculture awareness and education.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Site_Survey = Transition(label='Site Survey')
Permit_Filing = Transition(label='Permit Filing')
Structure_Check = Transition(label='Structure Check')
Layout_Design = Transition(label='Layout Design')
Water_Setup = Transition(label='Water Setup')
Seed_Sourcing = Transition(label='Seed Sourcing')
Staff_Training = Transition(label='Staff Training')
Pest_Control = Transition(label='Pest Control')
IoT_Monitoring = Transition(label='IoT Monitoring')
Crop_Harvest = Transition(label='Crop Harvest')
Waste_Recycling = Transition(label='Waste Recycling')
Energy_Setup = Transition(label='Energy Setup')
Market_Plan = Transition(label='Market Plan')
Community_Engage = Transition(label='Community Engage')
Crop_Rotation = Transition(label='Crop Rotation')

# Step 1: Assess structural integrity (Site Survey -> Structure Check)
survey_and_structure = StrictPartialOrder(nodes=[Site_Survey, Structure_Check])
survey_and_structure.order.add_edge(Site_Survey, Structure_Check)

# Step 2: Secure permits (after structure check)
permits = Permit_Filing

# Step 3: Design layout that includes Water Setup (irrigation/hydroponics)
# Layout design must precede Water Setup
layout_water = StrictPartialOrder(nodes=[Layout_Design, Water_Setup])
layout_water.order.add_edge(Layout_Design, Water_Setup)

# Step 4: Seed Sourcing and Staff Training happen in parallel after permits
seed_and_staff = StrictPartialOrder(nodes=[Seed_Sourcing, Staff_Training])
# Both after permits

# Step 5: Pest Control and IoT Monitoring are after seed & staff
pest_and_iot = StrictPartialOrder(nodes=[Pest_Control, IoT_Monitoring])
# Both after seed_and_staff

# Step 6: Crop Harvest happens after pest control and IoT monitoring
harvest = Crop_Harvest

# Step 7: Waste Recycling, Energy Setup, Community Engage, Crop Rotation happen continuously or concurrently
# These can run concurrently, but Crop Rotation logically related to the farm operation cycle, so can be parallel with Waste Recycling, Energy Setup, Community Engage.

# Group these four in parallel
misc_activities = StrictPartialOrder(nodes=[Waste_Recycling, Energy_Setup, Community_Engage, Crop_Rotation])

# Step 8: Marketing Plan happens after Crop Harvest
marketing = Market_Plan

# Compose partial orders and dependencies (edges) according to process logic.

# Main core process partial order node sets:
# Start: survey_and_structure
# Then permits
# Then layout_water
# Then seed_and_staff
# Then pest_and_iot
# Then harvest
# Then marketing

# We'll create PO nodes for these groupings to link them
po1 = survey_and_structure                  # Site Survey -> Structure Check
po2 = StrictPartialOrder(nodes=[permits])  # Permit Filing
po3 = layout_water                          # Layout Design -> Water Setup
po4 = seed_and_staff                        # Seed Sourcing || Staff Training
po5 = pest_and_iot                         # Pest Control || IoT Monitoring
po6 = StrictPartialOrder(nodes=[harvest])  # Crop Harvest
po7 = StrictPartialOrder(nodes=[marketing]) # Market Plan
po8 = misc_activities                       # Waste Recycling || Energy Setup || Community Engage || Crop Rotation

# Create root PO with all nodes: po1..po8
nodes = [po1, po2, po3, po4, po5, po6, po7, po8]
root = StrictPartialOrder(nodes=nodes)

# Now add edges reflecting the process flow

# po1 -> po2 (after survey and structure check, permit filing)
root.order.add_edge(po1, po2)

# po2 -> po3 (permits before layout and water setup)
root.order.add_edge(po2, po3)

# po3 -> po4 (layout and water setup before seed sourcing and staff training)
root.order.add_edge(po3, po4)

# po4 -> po5 (seed sourcing and staff training before pest control and IoT monitoring)
root.order.add_edge(po4, po5)

# po5 -> po6 (pest control and IoT monitoring before crop harvest)
root.order.add_edge(po5, po6)

# po6 -> po7 (crop harvest before marketing)
root.order.add_edge(po6, po7)

# po8 (waste recycling, energy, community, crop rotation) runs concurrently but could start early
# We can assume it is concurrent with main flow but after po1 (site survey and structure check)
root.order.add_edge(po1, po8)