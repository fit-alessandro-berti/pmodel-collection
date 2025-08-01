# Generated from: acdbef5f-82bd-4032-8513-76f7f49cb397.json
# Description: This process involves sourcing rare milk varieties from multiple micro-dairies, followed by precision aging in controlled environments. Each batch undergoes microbiological testing and sensory evaluation before packaging. The logistics team coordinates temperature-sensitive transport to specialty retailers, while marketing crafts bespoke campaigns targeting niche gourmet consumers. Inventory management adapts dynamically according to seasonal milk yields and demand fluctuations. Regulatory compliance checks ensure adherence to evolving food safety standards. The process culminates in customer feedback collection to refine future production cycles, balancing artisanal quality with scalable distribution challenges.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Milk_Sourcing = Transition(label='Milk Sourcing')
Batch_Testing = Transition(label='Batch Testing')
Microbial_Check = Transition(label='Microbial Check')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Curd_Formation = Transition(label='Curd Formation')
Press_Cheese = Transition(label='Press Cheese')
Controlled_Aging = Transition(label='Controlled Aging')
Sensory_Review = Transition(label='Sensory Review')
Package_Cheese = Transition(label='Package Cheese')
Temp_Transport = Transition(label='Temp Transport')
Retail_Distribution = Transition(label='Retail Distribution')
Market_Campaign = Transition(label='Market Campaign')
Inventory_Monitor = Transition(label='Inventory Monitor')
Compliance_Audit = Transition(label='Compliance Audit')
Feedback_Collect = Transition(label='Feedback Collect')
Demand_Forecast = Transition(label='Demand Forecast')

# Partial order on cheese production and testing pipeline:
# Milk sourcing leads to milk pasteurize (assumed before microbial check),
# then microbial check, then batch testing,
# then curd formation and pressing cheese (these two can be concurrent or ordered; 
# press cheese logically after curd formation)
# followed by controlled aging, sensory review, and packaging.
cheese_production = StrictPartialOrder(nodes=[
    Milk_Sourcing,
    Milk_Pasteurize,
    Microbial_Check,
    Batch_Testing,
    Curd_Formation,
    Press_Cheese,
    Controlled_Aging,
    Sensory_Review,
    Package_Cheese
])
cheese_production.order.add_edge(Milk_Sourcing, Milk_Pasteurize)
cheese_production.order.add_edge(Milk_Pasteurize, Microbial_Check)
cheese_production.order.add_edge(Microbial_Check, Batch_Testing)
cheese_production.order.add_edge(Batch_Testing, Curd_Formation)
cheese_production.order.add_edge(Curd_Formation, Press_Cheese)
cheese_production.order.add_edge(Press_Cheese, Controlled_Aging)
cheese_production.order.add_edge(Controlled_Aging, Sensory_Review)
cheese_production.order.add_edge(Sensory_Review, Package_Cheese)

# Logistics branch: temp transport then retail distribution
logistics = StrictPartialOrder(nodes=[Temp_Transport, Retail_Distribution])
logistics.order.add_edge(Temp_Transport, Retail_Distribution)

# Marketing branch: market campaign and demand forecast concurrent; inventory monitor ordered after demand forecast
marketing = StrictPartialOrder(nodes=[Market_Campaign, Demand_Forecast, Inventory_Monitor])
marketing.order.add_edge(Demand_Forecast, Inventory_Monitor)

# Compliance audit standalone

# Final process order connects major subprocesses:
# 1) cheese production pipeline
# 2) logistics
# 3) marketing-inventory
# 4) compliance audit
# 5) feedback collection at the end

root = StrictPartialOrder(nodes=[
    cheese_production,
    logistics,
    marketing,
    Compliance_Audit,
    Feedback_Collect
])

# Order edges chaining major subprocesses:
root.order.add_edge(cheese_production, logistics)
root.order.add_edge(cheese_production, marketing)
root.order.add_edge(logistics, Compliance_Audit)
root.order.add_edge(marketing, Compliance_Audit)
root.order.add_edge(Compliance_Audit, Feedback_Collect)