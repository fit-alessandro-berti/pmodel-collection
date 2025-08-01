# Generated from: 6734dc9e-536f-40bf-a717-032633d46d55.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farming facility within a repurposed industrial building. It includes initial site assessment, modular system design, environmental control calibration, automated nutrient delivery setup, and integration with local distribution networks. The process also covers regulatory compliance, waste recycling implementation, real-time crop monitoring, and adaptive pest control strategies. Special attention is given to energy optimization, workforce training, data analytics for yield prediction, and continuous system maintenance to ensure sustainable and efficient production in a high-density urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey      = Transition(label='Site Survey')
permits_acquire  = Transition(label='Permits Acquire')
system_design    = Transition(label='System Design')
modular_build    = Transition(label='Modular Build')
env_control      = Transition(label='Env Control')
nutrient_setup   = Transition(label='Nutrient Setup')
lighting_install = Transition(label='Lighting Install')
irrigation_test  = Transition(label='Irrigation Test')
sensor_deploy    = Transition(label='Sensor Deploy')
waste_plan       = Transition(label='Waste Plan')
staff_training   = Transition(label='Staff Training')
data_setup       = Transition(label='Data Setup')
yield_monitor    = Transition(label='Yield Monitor')
pest_control     = Transition(label='Pest Control')
energy_audit     = Transition(label='Energy Audit')
logistics_sync   = Transition(label='Logistics Sync')
maintenance_plan = Transition(label='Maintenance Plan')

# Define the cycle body for adaptive pest control & energy optimization
cycle_body = StrictPartialOrder(nodes=[pest_control, energy_audit])
cycle_body.order.add_edge(pest_control, energy_audit)

# Define the loop: perform yield_monitor, then either exit or do cycle_body then yield_monitor again
monitor_cycle = OperatorPOWL(
    operator=Operator.LOOP,
    children=[yield_monitor, cycle_body]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    permits_acquire,
    system_design,
    modular_build,
    env_control,
    nutrient_setup,
    lighting_install,
    irrigation_test,
    sensor_deploy,
    waste_plan,
    staff_training,
    data_setup,
    monitor_cycle,
    logistics_sync,
    maintenance_plan
])

# Add the control-flow edges
edges = [
    (site_survey,      permits_acquire),
    (permits_acquire,  system_design),
    (system_design,    modular_build),
    (modular_build,    env_control),
    (env_control,      nutrient_setup),
    (nutrient_setup,   lighting_install),
    (lighting_install, irrigation_test),
    (irrigation_test,  sensor_deploy),
    (sensor_deploy,    waste_plan),
    (waste_plan,       staff_training),
    (staff_training,   data_setup),
    (data_setup,       monitor_cycle),
    (monitor_cycle,    logistics_sync),
    (logistics_sync,   maintenance_plan)
]
for src, tgt in edges:
    root.order.add_edge(src, tgt)