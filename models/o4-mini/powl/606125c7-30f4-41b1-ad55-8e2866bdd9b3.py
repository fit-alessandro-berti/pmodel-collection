# Generated from: 606125c7-30f4-41b1-ad55-8e2866bdd9b3.json
# Description: This process manages the entire lifecycle of an urban vertical farm, integrating automated crop cultivation with environmental controls and real-time data analytics. It starts with seed selection based on AI-driven market demand forecasts, followed by nutrient solution formulation tailored to each plant species. The system then initiates germination under controlled humidity and light conditions, transitioning to automated transplanting into vertical racks. Continuous monitoring via IoT sensors adjusts watering, lighting, and temperature dynamically. Crop health is assessed using drone-based multispectral imaging, triggering pest control measures or nutrient adjustments as needed. Harvest scheduling optimizes yield and freshness, while post-harvest processing includes automated packaging and cold storage. Finally, waste from plant residues is processed into bio-compost, closing the sustainability loop. This atypical agricultural process leverages advanced technology to maximize productivity in limited urban spaces, ensuring fresh produce availability with minimal environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
df = Transition(label='Demand Forecast')
ss = Transition(label='Seed Select')
nm = Transition(label='Nutrient Mix')
gs = Transition(label='Germination Start')
ha = Transition(label='Humidity Adjust')
lc_init = Transition(label='Light Control')
tr = Transition(label='Transplant Racks')
iot = Transition(label='IoT Monitor')
wa = Transition(label='Watering Adjust')
lc_adj = Transition(label='Light Control')
tc = Transition(label='Temp Control')
ds = Transition(label='Drone Scan')
pc = Transition(label='Pest Control')
hp = Transition(label='Harvest Plan')
ap = Transition(label='Auto Package')
cs = Transition(label='Cold Storage')
wp = Transition(label='Waste Process')
bc = Transition(label='Bio-Compost')

# Silent transitions for optional behaviors
skip_adj = SilentTransition()
skip_pest = SilentTransition()

# Choice of dynamic adjustments in each monitoring cycle
adjust_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[wa, lc_adj, tc, skip_adj]
)

# Loop: monitor → adjust (repeat until exit)
loop_adjust = OperatorPOWL(
    operator=Operator.LOOP,
    children=[iot, adjust_choice]
)

# Optional pest control after drone scan
pest_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[pc, skip_pest]
)

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    df, ss, nm,
    gs, ha, lc_init, tr,
    loop_adjust,
    ds, pest_choice,
    hp, ap, cs,
    wp, bc
])

# Define the control‐flow edges
root.order.add_edge(df, ss)
root.order.add_edge(ss, nm)
root.order.add_edge(nm, gs)
root.order.add_edge(gs, ha)
root.order.add_edge(gs, lc_init)
root.order.add_edge(ha, tr)
root.order.add_edge(lc_init, tr)
root.order.add_edge(tr, loop_adjust)
root.order.add_edge(loop_adjust, ds)
root.order.add_edge(ds, pest_choice)
root.order.add_edge(pest_choice, hp)
root.order.add_edge(hp, ap)
root.order.add_edge(ap, cs)
root.order.add_edge(cs, wp)
root.order.add_edge(wp, bc)