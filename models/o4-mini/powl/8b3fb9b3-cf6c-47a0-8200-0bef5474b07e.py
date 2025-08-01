# Generated from: 8b3fb9b3-cf6c-47a0-8200-0bef5474b07e.json
# Description: This process governs the rapid mobilization and coordination of resources during a sudden multi-regional crisis, such as a natural disaster combined with infrastructure failure. It involves initial threat assessment, stakeholder communication, resource allocation under uncertainty, dynamic route planning for aid delivery, contingency management for supply chain disruption, and real-time feedback incorporation from field teams. The process demands flexible decision-making frameworks, integration of multiple data sources including satellite and social media feeds, and simultaneous coordination with governmental agencies, NGOs, and private sector partners to minimize response time and maximize impact. Post-crisis evaluation and knowledge transfer to improve future responses are also key components.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
ta   = Transition(label='Threat Assess')
ss   = Transition(label='Stakeholder Sync')
rm   = Transition(label='Resource Map')
ps   = Transition(label='Priority Set')
di   = Transition(label='Data Integrate')
pa   = Transition(label='Partner Align')
sc   = Transition(label='Supply Check')
cs   = Transition(label='Contingency Set')
rmg  = Transition(label='Risk Manage')
rp   = Transition(label='Route Plan')
ad   = Transition(label='Asset Deploy')
tt   = Transition(label='Transport Track')
fb   = Transition(label='Field Brief')
fl   = Transition(label='Feedback Loop')
cr   = Transition(label='Crisis Review')
ls   = Transition(label='Lessons Share')

# Phase 1: initial assessment and coordination
decisionPO = StrictPartialOrder(nodes=[rm, ps])
decisionPO.order.add_edge(rm, ps)
coordPO = StrictPartialOrder(nodes=[di, pa])
coordPO.order.add_edge(di, pa)
initialPO = StrictPartialOrder(nodes=[ta, ss, decisionPO, coordPO])
initialPO.order.add_edge(ta, ss)
initialPO.order.add_edge(ss, decisionPO)
initialPO.order.add_edge(ss, coordPO)

# Phase 2: contingency management loop
contPO = StrictPartialOrder(nodes=[rmg, cs])
contPO.order.add_edge(rmg, cs)
supplyLoop = OperatorPOWL(operator=Operator.LOOP, children=[sc, contPO])

# Phase 3: dynamic routing with feedback loop
routeSeq = StrictPartialOrder(nodes=[rp, ad, tt, fb])
routeSeq.order.add_edge(rp, ad)
routeSeq.order.add_edge(ad, tt)
routeSeq.order.add_edge(tt, fb)
routeLoop = OperatorPOWL(operator=Operator.LOOP, children=[routeSeq, fl])

# Phase 4: post‐crisis evaluation
evalPO = StrictPartialOrder(nodes=[cr, ls])
evalPO.order.add_edge(cr, ls)

# Assemble the overall POWL model
root = StrictPartialOrder(nodes=[initialPO, supplyLoop, routeLoop, evalPO])
root.order.add_edge(initialPO, supplyLoop)
root.order.add_edge(supplyLoop, routeLoop)
root.order.add_edge(routeLoop, evalPO)