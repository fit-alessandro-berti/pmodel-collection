# Generated from: 7614ba32-f56c-4461-9958-8a52776936b2.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farming facility within a repurposed warehouse. It involves initial site assessment, environmental impact analysis, modular system design, installation of hydroponic and aeroponic units, integration of IoT sensors for climate control, training of staff on automated maintenance, development of crop rotation schedules, securing local compliance and certifications, implementation of renewable energy sources, continuous monitoring of plant health via AI, optimization of nutrient delivery, packaging logistics planning, marketing to local retailers, and establishing customer feedback loops to enhance product quality and operational efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the activities
site_assess      = Transition(label='Site Assess')
impact_study     = Transition(label='Impact Study')
system_design    = Transition(label='System Design')
unit_install     = Transition(label='Unit Install')
sensor_setup     = Transition(label='Sensor Setup')
staff_train      = Transition(label='Staff Train')
crop_schedule    = Transition(label='Crop Schedule')
compliance_check = Transition(label='Compliance Check')
energy_deploy    = Transition(label='Energy Deploy')
health_monitor   = Transition(label='Health Monitor')
nutrient_tune    = Transition(label='Nutrient Tune')
package_plan     = Transition(label='Package Plan')
market_outreach  = Transition(label='Market Outreach')
feedback_loop    = Transition(label='Feedback Loop')
data_analyze     = Transition(label='Data Analyze')

# Build a sequential partial order
root = StrictPartialOrder(nodes=[
    site_assess,
    impact_study,
    system_design,
    unit_install,
    sensor_setup,
    staff_train,
    crop_schedule,
    compliance_check,
    energy_deploy,
    health_monitor,
    nutrient_tune,
    package_plan,
    market_outreach,
    feedback_loop,
    data_analyze
])

# Add the execution order edges
root.order.add_edge(site_assess, impact_study)
root.order.add_edge(impact_study, system_design)
root.order.add_edge(system_design, unit_install)
root.order.add_edge(unit_install, sensor_setup)
root.order.add_edge(sensor_setup, staff_train)
root.order.add_edge(staff_train, crop_schedule)
root.order.add_edge(crop_schedule, compliance_check)
root.order.add_edge(compliance_check, energy_deploy)
root.order.add_edge(energy_deploy, health_monitor)
root.order.add_edge(health_monitor, nutrient_tune)
root.order.add_edge(nutrient_tune, package_plan)
root.order.add_edge(package_plan, market_outreach)
root.order.add_edge(market_outreach, feedback_loop)
root.order.add_edge(feedback_loop, data_analyze)