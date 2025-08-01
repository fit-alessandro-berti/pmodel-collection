# Generated from: 6fde2d59-127e-4ac2-aaab-e85fd63875f4.json
# Description: This process outlines the comprehensive cycle of urban vertical farming in a controlled environment. It begins with site assessment and structural installation, followed by seed selection and nutrient solution preparation. Automated planting and environmental monitoring ensure optimal growth. Pest control and disease detection use AI-driven sensors. Harvesting is scheduled based on maturity data, after which post-harvest processing including cleaning, packaging, and quality inspection occurs. The produce is then distributed via smart logistics to urban markets. Maintenance of the farming units and data analytics for yield improvement complete the cycle, integrating sustainability and technology in an atypical agricultural business model.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Site_Assess = Transition(label='Site Assess')
Install_Structure = Transition(label='Install Structure')
Select_Seeds = Transition(label='Select Seeds')
Prepare_Nutrients = Transition(label='Prepare Nutrients')
Automate_Planting = Transition(label='Automate Planting')
Monitor_Climate = Transition(label='Monitor Climate')
Detect_Pests = Transition(label='Detect Pests')
Control_Disease = Transition(label='Control Disease')
Schedule_Harvest = Transition(label='Schedule Harvest')
Harvest_Crops = Transition(label='Harvest Crops')
Clean_Produce = Transition(label='Clean Produce')
Package_Goods = Transition(label='Package Goods')
Inspect_Quality = Transition(label='Inspect Quality')
Distribute_Goods = Transition(label='Distribute Goods')
Maintain_Units = Transition(label='Maintain Units')
Analyze_Data = Transition(label='Analyze Data')

# Construct the partial order according to the described process:

# 1) Site assessment and structural installation sequentially
# 2) Seed selection and nutrient prep sequentially
# 3) Automated planting and climate monitoring concurrently after seed selection and prep
# 4) Pest control and disease detection concurrently after planting and monitoring
# 5) Harvest scheduling after pest and disease control
# 6) Harvest crops after scheduling
# 7) Post-harvest processing: clean, package, inspect sequentially
# 8) Distribute goods after inspection
# 9) Maintain units and analyze data concurrently after distribution

# Create PO nodes
nodes = [
    Site_Assess,
    Install_Structure,
    Select_Seeds,
    Prepare_Nutrients,
    Automate_Planting,
    Monitor_Climate,
    Detect_Pests,
    Control_Disease,
    Schedule_Harvest,
    Harvest_Crops,
    Clean_Produce,
    Package_Goods,
    Inspect_Quality,
    Distribute_Goods,
    Maintain_Units,
    Analyze_Data,
]

root = StrictPartialOrder(nodes=nodes)

# Add order edges

# 1) Site Assess --> Install Structure
root.order.add_edge(Site_Assess, Install_Structure)

# 2) Install Structure --> Select Seeds and Prepare Nutrients (these two can be concurrent)
root.order.add_edge(Install_Structure, Select_Seeds)
root.order.add_edge(Install_Structure, Prepare_Nutrients)

# 3) Select Seeds and Prepare Nutrients --> Automate Planting and Monitor Climate
root.order.add_edge(Select_Seeds, Automate_Planting)
root.order.add_edge(Prepare_Nutrients, Automate_Planting)
root.order.add_edge(Select_Seeds, Monitor_Climate)
root.order.add_edge(Prepare_Nutrients, Monitor_Climate)

# Automate Planting and Monitor Climate run concurrently, so no order edge between them

# 4) Automate Planting and Monitor Climate --> Detect Pests and Control Disease
root.order.add_edge(Automate_Planting, Detect_Pests)
root.order.add_edge(Monitor_Climate, Detect_Pests)
root.order.add_edge(Automate_Planting, Control_Disease)
root.order.add_edge(Monitor_Climate, Control_Disease)

# Detect Pests and Control Disease run concurrently, no edge between them

# 5) Detect Pests and Control Disease --> Schedule Harvest
root.order.add_edge(Detect_Pests, Schedule_Harvest)
root.order.add_edge(Control_Disease, Schedule_Harvest)

# 6) Schedule Harvest --> Harvest Crops
root.order.add_edge(Schedule_Harvest, Harvest_Crops)

# 7) Harvest Crops --> Clean Produce --> Package Goods --> Inspect Quality
root.order.add_edge(Harvest_Crops, Clean_Produce)
root.order.add_edge(Clean_Produce, Package_Goods)
root.order.add_edge(Package_Goods, Inspect_Quality)

# 8) Inspect Quality --> Distribute Goods
root.order.add_edge(Inspect_Quality, Distribute_Goods)

# 9) Distribute Goods --> Maintain Units and Analyze Data (concurrent)
root.order.add_edge(Distribute_Goods, Maintain_Units)
root.order.add_edge(Distribute_Goods, Analyze_Data)

# Maintain Units and Analyze Data concurrent, no edges between them

# 'root' is the final model