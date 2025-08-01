# Generated from: 45eed133-7dd3-43ef-be2d-9e9a89843f70.json
# Description: This process outlines the establishment of a sustainable urban vertical farm within a repurposed industrial building. It involves site analysis, structural assessment, installation of hydroponic systems, climate control setup, automation integration, and continuous monitoring. The process ensures optimized space utilization, resource efficiency, and year-round crop production. Collaborative efforts between architects, engineers, agronomists, and IT specialists are essential to address challenges such as lighting optimization, water recycling, pest control, and yield forecasting. The process also includes regulatory compliance checks, community engagement, and supply chain coordination for distribution and marketing of produce.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ss = Transition(label='Site Survey')
sc = Transition(label='Structure Check')
dl = Transition(label='Design Layout')
ifr = Transition(label='Install Frames')
sh = Transition(label='Setup Hydroponics')
csu = Transition(label='Climate Setup')
lc = Transition(label='Lighting Config')
ai = Transition(label='Automation Install')
sd = Transition(label='Sensor Deploy')
wc = Transition(label='Water Cycle')
pc = Transition(label='Pest Control')
st = Transition(label='System Testing')
ps = Transition(label='Plant Seeding')
gm = Transition(label='Growth Monitor')
yf = Transition(label='Yield Forecast')
audit = Transition(label='Regulation Audit')
meet = Transition(label='Community Meet')
supply = Transition(label='Supply Chain')

# Silent transition for loop exit
skip = SilentTransition()

# Monitoring sub‐process: Growth Monitor -> Yield Forecast
monitoring = StrictPartialOrder(nodes=[gm, yf])
monitoring.order.add_edge(gm, yf)

# Loop on the monitoring subprocess
loop = OperatorPOWL(operator=Operator.LOOP, children=[monitoring, skip])

# Final phase: after loop exit, do audit, then community engagement and supply chain in parallel
final_phase = StrictPartialOrder(nodes=[audit, meet, supply])
final_phase.order.add_edge(audit, meet)
final_phase.order.add_edge(audit, supply)

# Root process: sequence of setup activities, then seeding, then monitoring loop, then final phase
root = StrictPartialOrder(
    nodes=[ss, sc, dl, ifr, sh, csu, lc, ai, sd, wc, pc, st, ps, loop, final_phase]
)

# Define the sequential order of the main process
sequence = [
    (ss, sc), (sc, dl), (dl, ifr), (ifr, sh), (sh, csu), (csu, lc),
    (lc, ai), (ai, sd), (sd, wc), (wc, pc), (pc, st), (st, ps),
    (ps, loop), (loop, final_phase)
]
for src, tgt in sequence:
    root.order.add_edge(src, tgt)