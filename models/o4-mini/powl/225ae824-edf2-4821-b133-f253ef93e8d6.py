# Generated from: 225ae824-edf2-4821-b133-f253ef93e8d6.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farming system within a metropolitan environment. It includes site assessment, environmental analysis, infrastructure integration, technology deployment, crop selection, nutrient management, automation setup, yield monitoring, and sustainable waste handling. The process ensures efficient space utilization, maximizes crop output, minimizes energy consumption through IoT-enabled devices, and integrates renewable energy sources. Additionally, it incorporates community engagement and compliance with urban agricultural regulations, aiming to create a resilient, scalable, and eco-friendly food production model tailored for densely populated cities.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ss   = Transition(label='Site Survey')
cs   = Transition(label='Climate Study')
dl   = Transition(label='Design Layout')
sp   = Transition(label='Secure Permits')
ec   = Transition(label='Engage Community')
ifm  = Transition(label='Install Frames')
ir   = Transition(label='Set Irrigation')
ds   = Transition(label='Deploy Sensors')
cfg  = Transition(label='Configure AI')
sc   = Transition(label='Select Crops')
mn   = Transition(label='Mix Nutrients')
ssdn = Transition(label='Start Seeding')
mg   = Transition(label='Monitor Growth')
al   = Transition(label='Adjust Lighting')
hb   = Transition(label='Harvest Batches')
pw   = Transition(label='Process Waste')
rm   = Transition(label='Report Metrics')

# Loop for growth monitoring and lighting adjustment
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[mg, al])

# Build the overall partial order
root = StrictPartialOrder(
    nodes=[
        ss, cs, dl, sp, ec,
        ifm, ir, ds, cfg,
        sc, mn, ssdn,
        growth_loop, hb, pw, rm
    ]
)

# Define control-flow edges
root.order.add_edge(ss,   cs)
root.order.add_edge(cs,   dl)

# After layout: engage community & secure permits in parallel
root.order.add_edge(dl,   sp)
root.order.add_edge(dl,   ec)

# Infrastructure tasks in parallel after both permit & community
for infra in (ifm, ir, ds):
    root.order.add_edge(sp,  infra)
    root.order.add_edge(ec,  infra)

# Technology deployment after sensors
root.order.add_edge(ds,   cfg)
# Crop selection & nutrient prep
root.order.add_edge(cfg,  sc)
root.order.add_edge(sc,   mn)
# Seeding after automation and nutrients
root.order.add_edge(cfg,  ssdn)
root.order.add_edge(mn,   ssdn)
# Enter growth/lighting loop
root.order.add_edge(ssdn, growth_loop)
# Harvesting, waste handling, and reporting
root.order.add_edge(growth_loop, hb)
root.order.add_edge(hb,            pw)
root.order.add_edge(pw,            rm)