# Generated from: 92425317-a96e-4652-8425-2730c862f657.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farming system within a repurposed industrial building. The workflow begins with site analysis and environmental assessment, followed by modular farm design, nutrient solution formulation, and system integration of hydroponics and aeroponics. It includes procurement of specialized lighting, sensor calibration, and automation programming for climate control. Subsequent activities involve crop selection based on market trends, seedling propagation, and installation of water recycling mechanisms. Continuous monitoring, pest management using biological controls, and yield forecasting are also integral. The process concludes with packaging design, supply chain coordination, and community engagement to promote sustainable urban agriculture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
sa = Transition(label='Site Analysis')
ea = Transition(label='Env Assessment')
md = Transition(label='Modular Design')
nm = Transition(label='Nutrient Mix')
ss = Transition(label='System Setup')
li = Transition(label='Lighting Install')
sensor = Transition(label='Sensor Setup')
auto = Transition(label='Automation Prog')
cs = Transition(label='Crop Selection')
seed = Transition(label='Seedling Start')
water = Transition(label='Water Recycle')
pest = Transition(label='Pest Control')
yieldf = Transition(label='Yield Forecast')
pack = Transition(label='Packaging Plan')
supply = Transition(label='Supply Sync')
community = Transition(label='Community Out')

# Build the partial‐order workflow
root = StrictPartialOrder(
    nodes=[
        sa, ea, md, nm, ss,
        li, sensor, auto,
        cs, seed, water,
        pest, yieldf,
        pack, supply, community
    ]
)

# Sequential backbone up to system setup
root.order.add_edge(sa, ea)
root.order.add_edge(ea, md)
root.order.add_edge(md, nm)
root.order.add_edge(nm, ss)

# Procurement tasks in parallel after system setup
for t in (li, sensor, auto):
    root.order.add_edge(ss, t)

# Once lighting, sensors and automation are in place, choose crops
for t in (li, sensor, auto):
    root.order.add_edge(t, cs)

# After crop selection, start seedlings and install water recycling in parallel
root.order.add_edge(cs, seed)
root.order.add_edge(cs, water)

# After seedlings and water recycling, run pest control and yield forecast in parallel
for t in (seed, water):
    root.order.add_edge(t, pest)
    root.order.add_edge(t, yieldf)

# Packaging follows pest control and yield forecasting
root.order.add_edge(pest, pack)
root.order.add_edge(yieldf, pack)

# Supply chain synchronization then community outreach
root.order.add_edge(pack, supply)
root.order.add_edge(supply, community)