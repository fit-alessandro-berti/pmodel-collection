# Generated from: 56dd91c5-4fc5-4ec6-9a17-c9320950147a.json
# Description: This process encompasses the complex steps required to establish an urban vertical farm within a repurposed industrial building. It involves site analysis, environmental impact assessment, modular system design, customized nutrient solution formulation, automated climate control integration, and multi-tier crop scheduling. The process also includes community engagement for local sourcing, advanced pest control strategies without pesticides, renewable energy system installation, IoT sensor calibration, workforce training on agri-tech tools, and continuous yield optimization through data analytics. Each activity is critical to ensuring a sustainable, high-efficiency farm that maximizes urban space while minimizing environmental footprint, enabling year-round crop production in dense metropolitan areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Survey = Transition(label='Site Survey')
Impact_Study = Transition(label='Impact Study')
System_Design = Transition(label='System Design')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Setup = Transition(label='Climate Setup')
Crop_Schedule = Transition(label='Crop Schedule')
Community_Meet = Transition(label='Community Meet')
Pest_Control = Transition(label='Pest Control')
Energy_Install = Transition(label='Energy Install')
Sensor_Setup = Transition(label='Sensor Setup')
Tech_Training = Transition(label='Tech Training')
Data_Monitor = Transition(label='Data Monitor')
Yield_Adjust = Transition(label='Yield Adjust')
Waste_Manage = Transition(label='Waste Manage')
Quality_Audit = Transition(label='Quality Audit')

# Define partial orders for more structured dependencies

# First pair: Site Survey -> Impact Study -> System Design
po1 = StrictPartialOrder(nodes=[Site_Survey, Impact_Study, System_Design])
po1.order.add_edge(Site_Survey, Impact_Study)
po1.order.add_edge(Impact_Study, System_Design)

# Nutrient Mix and Climate Setup happen after System Design, partially ordered and concurrent with Crop Schedule
po2 = StrictPartialOrder(nodes=[Nutrient_Mix, Climate_Setup, Crop_Schedule])
po2.order.add_edge(Nutrient_Mix, Climate_Setup)  # Nutrient Mix needed for Climate Setup

# Community Meet can happen concurrently with Pest Control and Energy Install, but all after System Design
comm_group = StrictPartialOrder(nodes=[Community_Meet, Pest_Control, Energy_Install])
# no edges between them, fully concurrent

# Sensor Setup follows Energy Install and Climate Setup (both needed before sensors are set up)
po3 = StrictPartialOrder(nodes=[Energy_Install, Climate_Setup, Sensor_Setup])
po3.order.add_edge(Energy_Install, Sensor_Setup)
po3.order.add_edge(Climate_Setup, Sensor_Setup)

# Tech Training after Sensor Setup and Pest Control (training on IoT sensors and pest control tools)
po4 = StrictPartialOrder(nodes=[Sensor_Setup, Pest_Control, Tech_Training])
po4.order.add_edge(Sensor_Setup, Tech_Training)
po4.order.add_edge(Pest_Control, Tech_Training)

# Data Monitor and Yield Adjust form a loop for continuous yield optimization (Data Monitor feeds Yield Adjust,
# Yield Adjust goes back to Data Monitor)
loop_yield = OperatorPOWL(operator=Operator.LOOP, children=[Data_Monitor, Yield_Adjust])

# Waste Manage and Quality Audit happen after Tech Training, Quality Audit after Waste Manage
po5 = StrictPartialOrder(nodes=[Waste_Manage, Quality_Audit])
po5.order.add_edge(Waste_Manage, Quality_Audit)

# Compose the whole process
# System Design -> po2 and comm_group parallel -> po3 -> po4 -> po5; crop schedule starts in po2 but can be concurrent
# Overall partial order connecting all parts
root = StrictPartialOrder(
    nodes=[po1, po2, comm_group, po3, po4, po5, loop_yield]
)

# Edges connecting:
# po1 -> po2 and comm_group
root.order.add_edge(po1, po2)
root.order.add_edge(po1, comm_group)

# po2 and comm_group -> po3
root.order.add_edge(po2, po3)
root.order.add_edge(comm_group, po3)

# po3 -> po4
root.order.add_edge(po3, po4)

# po4 -> po5 and loop_yield (continuous optimization runs concurrently with final cleanup/audit)
root.order.add_edge(po4, po5)
root.order.add_edge(po4, loop_yield)