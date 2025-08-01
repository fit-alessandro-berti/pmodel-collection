# Generated from: 6b663351-8879-4958-8b72-e224005a8920.json
# Description: This process involves the meticulous restoration of historical artifacts that have been damaged or deteriorated over time. It begins with an initial assessment to evaluate the artifact's condition and material composition, followed by detailed documentation and imaging. After analysis, a tailored conservation plan is developed, incorporating both traditional craftsmanship and modern scientific techniques. The artifact then undergoes careful cleaning, structural stabilization, and surface treatment to halt further decay. Specialized repairs are performed using compatible materials, and any missing components are recreated with precision. Throughout the restoration, ongoing monitoring ensures environmental conditions remain optimal. Finally, a comprehensive report is generated, and the artifact is prepared for display or storage under controlled conditions, preserving cultural heritage for future generations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
ia = Transition(label='Initial Assess')
mt = Transition(label='Material Test')
cm = Transition(label='Condition Map')
iscan = Transition(label='Imaging Scan')
pd = Transition(label='Plan Draft')
ts = Transition(label='Tool Setup')
sc = Transition(label='Surface Clean')
sf = Transition(label='Structural Fix')
ra = Transition(label='Repair Apply')
cmp = Transition(label='Component Mold')
mm = Transition(label='Material Match')
se = Transition(label='Stabilize Env')
qc = Transition(label='Quality Check')
rw = Transition(label='Report Write')
ap = Transition(label='Artifact Pack')

# Silent skip
skip = SilentTransition()

# Choice: recreate missing components or skip
comp_seq = StrictPartialOrder(nodes=[cmp, mm])
comp_seq.order.add_edge(cmp, mm)
comp_choice = OperatorPOWL(operator=Operator.XOR, children=[comp_seq, skip])

# Loop: ongoing environment stabilization
loop_env = OperatorPOWL(operator=Operator.LOOP, children=[se, skip])

# Build the overall partial order
root = StrictPartialOrder(
    nodes=[ia, mt, cm, iscan, pd, ts, sc, sf, ra, comp_choice, loop_env, qc, rw, ap]
)

# Define dependencies
# Initial assessment then tests and mapping (concurrent)
root.order.add_edge(ia, mt)
root.order.add_edge(ia, cm)
root.order.add_edge(ia, iscan)
# After all three, draft the plan
root.order.add_edge(mt, pd)
root.order.add_edge(cm, pd)
root.order.add_edge(iscan, pd)
# Then tool setup and core restoration steps
root.order.add_edge(pd, ts)
root.order.add_edge(ts, sc)
root.order.add_edge(sc, sf)
root.order.add_edge(sf, ra)
# After specialized repairs, branch to component recreation or skip
root.order.add_edge(ra, comp_choice)
# Environment stabilization runs concurrently from tool setup until quality check
root.order.add_edge(ts, loop_env)
# Both restoration branch and environment loop must finish before quality check
root.order.add_edge(comp_choice, qc)
root.order.add_edge(loop_env, qc)
# Final reporting and packing
root.order.add_edge(qc, rw)
root.order.add_edge(rw, ap)