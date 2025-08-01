# Generated from: bb9e7015-f30a-471a-96f7-d79acb03ce3a.json
# Description: This process involves the comprehensive management of urban beekeeping operations, integrating hive maintenance, environmental monitoring, community engagement, and honey production optimization. Activities include assessing local flora, installing smart sensors for hive health, coordinating with city authorities for permits, conducting pest control using eco-friendly methods, harvesting honey with quality checks, and organizing educational workshops for local residents. The process ensures sustainability by tracking seasonal changes, analyzing pollen diversity, and implementing adaptive hive designs to maximize yield while minimizing urban impact. Additionally, it incorporates data reporting and collaboration with research institutions to contribute to broader ecological studies.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transition objects
Flora_Survey = Transition(label='Flora Survey')
Permit_Request = Transition(label='Permit Request')
Hive_Setup = Transition(label='Hive Setup')
Sensor_Install = Transition(label='Sensor Install')
Health_Check = Transition(label='Health Check')
Pest_Control = Transition(label='Pest Control')
Honey_Harvest = Transition(label='Honey Harvest')
Quality_Test = Transition(label='Quality Test')
Data_Upload = Transition(label='Data Upload')
Community_Meet = Transition(label='Community Meet')
Workshop_Plan = Transition(label='Workshop Plan')
Seasonal_Audit = Transition(label='Seasonal Audit')
Pollen_Analyze = Transition(label='Pollen Analyze')
Design_Update = Transition(label='Design Update')
Report_Compile = Transition(label='Report Compile')
Research_Link = Transition(label='Research Link')

# Let's model the process in logical blocks and partial orders

# 1. Initial assessment: Flora Survey then Permit Request
initial_assessment = StrictPartialOrder(nodes=[Flora_Survey, Permit_Request])
initial_assessment.order.add_edge(Flora_Survey, Permit_Request)

# 2. Hive setup and sensor install are sequential
setup = StrictPartialOrder(nodes=[Hive_Setup, Sensor_Install])
setup.order.add_edge(Hive_Setup, Sensor_Install)

# 3. Health check and pest control can be concurrent but both after sensor install
health_pest = StrictPartialOrder(nodes=[Health_Check, Pest_Control])
# no order between Health_Check and Pest_Control (concurrent)

# 4. Honey Harvest and Quality Test sequential
harvest_quality = StrictPartialOrder(nodes=[Honey_Harvest, Quality_Test])
harvest_quality.order.add_edge(Honey_Harvest, Quality_Test)

# 5. Data Upload follows Quality Test
data_upload_phase = StrictPartialOrder(nodes=[Quality_Test, Data_Upload])
data_upload_phase.order.add_edge(Quality_Test, Data_Upload)

# 6. Community engagement: Community Meet and Workshop Plan concurrent
community_engagement = StrictPartialOrder(nodes=[Community_Meet, Workshop_Plan])
# no order between Community_Meet and Workshop_Plan

# 7. Sustainability tracking loop:
# Loop body: Seasonal Audit then Pollen Analyze then Design Update
# Loop condition branch allows exit or re-execution of body
sustainability_body = StrictPartialOrder(nodes=[Seasonal_Audit, Pollen_Analyze, Design_Update])
sustainability_body.order.add_edge(Seasonal_Audit, Pollen_Analyze)
sustainability_body.order.add_edge(Pollen_Analyze, Design_Update)

sustainability_loop = OperatorPOWL(operator=Operator.LOOP, children=[sustainability_body, SilentTransition()])

# Alternative interpretation:
# The loop children are (A,B) 
# * (A, B): execute A then choose to exit or execute B then A again
# So B is done before repeating A
# Let's set B as a silent transition to represent exit or no additional task between iterations.
# The loop as sustainability_body for A and tau for B could also be done,
# but the process description suggests the loop involves repeating these sustainability steps,
# so the simplest is a loop with body=sustainability_body and nothing else.

# 8. Reporting and research collaboration sequential
reporting = StrictPartialOrder(nodes=[Report_Compile, Research_Link])
reporting.order.add_edge(Report_Compile, Research_Link)

# Now we define the top-level partial order connecting these blocks:

# Let's think about dependencies:
# Initial assessment must precede setup
# Setup precedes health & pest
# Health & pest precede harvest & quality
# Harvest & quality precede data upload phase (Quality test already inside)
# Data upload precedes community engagement and sustainability loop and reporting
# Community engagement can be concurrent with sustainability and reporting, but all after data upload
# Reporting after sustainability loop maybe? The text says "Additionally, it incorporates data reporting and collaboration..."
# We'll consider community engagement, sustainability loop, and reporting concurrent after data upload.

# Note: Quality test and data upload modeled separately for clarity but Quality test already in harvest_quality,
# so data_upload_phase re-contains Quality_Test - this duplication in nodes is legal if referring to same instance, but better to unify

# To unify, we update to remove Quality_Test from data_upload_phase and add edge from harvest_quality to data_upload_phase

# Correction:

# Since Quality_Test is already in harvest_quality, data_upload_phase nodes = [Data_Upload]
data_upload = Transition(label='Data Upload')  # reacquire instance for correct modelling

# Redefine previous data_upload phase with only Data_Upload and dependency on Quality_Test
data_upload_phase = StrictPartialOrder(nodes=[Data_Upload])
# order to be added from Quality_Test outside this PO

# Final combined partial order top-level nodes:

root = StrictPartialOrder(nodes=[
    initial_assessment,
    setup,
    health_pest,
    harvest_quality,
    data_upload_phase,
    community_engagement,
    sustainability_loop,
    reporting
])

# Add edges to represent dependencies between these blocks

# initial_assessment -> setup
root.order.add_edge(initial_assessment, setup)

# setup -> health_pest
root.order.add_edge(setup, health_pest)

# health_pest -> harvest_quality
root.order.add_edge(health_pest, harvest_quality)

# harvest_quality -> data_upload_phase
root.order.add_edge(harvest_quality, data_upload_phase)

# data_upload_phase -> community_engagement
root.order.add_edge(data_upload_phase, community_engagement)

# data_upload_phase -> sustainability_loop
root.order.add_edge(data_upload_phase, sustainability_loop)

# data_upload_phase -> reporting
root.order.add_edge(data_upload_phase, reporting)

# The concurrency between community_engagement, sustainability_loop, reporting is represented by lack of edges between them

# Also, Quality_Test is inside harvest_quality, so no need to connect it separately to data_upload_phase, already done top level from harvest_quality

# Final model is 'root'