# Generated from: 545c9233-2234-410a-b32b-f6e570dc8e64.json
# Description: This process involves coordinating a network of independent artisans and small-scale suppliers to produce bespoke handcrafted products. It starts with raw material sourcing from sustainable local farms, followed by quality vetting and batch allocation to different artisan groups. Each artisan customizes components based on unique client orders, integrating traditional techniques with modern design inputs. The process includes iterative feedback loops between artisans and design coordinators, logistics planning for staggered deliveries, and dynamic inventory adjustments. Final assembly is conducted in a centralized atelier where quality assurance and packaging are tailored to individual client specifications, culminating in a personalized delivery experience that emphasizes craftsmanship and sustainability throughout the supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Material_Sourcing = Transition(label='Material Sourcing')
Quality_Vetting = Transition(label='Quality Vetting')
Batch_Allocation = Transition(label='Batch Allocation')
Order_Customizing = Transition(label='Order Customizing')
Design_Feedback = Transition(label='Design Feedback')
Artisan_Coordination = Transition(label='Artisan Coordination')
Component_Tracking = Transition(label='Component Tracking')
Inventory_Adjusting = Transition(label='Inventory Adjusting')
Logistics_Planning = Transition(label='Logistics Planning')
Delivery_Scheduling = Transition(label='Delivery Scheduling')
Assembly_Prep = Transition(label='Assembly Prep')
Final_Assembly = Transition(label='Final Assembly')
Quality_Review = Transition(label='Quality Review')
Packaging_Tailoring = Transition(label='Packaging Tailoring')
Client_Delivery = Transition(label='Client Delivery')

tau = SilentTransition()

# Loop for iterative feedback between Artisans and Design Coordinators:
# Loop = *(Order_Customizing, X(Design_Feedback, Artisan_Coordination))
feedback_loop = OperatorPOWL(operator=Operator.XOR, children=[Design_Feedback, Artisan_Coordination])
loop_artisan_feedback = OperatorPOWL(operator=Operator.LOOP, children=[Order_Customizing, feedback_loop])

# Partial order for artisans working concurrently on tracking and inventory adjusting between feedback loop and logistics:
# They are concurrent with each other but after feedback loop and before logistics
artisan_tasks = StrictPartialOrder(nodes=[Component_Tracking, Inventory_Adjusting])
# No edge means concurrency between these two

# Logistics planning and delivery scheduling run sequentially
logistics_seq = StrictPartialOrder(nodes=[Logistics_Planning, Delivery_Scheduling])
logistics_seq.order.add_edge(Logistics_Planning, Delivery_Scheduling)

# Assembly prep before final assembly, then quality review and packaging tailoring sequentially
assembly_seq = StrictPartialOrder(nodes=[Assembly_Prep, Final_Assembly, Quality_Review, Packaging_Tailoring])
assembly_seq.order.add_edge(Assembly_Prep, Final_Assembly)
assembly_seq.order.add_edge(Final_Assembly, Quality_Review)
assembly_seq.order.add_edge(Quality_Review, Packaging_Tailoring)

# Final delivery after packaging
final_seq = StrictPartialOrder(nodes=[assembly_seq, Client_Delivery])
final_seq.order.add_edge(assembly_seq, Client_Delivery)

# Initial sequence: Material Sourcing -> Quality Vetting -> Batch Allocation
init_seq = StrictPartialOrder(nodes=[Material_Sourcing, Quality_Vetting, Batch_Allocation])
init_seq.order.add_edge(Material_Sourcing, Quality_Vetting)
init_seq.order.add_edge(Quality_Vetting, Batch_Allocation)

# Put all steps together in a big partial order:
# init_seq --> loop_artisan_feedback --> artisan_tasks --> logistics_seq --> final_seq

root = StrictPartialOrder(nodes=[init_seq, loop_artisan_feedback, artisan_tasks, logistics_seq, final_seq])
root.order.add_edge(init_seq, loop_artisan_feedback)
root.order.add_edge(loop_artisan_feedback, artisan_tasks)
root.order.add_edge(artisan_tasks, logistics_seq)
root.order.add_edge(logistics_seq, final_seq)