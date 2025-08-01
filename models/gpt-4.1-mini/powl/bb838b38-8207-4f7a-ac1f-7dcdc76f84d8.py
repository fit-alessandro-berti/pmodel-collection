# Generated from: bb838b38-8207-4f7a-ac1f-7dcdc76f84d8.json
# Description: This process outlines the complex supply chain and quality assurance workflow for artisanal cheese production and distribution. It involves sourcing rare milk varieties from micro-farms, coordinating with seasonal fermentation experts, monitoring aging environments with IoT sensors, conducting multi-stage sensory evaluations, and managing bespoke packaging that preserves flavor profiles. Additionally, it includes negotiating with niche gourmet retailers and organizing exclusive tasting events to maintain brand prestige and customer engagement in a highly competitive niche market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Milk_Sourcing = Transition(label='Milk Sourcing')
Farm_Audit = Transition(label='Farm Audit')
Milk_Testing = Transition(label='Milk Testing')
Starter_Prep = Transition(label='Starter Prep')
Curd_Formation = Transition(label='Curd Formation')
Pressing_Stage = Transition(label='Pressing Stage')
Salt_Application = Transition(label='Salt Application')
Fermentation = Transition(label='Fermentation')
Humidity_Control = Transition(label='Humidity Control')
Flavor_Tasting = Transition(label='Flavor Tasting')
Aging_Log = Transition(label='Aging Log')
Packaging_Design = Transition(label='Packaging Design')
Shelf_Labeling = Transition(label='Shelf Labeling')
Retail_Negotiation = Transition(label='Retail Negotiation')
Tasting_Event = Transition(label='Tasting Event')
Customer_Feedback = Transition(label='Customer Feedback')

# Build sub-processes
# Milk quality & preparation partial order
milk_quality_po = StrictPartialOrder(nodes=[
    Milk_Sourcing, Farm_Audit, Milk_Testing
])
milk_quality_po.order.add_edge(Milk_Sourcing, Farm_Audit)
milk_quality_po.order.add_edge(Farm_Audit, Milk_Testing)

# Cheese production partial order
cheese_production_po = StrictPartialOrder(nodes=[
    Starter_Prep, Curd_Formation, Pressing_Stage, Salt_Application, Fermentation
])
cheese_production_po.order.add_edge(Starter_Prep, Curd_Formation)
cheese_production_po.order.add_edge(Curd_Formation, Pressing_Stage)
cheese_production_po.order.add_edge(Pressing_Stage, Salt_Application)
cheese_production_po.order.add_edge(Salt_Application, Fermentation)

# Aging and monitoring partial order (Humidity_Control and Aging_Log can be concurrent)
aging_monitoring_po = StrictPartialOrder(nodes=[
    Humidity_Control, Aging_Log
])
# no order edge: concurrent monitoring

# Sensory evaluation partial order
sensory_po = StrictPartialOrder(nodes=[
    Flavor_Tasting
])  # single activity

# Packaging partial order
packaging_po = StrictPartialOrder(nodes=[
    Packaging_Design, Shelf_Labeling
])
packaging_po.order.add_edge(Packaging_Design, Shelf_Labeling)

# Marketing partial order
marketing_po = StrictPartialOrder(nodes=[
    Retail_Negotiation, Tasting_Event, Customer_Feedback
])
marketing_po.order.add_edge(Retail_Negotiation, Tasting_Event)
marketing_po.order.add_edge(Tasting_Event, Customer_Feedback)

# Loop on sensory evaluation and aging monitoring: repeatedly taste flavors after some aging until exit
sensory_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    Flavor_Tasting,
    StrictPartialOrder(nodes=[Humidity_Control, Aging_Log])
])

# Final partial order joining all main phases
root = StrictPartialOrder(nodes=[
    milk_quality_po,
    cheese_production_po,
    sensory_loop,
    packaging_po,
    marketing_po
])

# Order between phases:
# Milk quality precedes cheese production
root.order.add_edge(milk_quality_po, cheese_production_po)
# Cheese production precedes sensory loops
root.order.add_edge(cheese_production_po, sensory_loop)
# Sensory loop precedes packaging
root.order.add_edge(sensory_loop, packaging_po)
# Packaging precedes marketing
root.order.add_edge(packaging_po, marketing_po)