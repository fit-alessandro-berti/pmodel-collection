# Generated from: a76c6456-d81f-48af-9145-077e5ffa2536.json
# Description: This process outlines the setup of an urban rooftop farming system integrating sustainable agriculture with smart technology on city rooftops. It begins with site assessment and structural analysis, followed by modular bed installation and soil conditioning. The process then incorporates automated irrigation setup, sensor deployment for real-time monitoring, and nutrient management calibration. Subsequent activities include crop selection based on microclimate data, pest control via integrated biological agents, and periodic growth assessment using drones. The process concludes with harvest scheduling, produce packaging optimization, and data-driven yield forecasting to maximize productivity and sustainability in limited urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Site_Assess = Transition(label='Site Assess')
Structure_Check = Transition(label='Structure Check')
Bed_Install = Transition(label='Bed Install')
Soil_Prep = Transition(label='Soil Prep')
Irrigation_Set = Transition(label='Irrigation Set')
Sensor_Deploy = Transition(label='Sensor Deploy')
Nutrient_Tune = Transition(label='Nutrient Tune')
Crop_Select = Transition(label='Crop Select')
Pest_Control = Transition(label='Pest Control')
Growth_Scan = Transition(label='Growth Scan')
Drone_Survey = Transition(label='Drone Survey')
Harvest_Plan = Transition(label='Harvest Plan')
Package_Opt = Transition(label='Package Opt')
Yield_Forecast = Transition(label='Yield Forecast')
Waste_Manage = Transition(label='Waste Manage')

# Compose the partial order based on the described order:
# 1. Site Assess --> Structure Check
# 2. Structure Check --> Bed Install --> Soil Prep
# 3. Soil Prep --> Irrigation Set --> Sensor Deploy --> Nutrient Tune
# 4. Nutrient Tune --> Crop Select --> Pest Control
# 5. Pest Control --> Growth Scan --> Drone Survey
# 6. Drone Survey --> Harvest Plan --> Package Opt --> Yield Forecast
# 7. Yield Forecast --> Waste Manage

nodes = [Site_Assess, Structure_Check, Bed_Install, Soil_Prep, Irrigation_Set,
         Sensor_Deploy, Nutrient_Tune, Crop_Select, Pest_Control, Growth_Scan,
         Drone_Survey, Harvest_Plan, Package_Opt, Yield_Forecast, Waste_Manage]

root = StrictPartialOrder(nodes=nodes)

# Add edges to represent the sequence dependencies
root.order.add_edge(Site_Assess, Structure_Check)
root.order.add_edge(Structure_Check, Bed_Install)
root.order.add_edge(Bed_Install, Soil_Prep)

root.order.add_edge(Soil_Prep, Irrigation_Set)
root.order.add_edge(Irrigation_Set, Sensor_Deploy)
root.order.add_edge(Sensor_Deploy, Nutrient_Tune)

root.order.add_edge(Nutrient_Tune, Crop_Select)
root.order.add_edge(Crop_Select, Pest_Control)

root.order.add_edge(Pest_Control, Growth_Scan)
root.order.add_edge(Growth_Scan, Drone_Survey)

root.order.add_edge(Drone_Survey, Harvest_Plan)
root.order.add_edge(Harvest_Plan, Package_Opt)
root.order.add_edge(Package_Opt, Yield_Forecast)

root.order.add_edge(Yield_Forecast, Waste_Manage)