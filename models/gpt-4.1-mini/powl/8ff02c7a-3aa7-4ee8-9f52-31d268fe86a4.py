# Generated from: 8ff02c7a-3aa7-4ee8-9f52-31d268fe86a4.json
# Description: This process outlines the integration of vertical farming systems within urban infrastructure to optimize food production, resource management, and sustainability. It involves site analysis, modular farm design, environmental control calibration, automated nutrient delivery, energy optimization, crop monitoring via IoT sensors, pest detection through AI image recognition, data-driven yield forecasting, community engagement initiatives, compliance checks with municipal regulations, waste recycling protocols, dynamic lighting adjustment, supply chain synchronization, urban market distribution planning, and continuous system upgrades to adapt to evolving urban needs and technology advancements.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Site_Analysis = Transition(label='Site Analysis')
Farm_Design = Transition(label='Farm Design')
Env_Calibration = Transition(label='Env Calibration')
Nutrient_Delivery = Transition(label='Nutrient Delivery')
Energy_Optimization = Transition(label='Energy Optimization')
Crop_Monitoring = Transition(label='Crop Monitoring')
Pest_Detection = Transition(label='Pest Detection')
Yield_Forecasting = Transition(label='Yield Forecasting')
Community_Outreach = Transition(label='Community Outreach')
Compliance_Check = Transition(label='Compliance Check')
Waste_Recycling = Transition(label='Waste Recycling')
Lighting_Adjust = Transition(label='Lighting Adjust')
Supply_Sync = Transition(label='Supply Sync')
Market_Planning = Transition(label='Market Planning')
System_Upgrade = Transition(label='System Upgrade')

# Build the strict partial order for the main sequence
root = StrictPartialOrder(nodes=[
    Site_Analysis, Farm_Design, Env_Calibration, Nutrient_Delivery, Energy_Optimization,
    Crop_Monitoring, Pest_Detection, Yield_Forecasting, Community_Outreach,
    Compliance_Check, Waste_Recycling, Lighting_Adjust, Supply_Sync,
    Market_Planning, System_Upgrade
])

# Define the natural process ordering based on description
root.order.add_edge(Site_Analysis, Farm_Design)
root.order.add_edge(Farm_Design, Env_Calibration)
root.order.add_edge(Env_Calibration, Nutrient_Delivery)
root.order.add_edge(Nutrient_Delivery, Energy_Optimization)

# Crop Monitoring, Pest Detection, Yield Forecasting are related and somewhat concurrent but ordered
root.order.add_edge(Energy_Optimization, Crop_Monitoring)
root.order.add_edge(Crop_Monitoring, Pest_Detection)
root.order.add_edge(Pest_Detection, Yield_Forecasting)

# Community Outreach, Compliance Check, Waste Recycling happen after yield forecasting
root.order.add_edge(Yield_Forecasting, Community_Outreach)
root.order.add_edge(Yield_Forecasting, Compliance_Check)
root.order.add_edge(Yield_Forecasting, Waste_Recycling)

# The last three start after these three but can be concurrent
root.order.add_edge(Community_Outreach, Lighting_Adjust)
root.order.add_edge(Compliance_Check, Lighting_Adjust)
root.order.add_edge(Waste_Recycling, Lighting_Adjust)

root.order.add_edge(Lighting_Adjust, Supply_Sync)
root.order.add_edge(Lighting_Adjust, Market_Planning)
root.order.add_edge(Lighting_Adjust, System_Upgrade)

# Supply Sync and Market Planning can be concurrent but both lead to System Upgrade
root.order.add_edge(Supply_Sync, System_Upgrade)
root.order.add_edge(Market_Planning, System_Upgrade)