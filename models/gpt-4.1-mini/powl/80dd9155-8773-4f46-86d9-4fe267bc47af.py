# Generated from: 80dd9155-8773-4f46-86d9-4fe267bc47af.json
# Description: This process outlines the setup of a vertical farming system within an urban environment, focusing on integrating hydroponics, IoT sensors, and renewable energy sources. It involves site assessment, environmental impact analysis, modular construction, nutrient solution preparation, sensor calibration, crop selection based on local climate, automated irrigation scheduling, real-time data monitoring, pest control using biological agents, waste recycling, market demand forecasting, and final system validation. The goal is to create a sustainable, scalable, and efficient vertical farm that maximizes space utilization while minimizing resource consumption and environmental footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Assess = Transition(label='Site Assess')
Impact_Study = Transition(label='Impact Study')
Design_Layout = Transition(label='Design Layout')
Material_Procure = Transition(label='Material Procure')
Module_Build = Transition(label='Module Build')
Sensor_Setup = Transition(label='Sensor Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Crop_Select = Transition(label='Crop Select')
Irrigation_Plan = Transition(label='Irrigation Plan')
Data_Monitor = Transition(label='Data Monitor')
Pest_Control = Transition(label='Pest Control')
Waste_Recycle = Transition(label='Waste Recycle')
Energy_Integrate = Transition(label='Energy Integrate')
Market_Forecast = Transition(label='Market Forecast')
System_Validate = Transition(label='System Validate')

# Construct partial orders

# Initial assessment phase
assessment = StrictPartialOrder(nodes=[Site_Assess, Impact_Study])
assessment.order.add_edge(Site_Assess, Impact_Study)

# Design and procurement phase
design_procure = StrictPartialOrder(
    nodes=[Design_Layout, Material_Procure, Energy_Integrate]
)
design_procure.order.add_edge(Design_Layout, Material_Procure)
design_procure.order.add_edge(Design_Layout, Energy_Integrate)

# Construction and setup phase
construction_setup = StrictPartialOrder(
    nodes=[Module_Build, Sensor_Setup, Nutrient_Mix]
)
construction_setup.order.add_edge(Module_Build, Sensor_Setup)
construction_setup.order.add_edge(Module_Build, Nutrient_Mix)

# Crop related activities
crop_related = StrictPartialOrder(
    nodes=[Crop_Select, Irrigation_Plan]
)
crop_related.order.add_edge(Crop_Select, Irrigation_Plan)

# Monitoring and control phase
monitor_control = StrictPartialOrder(
    nodes=[Data_Monitor, Pest_Control, Waste_Recycle]
)
# All three can be concurrent - no explicit order edges

# Market forecasting and validation phase
market_validate = StrictPartialOrder(
    nodes=[Market_Forecast, System_Validate]
)
market_validate.order.add_edge(Market_Forecast, System_Validate)

# Combine crop_related and monitor_control concurrently
crop_monitor = StrictPartialOrder(
    nodes=[crop_related, monitor_control]
)

# Complete process PO
root = StrictPartialOrder(
    nodes=[assessment, design_procure, construction_setup, crop_monitor, market_validate]
)

# Define ordering to represent process dependencies:
# assessment --> design_procure --> construction_setup --> crop_monitor --> market_validate
root.order.add_edge(assessment, design_procure)
root.order.add_edge(design_procure, construction_setup)
root.order.add_edge(construction_setup, crop_monitor)
root.order.add_edge(crop_monitor, market_validate)