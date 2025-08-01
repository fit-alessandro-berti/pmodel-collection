# Generated from: 3d109e69-7e79-421e-8d1e-a738e6e65cfa.json
# Description: This process oversees the end-to-end supply chain management of artisan cheese production, starting from raw milk sourcing from local farms, followed by quality testing and fermentation control. It includes specialized aging environment setup, periodic sensory evaluations, packaging customization, cold chain logistics, seasonal demand forecasting, compliance with regional food safety regulations, and collaboration with boutique retailers for exclusive product launches. The process ensures traceability, sustainability practices, and customer feedback integration to refine cheese varieties and distribution strategies, maintaining a balance between tradition and innovation throughout the supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')

# Fermentation sub-process
Starter_Culture = Transition(label='Starter Culture')
Coagulation = Transition(label='Coagulation')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Draining = Transition(label='Whey Draining')
Molding_Press = Transition(label='Molding Press')
Salting_Stage = Transition(label='Salting Stage')
fermentation_PO = StrictPartialOrder(nodes=[
    Starter_Culture, Coagulation, Curd_Cutting, Whey_Draining, Molding_Press, Salting_Stage])

fermentation_PO.order.add_edge(Starter_Culture, Coagulation)
fermentation_PO.order.add_edge(Coagulation, Curd_Cutting)
fermentation_PO.order.add_edge(Curd_Cutting, Whey_Draining)
fermentation_PO.order.add_edge(Whey_Draining, Molding_Press)
fermentation_PO.order.add_edge(Molding_Press, Salting_Stage)

# Aging sub-process
Aging_Setup = Transition(label='Aging Setup')
Temperature_Check = Transition(label='Temperature Check')
Sensory_Eval = Transition(label='Sensory Eval')
aging_PO = StrictPartialOrder(nodes=[Aging_Setup, Temperature_Check, Sensory_Eval])
aging_PO.order.add_edge(Aging_Setup, Temperature_Check)
aging_PO.order.add_edge(Temperature_Check, Sensory_Eval)

# Packaging sub-process
Packaging_Prep = Transition(label='Packaging Prep')
Label_Printing = Transition(label='Label Printing')
packaging_PO = StrictPartialOrder(nodes=[Packaging_Prep, Label_Printing])
packaging_PO.order.add_edge(Packaging_Prep, Label_Printing)

# Cold chain logistics sub-process
Cold_Storage = Transition(label='Cold Storage')
Logistics_Plan = Transition(label='Logistics Plan')
cold_logistics_PO = StrictPartialOrder(nodes=[Cold_Storage, Logistics_Plan])
cold_logistics_PO.order.add_edge(Cold_Storage, Logistics_Plan)

# Demand forecasting and compliance (concurrent with retail sync)
Order_Forecast = Transition(label='Order Forecast')
Reg_Compliance = Transition(label='Reg Compliance')
forecast_compliance_PO = StrictPartialOrder(nodes=[Order_Forecast, Reg_Compliance])

# Retail sync and feedback, concurrent
Retail_Sync = Transition(label='Retail Sync')
Feedback_Review = Transition(label='Feedback Review')
retail_feedback_PO = StrictPartialOrder(nodes=[Retail_Sync, Feedback_Review])

# Combine Order_Forecast and Reg_Compliance with Retail_Sync and Feedback_Review in parallel
concurrent_PO = StrictPartialOrder(nodes=[forecast_compliance_PO, retail_feedback_PO])
# Flatten nodes to top-level
nodes_top = [
    Milk_Sourcing,
    Quality_Testing,
    fermentation_PO,
    aging_PO,
    packaging_PO,
    cold_logistics_PO,
    forecast_compliance_PO,
    retail_feedback_PO,
]

root = StrictPartialOrder(nodes=nodes_top)

# Control flow edges:
root.order.add_edge(Milk_Sourcing, Quality_Testing)
root.order.add_edge(Quality_Testing, fermentation_PO)
root.order.add_edge(fermentation_PO, aging_PO)
root.order.add_edge(aging_PO, packaging_PO)
root.order.add_edge(packaging_PO, cold_logistics_PO)
root.order.add_edge(cold_logistics_PO, forecast_compliance_PO)
root.order.add_edge(forecast_compliance_PO, retail_feedback_PO)