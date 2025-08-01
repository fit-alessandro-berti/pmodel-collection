# Generated from: f1df3585-3cd1-4306-8f32-4ae2ed3e100d.json
# Description: This process involves establishing an urban vertical farm by integrating advanced hydroponic systems with IoT-based environmental controls. It begins with site assessment and infrastructure planning, followed by modular rack installation, nutrient solution formulation, and sensor calibration. Concurrently, automated lighting and climate systems are configured to optimize plant growth cycles. Seed selection and germination are closely monitored through data analytics to ensure maximum yield. The process also includes pest management using bio-controls, periodic system maintenance, and real-time crop health monitoring. Finally, harvested produce undergoes quality checks before packaging and distribution, ensuring freshness and sustainability in urban food supply chains.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the transitions (activities)
sa = Transition(label='Site Assess')
pl = Transition(label='Plan Layout')
ir = Transition(label='Install Racks')
mn = Transition(label='Mix Nutrients')
cs = Transition(label='Calibrate Sensors')
sl = Transition(label='Setup Lighting')
cc = Transition(label='Configure Climate')
ss = Transition(label='Select Seeds')
mg = Transition(label='Monitor Germinate')
ad = Transition(label='Analyze Data')
ab = Transition(label='Apply Bio-controls')
ms = Transition(label='Maintain Systems')
hc = Transition(label='Harvest Crops')
qc = Transition(label='Quality Check')
pp = Transition(label='Package Produce')
dg = Transition(label='Distribute Goods')

# Build the partial‐order (POWL) model
root = StrictPartialOrder(
    nodes=[
        sa, pl, ir, mn, cs,
        sl, cc, ss, mg, ad,
        ab, ms, hc, qc, pp, dg
    ]
)

# Define the control‐flow dependencies (partial order edges)
root.order.add_edge(sa, pl)
root.order.add_edge(pl, ir)
root.order.add_edge(ir, mn)
root.order.add_edge(mn, cs)

# After sensor calibration, lighting and climate setup proceed in parallel
root.order.add_edge(cs, sl)
root.order.add_edge(cs, cc)

# Both lighting and climate must finish before seed selection
root.order.add_edge(sl, ss)
root.order.add_edge(cc, ss)

# Seed selection → germination monitoring → data analysis
root.order.add_edge(ss, mg)
root.order.add_edge(mg, ad)

# After initial analysis, pest management and system maintenance can proceed in parallel
root.order.add_edge(ad, ab)
root.order.add_edge(ad, ms)

# Both pest management and maintenance must finish before harvest
root.order.add_edge(ab, hc)
root.order.add_edge(ms, hc)

# Finish with quality check, packaging, and distribution
root.order.add_edge(hc, qc)
root.order.add_edge(qc, pp)
root.order.add_edge(pp, dg)