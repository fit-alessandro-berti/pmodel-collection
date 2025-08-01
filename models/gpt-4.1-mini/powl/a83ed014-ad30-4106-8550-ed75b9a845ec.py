# Generated from: a83ed014-ad30-4106-8550-ed75b9a845ec.json
# Description: This process outlines the comprehensive steps required to establish a fully operational urban vertical farm within a constrained city environment. It involves initial site analysis, modular infrastructure design, controlled environment installation, seed selection, automated irrigation configuration, pest management system integration, and continuous monitoring setup. The process further includes workforce training on vertical farming techniques, supply chain coordination for organic inputs, energy efficiency optimization, and market launch strategies targeting local retailers and consumers. The aim is to maximize crop yield per square meter while minimizing water and energy consumption through innovative technologies and sustainable practices, ensuring year-round production and minimal environmental impact in a densely populated urban area.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activity transitions
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
modular_build = Transition(label='Modular Build')
env_control = Transition(label='Env Control')
seed_selection = Transition(label='Seed Selection')
irrigation_setup = Transition(label='Irrigation Setup')
pest_control = Transition(label='Pest Control')
lighting_install = Transition(label='Lighting Install')
sensor_config = Transition(label='Sensor Config')
data_integration = Transition(label='Data Integration')
staff_training = Transition(label='Staff Training')
supply_sourcing = Transition(label='Supply Sourcing')
energy_audit = Transition(label='Energy Audit')
yield_testing = Transition(label='Yield Testing')
market_launch = Transition(label='Market Launch')
waste_recycling = Transition(label='Waste Recycling')
feedback_review = Transition(label='Feedback Review')

# Build partial orders reflecting logical sequences and concurrency based on description.

# Initial core design and build sequence:
# Site Survey --> Design Layout --> Modular Build --> Env Control
initial_sequence = StrictPartialOrder(
    nodes=[site_survey, design_layout, modular_build, env_control]
)
initial_sequence.order.add_edge(site_survey, design_layout)
initial_sequence.order.add_edge(design_layout, modular_build)
initial_sequence.order.add_edge(modular_build, env_control)

# Seed Selection, Irrigation Setup, Pest Control can be done in parallel after Env Control
seed_irrig_pest = StrictPartialOrder(
    nodes=[seed_selection, irrigation_setup, pest_control]
)
# No edges => concurrent after Env Control

# Lighting Install and Sensor Config and Data Integration are related,
# assume Lighting Install --> Sensor Config --> Data Integration 
lighting_sensor_data = StrictPartialOrder(
    nodes=[lighting_install, sensor_config, data_integration]
)
lighting_sensor_data.order.add_edge(lighting_install, sensor_config)
lighting_sensor_data.order.add_edge(sensor_config, data_integration)

# Staff Training and Supply Sourcing run in parallel (independent from above groups)
staff_supply = StrictPartialOrder(
    nodes=[staff_training, supply_sourcing]
)
# no edges between these two, can be concurrent

# Energy Audit, Yield Testing, and Waste Recycling in sequence (sustainability related)
sustainability = StrictPartialOrder(
    nodes=[energy_audit, yield_testing, waste_recycling]
)
sustainability.order.add_edge(energy_audit, yield_testing)
sustainability.order.add_edge(yield_testing, waste_recycling)

# Feedback Review and Market Launch: assume after sustainability and staff/supply done,
# Assume Feedback Review --> Market Launch
feedback_market = StrictPartialOrder(
    nodes=[feedback_review, market_launch]
)
feedback_market.order.add_edge(feedback_review, market_launch)

# Now compose the full process partial order:

# After Env Control:
# Seed/Irrigation/Pest controls (group1)
# Lighting->Sensor->Data (group2)
# Staff Training and Supply Sourcing (group3)
# Sustainability (group4)

# Those four groups start after Env Control and run concurrently.

# Then after groups 3 and 4 finish, feedback and market launch happens,
# Feedback Review depends on sustainability and staff/supply completion

# Since feedback needs results from sustainability and staff/supply,
# we add edges sustainability --> feedback_review and supply_sourcing --> feedback_review

# Final PO nodes include:
# initial_sequence nodes + seed_irrig_pest + lighting_sensor_data + staff_supply + sustainability + feedback_market

nodes_all = [
    # initial sequence nodes
    site_survey, design_layout, modular_build, env_control,
    # after Env Control groups:
    seed_selection, irrigation_setup, pest_control,
    lighting_install, sensor_config, data_integration,
    staff_training, supply_sourcing,
    energy_audit, yield_testing, waste_recycling,
    feedback_review, market_launch
]

root = StrictPartialOrder(nodes=nodes_all)

# Add initial sequence edges
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, modular_build)
root.order.add_edge(modular_build, env_control)

# After Env Control:
# Seed/Irrigation/Pest run concurrently - means all depend on env_control
root.order.add_edge(env_control, seed_selection)
root.order.add_edge(env_control, irrigation_setup)
root.order.add_edge(env_control, pest_control)

# Lighting->Sensor->Data also depends on env_control
root.order.add_edge(env_control, lighting_install)
root.order.add_edge(lighting_install, sensor_config)
root.order.add_edge(sensor_config, data_integration)

# Staff Training and Supply Sourcing depend on env_control
root.order.add_edge(env_control, staff_training)
root.order.add_edge(env_control, supply_sourcing)
# no edge between those two, concurrent

# Sustainability chain depends on env_control as well
root.order.add_edge(env_control, energy_audit)
root.order.add_edge(energy_audit, yield_testing)
root.order.add_edge(yield_testing, waste_recycling)

# Feedback Review depends on sustainability (waste recycling) and supply_sourcing and staff_training (to be safe)
root.order.add_edge(waste_recycling, feedback_review)
root.order.add_edge(supply_sourcing, feedback_review)
root.order.add_edge(staff_training, feedback_review)

# Market Launch depends on Feedback Review
root.order.add_edge(feedback_review, market_launch)