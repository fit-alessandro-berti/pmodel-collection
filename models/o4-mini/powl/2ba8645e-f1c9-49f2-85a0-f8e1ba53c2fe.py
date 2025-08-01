# Generated from: 2ba8645e-f1c9-49f2-85a0-f8e1ba53c2fe.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm within a repurposed commercial building. It includes site analysis, structural modifications, installation of hydroponic and aeroponic systems, climate control programming, and integration of IoT sensors for real-time monitoring. The workflow also covers sourcing specialized LED lighting, nutrient solution formulation, recruitment of agronomists, and development of a supply chain for local distribution. Continuous optimization and data analysis ensure sustainability and yield maximization in a constrained urban environment, blending advanced technology with agricultural expertise to meet growing local food demands.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_survey       = Transition(label='Site Survey')
structural_scan   = Transition(label='Structural Scan')
permit_acquire    = Transition(label='Permit Acquire')
system_design     = Transition(label='System Design')
hydroponic_setup  = Transition(label='Hydroponic Setup')
aeroponic_install = Transition(label='Aeroponic Install')
led_mounting      = Transition(label='LED Mounting')
climate_config    = Transition(label='Climate Config')
sensor_deploy     = Transition(label='Sensor Deploy')
nutrient_mix      = Transition(label='Nutrient Mix')
agronomist_hire   = Transition(label='Agronomist Hire')
data_integration  = Transition(label='Data Integration')
trial_growth      = Transition(label='Trial Growth')
supply_chain      = Transition(label='Supply Chain')
yield_review      = Transition(label='Yield Review')
optimization_plan = Transition(label='Optimization Plan')

# 1) Initial site and structural setup (sequential)
initial_setup = StrictPartialOrder(nodes=[
    site_survey, structural_scan, permit_acquire, system_design
])
initial_setup.order.add_edge(site_survey, structural_scan)
initial_setup.order.add_edge(structural_scan, permit_acquire)
initial_setup.order.add_edge(permit_acquire, system_design)

# 2) System installation (hydroponic and aeroponic in parallel)
system_installation = StrictPartialOrder(nodes=[
    hydroponic_setup, aeroponic_install
])
# no edges -> concurrent

# 3) LED mounting after both installation tasks
# we'll connect these at the top level

# 4) Environment setup (climate & sensors in parallel)
env_setup = StrictPartialOrder(nodes=[
    climate_config, sensor_deploy
])
# no edges -> concurrent

# 5) Preparation (nutrient mix & agronomist hire in parallel)
prep = StrictPartialOrder(nodes=[
    nutrient_mix, agronomist_hire
])
# no edges -> concurrent

# 6) Trial loop: trial growth -> yield review, then optionally optimize and repeat
trial_seq = StrictPartialOrder(nodes=[trial_growth, yield_review])
trial_seq.order.add_edge(trial_growth, yield_review)

trial_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[trial_seq, optimization_plan]
)

# 7) Final supply chain deployment
# supply_chain is already defined as a Transition

# 8) Assemble the top‐level partial order
root = StrictPartialOrder(nodes=[
    initial_setup,
    system_installation,
    led_mounting,
    env_setup,
    prep,
    data_integration,
    trial_loop,
    supply_chain
])

# Define the global ordering among the top‐level fragments
root.order.add_edge(initial_setup, system_installation)
root.order.add_edge(system_installation, led_mounting)
root.order.add_edge(led_mounting, env_setup)
root.order.add_edge(env_setup, prep)
root.order.add_edge(prep, data_integration)
root.order.add_edge(data_integration, trial_loop)
root.order.add_edge(trial_loop, supply_chain)