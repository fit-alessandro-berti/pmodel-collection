# Generated from: 681d85be-9f10-4a84-85bc-cd205bc73758.json
# Description: This process manages the supply chain and operational flow of an urban vertical farm specializing in microgreens and exotic herbs. It begins with seed sourcing from specialized breeders, followed by environmental calibration of grow chambers using IoT sensors. Nutrient solutions are mixed precisely by automated systems, and planting is executed by robotic arms. Continuous monitoring detects plant health issues early, triggering adaptive lighting and humidity controls. Harvesting involves selective picking to maximize yield quality, with immediate packaging in biodegradable containers. Quality assurance includes rapid microbial testing and flavor profiling through AI analysis. The process concludes with dynamic distribution scheduling to local markets and restaurants, optimizing freshness and minimizing carbon footprint, while integrating customer feedback for iterative improvements.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ss = Transition(label='Seed Sourcing')
cs = Transition(label='Chamber Setup')
nm = Transition(label='Nutrient Mixing')
rp = Transition(label='Robotic Planting')
hm = Transition(label='Health Monitoring')
lc = Transition(label='Lighting Control')
ha = Transition(label='Humidity Adjust')
sh = Transition(label='Selective Harvest')
bp = Transition(label='Bio Packaging')
mt = Transition(label='Microbial Test')
fp = Transition(label='Flavor Profile')
qa = Transition(label='Quality Audit')
osched = Transition(label='Order Scheduling')
dr = Transition(label='Delivery Route')
fr = Transition(label='Feedback Review')
isync = Transition(label='Inventory Sync')

# Create a partial order for concurrent control actions
po_controls = StrictPartialOrder(nodes=[lc, ha])

# Create a loop: monitor health, then either exit or do controls and repeat
health_loop = OperatorPOWL(operator=Operator.LOOP, children=[hm, po_controls])

# Create a partial order for concurrent QA tests
po_tests = StrictPartialOrder(nodes=[mt, fp])

# Build the overall workflow as a strict partial order
root = StrictPartialOrder(nodes=[
    ss, cs, nm, rp,
    health_loop,
    sh, bp, po_tests, qa,
    osched, dr, fr, isync
])

# Define the control-flow dependencies
root.order.add_edge(ss, cs)
root.order.add_edge(cs, nm)
root.order.add_edge(nm, rp)
root.order.add_edge(rp, health_loop)
root.order.add_edge(health_loop, sh)
root.order.add_edge(sh, bp)
root.order.add_edge(bp, po_tests)
root.order.add_edge(po_tests, qa)
root.order.add_edge(qa, osched)
root.order.add_edge(osched, dr)
root.order.add_edge(dr, fr)
root.order.add_edge(fr, isync)