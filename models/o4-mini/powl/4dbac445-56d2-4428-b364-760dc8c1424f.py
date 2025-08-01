# Generated from: 4dbac445-56d2-4428-b364-760dc8c1424f.json
# Description: This process outlines the complex and multifaceted steps involved in establishing an urban vertical farming operation within a metropolitan environment. It includes site evaluation, modular system design, environmental controls integration, and supply chain coordination for organic seed sourcing. The process requires precise synchronization of technological installation, nutrient solution calibration, and real-time monitoring setup to optimize crop yield. Additionally, it incorporates community engagement for local market feedback and regulatory compliance checks to ensure sustainable practices. The workflow culminates with staff training, pilot harvests, and iterative system refinement based on data analytics, fostering a resilient and scalable urban agriculture model.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
seed_sourcing = Transition(label='Seed Sourcing')
permit_acquire = Transition(label='Permit Acquire')
module_install = Transition(label='Module Install')
irrigation_setup = Transition(label='Irrigation Setup')
lighting_configure = Transition(label='Lighting Configure')
climate_control = Transition(label='Climate Control')
nutrient_mix = Transition(label='Nutrient Mix')
sensor_calibrate = Transition(label='Sensor Calibrate')
data_integration = Transition(label='Data Integration')
market_engage = Transition(label='Market Engage')
compliance_audit = Transition(label='Compliance Audit')
staff_training = Transition(label='Staff Training')
# Loop body activities
trial_harvest = Transition(label='Trial Harvest')
yield_analyze = Transition(label='Yield Analyze')
system_review = Transition(label='System Review')
# Silent transition for loop redo
skip = SilentTransition()

# Build the inner loop body: Trial Harvest -> Yield Analyze -> System Review
po_loop_body = StrictPartialOrder(nodes=[trial_harvest, yield_analyze, system_review])
po_loop_body.order.add_edge(trial_harvest, yield_analyze)
po_loop_body.order.add_edge(yield_analyze, system_review)

# Define the loop: execute the body, then optionally redo
loop = OperatorPOWL(operator=Operator.LOOP, children=[po_loop_body, skip])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    seed_sourcing,
    permit_acquire,
    module_install,
    irrigation_setup,
    lighting_configure,
    climate_control,
    nutrient_mix,
    sensor_calibrate,
    data_integration,
    market_engage,
    compliance_audit,
    staff_training,
    loop
])

# Add control‐flow edges
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, seed_sourcing)
root.order.add_edge(seed_sourcing, permit_acquire)
root.order.add_edge(permit_acquire, module_install)
root.order.add_edge(permit_acquire, market_engage)
root.order.add_edge(permit_acquire, compliance_audit)

root.order.add_edge(module_install, irrigation_setup)
root.order.add_edge(module_install, lighting_configure)
root.order.add_edge(module_install, climate_control)
root.order.add_edge(module_install, sensor_calibrate)

root.order.add_edge(irrigation_setup, nutrient_mix)
root.order.add_edge(sensor_calibrate, data_integration)

# Ensure staff training waits for all setup, community & regulatory tasks
root.order.add_edge(lighting_configure, staff_training)
root.order.add_edge(climate_control, staff_training)
root.order.add_edge(nutrient_mix, staff_training)
root.order.add_edge(data_integration, staff_training)
root.order.add_edge(market_engage, staff_training)
root.order.add_edge(compliance_audit, staff_training)

# After training, enter the iterative pilot‐harvest loop
root.order.add_edge(staff_training, loop)