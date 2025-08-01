# Generated from: c121363a-d3d8-4399-92fc-785a72441319.json
# Description: This process manages the intricate supply chain for artisan cheese production, involving unique steps like milk sourcing from specific heritage breeds, microbial culture selection based on regional terroir, precise aging environment control, and customized packaging for niche markets. It also includes artisanal quality inspections, seasonal recipe adjustments, and direct collaboration with boutique retailers and specialty food events to ensure authenticity and premium customer experience throughout the product lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
BS = Transition(label='Breed Selection')
MH = Transition(label='Milk Harvest')
CP = Transition(label='Culture Prep')
MP = Transition(label='Milk Pasteurize')
CF = Transition(label='Curd Formation')
WD = Transition(label='Whey Drain')
MI = Transition(label='Mold Inoculate')
PC = Transition(label='Press Cheese')
SR = Transition(label='Salt Rub')
AM = Transition(label='Aging Monitor')
HC = Transition(label='Humidity Check')
FT = Transition(label='Flavor Test')
PD = Transition(label='Packaging Design')
RP = Transition(label='Retail Partner')
ES = Transition(label='Event Setup')
CFB = Transition(label='Customer Feedback')

# 1. Initial linear workflow up to salt rub
init = StrictPartialOrder(nodes=[BS, MH, CP, MP, CF, WD, MI, PC, SR])
linear_seq = [BS, MH, CP, MP, CF, WD, MI, PC, SR]
for i in range(len(linear_seq) - 1):
    init.order.add_edge(linear_seq[i], linear_seq[i+1])

# 2. Aging loop: concurrent monitoring then flavor test
monitor = StrictPartialOrder(nodes=[AM, HC])  # Aging Monitor and Humidity Check in parallel
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor, FT])

# 3. Packaging and collaboration, then feedback
# Build the top-level partial order
root = StrictPartialOrder(nodes=[init, aging_loop, PD, RP, ES, CFB])

# Connect the segments
root.order.add_edge(init, aging_loop)       # After salt rub -> start aging loop
root.order.add_edge(aging_loop, PD)         # After aging -> packaging design
root.order.add_edge(PD, RP)                 # Packaging -> retail partner
root.order.add_edge(PD, ES)                 # Packaging -> event setup
root.order.add_edge(RP, CFB)                # Retail collaboration -> feedback
root.order.add_edge(ES, CFB)                # Event setup -> feedback