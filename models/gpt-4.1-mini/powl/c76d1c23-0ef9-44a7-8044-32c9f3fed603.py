# Generated from: c76d1c23-0ef9-44a7-8044-32c9f3fed603.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farm within a densely populated city environment. It begins with site assessment and zoning approvals, followed by modular structure design and procurement of hydroponic systems. After installation, the farm undergoes environmental calibration to optimize light, humidity, and nutrient delivery. Crop selection is tailored to local demand and growth cycles. Continuous monitoring and adaptive pest management ensure sustainable yields. The process concludes with harvest scheduling, packaging, and distribution logistics targeted at local markets, while integrating data analytics for ongoing optimization and scalability of operations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Survey = Transition(label='Site Survey')
Zoning_Check = Transition(label='Zoning Check')
Design_Layout = Transition(label='Design Layout')
System_Order = Transition(label='System Order')
Structure_Build = Transition(label='Structure Build')
Install_Hydroponics = Transition(label='Install Hydroponics')
Calibrate_Sensors = Transition(label='Calibrate Sensors')
Select_Crops = Transition(label='Select Crops')
Plant_Seeding = Transition(label='Plant Seeding')
Monitor_Growth = Transition(label='Monitor Growth')
Manage_Pests = Transition(label='Manage Pests')
Schedule_Harvest = Transition(label='Schedule Harvest')
Package_Produce = Transition(label='Package Produce')
Local_Delivery = Transition(label='Local Delivery')
Analyze_Data = Transition(label='Analyze Data')

# Define loop for monitoring and pest management:
# Loop body B: Manage_Pests
# Loop body A: Monitor_Growth
# Loop = *(Monitor_Growth, Manage_Pests)
loop_monitor_pests = OperatorPOWL(operator=Operator.LOOP, children=[Monitor_Growth, Manage_Pests])

# Partial order for the modular construction and installation after zoning
construction_nodes = [Design_Layout, System_Order, Structure_Build, Install_Hydroponics]

construction_po = StrictPartialOrder(nodes=construction_nodes)
construction_po.order.add_edge(Design_Layout, System_Order)
construction_po.order.add_edge(System_Order, Structure_Build)
construction_po.order.add_edge(Structure_Build, Install_Hydroponics)

# Partial order for after installation: calibration, crop selection, planting
post_install_nodes = [Calibrate_Sensors, Select_Crops, Plant_Seeding]

post_install_po = StrictPartialOrder(nodes=post_install_nodes)
post_install_po.order.add_edge(Calibrate_Sensors, Select_Crops)
post_install_po.order.add_edge(Select_Crops, Plant_Seeding)

# Partial order for harvest and delivery
harvest_nodes = [Schedule_Harvest, Package_Produce, Local_Delivery]

harvest_po = StrictPartialOrder(nodes=harvest_nodes)
harvest_po.order.add_edge(Schedule_Harvest, Package_Produce)
harvest_po.order.add_edge(Package_Produce, Local_Delivery)

# Analyze data can run concurrently starting after Plant_Seeding (or maybe after loop finish)
# but since it's "ongoing optimization", let's consider it concurrent with harvest part, after seeding

# Assemble full partial order nodes
# We have site assessment first:
# Site Survey --> Zoning Check --> Construction PO --> Install Hydroponics -->
# Calibrate Sensors --> Select Crops --> Plant Seeding --> loop_monitor_pests,
# then in parallel Analyze_Data and harvest_po
all_nodes = [
    Site_Survey, Zoning_Check,
    construction_po,  # complex node
    Calibrate_Sensors, Select_Crops, Plant_Seeding,
    loop_monitor_pests,
    Analyze_Data,
    harvest_po
]

root = StrictPartialOrder(nodes=all_nodes)

# Add order constraints:

# Site Survey before Zoning Check
root.order.add_edge(Site_Survey, Zoning_Check)
# Zoning Check before construction start (Design Layout)
root.order.add_edge(Zoning_Check, construction_po)
# construction_po ends at Install Hydroponics - connect it to Calibrate Sensors
root.order.add_edge(construction_po, Calibrate_Sensors)
# Calibrate Sensors -> Select Crops -> Plant Seeding
root.order.add_edge(Calibrate_Sensors, Select_Crops)
root.order.add_edge(Select_Crops, Plant_Seeding)
# Plant Seeding before loop monitoring/pests
root.order.add_edge(Plant_Seeding, loop_monitor_pests)
# Plant Seeding before Analyze_Data and before harvest_po
root.order.add_edge(Plant_Seeding, Analyze_Data)
root.order.add_edge(Plant_Seeding, harvest_po)
# Analyze_Data and harvest_po run concurrently (no order between them)

# The process ends with Local Delivery (within harvest_po) and Analyze_Data can be ongoing after

# root represents the full process
