# Generated from: db0593b2-bab6-406e-9c49-63389b4817a0.json
# Description: This process outlines the establishment of an urban vertical farming system within a repurposed industrial building. It involves site assessment, environmental analysis, modular structure installation, automated irrigation setup, crop selection based on local demand and climate simulation, nutrient solution formulation, lighting system calibration, pest monitoring using AI-driven sensors, staff training on hydroponic techniques, integration of renewable energy sources, real-time data analytics implementation for crop health, waste recycling strategy, marketing channel development for fresh produce, and continuous process optimization to maximize yield while minimizing resource consumption and environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SA = Transition(label='Site Assess')
EA = Transition(label='Env Analysis')
MI = Transition(label='Modular Install')
IS = Transition(label='Irrigation Setup')
CS = Transition(label='Crop Selection')
NM = Transition(label='Nutrient Mix')
LC = Transition(label='Lighting Calibrate')
PM = Transition(label='Pest Monitor')
ST = Transition(label='Staff Training')
EI = Transition(label='Energy Integrate')
DA = Transition(label='Data Analytics')
WR = Transition(label='Waste Recycle')
MD = Transition(label='Market Develop')
YO = Transition(label='Yield Optimize')
CL = Transition(label='Climate Simulate')

# Crop Selection depends on Crop Selection done based on local demand and climate simulation
# So first simulate climate, then choose crop

# We'll build partial orders reflecting dependencies:

# Site Assess → Env Analysis → Modular Install → Irrigation Setup

# Climate Simulate and Crop Selection form a small partial order:
# Climate Simulate --> Crop Selection

# Nutrient Mix depends after Crop Selection
# Lighting Calibrate depends after Nutrient Mix
# Pest Monitor depends after Lighting Calibrate
# Staff Training depends after Pest Monitor
# Energy Integrate depends after Staff Training

# Data Analytics, Waste Recycle, Market Develop depend after Energy Integrate

# Yield Optimize depends after Data Analytics, Waste Recycle, Market Develop (all these three are concurrent)

root = StrictPartialOrder(nodes=[
    SA, EA, MI, IS, CL, CS, NM, LC, PM, ST, EI, DA, WR, MD, YO
])

# Adding edges per the described ordering:
root.order.add_edge(SA, EA)
root.order.add_edge(EA, MI)
root.order.add_edge(MI, IS)
root.order.add_edge(IS, CL)
root.order.add_edge(CL, CS)
root.order.add_edge(CS, NM)
root.order.add_edge(NM, LC)
root.order.add_edge(LC, PM)
root.order.add_edge(PM, ST)
root.order.add_edge(ST, EI)
root.order.add_edge(EI, DA)
root.order.add_edge(EI, WR)
root.order.add_edge(EI, MD)
root.order.add_edge(DA, YO)
root.order.add_edge(WR, YO)
root.order.add_edge(MD, YO)