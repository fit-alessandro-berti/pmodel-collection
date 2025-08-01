# Generated from: 139e241c-a75f-46f1-9954-e1e9737440f7.json
# Description: This process outlines the detailed steps required to establish a sustainable urban rooftop farm in a metropolitan environment. It involves evaluating structural integrity, selecting appropriate crops for limited space, integrating smart irrigation systems, ensuring compliance with local regulations, and setting up community engagement programs. The workflow includes sourcing environmentally friendly materials, installing modular planting beds, deploying IoT sensors for monitoring microclimates, and coordinating with city officials for necessary permits. Continuous assessment of plant health and yield optimization through data analytics is also integral, alongside organizing workshops to educate local residents on urban agriculture benefits. This atypical yet feasible business process blends construction, agriculture, technology, and community development in a unique urban context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey     = Transition(label='Site Survey')
load_test       = Transition(label='Load Test')
crop_select     = Transition(label='Crop Select')
material_order  = Transition(label='Material Order')
permit_apply    = Transition(label='Permit Apply')
bed_assembly    = Transition(label='Bed Assembly')
irrigation_setup= Transition(label='Irrigation Setup')
sensor_deploy   = Transition(label='Sensor Deploy')
data_sync       = Transition(label='Data Sync')
health_check    = Transition(label='Health Check')
yield_analyze   = Transition(label='Yield Analyze')
waste_manage    = Transition(label='Waste Manage')
workshop_plan   = Transition(label='Workshop Plan')
community_engage= Transition(label='Community Engage')
feedback_collect= Transition(label='Feedback Collect')

# Continuous assessment loop: do Data Sync, then repeatedly do (Health Check -> Yield Analyze -> Waste Manage)
assessment_body = StrictPartialOrder(nodes=[health_check, yield_analyze, waste_manage])
assessment_body.order.add_edge(health_check, yield_analyze)
assessment_body.order.add_edge(yield_analyze, waste_manage)

continuous_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[data_sync, assessment_body]
)

# Community engagement sequence: Workshop Plan -> Community Engage -> Feedback Collect
community_seq = StrictPartialOrder(
    nodes=[workshop_plan, community_engage, feedback_collect]
)
community_seq.order.add_edge(workshop_plan, community_engage)
community_seq.order.add_edge(community_engage, feedback_collect)

# Build the overall POWL model
root = StrictPartialOrder(nodes=[
    site_survey, load_test,
    crop_select, material_order, permit_apply,
    bed_assembly, irrigation_setup, sensor_deploy,
    continuous_loop, community_seq
])

# Structural integrity evaluation
root.order.add_edge(site_survey, load_test)

# Crop selection and material ordering after load test
root.order.add_edge(load_test, crop_select)
root.order.add_edge(crop_select, material_order)

# Permit application can run in parallel after structural tests
root.order.add_edge(load_test, permit_apply)

# Assembly and installation steps
root.order.add_edge(material_order, bed_assembly)
root.order.add_edge(permit_apply, bed_assembly)
root.order.add_edge(bed_assembly, irrigation_setup)
root.order.add_edge(irrigation_setup, sensor_deploy)

# After installation, branch into continuous assessment and community engagement
root.order.add_edge(sensor_deploy, continuous_loop)
root.order.add_edge(sensor_deploy, community_seq)