# Generated from: 6ed4d74a-84e0-40c9-9677-2fc225629373.json
# Description: This process outlines the complex steps involved in launching an urban rooftop farming initiative that integrates sustainable agriculture with smart city technology. It includes site assessment, regulatory compliance, sensor installation for microclimate monitoring, soil enhancement using biochar, seed selection tailored for urban environments, automated irrigation setup, pest management through integrated biological controls, community engagement for local support, harvesting logistics optimized for limited space, waste composting, data analysis for yield optimization, and continuous improvement cycles driven by sensor feedback. The goal is to create a self-sustaining, scalable urban farm that contributes to food security and environmental benefits while leveraging IoT and community involvement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Survey = Transition(label='Site Survey')
Permit_Review = Transition(label='Permit Review')
Sensor_Setup = Transition(label='Sensor Setup')
Soil_Testing = Transition(label='Soil Testing')
Biochar_Mix = Transition(label='Biochar Mix')
Seed_Selection = Transition(label='Seed Selection')
Irrigation_Install = Transition(label='Irrigation Install')
Pest_Control = Transition(label='Pest Control')
Community_Meet = Transition(label='Community Meet')
Planting_Phase = Transition(label='Planting Phase')
Growth_Monitor = Transition(label='Growth Monitor')
Harvest_Plan = Transition(label='Harvest Plan')
Waste_Compost = Transition(label='Waste Compost')
Data_Upload = Transition(label='Data Upload')
Yield_Analysis = Transition(label='Yield Analysis')
Feedback_Loop = Transition(label='Feedback Loop')

# Partial order for initial assessments:
# Site Survey --> Permit Review
# Soil Testing and Sensor Setup can be done concurrently after Permit Review
# Biochar Mix depends on Soil Testing
# Seed Selection depends on Biochar Mix
# Irrigation Install depends on Sensor Setup and Seed Selection
# Pest Control depends on Irrigation Install
# Community Meet runs in parallel with Pest Control

initial_assessment = StrictPartialOrder(
    nodes=[Site_Survey, Permit_Review, Sensor_Setup, Soil_Testing, Biochar_Mix, Seed_Selection, Irrigation_Install, Pest_Control, Community_Meet]
)
initial_assessment.order.add_edge(Site_Survey, Permit_Review)
initial_assessment.order.add_edge(Permit_Review, Soil_Testing)
initial_assessment.order.add_edge(Permit_Review, Sensor_Setup)
initial_assessment.order.add_edge(Soil_Testing, Biochar_Mix)
initial_assessment.order.add_edge(Biochar_Mix, Seed_Selection)
initial_assessment.order.add_edge(Sensor_Setup, Irrigation_Install)
initial_assessment.order.add_edge(Seed_Selection, Irrigation_Install)
initial_assessment.order.add_edge(Irrigation_Install, Pest_Control)
# Community Meet concurrent with Pest Control, no order edges needed.

# Partial order for planting and growth:
# Planting Phase starts after Seed Selection (also after Irrigation Install)
# Growth Monitor after Planting Phase
# Harvest Plan after Growth Monitor
planting_growth = StrictPartialOrder(
    nodes=[Planting_Phase, Growth_Monitor, Harvest_Plan]
)
# Both Seed Selection and Irrigation Install must complete before Planting Phase
planting_growth.order.add_edge(Planting_Phase, Growth_Monitor)  # Planting precedes growth monitoring
planting_growth.order.add_edge(Growth_Monitor, Harvest_Plan)

# We must link Seed_Selection and Irrigation_Install to Planting_Phase
# But these nodes are external to planting_growth,
# So create a PO combining initial_assessment and planting_growth, linking Seed_Selection & Irrigation_Install to Planting_Phase

# Partial order for post-harvest and analysis:
# Waste Compost starts after Harvest Plan
# Data Upload after Harvest Plan
# Yield Analysis after Data Upload
# Feedback Loop is a loop after Yield Analysis
post_harvest = StrictPartialOrder(
    nodes=[Waste_Compost, Data_Upload, Yield_Analysis, Feedback_Loop]
)
post_harvest.order.add_edge(Waste_Compost, Data_Upload)  # Waste Compost before Data Upload (we put this as a mild order, can be concurrent if desired)
post_harvest.order.add_edge(Data_Upload, Yield_Analysis)

# Define loop on Feedback Loop and Growth Monitor (monitoring and continuous improvement)
# Loop: Execute Growth Monitor + (Feedback Loop then Growth Monitor) repeatedly.
loop_monitor = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Growth_Monitor, Feedback_Loop]
)

# Replace Growth Monitor in planting_growth by loop_monitor to represent continuous cycles
# We'll rebuild planting_growth with Planting Phase --> loop_monitor --> Harvest Plan
planting_growth = StrictPartialOrder(
    nodes=[Planting_Phase, loop_monitor, Harvest_Plan]
)
planting_growth.order.add_edge(Planting_Phase, loop_monitor)
planting_growth.order.add_edge(loop_monitor, Harvest_Plan)

# Now combine initial_assessment, planting_growth and post_harvest in a single PO

root = StrictPartialOrder(
    nodes=[initial_assessment, planting_growth, post_harvest, Community_Meet, Pest_Control]
)

# Add edges to link subprocesses:
# Seed_Selection and Irrigation_Install are in initial_assessment; Planting_Phase in planting_growth
root.order.add_edge(initial_assessment, planting_growth)

# Pest_Control and Community_Meet are individual nodes also included in root
root.order.add_edge(initial_assessment, Pest_Control)
root.order.add_edge(initial_assessment, Community_Meet)

# Harvest Plan (in planting_growth) precedes Waste Compost & Data Upload (in post_harvest)
root.order.add_edge(planting_growth, post_harvest)