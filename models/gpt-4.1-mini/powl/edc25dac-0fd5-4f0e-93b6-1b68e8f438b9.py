# Generated from: edc25dac-0fd5-4f0e-93b6-1b68e8f438b9.json
# Description: This process outlines the establishment of an urban rooftop farm on a commercial building, involving unique steps such as structural load assessment, soil-less medium installation, microclimate analysis, and automated irrigation programming. It integrates multiple disciplines including architecture, agriculture, and environmental engineering to ensure sustainable food production in a limited urban space. The process also includes community engagement for local sourcing and education, regulatory compliance with city zoning laws, and the implementation of renewable energy systems to minimize environmental impact. Continuous monitoring and adaptive management ensure optimal crop yield while maintaining building integrity and tenant satisfaction.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transition nodes
Load_Assess = Transition(label='Load Assess')
Permit_Review = Transition(label='Permit Review')
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Soil_Mix = Transition(label='Soil Mix')
Install_Beds = Transition(label='Install Beds')
Irrigation_Set = Transition(label='Irrigation Set')
Climate_Test = Transition(label='Climate Test')
Sensor_Deploy = Transition(label='Sensor Deploy')
Energy_Setup = Transition(label='Energy Setup')
Crop_Select = Transition(label='Crop Select')
Plant_Seeding = Transition(label='Plant Seeding')
Community_Meet = Transition(label='Community Meet')
Compliance_Check = Transition(label='Compliance Check')
Growth_Monitor = Transition(label='Growth Monitor')
Harvest_Plan = Transition(label='Harvest Plan')
Waste_Recycle = Transition(label='Waste Recycle')

# PartialOrder structure

# The process logically can be split into phases with some concurrency

# Phase 1: Structural assessment, permitting and survey
phase1 = StrictPartialOrder(
    nodes=[Load_Assess, Permit_Review, Site_Survey]
)
phase1.order.add_edge(Load_Assess, Permit_Review)  # Load Assess before Permit Review
phase1.order.add_edge(Permit_Review, Site_Survey)  # Permit Review before Site Survey

# Phase 2: Design & soil/installation - once site is surveyed
phase2 = StrictPartialOrder(
    nodes=[Design_Layout, Soil_Mix, Install_Beds]
)
phase2.order.add_edge(Design_Layout, Soil_Mix)
phase2.order.add_edge(Soil_Mix, Install_Beds)

# Phase 3: Technical setups - irrigation, sensor, energy, climate test
# These can be concurrent after Install_Beds
phase3 = StrictPartialOrder(
    nodes=[Irrigation_Set, Sensor_Deploy, Energy_Setup, Climate_Test]
)
# No order between these 4 (concurrent)

# Phase 4: Crop selection and planting
phase4 = StrictPartialOrder(
    nodes=[Crop_Select, Plant_Seeding]
)
phase4.order.add_edge(Crop_Select, Plant_Seeding)

# Phase 5: Community & compliance (can be started in parallel with phase4)
phase5 = StrictPartialOrder(
    nodes=[Community_Meet, Compliance_Check]
)
# no order between Community_Meet and Compliance_Check

# Phase 6: Monitoring, planning harvest and recycling waste
phase6 = StrictPartialOrder(
    nodes=[Growth_Monitor, Harvest_Plan, Waste_Recycle]
)
phase6.order.add_edge(Growth_Monitor, Harvest_Plan)
phase6.order.add_edge(Harvest_Plan, Waste_Recycle)

# Compose the overall model:

# After phase1 (Load_Assess -> Permit_Review -> Site_Survey),
# phase2 starts (Design_Layout -> Soil_Mix -> Install_Beds),
# then phase3 runs concurrent tech setups,
# then phase4 and phase5 run concurrently,
# then phase6 ends the process.

# Compose concurrency of phase4 and phase5
phase45 = StrictPartialOrder(
    nodes=[phase4, phase5]
)
# no order edges, concurrency

# Compose phase345: phase3 followed by concurrency of phase4 and phase5
phase34 = StrictPartialOrder(
    nodes=[phase3, phase45]
)
phase34.order.add_edge(phase3, phase45)

# Compose phase2345: phase2 followed by phase34
phase234 = StrictPartialOrder(
    nodes=[phase2, phase34]
)
phase234.order.add_edge(phase2, phase34)

# Compose phase12345: phase1 followed by phase234
phase1234 = StrictPartialOrder(
    nodes=[phase1, phase234]
)
phase1234.order.add_edge(phase1, phase234)

# Compose entire root with phase6 after phase1234
root = StrictPartialOrder(
    nodes=[phase1234, phase6]
)
root.order.add_edge(phase1234, phase6)