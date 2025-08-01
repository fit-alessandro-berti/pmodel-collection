# Generated from: e59343c9-8a8b-4838-a92f-35112dfeb6d7.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm in a densely populated city environment. It combines aspects of architecture, agriculture, technology integration, and sustainability. The process begins with site analysis and regulatory approval, followed by structural design tailored for vertical hydroponic systems. Procurement of specialized equipment and organic nutrients ensures optimal growth conditions. Installation of IoT sensors and AI-driven climate control systems enables precise environmental management. Seed selection and germination protocols emphasize crop diversity and yield maximization. Continuous monitoring and data analytics support adaptive maintenance and pest control strategies. Finally, the process concludes with packaging and distribution logistics optimized for freshness and minimal environmental impact, ensuring a sustainable urban food supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Site_Survey = Transition(label='Site Survey')
Permit_Approval = Transition(label='Permit Approval')
Design_Layout = Transition(label='Design Layout')
System_Procure = Transition(label='System Procure')
Nutrient_Prep = Transition(label='Nutrient Prep')
Structure_Build = Transition(label='Structure Build')
Sensor_Install = Transition(label='Sensor Install')
Climate_Setup = Transition(label='Climate Setup')
Seed_Select = Transition(label='Seed Select')
Germinate_Seeds = Transition(label='Germinate Seeds')
Monitor_Growth = Transition(label='Monitor Growth')
Data_Analyze = Transition(label='Data Analyze')
Pest_Control = Transition(label='Pest Control')
Harvest_Crop = Transition(label='Harvest Crop')
Package_Goods = Transition(label='Package Goods')
Ship_Products = Transition(label='Ship Products')

# Model the monitoring loop: Monitor Growth, Data Analyze, Pest Control can repeat continuously
monitoring_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        Monitor_Growth,
        OperatorPOWL(operator=Operator.XOR, children=[Data_Analyze, Pest_Control])
    ]
)

# The core flow structured as partial order
# Steps:
# 1. Site Survey --> Permit Approval
# 2. Permit Approval --> Design Layout
# 3. Design Layout --> Structure Build (since structure is physical)
# 4. In parallel after Design Layout: System Procure and Nutrient Prep (can be concurrent)
# 5. After Structure Build and procurement/preparation, Sensor Install and Climate Setup (parallel)
# 6. Then Seed Select --> Germinate Seeds
# 7. Then monitoring loop (Monitor Growth, Data Analyze, Pest Control)
# 8. Then Harvest Crop
# 9. Finally Package Goods --> Ship Products

# Partial order nodes
nodes = [
    Site_Survey,
    Permit_Approval,
    Design_Layout,
    Structure_Build,
    System_Procure,
    Nutrient_Prep,
    Sensor_Install,
    Climate_Setup,
    Seed_Select,
    Germinate_Seeds,
    monitoring_loop,
    Harvest_Crop,
    Package_Goods,
    Ship_Products
]

root = StrictPartialOrder(nodes=nodes)

# Orders

# 1 -> 2 ->3
root.order.add_edge(Site_Survey, Permit_Approval)
root.order.add_edge(Permit_Approval, Design_Layout)

# Design_Layout --> Structure_Build
root.order.add_edge(Design_Layout, Structure_Build)

# Design_Layout -> System Procure and Nutrient Prep (both can start after design)
root.order.add_edge(Design_Layout, System_Procure)
root.order.add_edge(Design_Layout, Nutrient_Prep)

# After both Structure Build and procurement/prep, Sensor install and Climate setup can start
# So add edges Structure Build -> Sensor Install and Climate Setup
# and System Procure -> Sensor Install and Climate Setup
# and Nutrient Prep -> Sensor Install and Climate Setup
root.order.add_edge(Structure_Build, Sensor_Install)
root.order.add_edge(Structure_Build, Climate_Setup)

root.order.add_edge(System_Procure, Sensor_Install)
root.order.add_edge(System_Procure, Climate_Setup)

root.order.add_edge(Nutrient_Prep, Sensor_Install)
root.order.add_edge(Nutrient_Prep, Climate_Setup)

# Sensor Install and Climate Setup both must finish before Seed Select
root.order.add_edge(Sensor_Install, Seed_Select)
root.order.add_edge(Climate_Setup, Seed_Select)

# Seed Select -> Germinate Seeds
root.order.add_edge(Seed_Select, Germinate_Seeds)

# Germinate Seeds -> monitoring loop
root.order.add_edge(Germinate_Seeds, monitoring_loop)

# monitoring loop -> Harvest Crop
root.order.add_edge(monitoring_loop, Harvest_Crop)

# Harvest Crop -> Package Goods -> Ship Products
root.order.add_edge(Harvest_Crop, Package_Goods)
root.order.add_edge(Package_Goods, Ship_Products)