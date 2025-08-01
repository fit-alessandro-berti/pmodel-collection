# Generated from: 53d1a04f-2d5b-4757-aabd-e0435ed0d0cd.json
# Description: This process outlines a structured, iterative approach to generating breakthrough innovations by combining insights and technologies from disparate industries. It begins with Opportunity Scouting to identify unconventional problem spaces, followed by Cross-Pollination Workshops where multidisciplinary teams brainstorm and exchange domain knowledge. Prototyping leverages rapid, low-fidelity models to test core concepts, while Feedback Loops gather both internal and external stakeholder inputs to refine ideas. Parallel Pathways run simultaneous experiments in different sectors, increasing the chance of success. The Validation Gate assesses feasibility and potential impact before scaling. Finally, Knowledge Capture ensures lessons learned are documented for future cycles, promoting continuous improvement and fostering a culture of sustainable innovation beyond typical R&D pipelines.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the elementary activities
os = Transition(label="Opportunity Scout")
ih = Transition(label="Idea Harvest")
cp = Transition(label="Cross-Pollinate")
cs = Transition(label="Concept Sketch")
rp = Transition(label="Rapid Prototype")
ss = Transition(label="Stakeholder Sync")
fl = Transition(label="Feedback Loop")
resource_align = Transition(label="Resource Align")
parallel_experiment = Transition(label="Parallel Experiment")
risk_assess = Transition(label="Risk Assess")
vg = Transition(label="Validation Gate")
sp = Transition(label="Scale Plan")
pl = Transition(label="Pilot Launch")
ir = Transition(label="Impact Review")
kc = Transition(label="Knowledge Capture")
ci = Transition(label="Continuous Iterate")

# Build the core sequence (with a small parallel for the "Parallel Pathways" part)
core = StrictPartialOrder(
    nodes=[
        os,
        ih,
        cp,
        cs,
        rp,
        ss,
        fl,
        resource_align,
        parallel_experiment,
        risk_assess,
        vg,
        sp,
        pl,
        ir,
        kc,
    ]
)

# Sequential edges
core.order.add_edge(os, ih)
core.order.add_edge(ih, cp)
core.order.add_edge(cp, cs)
core.order.add_edge(cs, rp)
core.order.add_edge(rp, ss)
core.order.add_edge(ss, fl)

# After feedback, resource align and parallel experiment run in parallel
core.order.add_edge(fl, resource_align)
core.order.add_edge(fl, parallel_experiment)

# Both must complete before risk assessment
core.order.add_edge(resource_align, risk_assess)
core.order.add_edge(parallel_experiment, risk_assess)

# Finish the remainder of the sequence
core.order.add_edge(risk_assess, vg)
core.order.add_edge(vg, sp)
core.order.add_edge(sp, pl)
core.order.add_edge(pl, ir)
core.order.add_edge(ir, kc)

# Wrap in a LOOP: run 'core', then either exit or do 'Continuous Iterate' and run 'core' again
root = OperatorPOWL(operator=Operator.LOOP, children=[core, ci])