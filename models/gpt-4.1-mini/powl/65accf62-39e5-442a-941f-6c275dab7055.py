# Generated from: 65accf62-39e5-442a-941f-6c275dab7055.json
# Description: This process outlines a complex, atypical approach to fostering innovation by integrating expertise and resources across multiple unrelated industries. It begins with opportunity scanning across sectors, followed by cross-functional ideation workshops designed to blend diverse perspectives. Subsequently, hybrid prototyping leverages materials and technologies from different fields. The next phase includes iterative testing in parallel market environments to gather multifaceted feedback. Stakeholder alignment sessions ensure continuous buy-in from diverse partners, while adaptive strategy reviews recalibrate objectives based on emerging insights. Legal cross-compliance checks mitigate risks stemming from regulatory differences. Finally, the process culminates in joint commercialization planning and synchronized product launches targeting hybrid customer segments, fostering sustainable competitive advantages through unconventional collaboration.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Opportunity_Scan = Transition(label='Opportunity Scan')
Cross_Ideation = Transition(label='Cross Ideation')
Hybrid_Prototype = Transition(label='Hybrid Prototype')
Parallel_Testing = Transition(label='Parallel Testing')
Stakeholder_Align = Transition(label='Stakeholder Align')
Adaptive_Review = Transition(label='Adaptive Review')
Compliance_Check = Transition(label='Compliance Check')
Risk_Assessment = Transition(label='Risk Assessment')
Resource_Merge = Transition(label='Resource Merge')
Tech_Transfer = Transition(label='Tech Transfer')
Market_Sync = Transition(label='Market Sync')
Feedback_Loop = Transition(label='Feedback Loop')
Strategic_Pivot = Transition(label='Strategic Pivot')
Joint_Launch = Transition(label='Joint Launch')
Performance_Audit = Transition(label='Performance Audit')

# Model the loop of feedback and strategic pivot:
# loop body: Feedback Loop (B), then either exit or do Strategic Pivot (A) then repeat;
# according to LOOP(A,B) convention: do A, then choose exit or B then A again

feedback_loop_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Feedback_Loop, Strategic_Pivot]
)

# Parallel testing phase is iterative in parallel market environments
# Model Parallel Testing concurrent with Stakeholder Align since they can be parallel
# (they are in sequence but testing happens in parallel markets → so Parallel Testing happens then Stakeholder Align, but Stakeholder Align may overlap with Adaptive Review)
# We'll model Parallel Testing and Stakeholder Align partially ordered, no direct dependency -> concurrent

# Adaptive Review recalibrates objectives based on emerging insights from Stakeholder Align and Compliance Check
# So Adaptive Review depends on both Stakeholder Align and Compliance Check

# Compliance Check mitigates risks, so Risk Assessment happens before Compliance Check
risk_and_compliance = StrictPartialOrder(
    nodes=[Risk_Assessment, Compliance_Check]
)
risk_and_compliance.order.add_edge(Risk_Assessment, Compliance_Check)

# Resource Merge and Tech Transfer happen after Compliance Check as part of cross-industry resource usage
resource_and_tech = StrictPartialOrder(
    nodes=[Resource_Merge, Tech_Transfer]
)
# No strict order between Resource Merge and Tech Transfer, so concurrent

# Market Sync and Joint Launch come last
# Market Sync depends on Adaptive Review and Resource_Merge & Tech Transfer (they provide input)
# Joint Launch after Market Sync


# Partial order step by step:

# Step 1: Opportunity Scan
# Step 2: Cross Ideation after Opportunity Scan
# Step 3: Hybrid Prototype after Cross Ideation
# Step 4: Parallel Testing after Hybrid Prototype
# Stakeholder Align can start after Hybrid Prototype, concurrent with Parallel Testing

# Step 5: Adaptive Review after Stakeholder Align and Compliance Check
# Compliance Check after Risk Assessment
# Risk Assessment after Parallel Testing and Stakeholder Align (to reflect feedback on risk from both)
# Note: To avoid cycles, let's have Risk Assessment after Parallel Testing and Stakeholder Align

# Step 6: Resource Merge and Tech Transfer after Compliance Check
# Step 7: Market Sync after Adaptive Review, Resource Merge, Tech Transfer
# Step 8: Feedback Loop and Strategic Pivot modeled with loop included after Market Sync
# Step 9: Joint Launch after Feedback Loop loop
# Step 10: Performance Audit after Joint Launch

# Creating partial orders to reflect these dependencies:

po = StrictPartialOrder(
    nodes=[
        Opportunity_Scan,
        Cross_Ideation,
        Hybrid_Prototype,
        Parallel_Testing,
        Stakeholder_Align,
        Adaptive_Review,
        Risk_Assessment,
        Compliance_Check,
        Resource_Merge,
        Tech_Transfer,
        Market_Sync,
        feedback_loop_loop,
        Joint_Launch,
        Performance_Audit
    ]
)

# Add edges according to step by step reasoning

# Opportunity Scan -> Cross Ideation
po.order.add_edge(Opportunity_Scan, Cross_Ideation)

# Cross Ideation -> Hybrid Prototype
po.order.add_edge(Cross_Ideation, Hybrid_Prototype)

# Hybrid Prototype -> Parallel Testing
po.order.add_edge(Hybrid_Prototype, Parallel_Testing)

# Hybrid Prototype -> Stakeholder Align (stakeholder alignment sessions parallel to testing)
po.order.add_edge(Hybrid_Prototype, Stakeholder_Align)

# Parallel Testing -> Risk Assessment
po.order.add_edge(Parallel_Testing, Risk_Assessment)

# Stakeholder Align -> Risk Assessment
po.order.add_edge(Stakeholder_Align, Risk_Assessment)

# Risk Assessment -> Compliance Check
po.order.add_edge(Risk_Assessment, Compliance_Check)

# Compliance Check -> Resource Merge
po.order.add_edge(Compliance_Check, Resource_Merge)

# Compliance Check -> Tech Transfer
po.order.add_edge(Compliance_Check, Tech_Transfer)

# Stakeholder Align -> Adaptive Review
po.order.add_edge(Stakeholder_Align, Adaptive_Review)

# Compliance Check -> Adaptive Review
po.order.add_edge(Compliance_Check, Adaptive_Review)

# Resource Merge -> Market Sync
po.order.add_edge(Resource_Merge, Market_Sync)

# Tech Transfer -> Market Sync
po.order.add_edge(Tech_Transfer, Market_Sync)

# Adaptive Review -> Market Sync
po.order.add_edge(Adaptive_Review, Market_Sync)

# Market Sync -> feedback_loop_loop (Feedback Loop + Strategic Pivot loop)
po.order.add_edge(Market_Sync, feedback_loop_loop)

# feedback_loop_loop -> Joint Launch
po.order.add_edge(feedback_loop_loop, Joint_Launch)

# Joint Launch -> Performance Audit
po.order.add_edge(Joint_Launch, Performance_Audit)

root = po