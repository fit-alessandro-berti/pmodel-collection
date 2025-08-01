# Generated from: cbacbefb-0c7d-4b92-8e3e-fa461cba3574.json
# Description: This process encompasses the planning, development, and operational launch of a multi-level urban vertical farm designed to maximize limited space within city environments. It involves site analysis, modular infrastructure installation, climate control calibration, nutrient solution preparation, crop cycle scheduling, integrated pest management, and real-time sensor network deployment. The workflow ensures sustainable resource use, compliance with urban agricultural regulations, and continuous yield optimization through data-driven decisions, enabling efficient production of fresh produce for local markets and reducing transportation emissions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
SA = Transition(label='Site Analysis')
DL = Transition(label='Design Layout')
MA = Transition(label='Module Assembly')
CS = Transition(label='Climate Setup')
SI = Transition(label='Sensor Install')
WT = Transition(label='Water Testing')
NM = Transition(label='Nutrient Mix')
SS = Transition(label='Seed Selection')
PP = Transition(label='Planting Phase')
GM = Transition(label='Growth Monitor')
PC = Transition(label='Pest Control')
HP = Transition(label='Harvest Plan')
YA = Transition(label='Yield Audit')
PPp = Transition(label='Packaging Prep')
MD = Transition(label='Market Delivery')
WR = Transition(label='Waste Recycling')

# Silent transition for loop exit
skip = SilentTransition()

# Loop for continuous growth monitoring and pest control
growth_cycle = StrictPartialOrder(nodes=[GM, PC])
growth_cycle.order.add_edge(GM, PC)
loop_growth = OperatorPOWL(operator=Operator.LOOP, children=[growth_cycle, skip])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    SA, DL, MA, CS, SI, WT, NM, SS, PP,
    loop_growth,
    HP, YA, PPp, MD, WR
])

# Sequential dependencies
root.order.add_edge(SA, DL)
root.order.add_edge(DL, MA)
root.order.add_edge(MA, CS)
root.order.add_edge(CS, SI)
root.order.add_edge(SI, WT)
root.order.add_edge(WT, NM)
root.order.add_edge(NM, SS)
root.order.add_edge(SS, PP)

# After planting, enter the growth & pest-control loop
root.order.add_edge(PP, loop_growth)

# After exiting the loop, proceed to harvest and post-harvest steps
root.order.add_edge(loop_growth, HP)
root.order.add_edge(HP, YA)
root.order.add_edge(YA, PPp)
root.order.add_edge(PPp, MD)
root.order.add_edge(MD, WR)