# Generated from: dbd5669c-08c9-4154-98f0-7d7d8bd65725.json
# Description: This process outlines the intricate steps involved in establishing an urban vertical farm within a confined city environment. It integrates advanced hydroponic and aeroponic systems, sustainable energy solutions, and IoT sensors for real-time monitoring. The workflow includes site assessment, modular unit assembly, nutrient solution calibration, seed selection based on microclimate data, pest control via biological agents, and continuous yield optimization using AI-driven analytics. The process further encompasses community engagement, regulatory compliance checks, and scalable expansion planning to ensure sustainable urban agriculture that minimizes resource usage and maximizes output in limited spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Material_Sourcing = Transition(label='Material Sourcing')
Unit_Assembly = Transition(label='Unit Assembly')
System_Wiring = Transition(label='System Wiring')
Sensor_Install = Transition(label='Sensor Install')
Water_Testing = Transition(label='Water Testing')
Nutrient_Mix = Transition(label='Nutrient Mix')
Seed_Selection = Transition(label='Seed Selection')
Planting_Setup = Transition(label='Planting Setup')
Climate_Control = Transition(label='Climate Control')
Pest_Management = Transition(label='Pest Management')
Data_Calibration = Transition(label='Data Calibration')
Yield_Analysis = Transition(label='Yield Analysis')
Community_Meet = Transition(label='Community Meet')
Compliance_Check = Transition(label='Compliance Check')
Expansion_Plan = Transition(label='Expansion Plan')

# High level sequential partial order:
# 1. Site Survey -> Design Layout -> Material Sourcing
# 2. Then Unit Assembly, which includes System Wiring and Sensor Install in partial order (wiring before install)
# 3. Water Testing and Nutrient Mix concurrently after wiring and sensor install
# 4. Seed Selection after Nutrient Mix, depends on microclimate data (assumed after design layout too)
# 5. Planting Setup after Seed Selection
# 6. Climate Control and Pest Management concurrent after Planting Setup
# 7. Data Calibration after Sensor Install and Pest Management (sensor install already before water testing, so here after pest management is additional)
# 8. Yield Analysis after Data Calibration
# 9. Community Meet, Compliance Check, and Expansion Plan concurrently after Yield Analysis

# Define partial order nodes and edges explicitly:

# Compose Unit Assembly sub PO
unit_assembly_po = StrictPartialOrder(nodes=[Unit_Assembly, System_Wiring, Sensor_Install])
unit_assembly_po.order.add_edge(Unit_Assembly, System_Wiring)
unit_assembly_po.order.add_edge(System_Wiring, Sensor_Install)

# Compose testing and nutrient sub PO (concurrent)
testing_nutrient_po = StrictPartialOrder(nodes=[Water_Testing, Nutrient_Mix])
# No order edges -> concurrent

# Compose climate control and pest management concurrent
climate_pest_po = StrictPartialOrder(nodes=[Climate_Control, Pest_Management])
# concurrent

# Compose last community group concurrent
community_group_po = StrictPartialOrder(nodes=[Community_Meet, Compliance_Check, Expansion_Plan])
# concurrent

# Main partial order nodes including all major blocks and activities
nodes = [
    Site_Survey,
    Design_Layout,
    Material_Sourcing,
    unit_assembly_po,
    testing_nutrient_po,
    Seed_Selection,
    Planting_Setup,
    climate_pest_po,
    Data_Calibration,
    Yield_Analysis,
    community_group_po
]

root = StrictPartialOrder(nodes=nodes)

# Add edges for main sequence and dependencies:

root.order.add_edge(Site_Survey, Design_Layout)
root.order.add_edge(Design_Layout, Material_Sourcing)

root.order.add_edge(Material_Sourcing, unit_assembly_po)

root.order.add_edge(unit_assembly_po, testing_nutrient_po)

# Seed Selection depends on Nutrient Mix and Design Layout (microclimate data)
root.order.add_edge(testing_nutrient_po, Seed_Selection)
root.order.add_edge(Design_Layout, Seed_Selection)

root.order.add_edge(Seed_Selection, Planting_Setup)

# Climate control and pest management concurrent after Planting Setup
root.order.add_edge(Planting_Setup, climate_pest_po)

# Data Calibration after Sensor Install and Pest Management:
# Sensor Install inside unit_assembly_po (end node Sensor_Install)
# Pest Management inside climate_pest_po
# To model dependency on specific nodes inside partial orders,
# add edges from partial orders which contain them- 
# This is an approximation as only nodes themselves can be sources or targets.
# So we assume here Data_Calibration depends on those whole sub pos.
root.order.add_edge(unit_assembly_po, Data_Calibration)  # for Sensor Install
root.order.add_edge(climate_pest_po, Data_Calibration)  # for Pest Management

root.order.add_edge(Data_Calibration, Yield_Analysis)

root.order.add_edge(Yield_Analysis, community_group_po)