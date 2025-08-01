# Generated from: 2a406831-7835-49aa-9612-e0de648d3e25.json
# Description: This process outlines the complex establishment of an urban vertical farm within a dense city environment. It involves site assessment, modular system design, environmental impact evaluation, securing permits, sourcing specialized hydroponic equipment, installing automated climate controls, integrating AI-driven nutrient delivery, recruiting skilled agronomists, conducting pilot crop trials, optimizing energy consumption, establishing local distribution channels, and implementing continuous monitoring for yield maximization and sustainability compliance. The goal is to create a scalable, high-efficiency farming solution that minimizes footprint while maximizing fresh produce output year-round in urban settings.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL Transitions
site_survey          = Transition(label='Site Survey')
system_design        = Transition(label='System Design')
impact_study         = Transition(label='Impact Study')
permit_filing        = Transition(label='Permit Filing')
equipment_sourcing   = Transition(label='Equipment Sourcing')
climate_setup        = Transition(label='Climate Setup')
ai_integration       = Transition(label='AI Integration')
staff_hiring         = Transition(label='Staff Hiring')
crop_testing         = Transition(label='Crop Testing')
energy_audit         = Transition(label='Energy Audit')
logistics_plan       = Transition(label='Logistics Plan')
yield_analysis       = Transition(label='Yield Analysis')
sustainability_check = Transition(label='Sustainability Check')
market_launch        = Transition(label='Market Launch')
feedback_loop        = Transition(label='Feedback Loop')

# Main process partial order
main_process = StrictPartialOrder(nodes=[
    site_survey, system_design, impact_study, permit_filing, equipment_sourcing,
    climate_setup, ai_integration, staff_hiring, crop_testing,
    energy_audit, logistics_plan, yield_analysis,
    sustainability_check, market_launch
])

# Site Survey feeds both System Design and Impact Study
main_process.order.add_edge(site_survey, system_design)
main_process.order.add_edge(site_survey, impact_study)

# Impact Study -> Permit Filing
main_process.order.add_edge(impact_study, permit_filing)
# System Design -> Equipment Sourcing
main_process.order.add_edge(system_design, equipment_sourcing)

# Permit Filing & Equipment Sourcing -> Climate Setup
main_process.order.add_edge(permit_filing, climate_setup)
main_process.order.add_edge(equipment_sourcing, climate_setup)

# Climate Setup & Equipment Sourcing -> AI Integration
main_process.order.add_edge(climate_setup, ai_integration)
main_process.order.add_edge(equipment_sourcing, ai_integration)

# AI Integration -> Staff Hiring -> Crop Testing
main_process.order.add_edge(ai_integration, staff_hiring)
main_process.order.add_edge(staff_hiring, crop_testing)

# Crop Testing -> Energy Audit, Logistics Plan, Yield Analysis (concurrent)
main_process.order.add_edge(crop_testing, energy_audit)
main_process.order.add_edge(crop_testing, logistics_plan)
main_process.order.add_edge(crop_testing, yield_analysis)

# Energy Audit, Logistics Plan, Yield Analysis -> Sustainability Check
main_process.order.add_edge(energy_audit, sustainability_check)
main_process.order.add_edge(logistics_plan, sustainability_check)
main_process.order.add_edge(yield_analysis, sustainability_check)

# Sustainability Check -> Market Launch
main_process.order.add_edge(sustainability_check, market_launch)

# Wrap the main process in a loop with a feedback loop transition
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[main_process, feedback_loop]
)