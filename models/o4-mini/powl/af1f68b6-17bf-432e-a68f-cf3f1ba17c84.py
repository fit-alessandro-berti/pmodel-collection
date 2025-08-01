# Generated from: af1f68b6-17bf-432e-a68f-cf3f1ba17c84.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farming operation within a repurposed industrial building. It involves site analysis, structural retrofitting, environmental system integration, crop selection, automation setup, nutrient cycling design, community engagement, and regulatory compliance. The process must balance sustainable resource use, technological innovation, and local food production goals while addressing unique challenges such as lighting optimization, water recycling, pest management without chemicals, and efficient harvest logistics. The integration of IoT sensors to monitor microclimates and plant health is critical, alongside employee training and continuous process refinement based on data analytics to maximize yield and minimize environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
structural_check = Transition(label='Structural Check')
retrofit_plan = Transition(label='Retrofit Plan')
lighting_setup = Transition(label='Lighting Setup')
irrigation_install = Transition(label='Irrigation Install')
sensor_deploy = Transition(label='Sensor Deploy')
crop_select = Transition(label='Crop Select')
nutrient_mix = Transition(label='Nutrient Mix')
pest_control = Transition(label='Pest Control')
automation_config = Transition(label='Automation Config')
data_monitor = Transition(label='Data Monitor')
employee_train = Transition(label='Employee Train')
community_meet = Transition(label='Community Meet')
compliance_audit = Transition(label='Compliance Audit')
harvest_plan = Transition(label='Harvest Plan')
waste_recycle = Transition(label='Waste Recycle')
energy_audit = Transition(label='Energy Audit')

# Loop for continuous refinement: Data Monitor then optionally Employee Train, then back
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_monitor, employee_train])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    structural_check,
    retrofit_plan,
    lighting_setup,
    irrigation_install,
    sensor_deploy,
    crop_select,
    nutrient_mix,
    pest_control,
    automation_config,
    monitor_loop,
    community_meet,
    compliance_audit,
    energy_audit,
    harvest_plan,
    waste_recycle
])

# Define edges for the workflow ordering
root.order.add_edge(site_survey, structural_check)
root.order.add_edge(structural_check, retrofit_plan)

root.order.add_edge(retrofit_plan, lighting_setup)
root.order.add_edge(retrofit_plan, irrigation_install)

root.order.add_edge(lighting_setup, sensor_deploy)
root.order.add_edge(irrigation_install, sensor_deploy)

root.order.add_edge(sensor_deploy, crop_select)
root.order.add_edge(crop_select, nutrient_mix)
root.order.add_edge(nutrient_mix, pest_control)

root.order.add_edge(pest_control, automation_config)
root.order.add_edge(automation_config, monitor_loop)

# After the refinement loop, all these can proceed (concurrent)
for next_activity in [
    community_meet,
    compliance_audit,
    energy_audit,
    harvest_plan,
    waste_recycle
]:
    root.order.add_edge(monitor_loop, next_activity)