# Generated from: 5eafc56c-44f1-4ad5-80ea-194cae47f802.json
# Description: This process outlines the complex and atypical steps required to establish an urban rooftop farm in a dense metropolitan area. It involves assessing rooftop structural integrity, navigating municipal permits, designing modular planting systems, sourcing sustainable materials, integrating IoT sensors for climate control, training staff on vertical farming techniques, and coordinating with local markets for produce distribution. Additional considerations include managing water recycling systems, implementing pest control without harmful chemicals, optimizing energy use via solar panels, and ensuring compliance with health and safety regulations. The process culminates in a launch event to promote community engagement and secure ongoing funding through local grants and partnerships, ensuring sustainability and long-term impact within an urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Survey = Transition(label='Site Survey')
Permit_Review = Transition(label='Permit Review')
Structural_Test = Transition(label='Structural Test')
Design_Layout = Transition(label='Design Layout')
Material_Sourcing = Transition(label='Material Sourcing')
Sensor_Setup = Transition(label='Sensor Setup')
Water_System = Transition(label='Water System')
Pest_Control = Transition(label='Pest Control')
Staff_Training = Transition(label='Staff Training')
Energy_Install = Transition(label='Energy Install')
Crop_Planning = Transition(label='Crop Planning')
Market_Liaison = Transition(label='Market Liaison')
Safety_Audit = Transition(label='Safety Audit')
Launch_Event = Transition(label='Launch Event')
Funding_Apply = Transition(label='Funding Apply')
Community_Meet = Transition(label='Community Meet')

# Structural assessment: Site Survey then Structural Test and Permit Review in parallel (no order between them)
structural_assessment = StrictPartialOrder(nodes=[Site_Survey, Structural_Test, Permit_Review])
structural_assessment.order.add_edge(Site_Survey, Structural_Test)
structural_assessment.order.add_edge(Site_Survey, Permit_Review)

# Design and sourcing after structural and permits
design_and_sourcing = StrictPartialOrder(nodes=[Design_Layout, Material_Sourcing])
# Design Layout and Material Sourcing are concurrent (no order between them)

# Sensor setup, water system and pest control can be concurrent after Material Sourcing
sensor_water_pest = StrictPartialOrder(nodes=[Sensor_Setup, Water_System, Pest_Control])
# no order edges means concurrency

# Staff Training, Energy Installation, and Crop Planning can be concurrent after Sensor/Water/Pest
training_energy_crop = StrictPartialOrder(nodes=[Staff_Training, Energy_Install, Crop_Planning])

# Market Liaison and Safety Audit after these preparations (concurrent)
market_safety = StrictPartialOrder(nodes=[Market_Liaison, Safety_Audit])

# Funding Apply and Community Meet are concurrent and happen after Market and Safety
funding_community = StrictPartialOrder(nodes=[Funding_Apply, Community_Meet])

# Launch Event is last

# Compose partial orders with dependencies as edges
root = StrictPartialOrder(nodes=[
    structural_assessment,
    design_and_sourcing,
    sensor_water_pest,
    training_energy_crop,
    market_safety,
    funding_community,
    Launch_Event
])

# Structural assessment before design and sourcing
root.order.add_edge(structural_assessment, design_and_sourcing)
# Design and sourcing before sensor/water/pest
root.order.add_edge(design_and_sourcing, sensor_water_pest)
# Sensor/water/pest before training/energy/crop
root.order.add_edge(sensor_water_pest, training_energy_crop)
# Training/energy/crop before market/safety
root.order.add_edge(training_energy_crop, market_safety)
# Market/safety before funding/community meet
root.order.add_edge(market_safety, funding_community)
# Funding/community meet before launch event
root.order.add_edge(funding_community, Launch_Event)