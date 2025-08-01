# Generated from: 8544dbb6-da91-4730-86cc-b62679341524.json
# Description: This process governs the end-to-end management of urban beekeeping supplies, starting from sourcing sustainable materials to packaging and distributing specialized equipment tailored for city environments. It involves coordinating with local artisans for custom hive designs, ensuring regulatory compliance for urban apiaries, managing seasonal demand fluctuations, and integrating feedback from beekeepers to continuously improve product offerings while minimizing environmental impact through eco-friendly logistics and waste reduction strategies.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
Material_Sourcing = Transition(label='Material Sourcing')
Supplier_Vetting = Transition(label='Supplier Vetting')
Design_Customization = Transition(label='Design Customization')
Prototype_Testing = Transition(label='Prototype Testing')
Regulation_Review = Transition(label='Regulation Review')
Compliance_Audit = Transition(label='Compliance Audit')
Inventory_Setup = Transition(label='Inventory Setup')
Demand_Forecast = Transition(label='Demand Forecast')
Order_Processing = Transition(label='Order Processing')
Assembly_Line = Transition(label='Assembly Line')
Quality_Check = Transition(label='Quality Check')
Packaging_Design = Transition(label='Packaging Design')
Eco_Logistics = Transition(label='Eco Logistics')
Customer_Training = Transition(label='Customer Training')
Feedback_Analysis = Transition(label='Feedback Analysis')
Waste_Management = Transition(label='Waste Management')
Seasonal_Planning = Transition(label='Seasonal Planning')

# Partial order for supplier qualification
supplier_qualification = StrictPartialOrder(nodes=[Material_Sourcing, Supplier_Vetting])
supplier_qualification.order.add_edge(Material_Sourcing, Supplier_Vetting)

# Design loop: Design_Customization -> Prototype_Testing loop (can repeat testing and redesign)
design_loop = OperatorPOWL(operator=Operator.LOOP, children=[Design_Customization, Prototype_Testing])

# Compliance check partial order
compliance_check = StrictPartialOrder(nodes=[Regulation_Review, Compliance_Audit])
compliance_check.order.add_edge(Regulation_Review, Compliance_Audit)

# Inventory & planning partial order (Seasonal planning and inventory setup concurrent with demand forecast)
inventory_planning = StrictPartialOrder(nodes=[Inventory_Setup, Demand_Forecast, Seasonal_Planning])
inventory_planning.order.add_edge(Seasonal_Planning, Inventory_Setup)

# After compliance and inventory planning, start order processing and assembly concurrently
order_assembly = StrictPartialOrder(nodes=[Order_Processing, Assembly_Line])
# Assembly depends on order processing
order_assembly.order.add_edge(Order_Processing, Assembly_Line)

# Quality check after assembly
quality_phase = StrictPartialOrder(nodes=[order_assembly, Quality_Check])
quality_phase.order.add_edge(order_assembly, Quality_Check)

# Packaging and eco logistics partial order (can be concurrent or sequential - let's assume packaging before eco logistics)
packaging_logistics = StrictPartialOrder(nodes=[Packaging_Design, Eco_Logistics])
packaging_logistics.order.add_edge(Packaging_Design, Eco_Logistics)

# Customer training and feedback analysis are concurrent with waste management
customer_feedback_waste = StrictPartialOrder(nodes=[Customer_Training, Feedback_Analysis, Waste_Management])

# Combine the supply chain start: supplier_qualification --> design_loop --> compliance_check
start_phase = StrictPartialOrder(nodes=[supplier_qualification, design_loop, compliance_check])
start_phase.order.add_edge(supplier_qualification, design_loop)
start_phase.order.add_edge(design_loop, compliance_check)

# Combine mid phase: compliance_check --> inventory_planning --> quality phase
mid_phase = StrictPartialOrder(nodes=[compliance_check, inventory_planning, quality_phase])
mid_phase.order.add_edge(compliance_check, inventory_planning)
mid_phase.order.add_edge(inventory_planning, quality_phase)

# Final phase: quality_phase --> packaging_logistics --> customer_feedback_waste
final_phase = StrictPartialOrder(nodes=[quality_phase, packaging_logistics, customer_feedback_waste])
final_phase.order.add_edge(quality_phase, packaging_logistics)
final_phase.order.add_edge(packaging_logistics, customer_feedback_waste)

# Compose the full root POWL as a partial order of start, mid, and final phases
root = StrictPartialOrder(nodes=[start_phase, mid_phase, final_phase])
root.order.add_edge(start_phase, mid_phase)
root.order.add_edge(mid_phase, final_phase)