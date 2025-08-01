# Generated from: ddc97543-46bd-4424-9b7b-948720b19620.json
# Description: This process outlines the establishment of an urban vertical farm designed to maximize crop yield in limited city spaces using innovative hydroponic systems. It includes site assessment, structural retrofitting, environmental control calibration, nutrient solution formulation, crop selection based on climate resilience, and integration of AI-driven monitoring. The workflow further involves worker training on specialized equipment, implementation of pest management strategies without pesticides, scheduling automated irrigation cycles, and establishing supply chain logistics to deliver fresh produce to local markets efficiently. Continuous data collection and analysis ensure optimization of growth conditions and energy consumption, promoting sustainability and profitability in an unconventional agricultural model within urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Structure_Prep = Transition(label='Structure Prep')
System_Install = Transition(label='System Install')
Env_Control = Transition(label='Env Control')
Nutrient_Mix = Transition(label='Nutrient Mix')
Crop_Select = Transition(label='Crop Select')
AI_Setup = Transition(label='AI Setup')
Worker_Train = Transition(label='Worker Train')
Pest_Control = Transition(label='Pest Control')
Irrigation_Plan = Transition(label='Irrigation Plan')
Data_Monitor = Transition(label='Data Monitor')
Yield_Forecast = Transition(label='Yield Forecast')
Energy_Audit = Transition(label='Energy Audit')
Market_Setup = Transition(label='Market Setup')
Logistics_Plan = Transition(label='Logistics Plan')
Waste_Manage = Transition(label='Waste Manage')

# Construct a partial order that respects the described workflow:

# Initial sequence: Site Survey --> Structure Prep --> System Install
# Then parallel branching of environment/nutrient/crop/AI setup (Env Control, Nutrient Mix, Crop Select, AI Setup)
# after installation, they are concurrent

# After these setup activities, worker training, pest control, irrigation plan occur concurrently

# Then data monitor and yield forecast in sequence, followed by energy audit
# These are sequential analytics steps after above

# Market setup and logistics plan form a sequence after the analytics steps
# Waste manage parallels market/logistics planning (can be done concurrently)

# Build nodes list
nodes = [
    Site_Survey, Structure_Prep, System_Install,
    Env_Control, Nutrient_Mix, Crop_Select, AI_Setup,
    Worker_Train, Pest_Control, Irrigation_Plan,
    Data_Monitor, Yield_Forecast, Energy_Audit,
    Market_Setup, Logistics_Plan, Waste_Manage
]

root = StrictPartialOrder(nodes=nodes)
order = root.order

# sequence: Site Survey --> Structure Prep --> System Install
order.add_edge(Site_Survey, Structure_Prep)
order.add_edge(Structure_Prep, System_Install)

# after System Install, Env Control, Nutrient Mix, Crop Select, AI Setup can run concurrently
order.add_edge(System_Install, Env_Control)
order.add_edge(System_Install, Nutrient_Mix)
order.add_edge(System_Install, Crop_Select)
order.add_edge(System_Install, AI_Setup)

# Worker Train, Pest Control, Irrigation Plan can start after all four above complete
# To correctly model "after these four completed" the concurrency, we add edges from each of the four to each of the three:
for before_node in [Env_Control, Nutrient_Mix, Crop_Select, AI_Setup]:
    order.add_edge(before_node, Worker_Train)
    order.add_edge(before_node, Pest_Control)
    order.add_edge(before_node, Irrigation_Plan)

# Data Monitor --> Yield Forecast --> Energy Audit (sequential)
order.add_edge(Worker_Train, Data_Monitor)
order.add_edge(Pest_Control, Data_Monitor)
order.add_edge(Irrigation_Plan, Data_Monitor)

order.add_edge(Data_Monitor, Yield_Forecast)
order.add_edge(Yield_Forecast, Energy_Audit)

# Market Setup --> Logistics Plan sequence after Energy Audit
order.add_edge(Energy_Audit, Market_Setup)
order.add_edge(Market_Setup, Logistics_Plan)

# Waste Manage concurrent with Market Setup and Logistics Plan (starts after Energy Audit)
order.add_edge(Energy_Audit, Waste_Manage)

# The partial order captures that Market Setup and Logistics Plan are sequential, Waste Manage concurrent with both

# The result is:
# Site Survey --> Structure Prep --> System Install
# System Install --> (Env Control, Nutrient Mix, Crop Select, AI Setup) [concurrent]
# All four --> (Worker Train, Pest Control, Irrigation Plan) [concurrent]
# All three --> Data Monitor --> Yield Forecast --> Energy Audit --> Market Setup --> Logistics Plan
# Energy Audit --> Waste Manage (concurrent with Market/Logistics)

# root is the StrictPartialOrder capturing this.

# root variable is now ready.