# Generated from: cf587e93-dc8f-4316-99f3-a21aa92cab72.json
# Description: This process outlines the intricate cycle of managing an urban vertical farm that integrates IoT sensors, hydroponic systems, and AI-driven growth optimization. It begins with seed selection tailored to urban microclimates, followed by nutrient calibration and environmental monitoring. The cycle includes periodic pest management using organic biocontrol agents, automated harvesting via robotic arms, and dynamic market demand analysis to adjust crop variety. Waste is recycled into bio-compost onsite, and energy consumption is optimized through smart grid integration. The process culminates in packaging using biodegradable materials and real-time logistics coordination to ensure freshest delivery to urban retailers, closing the sustainability loop in a dense metropolitan context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seedSelect   = Transition(label='Seed Select')
nutrientMix  = Transition(label='Nutrient Mix')
sensorSetup  = Transition(label='Sensor Setup')
envMonitor   = Transition(label='Env Monitor')
growthScan   = Transition(label='Growth Scan')
waterCycle   = Transition(label='Water Cycle')
pestControl  = Transition(label='Pest Control')
harvestRobo  = Transition(label='Harvest Robo')
yieldAssess  = Transition(label='Yield Assess')
marketTrack  = Transition(label='Market Track')
orderAlign   = Transition(label='Order Align')
wasteProcess = Transition(label='Waste Process')
energySync   = Transition(label='Energy Sync')
packBiodeg   = Transition(label='Pack Biodeg')
logisticsPlan= Transition(label='Logistics Plan')
feedbackLoop = Transition(label='Feedback Loop')

# Pre‐loop (initial setup & monitoring) partial order
pre_loop = StrictPartialOrder(
    nodes=[
        seedSelect, nutrientMix, sensorSetup,
        envMonitor, growthScan, waterCycle
    ]
)
pre_loop.order.add_edge(seedSelect,   nutrientMix)
pre_loop.order.add_edge(nutrientMix,  sensorSetup)
pre_loop.order.add_edge(sensorSetup,  envMonitor)
pre_loop.order.add_edge(envMonitor,   growthScan)
pre_loop.order.add_edge(growthScan,   waterCycle)

# Loop body (cycle of farm operations)
body = StrictPartialOrder(
    nodes=[
        pestControl, harvestRobo, yieldAssess,
        marketTrack, orderAlign,
        wasteProcess, energySync,
        packBiodeg, logisticsPlan,
        feedbackLoop
    ]
)
body.order.add_edge(pestControl,   harvestRobo)
body.order.add_edge(harvestRobo,   yieldAssess)
body.order.add_edge(yieldAssess,   marketTrack)
body.order.add_edge(marketTrack,   orderAlign)
body.order.add_edge(orderAlign,    wasteProcess)
body.order.add_edge(wasteProcess,  energySync)
body.order.add_edge(energySync,    packBiodeg)
body.order.add_edge(packBiodeg,    logisticsPlan)
body.order.add_edge(logisticsPlan, feedbackLoop)

# Construct the LOOP operator: run pre_loop, then zero or more iterations of (body → pre_loop)
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[pre_loop, body]
)

# The root of our POWL model
root = loop