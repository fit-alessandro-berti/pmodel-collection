# Generated from: 3e8eb1d4-f5f5-41c7-841e-42282a8bb617.json
# Description: This process outlines the complex steps required to establish a sustainable urban beekeeping operation within city limits. It involves selecting appropriate rooftop locations, obtaining legal permits, designing hive layouts that comply with local regulations, sourcing resilient bee colonies, implementing pollen monitoring systems, training staff in urban-specific hive management, scheduling regular health inspections, coordinating with local environmental groups, managing urban foraging resources, setting up honey extraction and packaging facilities on-site, integrating pest control measures that are safe for dense populations, marketing locally produced honey through community channels, and continuously adapting practices to evolving urban ecosystems and climate conditions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ss = Transition(label='Site Survey')
pf = Transition(label='Permit Filing')
fd = Transition(label='Hive Design')
cs = Transition(label='Colony Sourcing')
pt = Transition(label='Pollen Testing')
st = Transition(label='Staff Training')
hc = Transition(label='Health Check')
el = Transition(label='Enviro Liaison')
fm = Transition(label='Forage Mapping')
es = Transition(label='Extraction Setup')
pc = Transition(label='Pest Control')
hp = Transition(label='Honey Packing')
lm = Transition(label='Local Marketing')
cl = Transition(label='Climate Adapt')
dl = Transition(label='Data Logging')

# Loop for continuous data logging and climate adaptation
loop = OperatorPOWL(operator=Operator.LOOP, children=[dl, cl])

# Build the root partial order
root = StrictPartialOrder(
    nodes=[
        ss, pf, el, fm,
        fd, cs, st,
        pt, pc, hc, es,
        hp, lm, loop
    ]
)

# Define the precedence relations
o = root.order
o.add_edge(ss, pf)
o.add_edge(ss, el)
o.add_edge(ss, fm)

o.add_edge(pf, fd)

o.add_edge(fd, cs)
o.add_edge(fd, st)
o.add_edge(fd, es)

o.add_edge(cs, pt)
o.add_edge(cs, pc)
o.add_edge(cs, hc)

o.add_edge(st, hc)

o.add_edge(es, hp)
o.add_edge(hp, lm)

o.add_edge(lm, loop)