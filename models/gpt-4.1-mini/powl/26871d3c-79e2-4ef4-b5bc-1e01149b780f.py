# Generated from: 26871d3c-79e2-4ef4-b5bc-1e01149b780f.json
# Description: This process outlines the complex sequence of activities required to establish a fully operational urban vertical farm within a constrained city environment. It involves site assessment, modular structure design, climate control calibration, nutrient cycling optimization, automation integration, and compliance with local agricultural and environmental regulations. The process also includes workforce training, system testing, crop scheduling, pest monitoring, and community engagement to ensure sustainability and productivity in a high-density urban setting, reflecting a cutting-edge approach to food production and resource management.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Structural_Build = Transition(label='Structural Build')
Install_Panels = Transition(label='Install Panels')
Climate_Setup = Transition(label='Climate Setup')
Water_System = Transition(label='Water System')
Nutrient_Mix = Transition(label='Nutrient Mix')
Automation_Config = Transition(label='Automation Config')
Seed_Selection = Transition(label='Seed Selection')
Planting_Cycle = Transition(label='Planting Cycle')
Pest_Monitor = Transition(label='Pest Monitor')
Data_Collection = Transition(label='Data Collection')
Staff_Training = Transition(label='Staff Training')
Compliance_Check = Transition(label='Compliance Check')
Harvest_Plan = Transition(label='Harvest Plan')
Waste_Manage = Transition(label='Waste Manage')
Community_Outreach = Transition(label='Community Outreach')

# Construct partial orders to reflect the logical ordering and concurrency described.

# Phase 1: Site Assessment and Design
phase1 = StrictPartialOrder(nodes=[
    Site_Survey,
    Design_Layout
])
phase1.order.add_edge(Site_Survey, Design_Layout)

# Phase 2: Build & Infrastructure, after design layout
infrastructure_nodes = [
    Structural_Build,
    Install_Panels,
    Climate_Setup,
    Water_System
]
# Structural Build first
phase2 = StrictPartialOrder(nodes=infrastructure_nodes)
phase2.order.add_edge(Structural_Build, Install_Panels)  # Install Panels after structure
phase2.order.add_edge(Structural_Build, Climate_Setup)  # Climate setup after structure
phase2.order.add_edge(Structural_Build, Water_System)   # Water system after structure
# Install_Panels, Climate_Setup and Water_System concurrent after Structural_Build

# Phase 3: Nutrient & Automation Configuration after installation and climate & water setup
phase3 = StrictPartialOrder(nodes=[
    Nutrient_Mix,
    Automation_Config
])
# Assume Nutrient Mix and Automation Config concurrent after Phase 2 complete
# So partial order connects end of phase2 to phase3, but concurrency within phase3
# we will manage this linking later

# Phase 4: Planting Cycle Setup concurrently:
planting_preparation = StrictPartialOrder(nodes=[
    Seed_Selection,
    Planting_Cycle
])
planting_preparation.order.add_edge(Seed_Selection, Planting_Cycle)

# Phase 5: Monitoring and Data collection after planting cycle
monitoring = StrictPartialOrder(nodes=[
    Pest_Monitor,
    Data_Collection
])
# Concurrently monitor pest and collect data, no order between them

# Phase 6: Workforce and Compliance after infrastructures and preliminary plant setup
training_compliance = StrictPartialOrder(nodes=[
    Staff_Training,
    Compliance_Check
])
# Staff training and compliance check concurrent

# Phase 7: Harvest and Waste management after planting cycles and compliance
harvest_waste = StrictPartialOrder(nodes=[
    Harvest_Plan,
    Waste_Manage
])
harvest_waste.order.add_edge(Harvest_Plan, Waste_Manage)

# Phase 8: Community outreach can happen after compliance check is done
community = StrictPartialOrder(nodes=[
    Community_Outreach
])

# Now link phases together into a global partial order respecting dependencies:
root_nodes = [
    phase1,
    phase2,
    phase3,
    planting_preparation,
    monitoring,
    training_compliance,
    harvest_waste,
    community
]

root = StrictPartialOrder(nodes=root_nodes)

# Edges linking phases:
# phase1 -> phase2
root.order.add_edge(phase1, phase2)

# phase2 -> phase3
root.order.add_edge(phase2, phase3)

# phase3 -> planting_preparation
root.order.add_edge(phase3, planting_preparation)

# planting_preparation -> monitoring
root.order.add_edge(planting_preparation, monitoring)

# phase2 -> training_compliance (infrastructure must exist before training/compliance)
root.order.add_edge(phase2, training_compliance)

# training_compliance -> harvest_waste (harvesting and waste after training/compliance)
root.order.add_edge(training_compliance, harvest_waste)

# harvest_waste -> community (community outreach last)
root.order.add_edge(harvest_waste, community)