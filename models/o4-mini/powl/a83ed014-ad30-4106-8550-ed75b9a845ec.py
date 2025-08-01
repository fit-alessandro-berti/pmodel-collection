# Generated from: a83ed014-ad30-4106-8550-ed75b9a845ec.json
# Description: This process outlines the comprehensive steps required to establish a fully operational urban vertical farm within a constrained city environment. It involves initial site analysis, modular infrastructure design, controlled environment installation, seed selection, automated irrigation configuration, pest management system integration, and continuous monitoring setup. The process further includes workforce training on vertical farming techniques, supply chain coordination for organic inputs, energy efficiency optimization, and market launch strategies targeting local retailers and consumers. The aim is to maximize crop yield per square meter while minimizing water and energy consumption through innovative technologies and sustainable practices, ensuring year-round production and minimal environmental impact in a densely populated urban area.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# define all activities as transitions
site_survey       = Transition(label='Site Survey')
design_layout     = Transition(label='Design Layout')
modular_build     = Transition(label='Modular Build')
env_control       = Transition(label='Env Control')
seed_selection    = Transition(label='Seed Selection')
irrigation_setup  = Transition(label='Irrigation Setup')
pest_control      = Transition(label='Pest Control')
lighting_install  = Transition(label='Lighting Install')
sensor_config     = Transition(label='Sensor Config')
data_integration  = Transition(label='Data Integration')
staff_training    = Transition(label='Staff Training')
supply_sourcing   = Transition(label='Supply Sourcing')
energy_audit      = Transition(label='Energy Audit')
yield_testing     = Transition(label='Yield Testing')
market_launch     = Transition(label='Market Launch')
waste_recycling   = Transition(label='Waste Recycling')
feedback_review   = Transition(label='Feedback Review')

# create the partial order model
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    modular_build,
    env_control,
    seed_selection,
    irrigation_setup,
    pest_control,
    lighting_install,
    sensor_config,
    data_integration,
    staff_training,
    supply_sourcing,
    energy_audit,
    yield_testing,
    market_launch,
    waste_recycling,
    feedback_review
])

# define the control-flow dependencies
root.order.add_edge(site_survey,      design_layout)
root.order.add_edge(design_layout,    modular_build)
root.order.add_edge(modular_build,    env_control)

# after environment control, several activities can run in parallel
root.order.add_edge(env_control,      seed_selection)
root.order.add_edge(env_control,      irrigation_setup)
root.order.add_edge(env_control,      pest_control)
root.order.add_edge(env_control,      lighting_install)
root.order.add_edge(env_control,      sensor_config)

# all above feed into data integration
for precursor in [seed_selection,
                  irrigation_setup,
                  pest_control,
                  lighting_install,
                  sensor_config]:
    root.order.add_edge(precursor, data_integration)

# after data integration, training, sourcing and auditing can run concurrently
root.order.add_edge(data_integration, staff_training)
root.order.add_edge(data_integration, supply_sourcing)
root.order.add_edge(data_integration, energy_audit)

# all three lead to yield testing
for precursor in [staff_training, supply_sourcing, energy_audit]:
    root.order.add_edge(precursor, yield_testing)

# yield testing precedes market launch
root.order.add_edge(yield_testing,    market_launch)

# after market launch, wrap-up activities run in parallel
root.order.add_edge(market_launch,    waste_recycling)
root.order.add_edge(market_launch,    feedback_review)