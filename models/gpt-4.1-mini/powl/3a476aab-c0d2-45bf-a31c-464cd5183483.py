# Generated from: 3a476aab-c0d2-45bf-a31c-464cd5183483.json
# Description: This process outlines the unconventional approach of establishing a sustainable urban rooftop farm on a high-rise building. It involves site assessment, structural analysis, soil preparation, microclimate optimization, planting, automated irrigation setup, pest control using integrated biological methods, crop monitoring via drones, community engagement for education, harvesting, yield analysis, and finally, distribution logistics tailored for urban markets. The process requires coordination among architects, agronomists, engineers, and local authorities to ensure compliance with safety and environmental standards while maximizing crop output and minimizing resource usage, making it a complex yet innovative business model for urban agriculture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Site_Assess = Transition(label='Site Assess')
Structural_Check = Transition(label='Structural Check')
Soil_Prep = Transition(label='Soil Prep')
Climate_Tune = Transition(label='Climate Tune')
Planting_Plan = Transition(label='Planting Plan')
Irrigation_Setup = Transition(label='Irrigation Setup')
Pest_Control = Transition(label='Pest Control')
Drone_Survey = Transition(label='Drone Survey')
Community_Meet = Transition(label='Community Meet')
Growth_Monitor = Transition(label='Growth Monitor')
Harvest_Crop = Transition(label='Harvest Crop')
Yield_Audit = Transition(label='Yield Audit')
Market_Link = Transition(label='Market Link')
Waste_Manage = Transition(label='Waste Manage')
Report_Review = Transition(label='Report Review')

# Partial Order representing the main linear flow:
# Site Assess -> Structural Check -> Soil Prep -> Climate Tune -> Planting Plan -> Irrigation Setup
# -> Pest Control -> Drone Survey -> Community Meet -> Growth Monitor -> Harvest Crop -> Yield Audit -> Market Link
# Then in parallel: Waste Manage and Report Review (last activities)
root = StrictPartialOrder(nodes=[
    Site_Assess, Structural_Check, Soil_Prep, Climate_Tune, Planting_Plan, Irrigation_Setup,
    Pest_Control, Drone_Survey, Community_Meet, Growth_Monitor, Harvest_Crop, Yield_Audit,
    Market_Link, Waste_Manage, Report_Review
])

root.order.add_edge(Site_Assess, Structural_Check)
root.order.add_edge(Structural_Check, Soil_Prep)
root.order.add_edge(Soil_Prep, Climate_Tune)
root.order.add_edge(Climate_Tune, Planting_Plan)
root.order.add_edge(Planting_Plan, Irrigation_Setup)
root.order.add_edge(Irrigation_Setup, Pest_Control)
root.order.add_edge(Pest_Control, Drone_Survey)
root.order.add_edge(Drone_Survey, Community_Meet)
root.order.add_edge(Community_Meet, Growth_Monitor)
root.order.add_edge(Growth_Monitor, Harvest_Crop)
root.order.add_edge(Harvest_Crop, Yield_Audit)
root.order.add_edge(Yield_Audit, Market_Link)

# Waste Manage and Report Review run in parallel after Market Link (no order edges from Market Link to them)
# So no edges added, just nodes included - concurrent with Market Link or after

# To better reflect distribution logistics (Market Link) then two concurrent end tasks (Waste Manage, Report Review)
root.order.add_edge(Market_Link, Waste_Manage)
root.order.add_edge(Market_Link, Report_Review)