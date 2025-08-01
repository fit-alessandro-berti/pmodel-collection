# Generated from: 2cb8a47a-f03f-4646-9e7a-78e5d3cb0bc9.json
# Description: This process outlines the establishment of an urban vertical farm that integrates advanced hydroponic systems with AI-driven environmental controls. It involves site evaluation in dense metropolitan areas, modular infrastructure assembly, nutrient solution formulation, and real-time sensor calibration. The process also includes labor scheduling for crop monitoring, pest management using biocontrol agents, and dynamic yield forecasting. Additionally, it covers regulatory compliance for urban agriculture, marketing to local retailers, harvesting automation, and waste recycling protocols to ensure sustainability and profitability in constrained urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Permits_Obtain = Transition(label='Permits Obtain')
Structure_Build = Transition(label='Structure Build')
Hydro_Setup = Transition(label='Hydro Setup')
Sensor_Install = Transition(label='Sensor Install')
Nutrient_Mix = Transition(label='Nutrient Mix')
AI_Config = Transition(label='AI Config')
Crop_Planting = Transition(label='Crop Planting')
Pest_Control = Transition(label='Pest Control')
Labor_Assign = Transition(label='Labor Assign')
Growth_Monitor = Transition(label='Growth Monitor')
Yield_Forecast = Transition(label='Yield Forecast')
Harvest_Automate = Transition(label='Harvest Automate')
Waste_Recycle = Transition(label='Waste Recycle')
Market_Engage = Transition(label='Market Engage')

# Build partial orders according to the description logic and typical process dependencies:

# Phase 1: Site evaluation and design
phase1 = StrictPartialOrder(
    nodes=[Site_Survey, Design_Layout, Permits_Obtain]
)
phase1.order.add_edge(Site_Survey, Design_Layout)
phase1.order.add_edge(Design_Layout, Permits_Obtain)

# Phase 2: Construct and setup infrastructure and systems
phase2 = StrictPartialOrder(
    nodes=[Structure_Build, Hydro_Setup, Sensor_Install]
)
phase2.order.add_edge(Structure_Build, Hydro_Setup)
phase2.order.add_edge(Hydro_Setup, Sensor_Install)

# Phase 3: Nutrient formulation and AI config
phase3 = StrictPartialOrder(
    nodes=[Nutrient_Mix, AI_Config]
)
# These two can be concurrent
# no edges added (concurrent)

# Phase 4: Planting and crop care loop: Crop Planting, Pest Control, Labor Assign, Growth Monitor, Yield Forecast
# Model growth monitoring and forecasting as a possible loop over Crop Planting with interventions

# Loop structure: execute Crop Planting first, then either exit or execute Pest Control, Labor Assign,
# Growth Monitor and Yield Forecast, then repeat Crop Planting.
# To keep reasoning simple:
# loop = LOOP(Crop_Planting, PO of Pest_Control, Labor_Assign, Growth_Monitor, Yield_Forecast)

growth_care_nodes = [Pest_Control, Labor_Assign, Growth_Monitor, Yield_Forecast]
growth_care_po = StrictPartialOrder(nodes=growth_care_nodes)
# Add edges to reflect logical order in crop care:
growth_care_po.order.add_edge(Pest_Control, Labor_Assign)
growth_care_po.order.add_edge(Labor_Assign, Growth_Monitor)
growth_care_po.order.add_edge(Growth_Monitor, Yield_Forecast)

growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[Crop_Planting, growth_care_po])

# Phase 5: Harvest, Waste recycle, Market engage run after the loop ends
phase5 = StrictPartialOrder(
    nodes=[Harvest_Automate, Waste_Recycle, Market_Engage]
)
phase5.order.add_edge(Harvest_Automate, Waste_Recycle)
# Harvest and Market likely concurrent after loop, but Market Engage is regulatory/marketing so let's add edge from Waste Recycle
phase5.order.add_edge(Waste_Recycle, Market_Engage)

# Now combine all into a big partial order with dependencies

root = StrictPartialOrder(
    nodes=[phase1, phase2, phase3, growth_loop, phase5]
)

# phase1 before phase2 and phase3
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase1, phase3)

# phase2 and phase3 must finish before growth_loop
root.order.add_edge(phase2, growth_loop)
root.order.add_edge(phase3, growth_loop)

# growth_loop before final phase5
root.order.add_edge(growth_loop, phase5)