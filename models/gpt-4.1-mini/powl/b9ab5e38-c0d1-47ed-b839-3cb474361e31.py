# Generated from: b9ab5e38-c0d1-47ed-b839-3cb474361e31.json
# Description: This process outlines the comprehensive supply chain for artisan cheese production and distribution, starting from selecting rare milk sources to final delivery. It includes unique steps such as microbial culture optimization, aging environment control, sensory evaluation panels, and custom packaging design. The process integrates quality assurance with traditional craftsmanship, ensuring the preservation of unique flavor profiles while scaling production. It also incorporates traceability from farm to retailer, sustainable waste management, and customer feedback loops to continually refine the product and maintain artisanal authenticity in a competitive market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Milk_Sourcing = Transition(label='Milk Sourcing')
Microbe_Culturing = Transition(label='Microbe Culturing')
Coagulation = Transition(label='Coagulation')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Draining = Transition(label='Whey Draining')
Molding_Press = Transition(label='Molding Press')
Salting_Stage = Transition(label='Salting Stage')
Aging_Control = Transition(label='Aging Control')
Humidity_Check = Transition(label='Humidity Check')
Flavor_Testing = Transition(label='Flavor Testing')
Packaging_Design = Transition(label='Packaging Design')
Batch_Tracking = Transition(label='Batch Tracking')
Transport_Scheduling = Transition(label='Transport Scheduling')
Retail_Setup = Transition(label='Retail Setup')
Feedback_Review = Transition(label='Feedback Review')
Waste_Recycling = Transition(label='Waste Recycling')

# Aging environment control partial order (Aging_Control and Humidity_Check concurrent)
aging_PO = StrictPartialOrder(nodes=[Aging_Control, Humidity_Check])
# No order edges: concurrent checks for aging environment

# Quality assurance partial order: Flavor Testing and Packaging Design sequential (testing before packaging design)
qa_PO = StrictPartialOrder(nodes=[Flavor_Testing, Packaging_Design])
qa_PO.order.add_edge(Flavor_Testing, Packaging_Design)

# Distribution partial order: Batch Tracking -> Transport Scheduling -> Retail Setup
distribution_PO = StrictPartialOrder(nodes=[Batch_Tracking, Transport_Scheduling, Retail_Setup])
distribution_PO.order.add_edge(Batch_Tracking, Transport_Scheduling)
distribution_PO.order.add_edge(Transport_Scheduling, Retail_Setup)

# Feedback loop as a loop operator: Feedback Review then Waste Recycling, repeat or exit
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Review, Waste_Recycling])

# Production sequence: Milk_Sourcing -> Microbe_Culturing -> Coagulation -> Curd_Cutting -> Whey_Draining -> Molding_Press -> Salting_Stage
production_PO = StrictPartialOrder(nodes=[
    Milk_Sourcing, Microbe_Culturing, Coagulation, Curd_Cutting,
    Whey_Draining, Molding_Press, Salting_Stage
])
production_PO.order.add_edge(Milk_Sourcing, Microbe_Culturing)
production_PO.order.add_edge(Microbe_Culturing, Coagulation)
production_PO.order.add_edge(Coagulation, Curd_Cutting)
production_PO.order.add_edge(Curd_Cutting, Whey_Draining)
production_PO.order.add_edge(Whey_Draining, Molding_Press)
production_PO.order.add_edge(Molding_Press, Salting_Stage)

# Combine aging_PO and qa_PO in parallel (concurrent)
aging_qa_PO = StrictPartialOrder(nodes=[aging_PO, qa_PO])
aging_qa_PO.order.add_edge(aging_PO, qa_PO)

# Combine production_PO and aging_qa_PO sequentially (aging and QA after production)
prod_aging_qa_PO = StrictPartialOrder(nodes=[production_PO, aging_qa_PO])
prod_aging_qa_PO.order.add_edge(production_PO, aging_qa_PO)

# Combine distribution_PO and feedback_loop concurrent with prod_aging_qa_PO finishing before them
final_PO = StrictPartialOrder(nodes=[prod_aging_qa_PO, distribution_PO, feedback_loop])
final_PO.order.add_edge(prod_aging_qa_PO, distribution_PO)
final_PO.order.add_edge(prod_aging_qa_PO, feedback_loop)

root = final_PO