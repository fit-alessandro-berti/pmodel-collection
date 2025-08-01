# Generated from: 16f13f47-998c-49ac-9e09-5f8c4fc7747d.json
# Description: This process details the complex steps involved in establishing an urban vertical farm within a repurposed industrial building. It integrates architectural redesign, advanced hydroponic system installation, environmental control calibration, and supply chain coordination. The workflow encompasses site analysis, regulatory compliance, modular assembly, nutrient solution formulation, automation programming, and staff training. Emphasis is placed on sustainability through energy-efficient lighting, water recycling, and waste management. The process concludes with quality assurance testing and market launch preparation to ensure consistent crop production and profitability in an unconventional urban agriculture setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

SiteSurvey = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
RegulatoryCheck = Transition(label='Regulatory Check')
StructuralReinforce = Transition(label='Structural Reinforce')
HydroponicSetup = Transition(label='Hydroponic Setup')
LightingInstall = Transition(label='Lighting Install')
ClimateControl = Transition(label='Climate Control')
WaterRecycling = Transition(label='Water Recycling')
NutrientMix = Transition(label='Nutrient Mix')
AutomationConfig = Transition(label='Automation Config')
SensorCalibrate = Transition(label='Sensor Calibrate')
SystemTesting = Transition(label='System Testing')
StaffTraining = Transition(label='Staff Training')
WasteDisposal = Transition(label='Waste Disposal')
MarketLaunch = Transition(label='Market Launch')

# Architectural redesign phase partial order
architectural_phase = StrictPartialOrder(
    nodes=[SiteSurvey, DesignLayout, RegulatoryCheck, StructuralReinforce]
)
architectural_phase.order.add_edge(SiteSurvey, DesignLayout)
architectural_phase.order.add_edge(DesignLayout, RegulatoryCheck)
architectural_phase.order.add_edge(RegulatoryCheck, StructuralReinforce)

# Hydroponic system installation & sustainability measures
# LightingInstall, ClimateControl, WaterRecycling can be done in parallel after StructuralReinforce
# HydroponicSetup depends on StructuralReinforce; NutrientMix on HydroponicSetup
# AutomationConfig and SensorCalibrate after NutrientMix
hydro_install_phase = StrictPartialOrder(
    nodes=[StructuralReinforce, HydroponicSetup, LightingInstall, ClimateControl,
           WaterRecycling, NutrientMix, AutomationConfig, SensorCalibrate]
)
hydro_install_phase.order.add_edge(StructuralReinforce, HydroponicSetup)
hydro_install_phase.order.add_edge(StructuralReinforce, LightingInstall)
hydro_install_phase.order.add_edge(StructuralReinforce, ClimateControl)
hydro_install_phase.order.add_edge(StructuralReinforce, WaterRecycling)
hydro_install_phase.order.add_edge(HydroponicSetup, NutrientMix)
hydro_install_phase.order.add_edge(NutrientMix, AutomationConfig)
hydro_install_phase.order.add_edge(NutrientMix, SensorCalibrate)

# Staff training and waste disposal after setup phase and automation
staff_waste_phase = StrictPartialOrder(
    nodes=[AutomationConfig, SensorCalibrate, StaffTraining, WasteDisposal]
)
staff_waste_phase.order.add_edge(AutomationConfig, StaffTraining)
staff_waste_phase.order.add_edge(SensorCalibrate, StaffTraining)
staff_waste_phase.order.add_edge(StaffTraining, WasteDisposal)

# Testing and market launch after staff training and waste disposal
final_phase = StrictPartialOrder(
    nodes=[WasteDisposal, SystemTesting, MarketLaunch]
)
final_phase.order.add_edge(WasteDisposal, SystemTesting)
final_phase.order.add_edge(SystemTesting, MarketLaunch)

# Compose whole process partial order
root = StrictPartialOrder(
    nodes=[architectural_phase, hydro_install_phase, staff_waste_phase, final_phase]
)
root.order.add_edge(architectural_phase, hydro_install_phase)
root.order.add_edge(hydro_install_phase, staff_waste_phase)
root.order.add_edge(staff_waste_phase, final_phase)