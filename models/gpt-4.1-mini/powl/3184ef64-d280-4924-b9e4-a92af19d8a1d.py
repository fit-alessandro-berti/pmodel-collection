# Generated from: 3184ef64-d280-4924-b9e4-a92af19d8a1d.json
# Description: This process outlines the complex operations involved in managing an urban vertical farming system that integrates automated hydroponics, climate control, and AI-driven nutrient optimization. It begins with seed selection tailored to urban environmental constraints, followed by precise germination monitoring using sensor arrays. Nutrient solution formulation adapts dynamically based on real-time plant growth data. Climate regulation adjusts humidity, temperature, and lighting to maximize photosynthesis efficiency. Periodic pest detection employs machine vision to identify and isolate affected zones. Harvesting is automated with robotic arms, while post-harvest sorting ensures quality consistency. Waste recycling converts organic remnants into bio-fertilizers, completing a sustainable loop. This atypical process requires coordination among IoT devices, AI analytics, and human oversight to maintain continuous production within limited urban spaces, addressing food security with minimal environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Seed_Selection = Transition(label='Seed Selection')
Germinate_Check = Transition(label='Germinate Check')
Nutrient_Mix = Transition(label='Nutrient Mix')
Growth_Monitor = Transition(label='Growth Monitor')
Climate_Adjust = Transition(label='Climate Adjust')
Light_Control = Transition(label='Light Control')
Humidity_Set = Transition(label='Humidity Set')
Pest_Detect = Transition(label='Pest Detect')
Zone_Isolation = Transition(label='Zone Isolation')
Robotic_Harvest = Transition(label='Robotic Harvest')
Quality_Sort = Transition(label='Quality Sort')
Waste_Collect = Transition(label='Waste Collect')
Bio_fertilize = Transition(label='Bio-fertilize')
Data_Sync = Transition(label='Data Sync')
System_Alert = Transition(label='System Alert')

# Build nuanced substructures:

# Climate regulation components run in parallel with internal order: Humidity_Set and Light_Control after Climate_Adjust
climate_PO = StrictPartialOrder(nodes=[Climate_Adjust, Humidity_Set, Light_Control])
climate_PO.order.add_edge(Climate_Adjust, Humidity_Set)
climate_PO.order.add_edge(Climate_Adjust, Light_Control)

# Pest detection followed by zone isolation
pest_PO = StrictPartialOrder(nodes=[Pest_Detect, Zone_Isolation])
pest_PO.order.add_edge(Pest_Detect, Zone_Isolation)

# Waste recycling loop: Waste_Collect -> Bio-fertilize, then option to loop back to Waste_Collect or exit
waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[Waste_Collect, Bio_fertilize])

# Growth monitoring influences nutrient mixing dynamically, so let's model Nutrient_Mix and Growth_Monitor as a partial order with Nutrient_Mix before Growth_Monitor
nutrient_growth_PO = StrictPartialOrder(nodes=[Nutrient_Mix, Growth_Monitor])
nutrient_growth_PO.order.add_edge(Nutrient_Mix, Growth_Monitor)

# Post-harvest steps: Robotic_Harvest then Quality_Sort
harvest_PO = StrictPartialOrder(nodes=[Robotic_Harvest, Quality_Sort])
harvest_PO.order.add_edge(Robotic_Harvest, Quality_Sort)

# Data_Sync and System_Alert run concurrently as final synchronizations/alerts with optional silent choice to alert
alert_xor = OperatorPOWL(operator=Operator.XOR, children=[System_Alert, SilentTransition()])

# Data_Sync before alert choice
data_alert_PO = StrictPartialOrder(nodes=[Data_Sync, alert_xor])
data_alert_PO.order.add_edge(Data_Sync, alert_xor)

# Compose all major steps in a partial order reflecting described process flow:

# Step 1: Seed Selection -> Germinate Check
sg_PO = StrictPartialOrder(nodes=[Seed_Selection, Germinate_Check])
sg_PO.order.add_edge(Seed_Selection, Germinate_Check)

# Step 2: After Germinate_Check comes Nutrient/Growth monitoring and Climate regulation in parallel:
# Because nutrient_growth_PO and climate_PO run in parallel and both depend on Germinate_Check
partial_after_germinate = StrictPartialOrder(nodes=[nutrient_growth_PO, climate_PO])
partial_after_germinate.order.add_edge(nutrient_growth_PO, climate_PO)  # We add no edge between them to keep concurrency

# Instead, we connect Germinate_Check --> both nutrient_growth_PO and climate_PO to denote activities start after it:
step2_PO = StrictPartialOrder(nodes=[Germinate_Check, nutrient_growth_PO, climate_PO])
step2_PO.order.add_edge(Germinate_Check, nutrient_growth_PO)
step2_PO.order.add_edge(Germinate_Check, climate_PO)

# Step 3: After these, Pest detection process occurs:
step3_PO = StrictPartialOrder(nodes=[step2_PO, pest_PO])
step3_PO.order.add_edge(step2_PO, pest_PO)

# Step 4: After pest handling, Harvest then Quality sort
step4_PO = StrictPartialOrder(nodes=[step3_PO, harvest_PO])
step4_PO.order.add_edge(step3_PO, harvest_PO)

# Step 5: Waste recycling loop starts after harvesting
step5_PO = StrictPartialOrder(nodes=[step4_PO, waste_loop])
step5_PO.order.add_edge(step4_PO, waste_loop)

# Step 6: Data sync and alerts after waste recycling
full_PO = StrictPartialOrder(
    nodes=[step5_PO, data_alert_PO]
)
full_PO.order.add_edge(step5_PO, data_alert_PO)

# Compose full initial sequence: Seed Selection -> Germinate Check -> parallel nutrient/climate -> pest detection -> harvesting -> waste loop -> final data sync/alert
# Because sg_PO represents just Seed->Germinate, we merge it into full_PO by connecting sg_PO -> nutrient/climate (which is in step2_PO)
# But step2_PO includes Germinate_Check so we just replace step2_PO with sg_PO + step2_PO minus Germinate_Check duplication

# To avoid confusion, just structurally embed sg_PO first:
root = StrictPartialOrder(
    nodes=[Seed_Selection, Germinate_Check, nutrient_growth_PO, climate_PO, pest_PO, harvest_PO, waste_loop, data_alert_PO]
)
root.order.add_edge(Seed_Selection, Germinate_Check)
root.order.add_edge(Germinate_Check, nutrient_growth_PO)
root.order.add_edge(Germinate_Check, climate_PO)
root.order.add_edge(nutrient_growth_PO, pest_PO)
root.order.add_edge(climate_PO, pest_PO)
root.order.add_edge(pest_PO, harvest_PO)
root.order.add_edge(harvest_PO, waste_loop)
root.order.add_edge(waste_loop, data_alert_PO)