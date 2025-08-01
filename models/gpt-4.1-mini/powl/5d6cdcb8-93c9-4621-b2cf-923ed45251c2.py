# Generated from: 5d6cdcb8-93c9-4621-b2cf-923ed45251c2.json
# Description: This process outlines the complex steps required to launch an urban vertical farming operation within a repurposed multi-story building. It involves site assessment, regulatory compliance, advanced hydroponic system design, resource logistics, and community integration. The process ensures sustainable energy use, waste recycling, and real-time crop monitoring, incorporating AI-driven growth optimization and dynamic market distribution channels. Stakeholder engagement and adaptive risk management are critical throughout to balance environmental impact with economic viability in an urban context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Survey = Transition(label='Site Survey')
Zoning_Check = Transition(label='Zoning Check')
Permits_Obtain = Transition(label='Permits Obtain')
Hydro_Design = Transition(label='Hydro Design')
System_Build = Transition(label='System Build')
Seed_Selection = Transition(label='Seed Selection')
Nutrient_Prep = Transition(label='Nutrient Prep')
Energy_Setup = Transition(label='Energy Setup')
Waste_Plan = Transition(label='Waste Plan')
AI_Calibration = Transition(label='AI Calibration')
Crop_Planting = Transition(label='Crop Planting')
Growth_Monitor = Transition(label='Growth Monitor')
Market_Analysis = Transition(label='Market Analysis')
Logistics_Plan = Transition(label='Logistics Plan')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Risk_Review = Transition(label='Risk Review')
Community_Outreach = Transition(label='Community Outreach')

# Phase 1: Site and regulatory compliance
phase1 = StrictPartialOrder(nodes=[Site_Survey, Zoning_Check, Permits_Obtain])
phase1.order.add_edge(Site_Survey, Zoning_Check)
phase1.order.add_edge(Zoning_Check, Permits_Obtain)

# Phase 2: Design and build hydroponic system
phase2 = StrictPartialOrder(nodes=[Hydro_Design, System_Build])
phase2.order.add_edge(Hydro_Design, System_Build)

# Phase 3: Prepare resources in parallel: Seed, Nutrients, Energy, Waste Plan
prep_resources = StrictPartialOrder(nodes=[Seed_Selection, Nutrient_Prep, Energy_Setup, Waste_Plan])
# No order edges - fully concurrent

# Phase 4: Calibration and planting with monitoring loop
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Crop_Planting, Growth_Monitor]
)
# Loop means: Crop_Planting then either exit or Growth_Monitor then Crop_Planting again

calibration_and_planting = StrictPartialOrder(
    nodes=[AI_Calibration, monitor_loop]
)
calibration_and_planting.order.add_edge(AI_Calibration, monitor_loop)

# Phase 5: Market and logistics parallel
market_logistics = StrictPartialOrder(nodes=[Market_Analysis, Logistics_Plan])
# concurrent

# Phase 6: Stakeholders engagement and risk review, can be sequential or choices. Model as sequential:
stakeholder_risk = StrictPartialOrder(nodes=[Stakeholder_Meet, Risk_Review])
stakeholder_risk.order.add_edge(Stakeholder_Meet, Risk_Review)

# Phase 7: Community outreach concurrent with stakeholder_risk
community_and_stakeholder = StrictPartialOrder(
    nodes=[stakeholder_risk, Community_Outreach]
)
# no edges => concurrent

# Compose full order as partial order with phases ordered where logical
root = StrictPartialOrder(
    nodes=[phase1, phase2, prep_resources, calibration_and_planting,
           market_logistics, community_and_stakeholder]
)
root.order.add_edge(phase1, phase2)                 # design after compliance
root.order.add_edge(phase2, prep_resources)         # prepare resources after build
root.order.add_edge(prep_resources, calibration_and_planting)  # calibration and plant after prep
root.order.add_edge(calibration_and_planting, market_logistics) # market info after crops
root.order.add_edge(calibration_and_planting, community_and_stakeholder) # stakeholder runs parallel to market, but after planting
root.order.add_edge(market_logistics, community_and_stakeholder) # community/stakeholder last, after market/logistics

# root is assigned