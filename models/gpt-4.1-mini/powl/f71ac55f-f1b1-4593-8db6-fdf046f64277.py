# Generated from: f71ac55f-f1b1-4593-8db6-fdf046f64277.json
# Description: This process outlines the establishment of an urban vertical farm within a repurposed industrial building. It involves site analysis, modular system design, climate control integration, nutrient delivery setup, automated monitoring installation, and crop scheduling. The workflow includes securing permits, sourcing sustainable materials, integrating renewable energy, and establishing waste recycling protocols. The process ensures efficient space utilization, maximizes crop yield, and supports community engagement through educational tours and local partnerships, fostering urban agriculture innovation and sustainability in dense city environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Site_Survey = Transition(label='Site Survey')
Permit_Review = Transition(label='Permit Review')
Design_Layout = Transition(label='Design Layout')
System_Assembly = Transition(label='System Assembly')
Climate_Setup = Transition(label='Climate Setup')
Nutrient_Prep = Transition(label='Nutrient Prep')
Irrigation_Test = Transition(label='Irrigation Test')
Lighting_Config = Transition(label='Lighting Config')
Energy_Install = Transition(label='Energy Install')
Sensor_Setup = Transition(label='Sensor Setup')
Automation_Deploy = Transition(label='Automation Deploy')
Crop_Seeding = Transition(label='Crop Seeding')
Waste_Plan = Transition(label='Waste Plan')
Staff_Training = Transition(label='Staff Training')
Community_Outreach = Transition(label='Community Outreach')
Yield_Monitor = Transition(label='Yield Monitor')
Maintenance_Check = Transition(label='Maintenance Check')

# PO 1: Initial site analysis & permits
# Site Survey --> Permit Review (must secure permits after survey)
initial_PO = StrictPartialOrder(nodes=[Site_Survey, Permit_Review])
initial_PO.order.add_edge(Site_Survey, Permit_Review)

# PO 2: Design & assembly partial order:
# Design Layout --> System Assembly --> Climate Setup --> Nutrient Prep --> Irrigation Test --> Lighting Config
design_assembly_PO = StrictPartialOrder(nodes=[
    Design_Layout, System_Assembly, Climate_Setup,
    Nutrient_Prep, Irrigation_Test, Lighting_Config
])
design_assembly_PO.order.add_edge(Design_Layout, System_Assembly)
design_assembly_PO.order.add_edge(System_Assembly, Climate_Setup)
design_assembly_PO.order.add_edge(Climate_Setup, Nutrient_Prep)
design_assembly_PO.order.add_edge(Nutrient_Prep, Irrigation_Test)
design_assembly_PO.order.add_edge(Irrigation_Test, Lighting_Config)

# PO 3: Energy and automation partial order:
# Energy Install --> Sensor Setup --> Automation Deploy --> Crop Seeding
energy_automation_PO = StrictPartialOrder(nodes=[
    Energy_Install, Sensor_Setup, Automation_Deploy, Crop_Seeding
])
energy_automation_PO.order.add_edge(Energy_Install, Sensor_Setup)
energy_automation_PO.order.add_edge(Sensor_Setup, Automation_Deploy)
energy_automation_PO.order.add_edge(Automation_Deploy, Crop_Seeding)

# PO 4: Waste management and staff training (concurrent)
waste_training_PO = StrictPartialOrder(nodes=[Waste_Plan, Staff_Training])
# no order edges since these can be concurrent

# PO 5: Community Outreach (after Staff Training)
community_PO = StrictPartialOrder(nodes=[Staff_Training, Community_Outreach])
community_PO.order.add_edge(Staff_Training, Community_Outreach)

# PO 6: Monitoring and maintenance loop
# Loop on (Yield Monitor --> Maintenance Check)
monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[Yield_Monitor, Maintenance_Check])

# Compose all partial orders into a larger partial order that respects logical sequence:

# Step 1: initial_PO
# Step 2: design_assembly_PO after Permit Review
# Step 3: energy_automation_PO after Lighting Config
# Step 4: waste_training_PO concurrent with community_PO but community_PO requires Staff Training before Community Outreach
# Step 5: monitoring_loop after Crop Seeding and Community Outreach (both finish before monitoring)

# Compose the top-level partial order nodes:
# We include all above partial orders and loop as nodes within the top PO

root_nodes = [
    initial_PO,
    design_assembly_PO,
    energy_automation_PO,
    waste_training_PO,
    community_PO,
    monitoring_loop
]

root = StrictPartialOrder(nodes=root_nodes)

# Add edges to represent dependencies between POs:
# initial_PO --> design_assembly_PO
root.order.add_edge(initial_PO, design_assembly_PO)
# design_assembly_PO --> energy_automation_PO
root.order.add_edge(design_assembly_PO, energy_automation_PO)
# energy_automation_PO --> community_PO
root.order.add_edge(energy_automation_PO, community_PO)
# waste_training_PO and community_PO are concurrent at this level, no edge between them
# community_PO --> monitoring_loop
root.order.add_edge(community_PO, monitoring_loop)
# Also Crop Seeding (inside energy_automation_PO) should be done before monitoring_loop
# But energy_automation_PO already precedes community_PO and monitoring_loop, so edge design_assembly_PO -> energy_automation_PO -> community_PO -> monitoring_loop 
# covers sequencing Crop Seeding before monitoring_loop

# This model ensures:
# Site Survey -> Permit Review -> Design & Assembly chain -> Energy & Automation chain -> Community outreach + Waste/Training -> Monitoring loop
