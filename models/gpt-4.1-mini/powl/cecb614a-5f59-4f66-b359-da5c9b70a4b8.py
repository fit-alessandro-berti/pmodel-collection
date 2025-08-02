# Generated from: cecb614a-5f59-4f66-b359-da5c9b70a4b8.json
# Description: This process outlines the establishment of an urban rooftop farm on commercial buildings, integrating environmental assessments, resource logistics, and community engagement. It involves evaluating structural integrity, selecting crop varieties suited for microclimates, installing irrigation systems, and coordinating with local authorities for compliance. Continuous monitoring of soil health and pest control is combined with marketing strategies to promote farm-to-table initiatives. The process also includes training sessions for staff and residents, waste recycling protocols, and seasonal harvest planning to maximize yield while ensuring sustainability and social impact within densely populated urban areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Survey = Transition(label='Site Survey')
Load_Testing = Transition(label='Load Testing')
Crop_Selection = Transition(label='Crop Selection')
Soil_Prep = Transition(label='Soil Prep')
Irrigation_Setup = Transition(label='Irrigation Setup')
Permits_Acquire = Transition(label='Permits Acquire')
Supplier_Outreach = Transition(label='Supplier Outreach')
Planting_Seedlings = Transition(label='Planting Seedlings')
Pest_Monitoring = Transition(label='Pest Monitoring')
Nutrient_Testing = Transition(label='Nutrient Testing')
Waste_Sorting = Transition(label='Waste Sorting')
Staff_Training = Transition(label='Staff Training')
Community_Meet = Transition(label='Community Meet')
Harvest_Planning = Transition(label='Harvest Planning')
Market_Launch = Transition(label='Market Launch')
Yield_Tracking = Transition(label='Yield Tracking')

# Phase 1: Evaluate structural integrity
# Site Survey then Load Testing
phase1 = StrictPartialOrder(nodes=[Site_Survey, Load_Testing])
phase1.order.add_edge(Site_Survey, Load_Testing)

# Phase 2: Crop variety selection suited for microclimates
# Crop Selection concurrent with Soil Prep and Supplier Outreach
phase2 = StrictPartialOrder(nodes=[Crop_Selection, Soil_Prep, Supplier_Outreach])

# Phase 3: Permits Acquire and Irrigation Setup
phase3 = StrictPartialOrder(nodes=[Permits_Acquire, Irrigation_Setup])
# Permits Acquire before Irrigation Setup
phase3.order.add_edge(Permits_Acquire, Irrigation_Setup)

# Phase 4: Planting Seedlings depends on Soil Prep and Irrigation Setup
phase4 = StrictPartialOrder(nodes=[Soil_Prep, Irrigation_Setup, Planting_Seedlings])
phase4.order.add_edge(Soil_Prep, Planting_Seedlings)
phase4.order.add_edge(Irrigation_Setup, Planting_Seedlings)

# Phase 5: Pest Monitoring and Nutrient Testing (continuous monitoring)
# Model loop: monitoring cycle = Pest Monitoring then Nutrient Testing, repeated
monitor_cycle = OperatorPOWL(operator=Operator.LOOP, children=[Pest_Monitoring, Nutrient_Testing])

# Phase 6: Waste sorting and Staff Training and Community Meet
# These can be concurrent, but Staff Training and Community Meet likely after Pest Monitoring starts
# We assume Staff Training can start concurrently with Waste Sorting and Community Meet after Planting_Seedlings
phase6 = StrictPartialOrder(nodes=[Waste_Sorting, Staff_Training, Community_Meet])

# Phase 7: Harvest Planning after Planting Seedlings
# Harvest Planning before Market Launch
# Yield Tracking after Market Launch
harvest_and_market = StrictPartialOrder(nodes=[Harvest_Planning, Market_Launch, Yield_Tracking])
harvest_and_market.order.add_edge(Harvest_Planning, Market_Launch)
harvest_and_market.order.add_edge(Market_Launch, Yield_Tracking)

# Now combine all phases with related ordering based on natural flow

# phase1 --> phase2 and phase3 (after structural integrity, select crops and acquire permits/supplier outreach)
# phase2 and phase3 --> phase4 (after soil prep, irrigation, and crop selection, plant seedlings)
# phase4 --> phase5 (start monitoring after planting)
# phase4 --> phase6 (start training, waste, community after planting)
# phase5 and phase6 --> harvest_and_market (harvest and marketing after monitoring + community/training)

# Start defining top-level nodes and edges

root = StrictPartialOrder(
    nodes=[phase1, phase2, phase3, phase4, monitor_cycle, phase6, harvest_and_market]
)

# phase1 --> phase2 & phase3
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase1, phase3)

# phase2 & phase3 --> phase4
root.order.add_edge(phase2, phase4)
root.order.add_edge(phase3, phase4)

# phase4 --> monitor_cycle and phase6
root.order.add_edge(phase4, monitor_cycle)
root.order.add_edge(phase4, phase6)

# monitor_cycle & phase6 --> harvest_and_market
root.order.add_edge(monitor_cycle, harvest_and_market)
root.order.add_edge(phase6, harvest_and_market)