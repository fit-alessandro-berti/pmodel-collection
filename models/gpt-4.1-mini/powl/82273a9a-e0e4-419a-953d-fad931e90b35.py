# Generated from: 82273a9a-e0e4-419a-953d-fad931e90b35.json
# Description: This process outlines the steps required to establish a sustainable urban rooftop farm on a commercial building. It involves initial structural assessments, environmental impact studies, selection of appropriate crops, installation of modular soil beds, irrigation systems, and solar-powered sensors. The process integrates community engagement for educational workshops, pest control using organic methods, and a logistics plan for weekly harvesting and distribution to local markets. Continuous monitoring and maintenance ensure optimal growth conditions, while data analytics optimize yield and resource usage, promoting a closed-loop urban agriculture ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
site_survey = Transition(label='Site Survey')
load_testing = Transition(label='Load Testing')
impact_study = Transition(label='Impact Study')
crop_selection = Transition(label='Crop Selection')
soil_prep = Transition(label='Soil Prep')
bed_install = Transition(label='Bed Install')
irrigation_setup = Transition(label='Irrigation Setup')
sensor_deploy = Transition(label='Sensor Deploy')
solar_config = Transition(label='Solar Config')
pest_control = Transition(label='Pest Control')
community_meet = Transition(label='Community Meet')
workshop_plan = Transition(label='Workshop Plan')
harvest_plan = Transition(label='Harvest Plan')
data_monitor = Transition(label='Data Monitor')
yield_analysis = Transition(label='Yield Analysis')
supply_route = Transition(label='Supply Route')
maintenance = Transition(label='Maintenance')

# Structural Assessment PO: Site Survey --> Load Testing
structural_assessment = StrictPartialOrder(nodes=[site_survey, load_testing])
structural_assessment.order.add_edge(site_survey, load_testing)

# Environmental Impact Study (independent concurrent with Structural Assessment end):
impact = impact_study  # single activity

# Crop selection and preparation partial order: Crop Selection --> Soil Prep --> Bed Install --> Irrigation Setup
crop_prep = StrictPartialOrder(
    nodes=[crop_selection, soil_prep, bed_install, irrigation_setup]
)
crop_prep.order.add_edge(crop_selection, soil_prep)
crop_prep.order.add_edge(soil_prep, bed_install)
crop_prep.order.add_edge(bed_install, irrigation_setup)

# Sensor deployment setup partial order: Sensor Deploy --> Solar Config
sensor_setup = StrictPartialOrder(nodes=[sensor_deploy, solar_config])
sensor_setup.order.add_edge(sensor_deploy, solar_config)

# Community engagement: Community Meet --> Workshop Plan
community_engagement = StrictPartialOrder(nodes=[community_meet, workshop_plan])
community_engagement.order.add_edge(community_meet, workshop_plan)

# Pest control: single activity
pest = pest_control

# Harvest and logistics plan partial order: Harvest Plan --> Supply Route
harvest_logistics = StrictPartialOrder(nodes=[harvest_plan, supply_route])
harvest_logistics.order.add_edge(harvest_plan, supply_route)

# Monitoring & maintenance loop:
# Loop body: Data Monitor --> Yield Analysis
monitoring_body = StrictPartialOrder(nodes=[data_monitor, yield_analysis])
monitoring_body.order.add_edge(data_monitor, yield_analysis)

# Loop: * (monitoring_body, Maintenance)
monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitoring_body, maintenance])

# Now combine all main branches in one partial order:
# Structural assessment and impact study run concurrently start --> then crop prep and sensor setup run concurrently -->
# then community engagement and pest control concurrent -->
# then harvest/logistics -->
# then monitoring loop

# To represent concurrency, they are nodes without order edges between them
# But to reflect the process flow, structure as partial order connecting main phases

# Define phase composites:
# Phase 1: structural_assessment and impact study concurrent 
phase1 = StrictPartialOrder(nodes=[structural_assessment, impact])
# No order edges: concurrent

# Phase 2: crop_prep and sensor_setup concurrent
phase2 = StrictPartialOrder(nodes=[crop_prep, sensor_setup])
# No order edges: concurrent

# Phase 3: community_engagement and pest_control concurrent
phase3 = StrictPartialOrder(nodes=[community_engagement, pest])
# No order edges: concurrent

# Create overall process as StrictPartialOrder with these phases as nodes
root = StrictPartialOrder(
    nodes=[phase1, phase2, phase3, harvest_logistics, monitoring_loop]
)

# Add order edges between phases to reflect sequence:
# phase1 --> phase2 --> phase3 --> harvest_logistics --> monitoring_loop
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, phase3)
root.order.add_edge(phase3, harvest_logistics)
root.order.add_edge(harvest_logistics, monitoring_loop)