# Generated from: ba91eb7e-f262-4f5d-b75d-7585f6bad373.json
# Description: This process involves the detailed authentication and valuation of antique assets for high-end auction houses. It begins with provenance verification through historical records and expert interviews, followed by material composition analysis using advanced spectroscopy. The condition assessment involves microscopic imaging and restoration history review. Ethical sourcing checks are conducted to ensure no illicit trade connections. Concurrently, market trend analysis predicts asset value fluctuations. Legal compliance reviews historical ownership rights and export restrictions. The process culminates in a comprehensive report combining technical data and market insights, enabling informed auction decisions and risk mitigation for stakeholders.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
Provenance_Check = Transition(label='Provenance Check')
Expert_Interview = Transition(label='Expert Interview')

Material_Analysis = Transition(label='Material Analysis')
Spectroscopy_Scan = Transition(label='Spectroscopy Scan')

Condition_Review = Transition(label='Condition Review')
Microscopic_Imaging = Transition(label='Microscopic Imaging')
Restoration_Audit = Transition(label='Restoration Audit')

Ethics_Screening = Transition(label='Ethics Screening')
Trade_Verification = Transition(label='Trade Verification')

Market_Analysis = Transition(label='Market Analysis')
Trend_Forecast = Transition(label='Trend Forecast')

Legal_Review = Transition(label='Legal Review')
Ownership_Audit = Transition(label='Ownership Audit')
Export_Check = Transition(label='Export Check')

Report_Compilation = Transition(label='Report Compilation')
Risk_Assessment = Transition(label='Risk Assessment')

# 1) Provenance verification through historical records and expert interviews:
provenance_PO = StrictPartialOrder(nodes=[Provenance_Check, Expert_Interview])
provenance_PO.order.add_edge(Provenance_Check, Expert_Interview)

# 2) Material composition analysis using advanced spectroscopy:
material_PO = StrictPartialOrder(nodes=[Material_Analysis, Spectroscopy_Scan])
material_PO.order.add_edge(Material_Analysis, Spectroscopy_Scan)

# 3) Condition assessment involves microscopic imaging and restoration history review:
condition_PO = StrictPartialOrder(nodes=[Condition_Review, Microscopic_Imaging, Restoration_Audit])
condition_PO.order.add_edge(Condition_Review, Microscopic_Imaging)
condition_PO.order.add_edge(Condition_Review, Restoration_Audit)

# 4) Ethical sourcing checks => two activities concurrent:
ethics_PO = StrictPartialOrder(nodes=[Ethics_Screening, Trade_Verification])

# 5) Market trend analysis:
market_PO = StrictPartialOrder(nodes=[Market_Analysis, Trend_Forecast])
market_PO.order.add_edge(Market_Analysis, Trend_Forecast)

# 6) Legal compliance reviews historical ownership and export checks:
legal_PO = StrictPartialOrder(nodes=[Legal_Review, Ownership_Audit, Export_Check])
legal_PO.order.add_edge(Legal_Review, Ownership_Audit)
legal_PO.order.add_edge(Legal_Review, Export_Check)

# 7) Final report and risk assessment concurrent:
final_PO = StrictPartialOrder(nodes=[Report_Compilation, Risk_Assessment])

# Compose process according to description:
# Step 1 then Step 2 then Step 3 then Step 4 concurrent with Step 5 and Step 6, finally Step 7

# Combine step 4, 5, and 6 concurrently:
concurrent_456_PO = StrictPartialOrder(nodes=[ethics_PO, market_PO, legal_PO])

# Build the full sequence:
root = StrictPartialOrder(nodes=[provenance_PO, material_PO, condition_PO, concurrent_456_PO, final_PO])

root.order.add_edge(provenance_PO, material_PO)
root.order.add_edge(material_PO, condition_PO)
root.order.add_edge(condition_PO, concurrent_456_PO)
root.order.add_edge(concurrent_456_PO, final_PO)