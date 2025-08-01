# Generated from: 9e99545e-688c-4e21-9efd-51862e13c59c.json
# Description: This process outlines the complex establishment of an urban vertical farm within a repurposed industrial building. It involves site assessment, modular system design, climate control integration, hydroponic setup, nutrient cycling optimization, and automated monitoring. The process also includes workforce training on advanced agricultural technology, securing sustainability certifications, and establishing direct-to-consumer supply chains. Coordination with local authorities for zoning compliance and environmental impact assessments is critical. Post-installation, ongoing data analysis and iterative system tuning ensure optimal crop yields and minimal resource consumption, fostering a resilient urban food production ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_assess = Transition(label='Site Assess')
review_compliance = Transition(label='Review Compliance')
design_modules = Transition(label='Design Modules')
set_climate = Transition(label='Set Climate')
connect_power = Transition(label='Connect Power')
integrate_sensors = Transition(label='Integrate Sensors')
calibrate_lighting = Transition(label='Calibrate Lighting')
install_hydroponics = Transition(label='Install Hydroponics')
test_irrigation = Transition(label='Test Irrigation')
configure_nutrients = Transition(label='Configure Nutrients')
train_staff = Transition(label='Train Staff')
certify_green = Transition(label='Certify Green')
launch_marketing = Transition(label='Launch Marketing')
analyze_data = Transition(label='Analyze Data')
adjust_parameters = Transition(label='Adjust Parameters')
schedule_maintenance = Transition(label='Schedule Maintenance')
manage_waste = Transition(label='Manage Waste')

# Define the body of the monitoring & tuning loop (B)
loop_body = StrictPartialOrder(nodes=[adjust_parameters, schedule_maintenance, manage_waste])
loop_body.order.add_edge(adjust_parameters, schedule_maintenance)
loop_body.order.add_edge(schedule_maintenance, manage_waste)

# Define the LOOP operator: analyze_data is A, loop_body is B
monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[analyze_data, loop_body])

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    site_assess, review_compliance, design_modules,
    set_climate, connect_power, integrate_sensors, calibrate_lighting,
    install_hydroponics, test_irrigation, configure_nutrients,
    train_staff, certify_green, launch_marketing,
    monitoring_loop
])

# Sequence of phases
root.order.add_edge(site_assess, review_compliance)
root.order.add_edge(review_compliance, design_modules)

# Parallel setup: climate branch
root.order.add_edge(design_modules, set_climate)
root.order.add_edge(set_climate, connect_power)
root.order.add_edge(connect_power, integrate_sensors)
root.order.add_edge(integrate_sensors, calibrate_lighting)

# Parallel setup: hydroponics branch
root.order.add_edge(design_modules, install_hydroponics)
root.order.add_edge(install_hydroponics, test_irrigation)
root.order.add_edge(test_irrigation, configure_nutrients)

# Join before training
root.order.add_edge(calibrate_lighting, train_staff)
root.order.add_edge(configure_nutrients, train_staff)

# Training, certification, marketing, then monitoring loop
root.order.add_edge(train_staff, certify_green)
root.order.add_edge(certify_green, launch_marketing)
root.order.add_edge(launch_marketing, monitoring_loop)