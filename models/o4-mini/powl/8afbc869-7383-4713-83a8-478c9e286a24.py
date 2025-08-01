# Generated from: 8afbc869-7383-4713-83a8-478c9e286a24.json
# Description: This process outlines the complex journey of artisanal cheese from small-scale farms to niche gourmet retailers. It involves milk sourcing with strict quality criteria, traditional curdling and aging techniques, rigorous sensory testing, custom packaging, and coordinating temperature-controlled logistics. Additionally, the process integrates direct farmer feedback loops, seasonal production adjustments, and targeted marketing strategies to maintain product authenticity and meet fluctuating demand in specialty markets. It also includes compliance with regional food safety regulations and proactive risk management to handle spoilage or supply disruptions, ensuring a consistent supply of high-quality artisan cheese to discerning consumers.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as POWL transitions
milk = Transition(label="Milk Sourcing")
quality = Transition(label="Quality Testing")
batch = Transition(label="Batch Mixing")
curd = Transition(label="Curd Formation")
whey = Transition(label="Whey Separation")
mold = Transition(label="Mold Inoculation")
press = Transition(label="Pressing Cheese")
aging = Transition(label="Cave Aging")
sensory = Transition(label="Sensory Check")
pack_design = Transition(label="Packaging Design")
label_print = Transition(label="Label Printing")
cold = Transition(label="Cold Storage")
order_proc = Transition(label="Order Processing")
schedule = Transition(label="Shipment Scheduling")
retail = Transition(label="Retail Delivery")
feedback = Transition(label="Farmer Feedback")
demand = Transition(label="Demand Forecast")

# Silent transitions for compliance and risk management
compliance = SilentTransition()
risk_mgmt = SilentTransition()

# Loop: after each Sensory Check, either exit or go to Farmer Feedback then back to Sensory Check
loop_sf = OperatorPOWL(operator=Operator.LOOP, children=[sensory, feedback])

# Construct the partial order
root = StrictPartialOrder(nodes=[
    demand,
    milk,
    quality,
    compliance,
    batch,
    curd,
    whey,
    mold,
    press,
    aging,
    loop_sf,
    pack_design,
    label_print,
    risk_mgmt,
    cold,
    order_proc,
    schedule,
    retail
])

# Define the ordering relations
root.order.add_edge(demand, milk)
root.order.add_edge(milk, quality)
root.order.add_edge(quality, compliance)
root.order.add_edge(compliance, batch)
root.order.add_edge(batch, curd)
root.order.add_edge(curd, whey)
root.order.add_edge(whey, mold)
root.order.add_edge(mold, press)
root.order.add_edge(press, aging)
root.order.add_edge(aging, loop_sf)
root.order.add_edge(loop_sf, pack_design)
root.order.add_edge(pack_design, label_print)
root.order.add_edge(label_print, risk_mgmt)
root.order.add_edge(risk_mgmt, cold)
root.order.add_edge(cold, order_proc)
root.order.add_edge(order_proc, schedule)
root.order.add_edge(schedule, retail)