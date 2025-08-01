# Generated from: b4734f32-70a6-4050-8903-a88325ecaeb2.json
# Description: This process involves the planning, setup, and operational launch of an urban rooftop farming initiative in a densely populated city. It includes site assessment, structural analysis, resource procurement, soil testing, microclimate evaluation, installation of irrigation and lighting systems, selection of crops, community engagement, and finally, the first planting and ongoing monitoring phases. The process is complex due to the constraints of urban infrastructure, regulatory compliance, sustainability goals, and integration with local community programs to ensure long-term viability and social impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Site_Survey = Transition(label='Site Survey')
Load_Analysis = Transition(label='Load Analysis')
Permit_Request = Transition(label='Permit Request')
Soil_Sampling = Transition(label='Soil Sampling')
Microclimate_Map = Transition(label='Microclimate Map')
System_Design = Transition(label='System Design')
Irrigation_Setup = Transition(label='Irrigation Setup')
Lighting_Install = Transition(label='Lighting Install')
Crop_Selection = Transition(label='Crop Selection')
Supplier_Sourcing = Transition(label='Supplier Sourcing')
Community_Meet = Transition(label='Community Meet')
Planting_Day = Transition(label='Planting Day')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control = Transition(label='Pest Control')
Harvest_Plan = Transition(label='Harvest Plan')
Waste_Manage = Transition(label='Waste Manage')
Feedback_Loop = Transition(label='Feedback Loop')

# Loop for ongoing monitoring phases including Growth Monitoring, Pest Control, Harvest Planning, Waste Management, Feedback Loop
# Loop structure: execute Growth_Monitor, then choose exit or execute the sequence (Pest Control -> Harvest Plan -> Waste Manage -> Feedback Loop) then Growth_Monitor again
monitoring_subseq = StrictPartialOrder(nodes=[Pest_Control, Harvest_Plan, Waste_Manage, Feedback_Loop])
monitoring_subseq.order.add_edge(Pest_Control, Harvest_Plan)
monitoring_subseq.order.add_edge(Harvest_Plan, Waste_Manage)
monitoring_subseq.order.add_edge(Waste_Manage, Feedback_Loop)

monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[Growth_Monitor, monitoring_subseq])

# Partial order for site assessment and regulatory compliance:
# Site Survey -> Load Analysis -> Permit Request (sequential)
site_assessment = StrictPartialOrder(nodes=[Site_Survey, Load_Analysis, Permit_Request])
site_assessment.order.add_edge(Site_Survey, Load_Analysis)
site_assessment.order.add_edge(Load_Analysis, Permit_Request)

# Partial order for environmental testing and system design:
# Soil Sampling and Microclimate Map concurrent, both precede System Design
env_testing = StrictPartialOrder(nodes=[Soil_Sampling, Microclimate_Map, System_Design])
env_testing.order.add_edge(Soil_Sampling, System_Design)
env_testing.order.add_edge(Microclimate_Map, System_Design)

# Partial order for setup activities after system design and supplier sourcing:
# Supplier Sourcing and System Design must complete before Irrigation Setup, Lighting Install, Crop Selection (these three concurrent)
setup_parallel = StrictPartialOrder(nodes=[Supplier_Sourcing, System_Design, Irrigation_Setup, Lighting_Install, Crop_Selection])
setup_parallel.order.add_edge(Supplier_Sourcing, Irrigation_Setup)
setup_parallel.order.add_edge(Supplier_Sourcing, Lighting_Install)
setup_parallel.order.add_edge(Supplier_Sourcing, Crop_Selection)
setup_parallel.order.add_edge(System_Design, Irrigation_Setup)
setup_parallel.order.add_edge(System_Design, Lighting_Install)
setup_parallel.order.add_edge(System_Design, Crop_Selection)

# Community meeting happens after setup activities complete (all three)
community_meet = Community_Meet

# After community meeting, Planting Day occurs
planting_day = Planting_Day

# Combine all in sequence as a partial order with dependencies:
root = StrictPartialOrder(nodes=[
    site_assessment,
    env_testing,
    setup_parallel,
    community_meet,
    planting_day,
    monitor_loop
])

# Add edges to establish order among higher level nodes:
root.order.add_edge(site_assessment, env_testing)
root.order.add_edge(env_testing, setup_parallel)
root.order.add_edge(setup_parallel, community_meet)
root.order.add_edge(community_meet, planting_day)
root.order.add_edge(planting_day, monitor_loop)