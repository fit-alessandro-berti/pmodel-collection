# Generated from: b1f47bc2-9356-4cce-899b-9a93512ed7cc.json
# Description: This process involves cross-disciplinary teams from different organizations working together to ideate, prototype, test, and refine a novel product concept in a highly iterative manner. It begins with opportunity identification and moves through co-creation workshops, rapid prototyping, and multi-stage validation involving customers and stakeholders. The process requires dynamic resource allocation, continuous feedback loops, and risk assessment at every stage to ensure alignment with strategic goals and market viability. The final stages include joint intellectual property agreements, pilot deployment, and knowledge transfer sessions to embed innovations into operational frameworks.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
opScan         = Transition(label='Opportunity Scan')
stakeMap       = Transition(label='Stakeholder Map')
ideaWorkshop   = Transition(label='Idea Workshop')
conceptDraft   = Transition(label='Concept Draft')
resourceAlign  = Transition(label='Resource Align')
prototypeBuild = Transition(label='Prototype Build')
userTesting    = Transition(label='User Testing')
feedbackLoop   = Transition(label='Feedback Loop')
riskReview     = Transition(label='Risk Review')
designIterate  = Transition(label='Design Iterate')
ipNegotiation  = Transition(label='IP Negotiation')
pilotLaunch    = Transition(label='Pilot Launch')
marketMonitor  = Transition(label='Market Monitor')
knowledgeShare = Transition(label='Knowledge Share')
scalePlan      = Transition(label='Scale Plan')
performanceAudit = Transition(label='Performance Audit')

# A silent transition (not strictly needed here but available for loop exits if desired)
skip = SilentTransition()

# Define the iterative feedback loop:
#   Prototype Build -> User Testing -> Feedback Loop -> Risk Review -> Design Iterate
loop_body = StrictPartialOrder(
    nodes=[userTesting, feedbackLoop, riskReview, designIterate]
)
loop_body.order.add_edge(userTesting,    feedbackLoop)
loop_body.order.add_edge(feedbackLoop,    riskReview)
loop_body.order.add_edge(riskReview,      designIterate)

# The LOOP operator: do prototypeBuild, then repeat (loop_body then prototypeBuild) until exit
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[prototypeBuild, loop_body]
)

# Assemble the full workflow as a single partial order
root = StrictPartialOrder(
    nodes=[
        opScan,
        stakeMap,
        ideaWorkshop,
        conceptDraft,
        resourceAlign,
        loop,
        ipNegotiation,
        pilotLaunch,
        marketMonitor,
        knowledgeShare,
        scalePlan,
        performanceAudit
    ]
)

# Define the sequence (strict ordering) of the main stages
root.order.add_edge(opScan,        stakeMap)
root.order.add_edge(stakeMap,      ideaWorkshop)
root.order.add_edge(ideaWorkshop,  conceptDraft)
root.order.add_edge(conceptDraft,  resourceAlign)
root.order.add_edge(resourceAlign, loop)
root.order.add_edge(loop,          ipNegotiation)
root.order.add_edge(ipNegotiation, pilotLaunch)
root.order.add_edge(pilotLaunch,   marketMonitor)
root.order.add_edge(marketMonitor, knowledgeShare)
root.order.add_edge(knowledgeShare, scalePlan)
root.order.add_edge(scalePlan,     performanceAudit)