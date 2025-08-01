# Generated from: 10cc6c0b-3b94-432f-9a28-6da34aeb1db1.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm within a repurposed industrial space. It begins with site analysis and environmental assessment, followed by modular structure design and procurement of specialized hydroponic systems. Subsequent activities include installation of climate control units, integration of IoT sensors for real-time monitoring, and calibration of lighting systems to optimize plant growth. The process also covers staff training on automated nutrient delivery, implementation of pest management protocols without chemicals, and setting up data analytics dashboards for yield prediction. Final stages focus on trial planting cycles, quality control checks, and establishing supply chain logistics to deliver fresh produce to local markets efficiently, ensuring sustainability and scalability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition, OperatorPOWL
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Site_Analysis = Transition(label='Site Analysis')
Env_Assessment = Transition(label='Env Assessment')
Structure_Design = Transition(label='Structure Design')
Hydroponic_Setup = Transition(label='Hydroponic Setup')
Climate_Install = Transition(label='Climate Install')
IoT_Integration = Transition(label='IoT Integration')
Lighting_Calibrate = Transition(label='Lighting Calibrate')
Staff_Training = Transition(label='Staff Training')
Nutrient_Delivery = Transition(label='Nutrient Delivery')
Pest_Protocols = Transition(label='Pest Protocols')
Data_Analytics = Transition(label='Data Analytics')
Trial_Planting = Transition(label='Trial Planting')
Quality_Control = Transition(label='Quality Control')
Supply_Logistics = Transition(label='Supply Logistics')
Market_Launch = Transition(label='Market Launch')

# Partial order for initial site and design phase
PO1 = StrictPartialOrder(nodes=[Site_Analysis, Env_Assessment, Structure_Design])
PO1.order.add_edge(Site_Analysis, Env_Assessment)
PO1.order.add_edge(Env_Assessment, Structure_Design)

# Partial order for hydroponic procurement and installation
PO2 = StrictPartialOrder(nodes=[Hydroponic_Setup, Climate_Install, IoT_Integration, Lighting_Calibrate])
PO2.order.add_edge(Hydroponic_Setup, Climate_Install)
PO2.order.add_edge(Climate_Install, IoT_Integration)
PO2.order.add_edge(IoT_Integration, Lighting_Calibrate)

# Partial order for training and protocols
PO3 = StrictPartialOrder(nodes=[Staff_Training, Nutrient_Delivery, Pest_Protocols])
PO3.order.add_edge(Staff_Training, Nutrient_Delivery)
PO3.order.add_edge(Nutrient_Delivery, Pest_Protocols)

# Data analytics setup can run concurrently with staff training/protocols
# So PO4 is Data Analytics alone
PO4 = StrictPartialOrder(nodes=[Data_Analytics])

# Partial order for final production and delivery chain
PO5 = StrictPartialOrder(nodes=[Trial_Planting, Quality_Control, Supply_Logistics, Market_Launch])
PO5.order.add_edge(Trial_Planting, Quality_Control)
PO5.order.add_edge(Quality_Control, Supply_Logistics)
PO5.order.add_edge(Supply_Logistics, Market_Launch)

# Compose middle phase: PO2 (installation) must come after PO1 (site and design)
# Then PO3 and PO4 run concurrently (training/protocols and data analytics)
mid_phase = StrictPartialOrder(
    nodes=[PO2, PO3, PO4]
)
mid_phase.order.add_edge(PO2, PO3)
mid_phase.order.add_edge(PO2, PO4)

# Compose whole process:
# PO1 -> mid_phase -> PO5
root = StrictPartialOrder(
    nodes=[PO1, mid_phase, PO5]
)
root.order.add_edge(PO1, mid_phase)
root.order.add_edge(mid_phase, PO5)