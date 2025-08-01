# Generated from: 09e4cbf7-12fe-451f-9877-cdd9ac6a819d.json
# Description: This process outlines the complex implementation of an urban vertical farming system within a densely populated city environment. It involves site evaluation, modular farm design, environmental control integration, resource logistics, crop selection based on microclimate data, advanced automation setup, continuous monitoring, and community engagement. The process also incorporates adaptive pest management strategies, energy optimization protocols, and real-time data analytics to ensure sustainable crop production. Additionally, it integrates waste recycling loops and supply chain coordination with local markets to maximize efficiency and reduce environmental impact. Coordination among multidisciplinary teams including agronomists, engineers, urban planners, and IT specialists is critical for successful deployment and scalability of the farming system.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Climate_Study = Transition(label='Climate Study')
Resource_Plan = Transition(label='Resource Plan')
Modular_Build = Transition(label='Modular Build')
Sensor_Install = Transition(label='Sensor Install')
Automation_Setup = Transition(label='Automation Setup')
Crop_Select = Transition(label='Crop Select')
Irrigation_Tune = Transition(label='Irrigation Tune')
Pest_Control = Transition(label='Pest Control')
Data_Monitor = Transition(label='Data Monitor')
Waste_Cycle = Transition(label='Waste Cycle')
Energy_Audit = Transition(label='Energy Audit')
Market_Link = Transition(label='Market Link')
Team_Sync = Transition(label='Team Sync')
Feedback_Loop = Transition(label='Feedback Loop')
Scale_Review = Transition(label='Scale Review')

# Waste recycling loop: Waste Cycle (A), Feedback Loop (B)
# loop( A=Waste Cycle, B=Feedback Loop )
Waste_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Waste_Cycle, Feedback_Loop])

# Pest control loop: Pest Control (A), Irrigation Tune (B)
Pest_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Pest_Control, Irrigation_Tune])

# Modular farm assembly order:
# Site Survey -> Design Layout -> Climate Study -> Resource Plan -> Modular Build -> Sensor Install
Modular_PO = StrictPartialOrder(nodes=[
    Site_Survey,
    Design_Layout,
    Climate_Study,
    Resource_Plan,
    Modular_Build,
    Sensor_Install,
])
Modular_PO.order.add_edge(Site_Survey, Design_Layout)
Modular_PO.order.add_edge(Design_Layout, Climate_Study)
Modular_PO.order.add_edge(Climate_Study, Resource_Plan)
Modular_PO.order.add_edge(Resource_Plan, Modular_Build)
Modular_PO.order.add_edge(Modular_Build, Sensor_Install)

# Crop selection after climate study (important data), parallel to Pest loop start
# Crop Select depends on Climate Study
# Crop Select -> Automation Setup -> Data Monitor
Crop_PO = StrictPartialOrder(nodes=[
    Crop_Select,
    Automation_Setup,
    Data_Monitor,
])
Crop_PO.order.add_edge(Crop_Select, Automation_Setup)
Crop_PO.order.add_edge(Automation_Setup, Data_Monitor)

# Energy Audit and Market Link can run in parallel but both after Resource Plan
Energy_Market_PO = StrictPartialOrder(nodes=[
    Energy_Audit,
    Market_Link,
])
# No order between Energy Audit and Market Link - concurrent
# But both after Resource Plan is enforced below at higher level by edges

# Team Sync and Scale Review are final coordination activities, after main flows
# Incorporate Pest Loop after Automation_Setup but before Data Monitor (allow monitoring pest management)
# We incorporate Pest_Loop and Waste_Loop as parallel to Data Monitor

# Combine Pest_Loop and Waste_Loop and Data Monitor in partial order with no ordering (concurrent)
Monitoring_PO = StrictPartialOrder(nodes=[Data_Monitor, Pest_Loop, Waste_Loop])

# Connect Automation_Setup to Monitoring_PO nodes (Data Monitor, Pest_Loop, Waste_Loop) 
# We achieve this by edges Automation_Setup --> Monitoring_PO nodes

# Now build a master PO with all components:
# Nodes: Modular_PO nodes + Crop_PO nodes + Energy_Audit + Market_Link + Team_Sync + Scale_Review + Monitoring_PO nodes
all_nodes = [
    Site_Survey, Design_Layout, Climate_Study, Resource_Plan, Modular_Build, Sensor_Install,
    Crop_Select, Automation_Setup,
    Energy_Audit, Market_Link,
    Data_Monitor, Pest_Loop, Waste_Loop,
    Team_Sync, Scale_Review,
]

root = StrictPartialOrder(nodes=all_nodes)

# Add edges for Modular_PO  
root.order.add_edge(Site_Survey, Design_Layout)
root.order.add_edge(Design_Layout, Climate_Study)
root.order.add_edge(Climate_Study, Resource_Plan)
root.order.add_edge(Resource_Plan, Modular_Build)
root.order.add_edge(Modular_Build, Sensor_Install)

# Crop Select depends on Climate Study
root.order.add_edge(Climate_Study, Crop_Select)
root.order.add_edge(Crop_Select, Automation_Setup)

# Automation Setup precedes Monitoring_PO nodes (Data Monitor, Pest_Loop, Waste_Loop)
root.order.add_edge(Automation_Setup, Data_Monitor)
root.order.add_edge(Automation_Setup, Pest_Loop)
root.order.add_edge(Automation_Setup, Waste_Loop)

# Energy Audit and Market Link depend on Resource Plan
root.order.add_edge(Resource_Plan, Energy_Audit)
root.order.add_edge(Resource_Plan, Market_Link)

# Team Sync after major setup steps (Sensor Install, Energy Audit, Market Link)
root.order.add_edge(Sensor_Install, Team_Sync)
root.order.add_edge(Energy_Audit, Team_Sync)
root.order.add_edge(Market_Link, Team_Sync)

# Scale Review after Team Sync and Data Monitor (final evaluation)
root.order.add_edge(Team_Sync, Scale_Review)
root.order.add_edge(Data_Monitor, Scale_Review)