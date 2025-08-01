# Generated from: 139e241c-a75f-46f1-9954-e1e9737440f7.json
# Description: This process outlines the detailed steps required to establish a sustainable urban rooftop farm in a metropolitan environment. It involves evaluating structural integrity, selecting appropriate crops for limited space, integrating smart irrigation systems, ensuring compliance with local regulations, and setting up community engagement programs. The workflow includes sourcing environmentally friendly materials, installing modular planting beds, deploying IoT sensors for monitoring microclimates, and coordinating with city officials for necessary permits. Continuous assessment of plant health and yield optimization through data analytics is also integral, alongside organizing workshops to educate local residents on urban agriculture benefits. This atypical yet feasible business process blends construction, agriculture, technology, and community development in a unique urban context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
SiteSurvey = Transition(label='Site Survey')
LoadTest = Transition(label='Load Test')
CropSelect = Transition(label='Crop Select')
MaterialOrder = Transition(label='Material Order')
BedAssembly = Transition(label='Bed Assembly')
IrrigationSetup = Transition(label='Irrigation Setup')
SensorDeploy = Transition(label='Sensor Deploy')
PermitApply = Transition(label='Permit Apply')
DataSync = Transition(label='Data Sync')
HealthCheck = Transition(label='Health Check')
YieldAnalyze = Transition(label='Yield Analyze')
WasteManage = Transition(label='Waste Manage')
WorkshopPlan = Transition(label='Workshop Plan')
CommunityEngage = Transition(label='Community Engage')
FeedbackCollect = Transition(label='Feedback Collect')

# Construction and material phase partial order
construction = StrictPartialOrder(nodes=[
    MaterialOrder,
    BedAssembly,
    IrrigationSetup,
    SensorDeploy])
construction.order.add_edge(MaterialOrder, BedAssembly)
construction.order.add_edge(BedAssembly, IrrigationSetup)
construction.order.add_edge(IrrigationSetup, SensorDeploy)

# Initial assessment partial order
assessment = StrictPartialOrder(nodes=[SiteSurvey, LoadTest, CropSelect])
assessment.order.add_edge(SiteSurvey, LoadTest)
assessment.order.add_edge(LoadTest, CropSelect)

# Permit application branch (can run concurrently with construction)
permits_and_construction = StrictPartialOrder(nodes=[construction, PermitApply])

# Data and monitoring partial order
monitoring = StrictPartialOrder(nodes=[DataSync, HealthCheck, YieldAnalyze])
monitoring.order.add_edge(DataSync, HealthCheck)
monitoring.order.add_edge(HealthCheck, YieldAnalyze)

# Community engagement partial order
community = StrictPartialOrder(nodes=[WorkshopPlan, CommunityEngage, FeedbackCollect])
community.order.add_edge(WorkshopPlan, CommunityEngage)
community.order.add_edge(CommunityEngage, FeedbackCollect)

# Waste Management (no order dependency, concurrent with monitoring and community)
waste = WasteManage

# Combine monitoring, community, and waste concurrently
post_install_nodes = [monitoring, community, waste]

# Top-level concurrency of post-install phase (build list nodes)
from pm4py.objects.powl.obj import StrictPartialOrder

post_install = StrictPartialOrder(nodes=post_install_nodes)
# no order edges because these activities are independent concurrently

# Build the main process partial order
root = StrictPartialOrder(nodes=[
    assessment,
    permits_and_construction,
    post_install,
])

# Define order edges for the main flow
root.order.add_edge(assessment, permits_and_construction)
root.order.add_edge(permits_and_construction, post_install)