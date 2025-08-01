# Generated from: 5d6cdcb8-93c9-4621-b2cf-923ed45251c2.json
# Description: This process outlines the complex steps required to launch an urban vertical farming operation within a repurposed multi-story building. It involves site assessment, regulatory compliance, advanced hydroponic system design, resource logistics, and community integration. The process ensures sustainable energy use, waste recycling, and real-time crop monitoring, incorporating AI-driven growth optimization and dynamic market distribution channels. Stakeholder engagement and adaptive risk management are critical throughout to balance environmental impact with economic viability in an urban context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
site_survey       = Transition(label='Site Survey')
zoning_check      = Transition(label='Zoning Check')
permits_obtain    = Transition(label='Permits Obtain')
hydro_design      = Transition(label='Hydro Design')
system_build      = Transition(label='System Build')

seed_selection    = Transition(label='Seed Selection')
nutrient_prep     = Transition(label='Nutrient Prep')
energy_setup      = Transition(label='Energy Setup')
waste_plan        = Transition(label='Waste Plan')
logistics_plan    = Transition(label='Logistics Plan')

market_analysis   = Transition(label='Market Analysis')

stakeholder_meet  = Transition(label='Stakeholder Meet')
community_outreach= Transition(label='Community Outreach')

crop_planting     = Transition(label='Crop Planting')
growth_monitor    = Transition(label='Growth Monitor')
ai_calibration    = Transition(label='AI Calibration')

risk_review       = Transition(label='Risk Review')

# 1. Technical setup: Site Survey -> Zoning Check -> Permits Obtain -> Hydro Design -> System Build
tech_setup = StrictPartialOrder(nodes=[
    site_survey, zoning_check, permits_obtain, hydro_design, system_build
])
tech_setup.order.add_edge(site_survey, zoning_check)
tech_setup.order.add_edge(zoning_check, permits_obtain)
tech_setup.order.add_edge(permits_obtain, hydro_design)
tech_setup.order.add_edge(hydro_design, system_build)

# 2. Resource & logistics preparation (can happen in parallel)
resource_logistics = StrictPartialOrder(nodes=[
    seed_selection, nutrient_prep, energy_setup, waste_plan, logistics_plan
])
# no internal edges => all four can proceed concurrently

# 3. Market analysis (follows resource & logistics)
market = StrictPartialOrder(nodes=[market_analysis])
# no internal edges

# 4. Stakeholder engagement sequence
stakeholder_seq = StrictPartialOrder(nodes=[
    stakeholder_meet, community_outreach
])
stakeholder_seq.order.add_edge(stakeholder_meet, community_outreach)

# 5. Monitoring & optimization loop:
#    A = Plant -> Monitor -> AI Calibrate
#    B = Risk Review
monitor_body = StrictPartialOrder(nodes=[
    crop_planting, growth_monitor, ai_calibration
])
monitor_body.order.add_edge(crop_planting, growth_monitor)
monitor_body.order.add_edge(growth_monitor, ai_calibration)

monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor_body, risk_review]
)

# 6. Compose the overall process partial order
root = StrictPartialOrder(nodes=[
    tech_setup,
    resource_logistics,
    market,
    stakeholder_seq,
    monitor_loop
])
# Enforce the high-level ordering
root.order.add_edge(tech_setup, resource_logistics)
root.order.add_edge(resource_logistics, market)
root.order.add_edge(market, stakeholder_seq)
root.order.add_edge(stakeholder_seq, monitor_loop)