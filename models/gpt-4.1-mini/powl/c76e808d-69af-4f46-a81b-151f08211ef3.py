# Generated from: c76e808d-69af-4f46-a81b-151f08211ef3.json
# Description: This process details the intricate and atypical supply chain for producing and distributing artisanal cheeses from small-scale farms to niche gourmet retailers. It involves unique steps like microbial culture selection, seasonal milk sourcing based on animal diet, controlled aging with environmental monitoring, and bespoke packaging tailored to cheese type. The process also integrates direct farmer collaboration, traceability through blockchain, and adaptive logistics that account for cheese maturation stages and fragile transport conditions, ensuring product quality and authenticity while balancing traditional methods with modern technology.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Milk_Sourcing = Transition(label='Milk Sourcing')
Culture_Selection = Transition(label='Culture Selection')
Milk_Testing = Transition(label='Milk Testing')
Curd_Formation = Transition(label='Curd Formation')
Whey_Separation = Transition(label='Whey Separation')
Molding_Cheese = Transition(label='Molding Cheese')
Salting_Process = Transition(label='Salting Process')
Aging_Setup = Transition(label='Aging Setup')
Env_Monitoring = Transition(label='Env Monitoring')
Flavor_Profiling = Transition(label='Flavor Profiling')
Packaging_Design = Transition(label='Packaging Design')
Blockchain_Entry = Transition(label='Blockchain Entry')
Quality_Audit = Transition(label='Quality Audit')
Retail_Sync = Transition(label='Retail Sync')
Transport_Prep = Transition(label='Transport Prep')
Delivery_Tracking = Transition(label='Delivery Tracking')
Customer_Feedback = Transition(label='Customer Feedback')

# Define partial orders for parallel steps

# Initial sourcing and culture selection happens first
initial_PO = StrictPartialOrder(nodes=[Milk_Sourcing, Culture_Selection])
initial_PO.order.add_edge(Milk_Sourcing, Culture_Selection)

# Milk testing after culture selection
testing_PO = StrictPartialOrder(nodes=[Culture_Selection, Milk_Testing])
testing_PO.order.add_edge(Culture_Selection, Milk_Testing)

# After testing comes curd formation and whey separation concurrently
curd_PO = StrictPartialOrder(nodes=[Milk_Testing, Curd_Formation, Whey_Separation])
curd_PO.order.add_edge(Milk_Testing, Curd_Formation)
curd_PO.order.add_edge(Milk_Testing, Whey_Separation)

# Molding cheese follows curd formation and whey separation (must wait for both)
molding_PO = StrictPartialOrder(nodes=[Curd_Formation, Whey_Separation, Molding_Cheese])
molding_PO.order.add_edge(Curd_Formation, Molding_Cheese)
molding_PO.order.add_edge(Whey_Separation, Molding_Cheese)

# Salting process after molding cheese
salting_PO = StrictPartialOrder(nodes=[Molding_Cheese, Salting_Process])
salting_PO.order.add_edge(Molding_Cheese, Salting_Process)

# Aging setup after salting process
aging_PO = StrictPartialOrder(nodes=[Salting_Process, Aging_Setup])
aging_PO.order.add_edge(Salting_Process, Aging_Setup)

# Env monitoring and flavor profiling parallel during aging
aging_monitoring_PO = StrictPartialOrder(nodes=[Aging_Setup, Env_Monitoring, Flavor_Profiling])
aging_monitoring_PO.order.add_edge(Aging_Setup, Env_Monitoring)
aging_monitoring_PO.order.add_edge(Aging_Setup, Flavor_Profiling)

# Packaging design starts after aging steps finish
packaging_PO = StrictPartialOrder(
    nodes=[Env_Monitoring, Flavor_Profiling, Packaging_Design]
)
packaging_PO.order.add_edge(Env_Monitoring, Packaging_Design)
packaging_PO.order.add_edge(Flavor_Profiling, Packaging_Design)

# Blockchain entry follows packaging design
blockchain_PO = StrictPartialOrder(nodes=[Packaging_Design, Blockchain_Entry])
blockchain_PO.order.add_edge(Packaging_Design, Blockchain_Entry)

# Quality audit follows blockchain entry
quality_PO = StrictPartialOrder(nodes=[Blockchain_Entry, Quality_Audit])
quality_PO.order.add_edge(Blockchain_Entry, Quality_Audit)

# Retail sync after quality audit
retail_PO = StrictPartialOrder(nodes=[Quality_Audit, Retail_Sync])
retail_PO.order.add_edge(Quality_Audit, Retail_Sync)

# Transport prep after retail sync
transport_PO = StrictPartialOrder(nodes=[Retail_Sync, Transport_Prep])
transport_PO.order.add_edge(Retail_Sync, Transport_Prep)

# Delivery tracking after transport prep
delivery_PO = StrictPartialOrder(nodes=[Transport_Prep, Delivery_Tracking])
delivery_PO.order.add_edge(Transport_Prep, Delivery_Tracking)

# Customer feedback last step after delivery tracking
feedback_PO = StrictPartialOrder(nodes=[Delivery_Tracking, Customer_Feedback])
feedback_PO.order.add_edge(Delivery_Tracking, Customer_Feedback)

# Compose from bottom to top chaining each PO
# Combine all smaller POS into a large PO that matches full process order

# Start combining as partial orders
po_1 = StrictPartialOrder(
    nodes=[
        initial_PO,
        testing_PO,
        curd_PO,
        molding_PO,
        salting_PO,
        aging_PO,
        aging_monitoring_PO,
        packaging_PO,
        blockchain_PO,
        quality_PO,
        retail_PO,
        transport_PO,
        delivery_PO,
        feedback_PO,
    ]
)

# Add edges to represent process flow dependencies between these submodels

# Edges:
po_1.order.add_edge(initial_PO, testing_PO)           # Milk_Sourcing->Culture_Selection->Milk_Testing
po_1.order.add_edge(testing_PO, curd_PO)             # Milk_Testing->Curd_Formation, Whey_Separation
po_1.order.add_edge(curd_PO, molding_PO)             # Curd_Formation & Whey_Separation -> Molding_Cheese
po_1.order.add_edge(molding_PO, salting_PO)          # Molding_Cheese->Salting_Process
po_1.order.add_edge(salting_PO, aging_PO)             # Salting_Process->Aging_Setup
po_1.order.add_edge(aging_PO, aging_monitoring_PO)    # Aging_Setup -> Env_Monitoring, Flavor_Profiling
po_1.order.add_edge(aging_monitoring_PO, packaging_PO)# Env_Monitoring, Flavor_Profiling -> Packaging_Design
po_1.order.add_edge(packaging_PO, blockchain_PO)     # Packaging_Design -> Blockchain_Entry
po_1.order.add_edge(blockchain_PO, quality_PO)       # Blockchain_Entry -> Quality_Audit
po_1.order.add_edge(quality_PO, retail_PO)            # Quality_Audit -> Retail_Sync
po_1.order.add_edge(retail_PO, transport_PO)          # Retail_Sync -> Transport_Prep
po_1.order.add_edge(transport_PO, delivery_PO)        # Transport_Prep -> Delivery_Tracking
po_1.order.add_edge(delivery_PO, feedback_PO)         # Delivery_Tracking -> Customer_Feedback

# Flatten nodes: po_1.nodes contains partial orders, but nodes might be nested;
# StrictPartialOrder nodes can store other StrictPartialOrder nodes or Transitions.

root = po_1