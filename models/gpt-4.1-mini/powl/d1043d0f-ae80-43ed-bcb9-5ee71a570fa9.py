# Generated from: d1043d0f-ae80-43ed-bcb9-5ee71a570fa9.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farm within a constrained city environment. It begins with site evaluation and environmental analysis, followed by modular structure design tailored to space limitations. Subsequent activities cover nutrient solution formulation, seed selection adapted to vertical growth, automated climate control integration, and installation of energy-efficient LED lighting. The process continues with IoT sensor deployment for real-time monitoring, pest management using biological agents, waste recycling protocols, hydroponic system testing, and staff training on operational procedures. Finally, it includes yield forecasting, market positioning strategies, and continuous improvement cycles based on data analytics to optimize production and sustainability in an urban setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Env_Analysis = Transition(label='Env Analysis')
Module_Design = Transition(label='Module Design')
Seed_Selection = Transition(label='Seed Selection')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Setup = Transition(label='Climate Setup')
LED_Install = Transition(label='LED Install')
Sensor_Deploy = Transition(label='Sensor Deploy')
Pest_Control = Transition(label='Pest Control')
Waste_Recycle = Transition(label='Waste Recycle')
Hydro_Test = Transition(label='Hydro Test')
Staff_Train = Transition(label='Staff Train')
Yield_Forecast = Transition(label='Yield Forecast')
Market_Plan = Transition(label='Market Plan')
Data_Review = Transition(label='Data Review')

root = StrictPartialOrder(nodes=[
    Site_Survey, Env_Analysis, Module_Design,
    Nutrient_Mix, Seed_Selection, Climate_Setup, LED_Install,
    Sensor_Deploy, Pest_Control, Waste_Recycle,
    Hydro_Test, Staff_Train, Yield_Forecast, Market_Plan, Data_Review
])

root.order.add_edge(Site_Survey, Env_Analysis)
root.order.add_edge(Env_Analysis, Module_Design)

# Nutrient Mix and Seed Selection depend on Module Design (sequence between them is unspecified, so partial order)
root.order.add_edge(Module_Design, Nutrient_Mix)
root.order.add_edge(Module_Design, Seed_Selection)

root.order.add_edge(Nutrient_Mix, Climate_Setup)
root.order.add_edge(Seed_Selection, Climate_Setup)

root.order.add_edge(Climate_Setup, LED_Install)

root.order.add_edge(LED_Install, Sensor_Deploy)
root.order.add_edge(Sensor_Deploy, Pest_Control)
root.order.add_edge(Pest_Control, Waste_Recycle)
root.order.add_edge(Waste_Recycle, Hydro_Test)

root.order.add_edge(Hydro_Test, Staff_Train)

root.order.add_edge(Staff_Train, Yield_Forecast)
root.order.add_edge(Yield_Forecast, Market_Plan)

root.order.add_edge(Market_Plan, Data_Review)