# Generated from: f16cf946-8543-4dee-9400-18c79ef7478b.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farming facility within a repurposed industrial building. It involves site assessment, environmental analysis, modular system design, seed selection based on microclimate, installation of hydroponic and aeroponic units, integration of IoT sensors for real-time monitoring, automation of nutrient delivery, energy optimization via renewable sources, pest management without pesticides, periodic crop rotation planning, quality control checks, yield forecasting using AI models, supply chain coordination for local distribution, employee training on system maintenance, and continuous process improvement through data analytics. The process ensures sustainable food production with minimal environmental impact in dense urban areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Survey = Transition(label='Site Survey')
Climate_Study = Transition(label='Climate Study')
System_Design = Transition(label='System Design')
Seed_Selection = Transition(label='Seed Selection')
Unit_Install = Transition(label='Unit Install')
Sensor_Setup = Transition(label='Sensor Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Energy_Audit = Transition(label='Energy Audit')
Pest_Control = Transition(label='Pest Control')
Crop_Plan = Transition(label='Crop Plan')
Quality_Check = Transition(label='Quality Check')
Yield_Forecast = Transition(label='Yield Forecast')
Supply_Sync = Transition(label='Supply Sync')
Staff_Train = Transition(label='Staff Train')
Data_Review = Transition(label='Data Review')

# Create a strict partial order with nodes and order:
# Orderings are constructed logically following the description:

# 1) Site Survey --> Climate Study (site assessment then environmental analysis)
# 2) Climate Study --> System Design (next step: modular system design)
# 3) System Design --> Seed Selection (seed selection based on microclimate)
# 4) Seed Selection --> Unit Install (install hydroponic and aeroponic units)
# 5) Unit Install --> Sensor Setup (integration of IoT sensors)
# 6) Sensor Setup --> Nutrient Mix (automation of nutrient delivery)
# 7) Nutrient Mix --> Energy Audit (energy optimization via renewables)
# 8) Energy Audit --> Pest Control (pest management)
# 9) Pest Control --> Crop Plan (crop rotation planning)
# 10) Crop Plan --> Quality Check (quality control checks)
# 11) Quality Check --> Yield Forecast (yield forecasting using AI)
# 12) Yield Forecast --> Supply Sync (supply chain coordination)
# 13) Supply Sync --> Staff Train (employee training)
# 14) Staff Train --> Data Review (continuous process improvement via data analytics)

nodes = [Site_Survey, Climate_Study, System_Design, Seed_Selection, Unit_Install, Sensor_Setup,
         Nutrient_Mix, Energy_Audit, Pest_Control, Crop_Plan, Quality_Check, Yield_Forecast,
         Supply_Sync, Staff_Train, Data_Review]

root = StrictPartialOrder(nodes=nodes)

root.order.add_edge(Site_Survey, Climate_Study)
root.order.add_edge(Climate_Study, System_Design)
root.order.add_edge(System_Design, Seed_Selection)
root.order.add_edge(Seed_Selection, Unit_Install)
root.order.add_edge(Unit_Install, Sensor_Setup)
root.order.add_edge(Sensor_Setup, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Energy_Audit)
root.order.add_edge(Energy_Audit, Pest_Control)
root.order.add_edge(Pest_Control, Crop_Plan)
root.order.add_edge(Crop_Plan, Quality_Check)
root.order.add_edge(Quality_Check, Yield_Forecast)
root.order.add_edge(Yield_Forecast, Supply_Sync)
root.order.add_edge(Supply_Sync, Staff_Train)
root.order.add_edge(Staff_Train, Data_Review)