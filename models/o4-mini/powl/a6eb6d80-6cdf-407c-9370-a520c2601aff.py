# Generated from: a6eb6d80-6cdf-407c-9370-a520c2601aff.json
# Description: This process outlines the end-to-end setup of an urban vertical farm, integrating advanced hydroponics, renewable energy sourcing, and automated climate control. It includes site analysis, modular construction, nutrient solution formulation, sensor calibration, crop seeding, growth monitoring, pest management with bioagents, yield forecasting using AI models, and finally, supply chain coordination for fresh produce delivery to local markets. The process emphasizes sustainability, tech integration, and urban space optimization to maximize output in limited areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
ss = Transition(label="Site Survey")
dl = Transition(label="Design Layout")
sb = Transition(label="Structure Build")
ih = Transition(label="Install Hydroponics")
es = Transition(label="Energy Setup")
nm = Transition(label="Nutrient Mix")
sc = Transition(label="Sensor Calibrate")
ct = Transition(label="Climate Tune")
sd = Transition(label="Seed Crops")
mg = Transition(label="Monitor Growth")
pc = Transition(label="Pest Control")
da = Transition(label="Data Analyze")
yf = Transition(label="Yield Forecast")
hp = Transition(label="Harvest Plan")
ls = Transition(label="Logistics Sync")
mo = Transition(label="Market Outreach")

# Build the partial order
root = StrictPartialOrder(
    nodes=[ss, dl, sb, ih, es, nm, sc, ct, sd, mg, pc, da, yf, hp, ls, mo]
)

# Linear dependencies
root.order.add_edge(ss, dl)
root.order.add_edge(dl, sb)

# Parallel install hydroponics and energy setup after structure build
root.order.add_edge(sb, ih)
root.order.add_edge(sb, es)

# Both branches join at nutrient mixing
root.order.add_edge(ih, nm)
root.order.add_edge(es, nm)

# Parallel sensor calibration and climate tuning before seeding
root.order.add_edge(nm, sc)
root.order.add_edge(nm, ct)

# Both join at seed crops
root.order.add_edge(sc, sd)
root.order.add_edge(ct, sd)

# Continue linearly to market outreach
root.order.add_edge(sd, mg)
root.order.add_edge(mg, pc)
root.order.add_edge(pc, da)
root.order.add_edge(da, yf)
root.order.add_edge(yf, hp)
root.order.add_edge(hp, ls)
root.order.add_edge(ls, mo)