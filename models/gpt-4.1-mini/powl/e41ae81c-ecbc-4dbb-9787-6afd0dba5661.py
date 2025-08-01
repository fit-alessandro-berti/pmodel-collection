# Generated from: e41ae81c-ecbc-4dbb-9787-6afd0dba5661.json
# Description: This process outlines the establishment of an urban vertical farming facility within a repurposed multi-story building. It involves site evaluation, structural modifications to support hydroponic systems, installation of climate control technologies, and integration of AI-driven monitoring tools. The procedure further includes sourcing organic seeds, setting up nutrient delivery systems, training staff on crop management, and establishing supply chain logistics tailored for fresh produce delivery in dense urban markets. Continuous optimization cycles are incorporated to maximize yield and sustainability while minimizing resource consumption and environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Site_Survey = Transition(label='Site Survey')
Structure_Reinforce = Transition(label='Structure Reinforce')
Hydroponic_Setup = Transition(label='Hydroponic Setup')
Climate_Install = Transition(label='Climate Install')
AI_Integration = Transition(label='AI Integration')
Seed_Sourcing = Transition(label='Seed Sourcing')
Nutrient_Prep = Transition(label='Nutrient Prep')
System_Testing = Transition(label='System Testing')
Staff_Training = Transition(label='Staff Training')
Crop_Planting = Transition(label='Crop Planting')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control = Transition(label='Pest Control')
Harvest_Schedule = Transition(label='Harvest Schedule')
Quality_Check = Transition(label='Quality Check')
Market_Dispatch = Transition(label='Market Dispatch')
Waste_Recycle = Transition(label='Waste Recycle')
Data_Analysis = Transition(label='Data Analysis')

skip = SilentTransition()

# Structural preparation partial order
prep_PO = StrictPartialOrder(nodes=[Site_Survey, Structure_Reinforce, Hydroponic_Setup, Climate_Install, AI_Integration])
prep_PO.order.add_edge(Site_Survey, Structure_Reinforce)
prep_PO.order.add_edge(Structure_Reinforce, Hydroponic_Setup)
prep_PO.order.add_edge(Hydroponic_Setup, Climate_Install)
prep_PO.order.add_edge(Climate_Install, AI_Integration)

# Supply chain preparation partial order
supply_PO = StrictPartialOrder(nodes=[Seed_Sourcing, Nutrient_Prep, System_Testing])
# These three can be done concurrently; no order edges

# Staff training before planting
training_PO = StrictPartialOrder(nodes=[Staff_Training, Crop_Planting])
training_PO.order.add_edge(Staff_Training, Crop_Planting)

# Growing cycle loop (Growth_Monitor, Pest_Control, Data_Analysis)
grow_loop_body = StrictPartialOrder(nodes=[Growth_Monitor, Pest_Control, Data_Analysis])
grow_loop_body.order.add_edge(Growth_Monitor, Pest_Control)
grow_loop_body.order.add_edge(Pest_Control, Data_Analysis)

grow_loop = OperatorPOWL(operator=Operator.LOOP, children=[grow_loop_body, skip])

# Harvest, quality check, dispatch, and waste recycle partial order
harvest_PO = StrictPartialOrder(
    nodes=[Harvest_Schedule, Quality_Check, Market_Dispatch, Waste_Recycle]
)
harvest_PO.order.add_edge(Harvest_Schedule, Quality_Check)
harvest_PO.order.add_edge(Quality_Check, Market_Dispatch)
# Waste recycle can be concurrent with Market Dispatch (no edge)
# Also no order edge from Quality_Check to Waste_Recycle to keep concurrency

# Combine staff training and planting with growing loop and harvesting
post_prep_PO = StrictPartialOrder(
    nodes=[training_PO, grow_loop, harvest_PO]
)
# training_PO --> grow_loop
post_prep_PO.order.add_edge(training_PO, grow_loop)
# grow_loop --> harvest_PO
post_prep_PO.order.add_edge(grow_loop, harvest_PO)

# Combine preparation, supply, and post-preparation
root = StrictPartialOrder(
    nodes=[prep_PO, supply_PO, post_prep_PO]
)
root.order.add_edge(prep_PO, supply_PO)
root.order.add_edge(supply_PO, post_prep_PO)