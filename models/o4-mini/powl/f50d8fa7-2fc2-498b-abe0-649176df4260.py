# Generated from: f50d8fa7-2fc2-498b-abe0-649176df4260.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban vertical farm within a repurposed industrial building. It integrates architectural retrofitting, advanced hydroponic system installation, energy-efficient lighting calibration, and IoT-based environmental monitoring. The process manages supply chain logistics for seeds and nutrients, secures regulatory compliance for urban agriculture, and coordinates labor training on both agricultural and technological operations. Continuous data analysis is employed to optimize crop yields while minimizing resource consumption, all within the constraints of urban zoning and community engagement initiatives. The process concludes with market launch planning and distribution network setup for fresh produce delivery.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
site_survey     = Transition(label='Site Survey')
design_plan     = Transition(label='Design Plan')
permit_acquire  = Transition(label='Permit Acquire')
compliance_chk  = Transition(label='Compliance Check')
community_meet  = Transition(label='Community Meet')
struct_retrofit = Transition(label='Structural Retrofit')
system_install  = Transition(label='System Install')
lighting_setup  = Transition(label='Lighting Setup')
sensor_deploy   = Transition(label='Sensor Deploy')
seed_sourcing   = Transition(label='Seed Sourcing')
nutrient_prep   = Transition(label='Nutrient Prep')
staff_training  = Transition(label='Staff Training')
data_monitor    = Transition(label='Data Monitor')
yield_analyze   = Transition(label='Yield Analyze')
market_launch   = Transition(label='Market Launch')
logistics_plan  = Transition(label='Logistics Plan')

# Loop for continuous data analysis: Data Monitor then either exit or Yield Analyze then Data Monitor again
analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_monitor, yield_analyze])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_plan,
    permit_acquire,
    compliance_chk,
    community_meet,
    struct_retrofit,
    system_install,
    lighting_setup,
    sensor_deploy,
    seed_sourcing,
    nutrient_prep,
    staff_training,
    analysis_loop,
    market_launch,
    logistics_plan
])

# Define the control-flow edges

# 1. Initial phase: site survey -> design
root.order.add_edge(site_survey, design_plan)

# 2. Regulatory phase: design -> permit -> compliance & community engagement
root.order.add_edge(design_plan, permit_acquire)
root.order.add_edge(permit_acquire, compliance_chk)
root.order.add_edge(permit_acquire, community_meet)

# 3. Building phase: after compliance, retrofit -> install -> lighting -> sensor deploy
root.order.add_edge(compliance_chk, struct_retrofit)
root.order.add_edge(struct_retrofit, system_install)
root.order.add_edge(system_install, lighting_setup)
root.order.add_edge(lighting_setup, sensor_deploy)

# 4. Supply chain & training in parallel after design
root.order.add_edge(design_plan, seed_sourcing)
root.order.add_edge(seed_sourcing, nutrient_prep)
root.order.add_edge(design_plan, staff_training)

# 5. Start the continuous analysis loop once sensor, nutrients, and training are in place
root.order.add_edge(sensor_deploy, analysis_loop)
root.order.add_edge(nutrient_prep, analysis_loop)
root.order.add_edge(staff_training, analysis_loop)

# 6. Final phase: once the loop exits, market launch -> logistics
root.order.add_edge(analysis_loop, market_launch)
root.order.add_edge(market_launch, logistics_plan)