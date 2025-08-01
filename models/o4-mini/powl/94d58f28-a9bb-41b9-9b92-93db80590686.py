# Generated from: 94d58f28-a9bb-41b9-9b92-93db80590686.json
# Description: This process encompasses the unique steps involved in producing and distributing artisanal cheese from farm to gourmet retailer. It begins with selecting rare milk breeds and monitoring animal diet to influence flavor profiles. The milk undergoes micro-filtering and custom fermentation using wild cultures. Aging occurs in controlled microclimates with periodic turning and humidity adjustments. Quality is assessed through sensory panels and microbial analysis. Packaging utilizes biodegradable materials with embedded QR codes detailing provenance. Finally, logistics involve temperature-monitored transport and boutique delivery, ensuring freshness and traceability throughout the supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
breed_select    = Transition(label="Breed Select")
diet_monitor    = Transition(label="Diet Monitor")
milk_harvest    = Transition(label="Milk Harvest")
micro_filter    = Transition(label="Micro Filter")
wild_culture    = Transition(label="Wild Culture")
custom_ferment  = Transition(label="Custom Ferment")
curd_cut        = Transition(label="Curd Cut")
press_form      = Transition(label="Press Form")
micro_age       = Transition(label="Microclimate Age")
turn_cheese     = Transition(label="Turn Cheese")
humidity_adjust = Transition(label="Humidity Adjust")
sensory_panel   = Transition(label="Sensory Panel")
microbial_test  = Transition(label="Microbial Test")
eco_package     = Transition(label="Eco Package")
qr_code         = Transition(label="QR Code")
temp_transport  = Transition(label="Temp Transport")
boutique_deliver= Transition(label="Boutique Deliver")

# Loop for aging with periodic turning and humidity adjustments
loop_body = StrictPartialOrder(nodes=[turn_cheese, humidity_adjust])
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[micro_age, loop_body])

# Assemble the full workflow as a strict partial order
root = StrictPartialOrder(nodes=[
    breed_select, diet_monitor, milk_harvest,
    micro_filter, wild_culture, custom_ferment,
    curd_cut, press_form, aging_loop,
    sensory_panel, microbial_test,
    eco_package, qr_code,
    temp_transport, boutique_deliver
])

# Define control-flow edges
root.order.add_edge(breed_select,    diet_monitor)
root.order.add_edge(diet_monitor,    milk_harvest)
root.order.add_edge(milk_harvest,    micro_filter)
root.order.add_edge(micro_filter,    wild_culture)
root.order.add_edge(wild_culture,    custom_ferment)
root.order.add_edge(custom_ferment,  curd_cut)
root.order.add_edge(curd_cut,        press_form)
root.order.add_edge(press_form,      aging_loop)

# After aging loop, quality checks in parallel
root.order.add_edge(aging_loop,      sensory_panel)
root.order.add_edge(aging_loop,      microbial_test)

# Packaging begins once both quality checks are done
root.order.add_edge(sensory_panel,   eco_package)
root.order.add_edge(microbial_test,  eco_package)
root.order.add_edge(eco_package,     qr_code)

# Logistics after packaging
root.order.add_edge(qr_code,         temp_transport)
root.order.add_edge(temp_transport,  boutique_deliver)