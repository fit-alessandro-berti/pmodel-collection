# Generated from: 07e3abde-0328-4c9d-a097-b302a88391fa.json
# Description: This process involves sourcing rare milk varieties from micro-dairies, performing microbial culture selection, and carefully controlling aging conditions to produce unique artisan cheeses. It includes quality testing, packaging in eco-friendly materials, coordinating limited batch logistics, and managing niche market demand forecasts. The process requires close collaboration with local farmers, regulatory compliance checks, and continuous product innovation to maintain exclusivity and high standards in a competitive gourmet market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as labeled transitions
Milk_Sourcing = Transition(label='Milk Sourcing')
Culture_Selection = Transition(label='Culture Selection')
Pasteurization_Check = Transition(label='Pasteurization Check')
Curd_Formation = Transition(label='Curd Formation')
Pressing_Cheese = Transition(label='Pressing Cheese')
Salting_Process = Transition(label='Salting Process')
Aging_Setup = Transition(label='Aging Setup')
Humidity_Control = Transition(label='Humidity Control')
Quality_Testing = Transition(label='Quality Testing')
Packaging_Prep = Transition(label='Packaging Prep')
Eco_Packaging = Transition(label='Eco Packaging')
Batch_Tracking = Transition(label='Batch Tracking')
Logistics_Plan = Transition(label='Logistics Plan')
Market_Forecast = Transition(label='Market Forecast')
Regulatory_Audit = Transition(label='Regulatory Audit')
Farmer_Liaison = Transition(label='Farmer Liaison')
Product_Innovation = Transition(label='Product Innovation')

# First partial order: core production flow up to aging control
core_production = StrictPartialOrder(nodes=[Milk_Sourcing, Culture_Selection, Pasteurization_Check,
                                            Curd_Formation, Pressing_Cheese, Salting_Process,
                                            Aging_Setup, Humidity_Control])
core_production.order.add_edge(Milk_Sourcing, Culture_Selection)
core_production.order.add_edge(Culture_Selection, Pasteurization_Check)
core_production.order.add_edge(Pasteurization_Check, Curd_Formation)
core_production.order.add_edge(Curd_Formation, Pressing_Cheese)
core_production.order.add_edge(Pressing_Cheese, Salting_Process)
core_production.order.add_edge(Salting_Process, Aging_Setup)
core_production.order.add_edge(Aging_Setup, Humidity_Control)

# Second partial order: quality and packaging preparation flow
quality_packaging = StrictPartialOrder(nodes=[Quality_Testing, Packaging_Prep, Eco_Packaging])
quality_packaging.order.add_edge(Quality_Testing, Packaging_Prep)
quality_packaging.order.add_edge(Packaging_Prep, Eco_Packaging)

# Third partial order: logistics related activities
logistics = StrictPartialOrder(nodes=[Batch_Tracking, Logistics_Plan])
logistics.order.add_edge(Batch_Tracking, Logistics_Plan)

# Fourth partial order: market and compliance related
market_regulatory = StrictPartialOrder(nodes=[Market_Forecast, Regulatory_Audit, Farmer_Liaison])
market_regulatory.order.add_edge(Market_Forecast, Regulatory_Audit)
market_regulatory.order.add_edge(Regulatory_Audit, Farmer_Liaison)

# Product innovation can run concurrently with market_regulatory
# Combine market_regulatory and product innovation
market_innovation = StrictPartialOrder(nodes=[market_regulatory, Product_Innovation])
# No explicit order edges because Product Innovation runs concurrently with that entire sub-flow

# Combine all major subprocesses with a partial order reflecting logical dependencies
root = StrictPartialOrder(nodes=[core_production, quality_packaging, logistics, market_innovation])

# Define dependencies between subprocesses
# Quality testing depends on completion of Humidity Control (end of production flow)
root.order.add_edge(core_production, quality_packaging)
# Logistics depends on completion of packaging
root.order.add_edge(quality_packaging, logistics)
# Market / regulatory and innovation can start after logistics but run concurrently internally
root.order.add_edge(logistics, market_innovation)