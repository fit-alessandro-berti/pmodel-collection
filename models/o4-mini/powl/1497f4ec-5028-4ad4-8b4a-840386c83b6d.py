# Generated from: 1497f4ec-5028-4ad4-8b4a-840386c83b6d.json
# Description: This process involves establishing a multi-tiered urban vertical farm within a repurposed warehouse. It includes site analysis, structural retrofitting, climate control installation, hydroponic system setup, seed selection, nutrient calibration, automated monitoring deployment, pest management integration, crop scheduling, continuous yield assessment, and community engagement initiatives. The objective is to maximize crop output within limited urban spaces while ensuring sustainability and minimal environmental impact through advanced automation and data-driven cultivation techniques.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ss = Transition(label='Site Survey')
sr = Transition(label='Structure Retrofit')
hvac = Transition(label='HVAC Install')
lighting = Transition(label='Lighting Setup')
hydro = Transition(label='Hydroponics Init')
seed = Transition(label='Seed Selection')
nm = Transition(label='Nutrient Mix')
sd = Transition(label='Sensor Deploy')
pc = Transition(label='Pest Control')
ip = Transition(label='Irrigation Plan')
cs = Transition(label='Crop Scheduling')
ym = Transition(label='Yield Monitor')
da = Transition(label='Data Analysis')
wr = Transition(label='Waste Recycle')
co = Transition(label='Community Outreach')
ea = Transition(label='Energy Audit')

# Silent transition for loop exit
skip = SilentTransition()

# Define the cycle of cultivation tasks: Nutrient Mix -> Sensor Deploy -> Pest Control ->
# Irrigation Plan -> Crop Scheduling -> Yield Monitor -> Data Analysis -> Waste Recycle
cycle = StrictPartialOrder(nodes=[nm, sd, pc, ip, cs, ym, da, wr])
cycle.order.add_edge(nm, sd)
cycle.order.add_edge(sd, pc)
cycle.order.add_edge(pc, ip)
cycle.order.add_edge(ip, cs)
cycle.order.add_edge(cs, ym)
cycle.order.add_edge(ym, da)
cycle.order.add_edge(da, wr)

# Loop: repeat the entire cycle until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[cycle, skip])

# Assemble the full process partial order
root = StrictPartialOrder(
    nodes=[ss, sr, hvac, lighting, hydro, seed, loop, co, ea]
)

# Define the control-flow dependencies
root.order.add_edge(ss, sr)
root.order.add_edge(sr, hvac)
root.order.add_edge(sr, lighting)
root.order.add_edge(hvac, hydro)
root.order.add_edge(lighting, hydro)
root.order.add_edge(hydro, seed)
root.order.add_edge(seed, loop)
root.order.add_edge(loop, co)
root.order.add_edge(loop, ea)