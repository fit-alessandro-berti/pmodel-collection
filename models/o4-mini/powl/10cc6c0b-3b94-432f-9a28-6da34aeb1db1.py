# Generated from: 10cc6c0b-3b94-432f-9a28-6da34aeb1db1.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm within a repurposed industrial space. It begins with site analysis and environmental assessment, followed by modular structure design and procurement of specialized hydroponic systems. Subsequent activities include installation of climate control units, integration of IoT sensors for real-time monitoring, and calibration of lighting systems to optimize plant growth. The process also covers staff training on automated nutrient delivery, implementation of pest management protocols without chemicals, and setting up data analytics dashboards for yield prediction. Final stages focus on trial planting cycles, quality control checks, and establishing supply chain logistics to deliver fresh produce to local markets efficiently, ensuring sustainability and scalability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_analysis      = Transition(label='Site Analysis')
env_assessment     = Transition(label='Env Assessment')
structure_design   = Transition(label='Structure Design')
hydroponic_setup   = Transition(label='Hydroponic Setup')
climate_install    = Transition(label='Climate Install')
iot_integration    = Transition(label='IoT Integration')
lighting_calibrate = Transition(label='Lighting Calibrate')
staff_training     = Transition(label='Staff Training')
nutrient_delivery  = Transition(label='Nutrient Delivery')
pest_protocols     = Transition(label='Pest Protocols')
data_analytics     = Transition(label='Data Analytics')
trial_planting     = Transition(label='Trial Planting')
quality_control    = Transition(label='Quality Control')
supply_logistics   = Transition(label='Supply Logistics')
market_launch      = Transition(label='Market Launch')

# Build a strict partial order representing the sequential workflow
root = StrictPartialOrder(nodes=[
    site_analysis,
    env_assessment,
    structure_design,
    hydroponic_setup,
    climate_install,
    iot_integration,
    lighting_calibrate,
    staff_training,
    nutrient_delivery,
    pest_protocols,
    data_analytics,
    trial_planting,
    quality_control,
    supply_logistics,
    market_launch
])

# Add the sequential order edges
root.order.add_edge(site_analysis, env_assessment)
root.order.add_edge(env_assessment, structure_design)
root.order.add_edge(structure_design, hydroponic_setup)
root.order.add_edge(hydroponic_setup, climate_install)
root.order.add_edge(climate_install, iot_integration)
root.order.add_edge(iot_integration, lighting_calibrate)
root.order.add_edge(lighting_calibrate, staff_training)
root.order.add_edge(staff_training, nutrient_delivery)
root.order.add_edge(nutrient_delivery, pest_protocols)
root.order.add_edge(pest_protocols, data_analytics)
root.order.add_edge(data_analytics, trial_planting)
root.order.add_edge(trial_planting, quality_control)
root.order.add_edge(quality_control, supply_logistics)
root.order.add_edge(supply_logistics, market_launch)