# Generated from: 80d79d76-4dd2-4c4f-b187-7e8a97a73aa5.json
# Description: This process outlines the intricate steps involved in restoring antique artifacts to preserve historical value while ensuring structural integrity and aesthetic authenticity. It begins with detailed provenance research, followed by condition assessment and material analysis. Conservation planning is then developed to balance restoration with preservation ethics, after which specialized cleaning and stabilization techniques are applied. Subsequent activities include delicate repair, color matching, and surface finishing using historically accurate materials. Final stages involve documentation, client review, and long-term maintenance scheduling to ensure the artifact's longevity and compliance with museum standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Provenance_Check = Transition(label='Provenance Check')
Condition_Scan = Transition(label='Condition Scan')
Material_Test = Transition(label='Material Test')
Plan_Creation = Transition(label='Plan Creation')
Ethics_Review = Transition(label='Ethics Review')
Surface_Clean = Transition(label='Surface Clean')
Structural_Fix = Transition(label='Structural Fix')
Color_Match = Transition(label='Color Match')
Paint_Apply = Transition(label='Paint Apply')
Finish_Polish = Transition(label='Finish Polish')
UV_Cure = Transition(label='UV Cure')
Documentation = Transition(label='Documentation')
Client_Review = Transition(label='Client Review')
Packaging_Prep = Transition(label='Packaging Prep')
Maintenance_Plan = Transition(label='Maintenance Plan')

# First partial order: detailed provenance research,
# followed by condition assessment and material analysis
po1 = StrictPartialOrder(
    nodes=[Provenance_Check, Condition_Scan, Material_Test]
)
po1.order.add_edge(Provenance_Check, Condition_Scan)
po1.order.add_edge(Condition_Scan, Material_Test)

# Conservation planning balancing restoration with preservation ethics
po2 = StrictPartialOrder(
    nodes=[Plan_Creation, Ethics_Review]
)
po2.order.add_edge(Plan_Creation, Ethics_Review)

# Specialized cleaning and stabilization techniques (Surface Clean then Structural Fix)
po3 = StrictPartialOrder(
    nodes=[Surface_Clean, Structural_Fix]
)
po3.order.add_edge(Surface_Clean, Structural_Fix)

# Delicate repair, color matching, and surface finishing using historically accurate materials
po4 = StrictPartialOrder(
    nodes=[Color_Match, Paint_Apply, Finish_Polish, UV_Cure]
)
po4.order.add_edge(Color_Match, Paint_Apply)
po4.order.add_edge(Paint_Apply, Finish_Polish)
po4.order.add_edge(Finish_Polish, UV_Cure)

# Final stages: documentation, client review, packaging prep and maintenance plan
po5 = StrictPartialOrder(
    nodes=[Documentation, Client_Review, Packaging_Prep, Maintenance_Plan]
)
po5.order.add_edge(Documentation, Client_Review)
po5.order.add_edge(Client_Review, Packaging_Prep)
po5.order.add_edge(Packaging_Prep, Maintenance_Plan)

# Overall partial order:
# po1 --> po2 --> po3 --> po4 --> po5
root = StrictPartialOrder(
    nodes=[po1, po2, po3, po4, po5]
)
root.order.add_edge(po1, po2)
root.order.add_edge(po2, po3)
root.order.add_edge(po3, po4)
root.order.add_edge(po4, po5)