# Generated from: 4c3d0c53-61ce-42f1-b90a-61639764b8c7.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farming system within a metropolitan environment. It includes site assessment, modular farm design tailored to building constraints, sourcing sustainable materials, integrating IoT sensors for climate control, hydroponic system installation, nutrient solution calibration, crop selection based on urban demand, automated lighting setup, pest management using biological controls, data-driven growth monitoring, scheduled crop harvesting, waste recycling protocols, distribution logistics for local markets, customer feedback incorporation, and continuous system optimization to maximize yield and sustainability in a space-limited urban context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
sa = Transition(label='Site Assess')
df = Transition(label='Design Farm')
ms = Transition(label='Material Source')
isens = Transition(label='Install Sensors')
sh = Transition(label='Setup Hydroponics')
cn = Transition(label='Calibrate Nutrients')
sc = Transition(label='Select Crops')
cl = Transition(label='Configure Lighting')
mp = Transition(label='Manage Pests')
mg = Transition(label='Monitor Growth')
hc = Transition(label='Harvest Crops')
rw = Transition(label='Recycle Waste')
pd = Transition(label='Plan Distribution')
gf = Transition(label='Gather Feedback')
osyst = Transition(label='Optimize System')
skip = SilentTransition()

# Initial setup: strictly ordered
init = StrictPartialOrder(nodes=[sa, df, ms, isens, sh, cn, sc, cl])
init.order.add_edge(sa, df)
init.order.add_edge(df, ms)
init.order.add_edge(ms, isens)
init.order.add_edge(isens, sh)
init.order.add_edge(sh, cn)
init.order.add_edge(cn, sc)
init.order.add_edge(sc, cl)

# Operational cycle: strictly ordered
cycle = StrictPartialOrder(nodes=[mp, mg, hc, rw, pd, gf, osyst])
cycle.order.add_edge(mp, mg)
cycle.order.add_edge(mg, hc)
cycle.order.add_edge(hc, rw)
cycle.order.add_edge(rw, pd)
cycle.order.add_edge(pd, gf)
cycle.order.add_edge(gf, osyst)

# Loop over the operational cycle for continuous optimization
loop = OperatorPOWL(operator=Operator.LOOP, children=[cycle, skip])

# Root POWL: initial setup followed by loop
root = StrictPartialOrder(nodes=[init, loop])
root.order.add_edge(init, loop)