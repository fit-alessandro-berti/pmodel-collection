# Generated from: d1e5daa5-fcc0-4512-8f7b-8858653c18a6.json
# Description: This process outlines the complex and multifaceted steps required to establish an urban vertical farming facility. It involves site assessment, regulatory compliance checks, modular system design, installation of hydroponic units, integration of IoT sensors, nutrient solution calibration, climate control programming, crop selection based on microclimate data, lighting optimization, staff training on automated systems, harvesting schedule development, waste recycling protocols, market demand analysis, distribution logistics planning, and ongoing system performance monitoring to ensure sustainable and efficient crop production within constrained urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Survey = Transition(label='Site Survey')
Regulation_Check = Transition(label='Regulation Check')
Design_Modules = Transition(label='Design Modules')
Install_Hydroponics = Transition(label='Install Hydroponics')
Integrate_Sensors = Transition(label='Integrate Sensors')
Calibrate_Nutrients = Transition(label='Calibrate Nutrients')
Program_Climate = Transition(label='Program Climate')
Select_Crops = Transition(label='Select Crops')
Optimize_Lighting = Transition(label='Optimize Lighting')
Train_Staff = Transition(label='Train Staff')
Plan_Harvest = Transition(label='Plan Harvest')
Recycle_Waste = Transition(label='Recycle Waste')
Analyze_Demand = Transition(label='Analyze Demand')
Plan_Logistics = Transition(label='Plan Logistics')
Monitor_Systems = Transition(label='Monitor Systems')

# Build a StrictPartialOrder representing the process with ordering dependencies:
# According to the description, ordering is roughly:
# 1) Site Survey and Regulation Check happen first (concurrent)
# 2) Design Modules comes after both site survey and regulation check
# 3) Install Hydroponics after Design Modules
# 4) Integrate Sensors after Install Hydroponics
# 5) Calibrate Nutrients after Integrate Sensors
# 6) Program Climate after Calibrate Nutrients
# 7) Select Crops after Program Climate
# 8) Optimize Lighting after Select Crops
# 9) Train Staff after Optimize Lighting
# 10) Plan Harvest after Train Staff
# 11) Recycle Waste after Plan Harvest
# 12) Analyze Demand after Recycle Waste
# 13) Plan Logistics after Analyze Demand
# 14) Monitor Systems after Plan Logistics

nodes = [
    Site_Survey,
    Regulation_Check,
    Design_Modules,
    Install_Hydroponics,
    Integrate_Sensors,
    Calibrate_Nutrients,
    Program_Climate,
    Select_Crops,
    Optimize_Lighting,
    Train_Staff,
    Plan_Harvest,
    Recycle_Waste,
    Analyze_Demand,
    Plan_Logistics,
    Monitor_Systems,
]

root = StrictPartialOrder(nodes=nodes)

# Concurrent start: Site Survey and Regulation Check run concurrently, no edge between them

root.order.add_edge(Site_Survey, Design_Modules)
root.order.add_edge(Regulation_Check, Design_Modules)

root.order.add_edge(Design_Modules, Install_Hydroponics)
root.order.add_edge(Install_Hydroponics, Integrate_Sensors)
root.order.add_edge(Integrate_Sensors, Calibrate_Nutrients)
root.order.add_edge(Calibrate_Nutrients, Program_Climate)
root.order.add_edge(Program_Climate, Select_Crops)
root.order.add_edge(Select_Crops, Optimize_Lighting)
root.order.add_edge(Optimize_Lighting, Train_Staff)
root.order.add_edge(Train_Staff, Plan_Harvest)
root.order.add_edge(Plan_Harvest, Recycle_Waste)
root.order.add_edge(Recycle_Waste, Analyze_Demand)
root.order.add_edge(Analyze_Demand, Plan_Logistics)
root.order.add_edge(Plan_Logistics, Monitor_Systems)