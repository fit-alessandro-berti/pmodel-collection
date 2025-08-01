# Generated from: 879c8f2d-6f54-43b8-94bc-724715141cee.json
# Description: This process outlines the complex and interdisciplinary steps required to establish a fully operational urban vertical farm within a repurposed industrial building. It involves integrating agricultural science with urban planning, engineering, and sustainability practices. The workflow includes site assessment, modular system design, climate control calibration, nutrient solution formulation, automated planting schedules, real-time environmental monitoring, waste recycling protocols, energy optimization, and community engagement strategies. Each phase requires coordination between agronomists, engineers, IT specialists, and local authorities to ensure the farm meets productivity, safety, and environmental standards while adapting to the unique constraints of an urban setting. The process emphasizes innovative technology use, such as AI-driven crop health analysis and IoT-enabled resource management, to maximize yield and minimize resource consumption.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Survey = Transition(label='Site Survey')
Structural_Audit = Transition(label='Structural Audit')
System_Design = Transition(label='System Design')
Climate_Setup = Transition(label='Climate Setup')
Water_Testing = Transition(label='Water Testing')
Nutrient_Mix = Transition(label='Nutrient Mix')
Seed_Selection = Transition(label='Seed Selection')
Planting_Cycle = Transition(label='Planting Cycle')
Sensor_Install = Transition(label='Sensor Install')
Data_Integration = Transition(label='Data Integration')
Waste_Sorting = Transition(label='Waste Sorting')
Energy_Audit = Transition(label='Energy Audit')
Automation_Setup = Transition(label='Automation Setup')
Health_Check = Transition(label='Health Check')
Community_Meet = Transition(label='Community Meet')
Yield_Forecast = Transition(label='Yield Forecast')
Maintenance_Plan = Transition(label='Maintenance Plan')

# Phase 1: Site assessment and structural checks in parallel
site_assessment = StrictPartialOrder(nodes=[Site_Survey, Structural_Audit])
# No order edges between these two, parallel activities

# Phase 2: Design and system setup sequence
# System Design --> Climate Setup --> Water Testing --> Nutrient Mix
design_setup = StrictPartialOrder(nodes=[System_Design, Climate_Setup, Water_Testing, Nutrient_Mix])
design_setup.order.add_edge(System_Design, Climate_Setup)
design_setup.order.add_edge(Climate_Setup, Water_Testing)
design_setup.order.add_edge(Water_Testing, Nutrient_Mix)

# Phase 3: Planting prep: Seed Selection and Automation Setup in parallel before Planting Cycle
planting_prep = StrictPartialOrder(nodes=[Seed_Selection, Automation_Setup, Planting_Cycle])
planting_prep.order.add_edge(Seed_Selection, Planting_Cycle)
planting_prep.order.add_edge(Automation_Setup, Planting_Cycle)

# Phase 4: Environment monitoring and data integration (Sensor Install --> Data Integration)
monitoring = StrictPartialOrder(nodes=[Sensor_Install, Data_Integration])
monitoring.order.add_edge(Sensor_Install, Data_Integration)

# Phase 5: Maintenance and sustainability parallel tasks
# Waste Sorting --> Energy Audit --> Maintenance Plan
# Health Check --> Yield Forecast
maintenance1 = StrictPartialOrder(nodes=[Waste_Sorting, Energy_Audit, Maintenance_Plan])
maintenance1.order.add_edge(Waste_Sorting, Energy_Audit)
maintenance1.order.add_edge(Energy_Audit, Maintenance_Plan)
maintenance2 = StrictPartialOrder(nodes=[Health_Check, Yield_Forecast])
maintenance2.order.add_edge(Health_Check, Yield_Forecast)

# Community engagement runs partially in parallel but starts after Planting Cycle
community = Community_Meet

# Top level partial order:
# Site Assessment (Site_Survey & Structural_Audit) --> Design and Setup -->
# Planting Prep --> Monitoring in parallel with Maintenance tasks and Community meet starts after Planting Cycle
top_level_nodes = [site_assessment, design_setup, planting_prep, monitoring, maintenance1, maintenance2, community]

root = StrictPartialOrder(nodes=top_level_nodes)

# Site assessment before Design and Setup
root.order.add_edge(site_assessment, design_setup)
# Design and Setup before Planting Prep
root.order.add_edge(design_setup, planting_prep)
# Planting Prep before Monitoring and Maintenance & Community
root.order.add_edge(planting_prep, monitoring)
root.order.add_edge(planting_prep, maintenance1)
root.order.add_edge(planting_prep, maintenance2)
root.order.add_edge(planting_prep, community)

# Monitoring, maintenance1, maintenance2 and community run concurrently after planting prep
# so no edges between them
