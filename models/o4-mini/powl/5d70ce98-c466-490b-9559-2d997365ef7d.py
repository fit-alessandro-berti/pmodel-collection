# Generated from: 5d70ce98-c466-490b-9559-2d997365ef7d.json
# Description: This process details the comprehensive operational cycle of an urban vertical farm that integrates automated hydroponics, AI-driven climate control, and real-time crop health monitoring. It begins with seed selection based on market demand predictions, followed by nutrient solution preparation and precise planting. Growth phases are continuously optimized through sensor data analytics and robotic pruning. Concurrently, pest detection algorithms trigger targeted biological interventions. Harvesting is automated, with quality sorting and packaging adapting dynamically to supply chain requirements. Waste biomass is processed on-site for energy recovery, closing the sustainability loop. The process concludes with data-driven reporting to improve future yield forecasts and resource efficiency, ensuring a resilient urban agriculture model.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
df = Transition(label='Demand Forecast')
ss = Transition(label='Seed Select')
nm = Transition(label='Nutrient Mix')
ps = Transition(label='Plant Setup')

ca = Transition(label='Climate Adjust')
sm = Transition(label='Sensor Monitor')
ga = Transition(label='Growth Analyze')
rp = Transition(label='Robotic Prune')
pd = Transition(label='Pest Detect')
bi = Transition(label='Bio Intervention')

ah = Transition(label='Auto Harvest')
qs = Transition(label='Quality Sort')
dp = Transition(label='Dynamic Pack')
wp = Transition(label='Waste Process')
dr = Transition(label='Data Report')
yf = Transition(label='Yield Forecast')

# Build the intervention partial order (concurrent interventions with pest→bio ordering)
po_interventions = StrictPartialOrder(nodes=[ga, rp, ca, pd, bi])
po_interventions.order.add_edge(pd, bi)

# Growth loop: monitor, then either exit or do all interventions and repeat
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[sm, po_interventions])

# Main process partial order
root = StrictPartialOrder(
    nodes=[df, ss, nm, ps, growth_loop, ah, qs, dp, wp, dr, yf]
)

# Sequential dependencies
root.order.add_edge(df, ss)
root.order.add_edge(ss, nm)
root.order.add_edge(nm, ps)
root.order.add_edge(ps, growth_loop)
root.order.add_edge(growth_loop, ah)
root.order.add_edge(ah, qs)
root.order.add_edge(qs, dp)
root.order.add_edge(dp, wp)
root.order.add_edge(wp, dr)
root.order.add_edge(dr, yf)