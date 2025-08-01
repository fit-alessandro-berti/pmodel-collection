# Generated from: 97b3578a-2e50-4c0b-8294-4fea9495ca63.json
# Description: This process outlines the comprehensive management cycle of an urban vertical farming operation that integrates automated climate control, nutrient monitoring, and staggered crop harvesting to maximize yield in limited spaces. The process begins with seed selection based on market demand forecasts, followed by precision seeding using robotic planters. Continuous environmental monitoring adjusts humidity, light intensity, and temperature to optimize growth conditions. Nutrient delivery is automated and adapted in real-time through IoT sensors detecting plant health. Pest management employs integrated biological controls rather than chemicals, ensuring sustainability. Crop growth stages are tracked digitally, triggering staggered harvesting to maintain a steady supply chain. Post-harvest, produce undergoes rapid quality assessment, packaging, and cold storage before distribution. Data analytics feed back into operational adjustments, improving future cycles and reducing waste while aligning with urban food security goals.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
df = Transition(label='Demand Forecast')
ss = Transition(label='Seed Select')
rp = Transition(label='Robotic Planting')
ca = Transition(label='Climate Adjust')
hc = Transition(label='Humidity Control')
lm = Transition(label='Light Modulate')
tm = Transition(label='Temp Maintain')
nf = Transition(label='Nutrient Flow')
sc = Transition(label='Sensor Check')
pm_ = Transition(label='Pest Monitor')
bc = Transition(label='Bio Control')
gt = Transition(label='Growth Track')
sh = Transition(label='Stagger Harvest')
qs = Transition(label='Quality Scan')
pp = Transition(label='Pack Produce')
cs = Transition(label='Cold Store')
da = Transition(label='Data Analyze')
wr = Transition(label='Waste Reduce')

# Silent transition for loop
skip = SilentTransition()

# Climate control runs concurrently after Climate Adjust
climateSeg = StrictPartialOrder(nodes=[ca, hc, lm, tm])
climateSeg.order.add_edge(ca, hc)
climateSeg.order.add_edge(ca, lm)
climateSeg.order.add_edge(ca, tm)

# Nutrient and sensing can run in parallel
sensorSeg = StrictPartialOrder(nodes=[nf, sc])
# no edges => fully concurrent

# Pest management sequence
pestSeg = StrictPartialOrder(nodes=[pm_, bc])
pestSeg.order.add_edge(pm_, bc)

# Growth tracking and staggered harvesting
growthSeg = StrictPartialOrder(nodes=[gt, sh])
growthSeg.order.add_edge(gt, sh)

# Post-harvest quality, packing, storage
harvestSeg = StrictPartialOrder(nodes=[qs, pp, cs])
harvestSeg.order.add_edge(qs, pp)
harvestSeg.order.add_edge(pp, cs)

# Data analytics and waste reduction
analyzeSeg = StrictPartialOrder(nodes=[da, wr])
analyzeSeg.order.add_edge(da, wr)

# One full cycle body
body = StrictPartialOrder(nodes=[
    df, ss, rp,
    climateSeg,
    sensorSeg,
    pestSeg,
    growthSeg,
    harvestSeg,
    analyzeSeg
])
body.order.add_edge(df, ss)
body.order.add_edge(ss, rp)
body.order.add_edge(rp, climateSeg)
body.order.add_edge(climateSeg, sensorSeg)
body.order.add_edge(sensorSeg, pestSeg)
body.order.add_edge(pestSeg, growthSeg)
body.order.add_edge(growthSeg, harvestSeg)
body.order.add_edge(harvestSeg, analyzeSeg)

# Wrap the cycle in a loop: execute body, then optionally skip and repeat
root = OperatorPOWL(operator=Operator.LOOP, children=[body, skip])