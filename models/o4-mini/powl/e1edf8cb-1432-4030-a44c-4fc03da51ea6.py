# Generated from: e1edf8cb-1432-4030-a44c-4fc03da51ea6.json
# Description: This process outlines the setup of an urban vertical farming system within a repurposed industrial building. It involves site analysis, environmental control installation, hydroponic system configuration, crop selection based on urban demand, integration of IoT sensors for monitoring, staff training on automated systems, and establishing supply chain logistics for fresh produce delivery. The process ensures optimal space utilization, sustainability, and year-round crop production despite urban constraints, incorporating waste recycling and energy efficiency measures to reduce operational costs and environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
tsurvey    = Transition(label='Site Survey')
struct     = Transition(label='Structural Check')
env        = Transition(label='Env Control')
hydro      = Transition(label='Hydro Setup')
crop       = Transition(label='Crop Select')
iot        = Transition(label='IoT Install')
cal        = Transition(label='Sensor Calibrate')
staff      = Transition(label='Staff Train')
waste      = Transition(label='Waste Manage')
water      = Transition(label='Water Cycle')
nutrient   = Transition(label='Nutrient Mix')
light      = Transition(label='Lighting Adjust')
energy     = Transition(label='Energy Audit')
harvest    = Transition(label='Harvest Plan')
delivery   = Transition(label='Delivery Setup')
market     = Transition(label='Market Align')

# Define the maintenance sub-process as a partial order
maintenance_body = StrictPartialOrder(nodes=[water, nutrient, light, energy])
maintenance_body.order.add_edge(water, nutrient)
maintenance_body.order.add_edge(water, light)
maintenance_body.order.add_edge(nutrient, energy)
maintenance_body.order.add_edge(light, energy)

# Wrap maintenance in a loop: Waste Manage as the "A" part, maintenance_body as "B"
maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste, maintenance_body])

# Assemble the full process as a strict partial order
root = StrictPartialOrder(nodes=[
    tsurvey, struct,
    env, hydro,
    crop,
    iot, cal,
    staff,
    maintenance_loop,
    harvest,
    delivery, market
])

# Add control-flow dependencies
root.order.add_edge(tsurvey, struct)
root.order.add_edge(struct, env)
root.order.add_edge(struct, hydro)
root.order.add_edge(env, crop)
root.order.add_edge(hydro, crop)
root.order.add_edge(crop, iot)
root.order.add_edge(iot, cal)
root.order.add_edge(cal, staff)
root.order.add_edge(staff, maintenance_loop)
root.order.add_edge(maintenance_loop, harvest)
root.order.add_edge(harvest, delivery)
root.order.add_edge(harvest, market)