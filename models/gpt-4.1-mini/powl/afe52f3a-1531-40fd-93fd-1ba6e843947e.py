# Generated from: afe52f3a-1531-40fd-93fd-1ba6e843947e.json
# Description: This process outlines the integration of vertical farming systems within urban infrastructure, combining agricultural technology, supply chain logistics, and municipal regulations to produce fresh, sustainable crops in city environments. It involves site assessment, modular system installation, climate control calibration, automated nutrient delivery, crop monitoring using AI, waste recycling, energy optimization, community engagement, and real-time yield forecasting. The process ensures minimal environmental impact while maximizing productivity and urban space utilization, requiring collaboration between agronomists, engineers, city planners, and local stakeholders to create a resilient and scalable urban farming ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Permits_Check = Transition(label='Permits Check')
Module_Install = Transition(label='Module Install')
Climate_Setup = Transition(label='Climate Setup')
Nutrient_Flow = Transition(label='Nutrient Flow')
AI_Monitoring = Transition(label='AI Monitoring')
Pest_Control = Transition(label='Pest Control')
Waste_Cycle = Transition(label='Waste Cycle')
Energy_Audit = Transition(label='Energy Audit')
Data_Sync = Transition(label='Data Sync')
Yield_Forecast = Transition(label='Yield Forecast')
Community_Meet = Transition(label='Community Meet')
Logistics_Plan = Transition(label='Logistics Plan')
Harvest_Pack = Transition(label='Harvest Pack')

# Capturing core phases:
# Phase 1: Site assessment and design -> Site Survey -> Design Layout -> Permits Check
phase1 = StrictPartialOrder(nodes=[Site_Survey, Design_Layout, Permits_Check])
phase1.order.add_edge(Site_Survey, Design_Layout)
phase1.order.add_edge(Design_Layout, Permits_Check)

# Phase 2: Installation and calibration -> Module Install -> Climate Setup -> Nutrient Flow
phase2 = StrictPartialOrder(nodes=[Module_Install, Climate_Setup, Nutrient_Flow])
phase2.order.add_edge(Module_Install, Climate_Setup)
phase2.order.add_edge(Climate_Setup, Nutrient_Flow)

# Phase 3: Monitoring and control - AI Monitoring and Pest Control happen concurrently
monitoring = StrictPartialOrder(nodes=[AI_Monitoring, Pest_Control])

# Phase 4: Supportive tasks - Waste Cycle, Energy Audit, Data Sync happen concurrently
supportive_tasks = StrictPartialOrder(nodes=[Waste_Cycle, Energy_Audit, Data_Sync])

# Combine monitoring and supportive in parallel with partial order:
# Data Sync precedes Yield Forecast
yield_fcast_and_community = StrictPartialOrder(
    nodes=[Yield_Forecast, Community_Meet, Logistics_Plan, Harvest_Pack]
)
# Order: Yield Forecast must precede Harvest Pack
yield_fcast_and_community.order.add_edge(Yield_Forecast, Harvest_Pack)
# Logistics Plan and Community Meet happen before Harvest Pack and can be concurrent
yield_fcast_and_community.order.add_edge(Community_Meet, Harvest_Pack)
yield_fcast_and_community.order.add_edge(Logistics_Plan, Harvest_Pack)

# Data Sync precedes Yield Forecast
supportive_to_yield = StrictPartialOrder(nodes=[supportive_tasks, yield_fcast_and_community])
supportive_to_yield.order.add_edge(supportive_tasks, yield_fcast_and_community)

# Combine monitoring and supportive with yield_fcast_and_community partial order
monitor_and_support = StrictPartialOrder(nodes=[monitoring, supportive_tasks, yield_fcast_and_community])
monitor_and_support.order.add_edge(monitoring, yield_fcast_and_community)
monitor_and_support.order.add_edge(supportive_tasks, yield_fcast_and_community)

# Full pipeline ordering:
# phase1 > phase2 > monitor_and_support > Harvest Pack
full_process = StrictPartialOrder(
    nodes=[phase1, phase2, monitoring, supportive_tasks, yield_fcast_and_community]
)
full_process.order.add_edge(phase1, phase2)
full_process.order.add_edge(phase2, monitoring)
full_process.order.add_edge(phase2, supportive_tasks)
full_process.order.add_edge(monitoring, yield_fcast_and_community)
full_process.order.add_edge(supportive_tasks, yield_fcast_and_community)

# Finally Harvest Pack after all above
root = StrictPartialOrder(
    nodes=[phase1, phase2, monitoring, supportive_tasks, yield_fcast_and_community, Harvest_Pack]
)
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, monitoring)
root.order.add_edge(phase2, supportive_tasks)
root.order.add_edge(monitoring, yield_fcast_and_community)
root.order.add_edge(supportive_tasks, yield_fcast_and_community)
root.order.add_edge(yield_fcast_and_community, Harvest_Pack)