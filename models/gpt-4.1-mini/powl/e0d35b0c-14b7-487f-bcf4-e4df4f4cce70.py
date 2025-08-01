# Generated from: e0d35b0c-14b7-487f-bcf4-e4df4f4cce70.json
# Description: This process outlines the establishment of a sustainable urban rooftop farm, integrating advanced hydroponic technology with local community engagement. It begins with site analysis and structural assessment to ensure safety and viability. Subsequent steps include resource sourcing, installation of modular grow systems, and environmental control setup such as lighting and irrigation. Parallel activities involve stakeholder coordination, training of local volunteers, and compliance with urban agricultural regulations. The process concludes with iterative crop monitoring, data collection for yield optimization, and community harvest events to promote urban food resilience and social cohesion.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as labeled transitions
Site_Survey = Transition(label='Site Survey')
Structural_Check = Transition(label='Structural Check')
Resource_Sourcing = Transition(label='Resource Sourcing')
System_Install = Transition(label='System Install')
Lighting_Setup = Transition(label='Lighting Setup')
Irrigation_Setup = Transition(label='Irrigation Setup')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Volunteer_Train = Transition(label='Volunteer Train')
Regulation_Review = Transition(label='Regulation Review')
Crop_Selection = Transition(label='Crop Selection')
Planting_Phase = Transition(label='Planting Phase')
Climate_Control = Transition(label='Climate Control')
Growth_Monitor = Transition(label='Growth Monitor')
Data_Logging = Transition(label='Data Logging')
Harvest_Event = Transition(label='Harvest Event')
Waste_Manage = Transition(label='Waste Manage')
Feedback_Collect = Transition(label='Feedback Collect')

# Step 1: Site Survey --> Structural Check
site_struct_PO = StrictPartialOrder(nodes=[Site_Survey, Structural_Check])
site_struct_PO.order.add_edge(Site_Survey, Structural_Check)

# Step 2: Resource Sourcing --> System Install --> (Lighting Setup & Irrigation Setup in parallel)
lighting_irrigation_PO = StrictPartialOrder(
    nodes=[Lighting_Setup, Irrigation_Setup],
    # no order edges = concurrent
)

res_sys_PO = StrictPartialOrder(nodes=[Resource_Sourcing, System_Install, lighting_irrigation_PO])
res_sys_PO.order.add_edge(Resource_Sourcing, System_Install)
res_sys_PO.order.add_edge(System_Install, lighting_irrigation_PO)

# Step 3: Parallel activities: Stakeholder Meet, Volunteer Train, Regulation Review
stakeholder_parallel_PO = StrictPartialOrder(
    nodes=[Stakeholder_Meet, Volunteer_Train, Regulation_Review]
    # all concurrent, no edges
)

# Step 4: Crop Selection --> Planting Phase --> Climate Control
crop_plant_PO = StrictPartialOrder(nodes=[Crop_Selection, Planting_Phase, Climate_Control])
crop_plant_PO.order.add_edge(Crop_Selection, Planting_Phase)
crop_plant_PO.order.add_edge(Planting_Phase, Climate_Control)

# Step 5: Loop of Growth Monitor --> Data Logging --> Harvest Event --> Waste Manage --> Feedback Collect
# Model iterative crop monitoring and data collection followed by harvest and feedback;
# The loop is: execute Growth Monitor (A), then choose to exit or Waste Manage + Feedback Collect (B) then Growth Monitor (A) again.
# But the description lists Data Logging and Harvest Event as continuous steps before Waste and Feedback.
# So A = Growth Monitor ; B = Data Logging --> Harvest Event --> Waste Manage --> Feedback Collect

data_harvest_PO = StrictPartialOrder(
    nodes=[Data_Logging, Harvest_Event, Waste_Manage, Feedback_Collect]
)
data_harvest_PO.order.add_edge(Data_Logging, Harvest_Event)
data_harvest_PO.order.add_edge(Harvest_Event, Waste_Manage)
data_harvest_PO.order.add_edge(Waste_Manage, Feedback_Collect)

loop_body_PO = StrictPartialOrder(
    nodes=[Growth_Monitor, data_harvest_PO]
)
loop_body_PO.order.add_edge(Growth_Monitor, data_harvest_PO)

loop = OperatorPOWL(operator=Operator.LOOP, children=[Growth_Monitor, data_harvest_PO])

# Step 6: Combine Crop -> Planting -> Climate Control with the loop on monitoring etc.
crop_monitor_PO = StrictPartialOrder(nodes=[crop_plant_PO, loop])
crop_monitor_PO.order.add_edge(crop_plant_PO, loop)

# Step 7: Partial order between Installation steps (res_sys_PO) and stakeholder parallel activities
# Installation finishes before stakeholder meet/training/regulation review start? The description suggests these three run in parallel.
# But they seem parallel to installation step, so model installation and stakeholder activities as concurrent with no order edges.

# Actually, the description says installation (resource sourcing, system install, lighting, irrigation) happens after site survey and structural check,
# and parallel activities involve stakeholder meet, volunteer train and regulation review.
# So after site_struct_PO ends, installation and those parallel activities start concurrently.

# So create a PO including:
# nodes = [res_sys_PO, stakeholder_parallel_PO]
# no order edges between them => concurrent

install_stakeholder_PO = StrictPartialOrder(
    nodes=[res_sys_PO, stakeholder_parallel_PO]
    # no edges = concurrent
)

# Step 8: Full ordering:
# site_struct_PO --> (installation and stakeholder parallel) running concurrently
# then --> crop_monitor_PO (crop selection onwards)

root = StrictPartialOrder(
    nodes=[site_struct_PO, install_stakeholder_PO, crop_monitor_PO]
)
root.order.add_edge(site_struct_PO, install_stakeholder_PO)
root.order.add_edge(install_stakeholder_PO, crop_monitor_PO)