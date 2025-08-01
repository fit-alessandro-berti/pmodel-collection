# Generated from: 07e3abde-0328-4c9d-a097-b302a88391fa.json
# Description: This process involves sourcing rare milk varieties from micro-dairies, performing microbial culture selection, and carefully controlling aging conditions to produce unique artisan cheeses. It includes quality testing, packaging in eco-friendly materials, coordinating limited batch logistics, and managing niche market demand forecasts. The process requires close collaboration with local farmers, regulatory compliance checks, and continuous product innovation to maintain exclusivity and high standards in a competitive gourmet market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
farmer_liaison     = Transition(label='Farmer Liaison')
milk_sourcing      = Transition(label='Milk Sourcing')
culture_selection  = Transition(label='Culture Selection')
pasteurization_chk = Transition(label='Pasteurization Check')
curd_formation     = Transition(label='Curd Formation')
pressing_cheese    = Transition(label='Pressing Cheese')
salting_process    = Transition(label='Salting Process')
aging_setup        = Transition(label='Aging Setup')
humidity_control   = Transition(label='Humidity Control')
quality_testing    = Transition(label='Quality Testing')
packaging_prep     = Transition(label='Packaging Prep')
eco_packaging      = Transition(label='Eco Packaging')
batch_tracking     = Transition(label='Batch Tracking')
logistics_plan     = Transition(label='Logistics Plan')
market_forecast    = Transition(label='Market Forecast')
regulatory_audit   = Transition(label='Regulatory Audit')
product_innovation = Transition(label='Product Innovation')

# A silent transition for the loop exit
skip = SilentTransition()

# Loop for continuous product innovation
innovation_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[product_innovation, skip]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    farmer_liaison,
    milk_sourcing,
    culture_selection,
    pasteurization_chk,
    curd_formation,
    pressing_cheese,
    salting_process,
    aging_setup,
    humidity_control,
    quality_testing,
    packaging_prep,
    eco_packaging,
    batch_tracking,
    logistics_plan,
    market_forecast,
    regulatory_audit,
    innovation_loop
])

# Define control‐flow (ordering) dependencies
o = root.order
o.add_edge(farmer_liaison,    milk_sourcing)
o.add_edge(milk_sourcing,     culture_selection)
o.add_edge(culture_selection, pasteurization_chk)
o.add_edge(pasteurization_chk, curd_formation)
o.add_edge(curd_formation,    pressing_cheese)
o.add_edge(pressing_cheese,   salting_process)
o.add_edge(salting_process,   aging_setup)
o.add_edge(aging_setup,       humidity_control)
o.add_edge(humidity_control,  quality_testing)

# After quality testing: packaging, audit, forecast
o.add_edge(quality_testing,    packaging_prep)
o.add_edge(packaging_prep,     eco_packaging)
o.add_edge(eco_packaging,      batch_tracking)
o.add_edge(batch_tracking,     logistics_plan)

o.add_edge(quality_testing,    regulatory_audit)
o.add_edge(regulatory_audit,   eco_packaging)

o.add_edge(batch_tracking,     market_forecast)
o.add_edge(market_forecast,    logistics_plan)

# After logistics, loop back to innovation
o.add_edge(logistics_plan,     innovation_loop)