# Generated from: 3879bc4a-bfa5-40df-a9e7-89f5da7af3d9.json
# Description: This process outlines the complex supply chain involved in urban beekeeping, integrating environmental monitoring, community engagement, and sustainable product distribution. It begins with hive site selection based on microclimate data and urban flora analysis, followed by custom hive fabrication using recycled materials. Next, queen bee sourcing is managed through selective breeding programs to ensure disease resistance. Routine hive inspections incorporate sensor data for hive health assessment, triggering adaptive feeding and pest control strategies. Honey extraction is performed in modular mobile units to minimize contamination, then quality tested for urban pollutants. Packaging combines eco-friendly materials with local branding initiatives. Distribution leverages a hybrid model of direct sales at farmers markets and subscription-based delivery services. Throughout the process, educational workshops and citizen-science data collection are integrated to foster community involvement and promote urban biodiversity awareness.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define Activities
Site_Select = Transition(label='Site Select')
Flora_Survey = Transition(label='Flora Survey')
Microclimate_Map = Transition(label='Microclimate Map')
Hive_Design = Transition(label='Hive Design')
Material_Source = Transition(label='Material Source')
Hive_Build = Transition(label='Hive Build')
Queen_Breed = Transition(label='Queen Breed')
Hive_Inspect = Transition(label='Hive Inspect')
Sensor_Check = Transition(label='Sensor Check')
Feed_Adjust = Transition(label='Feed Adjust')
Pest_Control = Transition(label='Pest Control')
Honey_Extract = Transition(label='Honey Extract')
Quality_Test = Transition(label='Quality Test')
Eco_Package = Transition(label='Eco Package')
Market_Setup = Transition(label='Market Setup')
Subscribe_Setup = Transition(label='Subscribe Setup')
Workshop_Plan = Transition(label='Workshop Plan')
Data_Collect = Transition(label='Data Collect')

# 1. Initial site selection based on microclimate data & flora analysis:
# Microclimate Map and Flora Survey concurrent, then Site Select
initial_PO = StrictPartialOrder(nodes=[Microclimate_Map, Flora_Survey, Site_Select])
initial_PO.order.add_edge(Microclimate_Map, Site_Select)
initial_PO.order.add_edge(Flora_Survey, Site_Select)

# 2. Custom hive fabrication using recycled materials:
# Material Source -> Hive Design -> Hive Build
fabrication_PO = StrictPartialOrder(nodes=[Material_Source, Hive_Design, Hive_Build])
fabrication_PO.order.add_edge(Material_Source, Hive_Design)
fabrication_PO.order.add_edge(Hive_Design, Hive_Build)

# 3. Queen bee sourcing through selective breeding:
# Single activity
queen_PO = Queen_Breed

# 4. Routine hive inspections:
# Hive Inspect includes Sensor Check, triggers Feed Adjust and Pest Control
# Sensor Check -> Hive Inspect order is natural, then Feed Adjust and Pest Control run concurrently after Hive Inspect
inspection_PO = StrictPartialOrder(
    nodes=[Sensor_Check, Hive_Inspect, Feed_Adjust, Pest_Control]
)
inspection_PO.order.add_edge(Sensor_Check, Hive_Inspect)
inspection_PO.order.add_edge(Hive_Inspect, Feed_Adjust)
inspection_PO.order.add_edge(Hive_Inspect, Pest_Control)

# 5. Honey extraction and quality test:
# Honey Extract -> Quality Test
extraction_PO = StrictPartialOrder(nodes=[Honey_Extract, Quality_Test])
extraction_PO.order.add_edge(Honey_Extract, Quality_Test)

# 6. Packaging:
# Eco Package after quality test
packaging_PO = Eco_Package

# Connect extraction_PO to packaging_PO
extract_pack_PO = StrictPartialOrder(nodes=[extraction_PO, packaging_PO])
extract_pack_PO.order.add_edge(extraction_PO, packaging_PO)  # extraction_PO < packaging_PO

# Since packaging_PO is a Transition, need to "flatten" nodes:
# StrictPartialOrder nodes require activities or other POWL objects
# Instead merge nodes of extraction_PO and packaging_PO

extraction_pack_PO = StrictPartialOrder(
    nodes=[Honey_Extract, Quality_Test, Eco_Package]
)
extraction_pack_PO.order.add_edge(Honey_Extract, Quality_Test)
extraction_pack_PO.order.add_edge(Quality_Test, Eco_Package)

# 7. Distribution - hybrid model: Market Setup and Subscribe Setup in XOR (choice)
distribution_xor = OperatorPOWL(operator=Operator.XOR, children=[Market_Setup, Subscribe_Setup])

# 8. Community involvement - Workshops and Data Collect run concurrently
community_PO = StrictPartialOrder(nodes=[Workshop_Plan, Data_Collect])
# no order edges - concurrent

# Now, assemble the main process order:

# Order:
# initial_PO -> fabrication_PO -> queen_PO -> inspection_PO -> extraction_pack_PO -> distribution_xor
# community_PO runs concurrently and integrated throughout the process,
# but description says "throughout"; let's run it concurrently with the main flow

# Define the main linear PO without community:
main_PO = StrictPartialOrder(
    nodes=[initial_PO, fabrication_PO, queen_PO, inspection_PO, extraction_pack_PO, distribution_xor]
)
main_PO.order.add_edge(initial_PO, fabrication_PO)
main_PO.order.add_edge(fabrication_PO, queen_PO)
main_PO.order.add_edge(queen_PO, inspection_PO)
main_PO.order.add_edge(inspection_PO, extraction_pack_PO)
main_PO.order.add_edge(extraction_pack_PO, distribution_xor)

# Finally, root combines main_PO and community_PO concurrently:
root = StrictPartialOrder(nodes=[main_PO, community_PO])
# no order edges between them -> run concurrently
