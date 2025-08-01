# Generated from: 3bc50827-0c76-4f4a-8720-7bdcdaa67a6c.json
# Description: This process involves the comprehensive management of urban beekeeping operations in a metropolitan environment, balancing ecological sustainability with city regulations. Activities include hive setup in constrained spaces, regular health assessments of bee colonies, monitoring urban flora for pollen diversity, and coordinating with local authorities on compliance. It also covers harvesting honey with minimal disruption to the ecosystem, processing and packaging products in small urban facilities, and community engagement through educational workshops. The process integrates data collection on bee behavior using IoT sensors, pest control with organic methods, and adaptive strategies to mitigate pollution impacts, ensuring a resilient urban apiary system that supports biodiversity while producing high-quality honey and bee products.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Hive_Setup = Transition(label='Hive Setup')
Colony_Check = Transition(label='Colony Check')
Pollen_Survey = Transition(label='Pollen Survey')
Regulation_Review = Transition(label='Regulation Review')
Health_Monitor = Transition(label='Health Monitor')
Pest_Control = Transition(label='Pest Control')
Harvest_Honey = Transition(label='Harvest Honey')
Product_Process = Transition(label='Product Process')
Package_Goods = Transition(label='Package Goods')
Data_Logging = Transition(label='Data Logging')
Community_Talk = Transition(label='Community Talk')
Flora_Mapping = Transition(label='Flora Mapping')
Pollution_Test = Transition(label='Pollution Test')
Sensor_Install = Transition(label='Sensor Install')
Waste_Manage = Transition(label='Waste Manage')
Weather_Watch = Transition(label='Weather Watch')
Supply_Order = Transition(label='Supply Order')

# Setup sensor install and hive setup sequentially
setup_po = StrictPartialOrder(nodes=[Sensor_Install, Hive_Setup])
setup_po.order.add_edge(Sensor_Install, Hive_Setup)

# Data collection sequence: Data Logging after Colony Check, Pollen Survey, Flora Mapping, Pollution Test, Weather Watch
data_collection_po = StrictPartialOrder(
    nodes=[Colony_Check, Pollen_Survey, Flora_Mapping, Pollution_Test, Weather_Watch, Data_Logging]
)
data_collection_po.order.add_edge(Colony_Check, Data_Logging)
data_collection_po.order.add_edge(Pollen_Survey, Data_Logging)
data_collection_po.order.add_edge(Flora_Mapping, Data_Logging)
data_collection_po.order.add_edge(Pollution_Test, Data_Logging)
data_collection_po.order.add_edge(Weather_Watch, Data_Logging)

# Health monitoring loop:
# After Regulation Review, repeatedly do Health Monitor and Pest Control until exit (loop)
health_loop = OperatorPOWL(operator=Operator.LOOP, children=[Health_Monitor, Pest_Control])

# Combine Regulation Review and health_loop sequentially
health_po = StrictPartialOrder(nodes=[Regulation_Review, health_loop])
health_po.order.add_edge(Regulation_Review, health_loop)

# Harvesting and processing sequence: Harvest Honey -> Product Process -> Package Goods
processing_po = StrictPartialOrder(nodes=[Harvest_Honey, Product_Process, Package_Goods])
processing_po.order.add_edge(Harvest_Honey, Product_Process)
processing_po.order.add_edge(Product_Process, Package_Goods)

# Community engagement parallel with waste management and supply order
community_po = StrictPartialOrder(nodes=[Community_Talk, Waste_Manage, Supply_Order])  # concurrent

# Overall order includes:
# setup_po -> data_collection_po -> health_po -> processing_po
# community_po runs concurrently with processing_po (and later stages)
# Combine all main parts in partial order

# Create main PO nodes list
nodes = [setup_po, data_collection_po, health_po, processing_po, community_po]

root = StrictPartialOrder(nodes=nodes)

# Define order dependencies between these major phases

# setup_po before data_collection_po
root.order.add_edge(setup_po, data_collection_po)

# data_collection_po before health_po
root.order.add_edge(data_collection_po, health_po)

# health_po before processing_po
root.order.add_edge(health_po, processing_po)

# No ordering edge for community_po => runs concurrently with processing_po (and other)