# Generated from: 84048b70-2ae7-4fad-9179-f21b702cd13b.json
# Description: This process outlines the complex and atypical steps required to onboard new employees into a fully remote, globally distributed team. It includes not only the standard HR and IT setup activities but also unique steps such as virtual cultural immersion, asynchronous mentorship pairing, equipment shipping logistics, timezone alignment workshops, and digital workspace personalization. The process ensures new hires are fully integrated into the company’s remote ecosystem, fostering engagement and productivity despite physical distances. It also handles compliance with varying international labor laws and data privacy regulations, requiring coordination among multiple departments and external vendors to deliver a seamless onboarding experience.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
ProfileSetup = Transition(label='Profile Setup')
EquipmentShip = Transition(label='Equipment Ship')
AccessGrant = Transition(label='Access Grant')
PolicyReview = Transition(label='Policy Review')
MentorMatch = Transition(label='Mentor Match')
CultureTour = Transition(label='Culture Tour')
TimezoneSync = Transition(label='Timezone Sync')
WorkspaceSetup = Transition(label='Workspace Setup')
SecurityTraining = Transition(label='Security Training')
ComplianceCheck = Transition(label='Compliance Check')
IntroMeeting = Transition(label='Intro Meeting')
FeedbackLoop = Transition(label='Feedback Loop')
ToolTraining = Transition(label='Tool Training')
NetworkIntro = Transition(label='Network Intro')
ProgressReview = Transition(label='Progress Review')

# Model onboarding major phases as partial orders
# Phase 1: Initial Setup and Compliance (ProfileSetup -> EquipmentShip -> AccessGrant -> PolicyReview -> ComplianceCheck)
phase1 = StrictPartialOrder(nodes=[ProfileSetup, EquipmentShip, AccessGrant, PolicyReview, ComplianceCheck])
phase1.order.add_edge(ProfileSetup, EquipmentShip)
phase1.order.add_edge(EquipmentShip, AccessGrant)
phase1.order.add_edge(AccessGrant, PolicyReview)
phase1.order.add_edge(PolicyReview, ComplianceCheck)

# Phase 2: Cultural and Mentorship Integration (MentorMatch, CultureTour, TimezoneSync, NetworkIntro)
# These can be partially ordered concurrent with MentorMatch first before CultureTour and TimezoneSync
phase2 = StrictPartialOrder(nodes=[MentorMatch, CultureTour, TimezoneSync, NetworkIntro])
phase2.order.add_edge(MentorMatch, CultureTour)
phase2.order.add_edge(MentorMatch, TimezoneSync)
phase2.order.add_edge(MentorMatch, NetworkIntro)

# Phase 3: Workspace and Tools Setup (WorkspaceSetup -> SecurityTraining -> ToolTraining)
phase3 = StrictPartialOrder(nodes=[WorkspaceSetup, SecurityTraining, ToolTraining])
phase3.order.add_edge(WorkspaceSetup, SecurityTraining)
phase3.order.add_edge(SecurityTraining, ToolTraining)

# Phase 4: Intro Meeting
intro_meeting = IntroMeeting  # single activity

# Phase 5: Feedback loop with ProgressReview and FeedbackLoop looping
progress_feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[ProgressReview, FeedbackLoop])

# Combine intro meeting and feedback loop partial order
post_intro = StrictPartialOrder(nodes=[intro_meeting, progress_feedback_loop])
post_intro.order.add_edge(intro_meeting, progress_feedback_loop)

# Combine phases 2 and 3 in parallel (cultural + mentorship and workspace/tools set up)
phase2and3 = StrictPartialOrder(nodes=[phase2, phase3])
# No edges: concurrent execution

# Combine phase2and3 with intro+feedback order (phase2and3 -> post_intro)
phase2_3_intro = StrictPartialOrder(nodes=[phase2and3, post_intro])
phase2_3_intro.order.add_edge(phase2and3, post_intro)

# Combine phase1 with the rest: phase1 -> phase2_3_intro
root = StrictPartialOrder(nodes=[phase1, phase2_3_intro])
root.order.add_edge(phase1, phase2_3_intro)