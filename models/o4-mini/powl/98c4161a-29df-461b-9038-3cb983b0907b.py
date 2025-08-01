# Generated from: 98c4161a-29df-461b-9038-3cb983b0907b.json
# Description: This process describes the onboarding and setup of an urban vertical farming operation within a repurposed commercial building. It involves multi-disciplinary coordination including site analysis, environmental control calibration, crop selection tailored to micro-climates, integration of IoT sensors for real-time monitoring, and staff training on automated nutrient delivery systems. The process also covers regulatory compliance checks, sustainability assessments, and market launch strategy to ensure the farm meets local food demand efficiently while minimizing resource consumption and environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
ss = Transition(label='Site Survey')
sa = Transition(label='Structural Audit')
cm = Transition(label='Climate Mapping')
cs = Transition(label='Crop Selection')
si = Transition(label='Sensor Install')
sc = Transition(label='System Calibrate')
ns = Transition(label='Nutrient Setup')
wt = Transition(label='Water Testing')
st = Transition(label='Staff Training')
cc = Transition(label='Compliance Check')
ea = Transition(label='Energy Audit')
wp = Transition(label='Waste Plan')
di = Transition(label='Data Integration')
mr = Transition(label='Market Research')
lp = Transition(label='Launch Planning')

# Build the partial order
root = StrictPartialOrder(nodes=[ss, sa, cm, cs, si, sc, ns, wt, st, cc, ea, wp, di, mr, lp])

# Site survey prerequisites
root.order.add_edge(ss, sa)   # Site Survey -> Structural Audit
root.order.add_edge(ss, cm)   # Site Survey -> Climate Mapping

# Structural audit leads to sustainability assessments
root.order.add_edge(sa, ea)   # Structural Audit -> Energy Audit
root.order.add_edge(sa, wp)   # Structural Audit -> Waste Plan

# Prerequisites for sensor installation
root.order.add_edge(ss, si)
root.order.add_edge(sa, si)
root.order.add_edge(cm, si)

# Calibration and data integration
root.order.add_edge(si, sc)   # Sensor Install -> System Calibrate
root.order.add_edge(sc, di)   # System Calibrate -> Data Integration

# Crop selection based on climate mapping
root.order.add_edge(cm, cs)   # Climate Mapping -> Crop Selection

# Nutrient setup and water testing
root.order.add_edge(cs, ns)   # Crop Selection -> Nutrient Setup
root.order.add_edge(sc, ns)   # System Calibrate -> Nutrient Setup
root.order.add_edge(ns, wt)   # Nutrient Setup -> Water Testing

# Staff training after calibration and nutrient setup
root.order.add_edge(sc, st)
root.order.add_edge(ns, st)

# Compliance check after sustainability assessments
root.order.add_edge(ea, cc)
root.order.add_edge(wp, cc)

# Market research once climate and crop selection are done
root.order.add_edge(cm, mr)
root.order.add_edge(cs, mr)

# Final launch planning depends on all readiness and research
root.order.add_edge(cc, lp)
root.order.add_edge(st, lp)
root.order.add_edge(wt, lp)
root.order.add_edge(di, lp)
root.order.add_edge(mr, lp)