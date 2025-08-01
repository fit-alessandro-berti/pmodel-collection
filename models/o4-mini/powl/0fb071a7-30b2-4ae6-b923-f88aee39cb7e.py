# Generated from: 0fb071a7-30b2-4ae6-b923-f88aee39cb7e.json
# Description: This process involves the identification, negotiation, and acquisition of valuable corporate artifacts from defunct or merged companies. It begins with research to locate items of interest such as patents, prototypes, or historical documents. Following discovery, legal clearance and ownership verification are conducted to ensure rights to acquire and use the artifacts. Negotiations with sellers or estates proceed alongside appraisal and valuation to determine fair market price. Once acquired, artifacts undergo authentication and restoration if needed. The process concludes with cataloging, digital archiving, and integration into the company’s heritage collection to preserve corporate history and leverage intangible assets for branding and innovation inspiration.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
AR = Transition(label='Artifact Research')
OV = Transition(label='Ownership Verify')
LC = Transition(label='Legal Clearance')
SN = Transition(label='Seller Negotiate')
PA = Transition(label='Price Appraise')
CD = Transition(label='Contract Draft')
AT = Transition(label='Authentication Test')
CA = Transition(label='Condition Assess')
RP = Transition(label='Restoration Plan')
RW = Transition(label='Restoration Work')
CE = Transition(label='Catalog Entry')
DA = Transition(label='Digital Archive')
HI = Transition(label='Heritage Integrate')
AL = Transition(label='Asset Leverage')
II = Transition(label='Innovation Inspire')
FR = Transition(label='Final Review')

# Silent skip for optional restoration
skip = SilentTransition()

# Restoration pipeline: assess → plan → work
rest_seq = StrictPartialOrder(nodes=[CA, RP, RW])
rest_seq.order.add_edge(CA, RP)
rest_seq.order.add_edge(RP, RW)

# Choice: either skip restoration or do the pipeline
rest_xor = OperatorPOWL(operator=Operator.XOR, children=[skip, rest_seq])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    AR, OV, LC,        # research, then verify & clearance
    SN, PA,            # negotiate & appraise
    CD,                # contract draft
    AT,                # authentication test
    rest_xor,          # optional restoration
    CE, DA,            # catalog entry & digital archive
    HI, AL, II, FR     # integrate → leverage → inspire → final review
])

# Edges: research → verify & clearance
root.order.add_edge(AR, OV)
root.order.add_edge(AR, LC)
# verify & clearance → negotiate & appraise
root.order.add_edge(OV, SN)
root.order.add_edge(OV, PA)
root.order.add_edge(LC, SN)
root.order.add_edge(LC, PA)
# negotiate & appraise → contract draft
root.order.add_edge(SN, CD)
root.order.add_edge(PA, CD)
# contract draft → authentication test
root.order.add_edge(CD, AT)
# authentication test → restoration choice
root.order.add_edge(AT, rest_xor)
# restoration choice → catalog & archive
root.order.add_edge(rest_xor, CE)
root.order.add_edge(rest_xor, DA)
# catalog & archive → heritage integration
root.order.add_edge(CE, HI)
root.order.add_edge(DA, HI)
# integration → leverage → inspire → final review
root.order.add_edge(HI, AL)
root.order.add_edge(AL, II)
root.order.add_edge(II, FR)