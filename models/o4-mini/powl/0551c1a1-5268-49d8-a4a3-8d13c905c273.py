# Generated from: 0551c1a1-5268-49d8-a4a3-8d13c905c273.json
# Description: This process involves establishing a fully operational urban vertical farm within a multi-story building. It begins with site analysis and design customization to maximize space utilization and light distribution. After structural modifications, hydroponic and aeroponic systems are installed, followed by climate control and sensor integration to monitor environmental parameters. Seed selection and planting schedules are coordinated with automated nutrient delivery systems. Staff training ensures proper maintenance and harvesting techniques. The process closes with quality assurance and market distribution planning to supply fresh produce locally, minimizing transportation footprint while maximizing yield and sustainability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as POWL transitions
sa   = Transition(label='Site Analysis')
dl   = Transition(label='Design Layout')
sm   = Transition(label='Structural Mod')
si   = Transition(label='System Install')
cs   = Transition(label='Climate Setup')
sd   = Transition(label='Sensor Deploy')
ss   = Transition(label='Seed Select')
pp   = Transition(label='Planting Plan')
nf   = Transition(label='Nutrient Flow')
at   = Transition(label='Automation Tune')
st   = Transition(label='Staff Training')
hp   = Transition(label='Harvest Prep')
qc   = Transition(label='Quality Check')
mp   = Transition(label='Market Plan')
dist = Transition(label='Distribution')

# Build the partial order
root = StrictPartialOrder(nodes=[
    sa, dl, sm, si, cs, sd, ss, pp, nf, at, st, hp, qc, mp, dist
])

# Sequential flow up to system install
root.order.add_edge(sa,   dl)
root.order.add_edge(dl,   sm)
root.order.add_edge(sm,   si)

# Climate setup and sensor deployment in parallel after system install
root.order.add_edge(si,   cs)
root.order.add_edge(si,   sd)
# Both must complete before seed selection
root.order.add_edge(cs,   ss)
root.order.add_edge(sd,   ss)

# Continue sequentially to distribution
root.order.add_edge(ss,   pp)
root.order.add_edge(pp,   nf)
root.order.add_edge(nf,   at)
root.order.add_edge(at,   st)
root.order.add_edge(st,   hp)
root.order.add_edge(hp,   qc)
root.order.add_edge(qc,   mp)
root.order.add_edge(mp,   dist)