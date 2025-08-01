# Generated from: 04f613a5-3ae2-455f-8a74-09c0fee36d56.json
# Description: This process outlines the establishment of a sustainable urban rooftop farming system in a densely populated city. It involves site assessment, structural analysis, soil testing, and environmental impact evaluation. The process also includes sourcing organic seeds, installing hydroponic systems, setting up automated irrigation, and integrating renewable energy sources. Additionally, it covers obtaining necessary permits, training local staff, implementing pest control measures, monitoring crop health with IoT sensors, harvesting schedules, and establishing distribution channels to local markets. The goal is to create a resilient, eco-friendly food production method within urban spaces that maximizes yield while minimizing environmental footprint and resource consumption.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# Define activities
ss   = Transition(label="Site Survey")
lc   = Transition(label="Load Check")
st   = Transition(label="Soil Test")
ie   = Transition(label="Impact Eval")
pa   = Transition(label="Permit Apply")
ssrc = Transition(label="Seed Source")
hi   = Transition(label="Hydro Install")
ir   = Transition(label="Irrigation Setup")
ec   = Transition(label="Energy Connect")
stt  = Transition(label="Staff Train")
pc   = Transition(label="Pest Control")
sd   = Transition(label="Sensor Deploy")
cm   = Transition(label="Crop Monitor")
hp   = Transition(label="Harvest Plan")
ml   = Transition(label="Market Link")

# Build the partial order
root = StrictPartialOrder(
    nodes=[ss, lc, st, ie, pa, ssrc, hi, ir, ec, stt, pc, sd, cm, hp, ml]
)

# Site Survey precedes structural, soil, and impact analyses
root.order.add_edge(ss, lc)
root.order.add_edge(ss, st)
root.order.add_edge(ss, ie)

# Analyses must finish before permit application
root.order.add_edge(lc, pa)
root.order.add_edge(st, pa)
root.order.add_edge(ie, pa)

# After permits are obtained, parallel preparatory tasks
root.order.add_edge(pa, ssrc)
root.order.add_edge(pa, hi)
root.order.add_edge(pa, ir)
root.order.add_edge(pa, ec)
root.order.add_edge(pa, stt)

# Equipment installation feeds sensor deployment
root.order.add_edge(hi, sd)
root.order.add_edge(ir, sd)
root.order.add_edge(ec, sd)

# Staff training precedes pest control
root.order.add_edge(stt, pc)

# Monitoring follows sensor deployment and pest control
root.order.add_edge(sd, cm)
root.order.add_edge(pc, cm)

# Harvest planning and market setup
root.order.add_edge(cm, hp)
root.order.add_edge(hp, ml)

# Seed sourcing informs harvest planning
root.order.add_edge(ssrc, hp)