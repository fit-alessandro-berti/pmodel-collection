# Generated from: 80dd9155-8773-4f46-86d9-4fe267bc47af.json
# Description: This process outlines the setup of a vertical farming system within an urban environment, focusing on integrating hydroponics, IoT sensors, and renewable energy sources. It involves site assessment, environmental impact analysis, modular construction, nutrient solution preparation, sensor calibration, crop selection based on local climate, automated irrigation scheduling, real-time data monitoring, pest control using biological agents, waste recycling, market demand forecasting, and final system validation. The goal is to create a sustainable, scalable, and efficient vertical farm that maximizes space utilization while minimizing resource consumption and environmental footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
SiteAssess       = Transition(label='Site Assess')
ImpactStudy      = Transition(label='Impact Study')
DesignLayout     = Transition(label='Design Layout')
MaterialProcure  = Transition(label='Material Procure')
ModuleBuild      = Transition(label='Module Build')
SensorSetup      = Transition(label='Sensor Setup')
NutrientMix      = Transition(label='Nutrient Mix')
CropSelect       = Transition(label='Crop Select')
IrrigationPlan   = Transition(label='Irrigation Plan')
DataMonitor      = Transition(label='Data Monitor')
PestControl      = Transition(label='Pest Control')
WasteRecycle     = Transition(label='Waste Recycle')
EnergyIntegrate  = Transition(label='Energy Integrate')
MarketForecast   = Transition(label='Market Forecast')
SystemValidate   = Transition(label='System Validate')

# Build a partial order:
# 1. A linear sequence from SiteAssess to IrrigationPlan
# 2. Then five activities in parallel: DataMonitor, PestControl, WasteRecycle,
#    EnergyIntegrate, MarketForecast
# 3. Finally SystemValidate depends on all five parallel activities

root = StrictPartialOrder(nodes=[
    SiteAssess, ImpactStudy, DesignLayout, MaterialProcure, ModuleBuild,
    SensorSetup, NutrientMix, CropSelect, IrrigationPlan,
    DataMonitor, PestControl, WasteRecycle, EnergyIntegrate, MarketForecast,
    SystemValidate
])

# Sequence up to IrrigationPlan
root.order.add_edge(SiteAssess,      ImpactStudy)
root.order.add_edge(ImpactStudy,     DesignLayout)
root.order.add_edge(DesignLayout,    MaterialProcure)
root.order.add_edge(MaterialProcure, ModuleBuild)
root.order.add_edge(ModuleBuild,     SensorSetup)
root.order.add_edge(SensorSetup,     NutrientMix)
root.order.add_edge(NutrientMix,     CropSelect)
root.order.add_edge(CropSelect,      IrrigationPlan)

# Parallel branches after IrrigationPlan
for act in [DataMonitor, PestControl, WasteRecycle, EnergyIntegrate, MarketForecast]:
    root.order.add_edge(IrrigationPlan, act)

# Join before SystemValidate
for act in [DataMonitor, PestControl, WasteRecycle, EnergyIntegrate, MarketForecast]:
    root.order.add_edge(act, SystemValidate)