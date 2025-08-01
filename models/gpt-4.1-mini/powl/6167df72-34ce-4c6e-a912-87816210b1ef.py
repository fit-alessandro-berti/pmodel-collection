# Generated from: 6167df72-34ce-4c6e-a912-87816210b1ef.json
# Description: This process involves leasing high-value contemporary artworks to corporate clients on a rotating basis. It begins with client profiling to understand aesthetic preferences and office ambiance needs. Next, inventory curation pairs available art pieces with client tastes. Contracts are drafted with flexible terms allowing periodic swaps. Logistics coordinate secure transportation and installation at client sites. Regular condition inspections ensure artwork preservation. Client feedback is gathered to adjust future selections. Marketing campaigns target emerging art trends to refresh inventory. Financial reconciliation tracks leasing fees, insurance, and depreciation. Finally, renewal negotiations or returns conclude the cycle, ensuring continuous client engagement and asset management in a niche leasing market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Client_Profiling = Transition(label='Client Profiling')
Inventory_Check = Transition(label='Inventory Check')
Art_Curation = Transition(label='Art Curation')
Contract_Draft = Transition(label='Contract Draft')
Terms_Review = Transition(label='Terms Review')
Logistics_Plan = Transition(label='Logistics Plan')
Transport_Secure = Transition(label='Transport Secure')
Install_Art = Transition(label='Install Art')
Condition_Audit = Transition(label='Condition Audit')
Feedback_Collect = Transition(label='Feedback Collect')
Trend_Monitor = Transition(label='Trend Monitor')
Marketing_Push = Transition(label='Marketing Push')
Finance_Track = Transition(label='Finance Track')
Renewal_Discuss = Transition(label='Renewal Discuss')
Asset_Return = Transition(label='Asset Return')

# Compose partial orders and choices

# Contracting phase: Contract Draft then Terms Review
contract_PO = StrictPartialOrder(nodes=[Contract_Draft, Terms_Review])
contract_PO.order.add_edge(Contract_Draft, Terms_Review)

# Logistics phase: Logistics Plan -> Transport Secure -> Install Art
logistics_PO = StrictPartialOrder(nodes=[Logistics_Plan, Transport_Secure, Install_Art])
logistics_PO.order.add_edge(Logistics_Plan, Transport_Secure)
logistics_PO.order.add_edge(Transport_Secure, Install_Art)

# Marketing phase: Trend Monitor -> Marketing Push
marketing_PO = StrictPartialOrder(nodes=[Trend_Monitor, Marketing_Push])
marketing_PO.order.add_edge(Trend_Monitor, Marketing_Push)

# Renewal phase choice: Renewal Discuss OR Asset Return
renewal_xor = OperatorPOWL(operator=Operator.XOR, children=[Renewal_Discuss, Asset_Return])

# Loop for ongoing cycle:
# Loop body: Condition Audit -> Feedback Collect -> Marketing phase -> Finance Track
# Then loop back or exit via Renewal xor
cycle_PO = StrictPartialOrder(nodes=[Condition_Audit, Feedback_Collect, marketing_PO, Finance_Track])
cycle_PO.order.add_edge(Condition_Audit, Feedback_Collect)
cycle_PO.order.add_edge(Feedback_Collect, marketing_PO)
cycle_PO.order.add_edge(marketing_PO, Finance_Track)

loop = OperatorPOWL(operator=Operator.LOOP, children=[cycle_PO, renewal_xor])

# Delivery phase: logistics_PO before loop
delivery_then_loop_PO = StrictPartialOrder(nodes=[logistics_PO, loop])
delivery_then_loop_PO.order.add_edge(logistics_PO, loop)

# At start, Client Profiling -> Inventory Check -> Art Curation -> Contracting -> Delivery then loop
root = StrictPartialOrder(
    nodes=[Client_Profiling, Inventory_Check, Art_Curation, contract_PO, delivery_then_loop_PO]
)
root.order.add_edge(Client_Profiling, Inventory_Check)
root.order.add_edge(Inventory_Check, Art_Curation)
root.order.add_edge(Art_Curation, contract_PO)
root.order.add_edge(contract_PO, delivery_then_loop_PO)