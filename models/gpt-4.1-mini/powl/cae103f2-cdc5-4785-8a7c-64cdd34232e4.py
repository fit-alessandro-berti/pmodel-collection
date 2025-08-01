# Generated from: cae103f2-cdc5-4785-8a7c-64cdd34232e4.json
# Description: This process outlines the complex steps involved in launching an urban vertical farming operation within a dense metropolitan area. It includes site acquisition, environmental impact assessment, modular infrastructure setup, multi-tier crop planting, automated nutrient management, integrated pest control, real-time growth monitoring, community engagement programs, yield forecasting, supply chain coordination, regulatory compliance verification, waste recycling systems, energy usage optimization, market entry strategy, and post-launch performance analysis to ensure sustainable urban agriculture and profitability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Site_Acquisition = Transition(label='Site Acquisition')
Impact_Assess = Transition(label='Impact Assess')
Modular_Setup = Transition(label='Modular Setup')
Crop_Planting = Transition(label='Crop Planting')
Nutrient_Control = Transition(label='Nutrient Control')
Pest_Control = Transition(label='Pest Control')
Growth_Monitor = Transition(label='Growth Monitor')
Community_Engage = Transition(label='Community Engage')
Yield_Forecast = Transition(label='Yield Forecast')
Supply_Coordinate = Transition(label='Supply Coordinate')
Compliance_Check = Transition(label='Compliance Check')
Waste_Recycle = Transition(label='Waste Recycle')
Energy_Optimize = Transition(label='Energy Optimize')
Market_Strategy = Transition(label='Market Strategy')
Performance_Review = Transition(label='Performance Review')

# Construct the partial order with the logical (likely) control flow.

# Base partial order with all nodes:
nodes = [
    Site_Acquisition,
    Impact_Assess,
    Modular_Setup,
    Crop_Planting,
    Nutrient_Control,
    Pest_Control,
    Growth_Monitor,
    Community_Engage,
    Yield_Forecast,
    Supply_Coordinate,
    Compliance_Check,
    Waste_Recycle,
    Energy_Optimize,
    Market_Strategy,
    Performance_Review
]

root = StrictPartialOrder(nodes=nodes)

# Add order edges reflecting typical logical sequence:

# Site Acquisition -> Impact Assessment -> Modular Setup
root.order.add_edge(Site_Acquisition, Impact_Assess)
root.order.add_edge(Impact_Assess, Modular_Setup)

# After Modular Setup, Crop Planting can start
root.order.add_edge(Modular_Setup, Crop_Planting)

# Nutrient Control and Pest Control happen concurrently after Crop Planting
# They probably begin after planting, can be done in parallel
root.order.add_edge(Crop_Planting, Nutrient_Control)
root.order.add_edge(Crop_Planting, Pest_Control)

# Growth Monitor depends on both Nutrient Control and Pest Control being started (not necessarily finished)
# But here modeled as after both to be conservative 
root.order.add_edge(Nutrient_Control, Growth_Monitor)
root.order.add_edge(Pest_Control, Growth_Monitor)

# Community Engage can start after Growth Monitor begins; model it concurrently with Growth Monitor but after Crop Planting
root.order.add_edge(Crop_Planting, Community_Engage)

# Yield Forecast and Supply Coordinate depend on Growth Monitor
root.order.add_edge(Growth_Monitor, Yield_Forecast)
root.order.add_edge(Growth_Monitor, Supply_Coordinate)

# Compliance Check may depend on Supply Coordinate and Yield Forecast
root.order.add_edge(Yield_Forecast, Compliance_Check)
root.order.add_edge(Supply_Coordinate, Compliance_Check)

# Waste Recycle and Energy Optimize can be done after Compliance Check, possibly concurrently
root.order.add_edge(Compliance_Check, Waste_Recycle)
root.order.add_edge(Compliance_Check, Energy_Optimize)

# Market Strategy depends on Waste Recycle and Energy Optimize
root.order.add_edge(Waste_Recycle, Market_Strategy)
root.order.add_edge(Energy_Optimize, Market_Strategy)

# Performance Review is last, depends on Market Strategy
root.order.add_edge(Market_Strategy, Performance_Review)