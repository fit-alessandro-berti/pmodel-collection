# Generated from: 9c69c021-a181-4094-a22b-cfe4d7323e99.json
# Description: This process involves the creation and market introduction of a niche artisan perfume line. Beginning with raw botanical sourcing from remote locations, the workflow includes scent formulation through iterative blending cycles, stability testing under varying environmental conditions, packaging design aligned with sustainable principles, and limited batch production using traditional methods. Following quality assurance, the marketing team crafts immersive storytelling campaigns targeting select luxury boutiques, followed by influencer collaboration and exclusive launch events. Post-launch, customer feedback is gathered via curated channels to inform future iterations and maintain brand authenticity in a competitive artisan space.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

BotanicalSourcing = Transition(label='Botanical Sourcing')

ScentFormulation = Transition(label='Scent Formulation')
BlendTesting = Transition(label='Blend Testing')

StabilityCheck = Transition(label='Stability Check')
PackagingDesign = Transition(label='Packaging Design')
BatchProduction = Transition(label='Batch Production')

QualityReview = Transition(label='Quality Review')

StoryCrafting = Transition(label='Story Crafting')
BoutiqueTargeting = Transition(label='Boutique Targeting')
InfluencerOutreach = Transition(label='Influencer Outreach')
LaunchPlanning = Transition(label='Launch Planning')
EventCoordination = Transition(label='Event Coordination')

FeedbackGathering = Transition(label='Feedback Gathering')
IterationPlanning = Transition(label='Iteration Planning')
BrandMonitoring = Transition(label='Brand Monitoring')

# Define the blending and testing loop: do (Blend Testing) then (Stability Check),
# then decide to exit or repeat Blend Testing + Stability Check again.
blend_test_check_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        BlendTesting,
        StabilityCheck
    ]
)

# After Scent Formulation, do the looping blend_test_check_loop
# The loop operator children: first child = body A, second child = loop body B:
# * (A, B): execute A, then choose exit or execute B then A again
# We want the loop to repeat blending + stability check, so A=BlendTesting, B=StabilityCheck,
# but we need both in the loop. Instead, model the loop as:
# execute BlendTesting, then choose exit or execute StabilityCheck then BlendTesting again
# The process requires iterative blending cycles, i.e., BlendTesting and StabilityCheck looped.
# So the loop children = [BlendTesting, StabilityCheck]

# We can wrap the loop around BlendTesting and StabilityCheck:
# So the loop node = LOOP(BlendTesting, StabilityCheck)

# Now the order:
# BotanicalSourcing --> ScentFormulation --> loop(BlendTesting, StabilityCheck) --> PackagingDesign --> BatchProduction

# Then QualityReview after BatchProduction

# Marketing activities after QualityReview:
# StoryCrafting --> BoutiqueTargeting --> InfluencerOutreach --> LaunchPlanning --> EventCoordination
# These are sequential

# Then post launch:
# FeedbackGathering --> IterationPlanning --> BrandMonitoring

# Construct POs to model concurrency where implied or sequential where clearly ordered

# Pre-loop partial order
pre_loop = StrictPartialOrder(
    nodes=[BotanicalSourcing, ScentFormulation]
)
pre_loop.order.add_edge(BotanicalSourcing, ScentFormulation)

loop_node = OperatorPOWL(
    operator=Operator.LOOP,
    children=[BlendTesting, StabilityCheck]
)

after_loop = StrictPartialOrder(
    nodes=[PackagingDesign, BatchProduction]
)
after_loop.order.add_edge(PackagingDesign, BatchProduction)

pre_marketing = StrictPartialOrder(
    nodes=[StoryCrafting, BoutiqueTargeting, InfluencerOutreach, LaunchPlanning, EventCoordination]
)
pre_marketing.order.add_edge(StoryCrafting, BoutiqueTargeting)
pre_marketing.order.add_edge(BoutiqueTargeting, InfluencerOutreach)
pre_marketing.order.add_edge(InfluencerOutreach, LaunchPlanning)
pre_marketing.order.add_edge(LaunchPlanning, EventCoordination)

post_launch = StrictPartialOrder(
    nodes=[FeedbackGathering, IterationPlanning, BrandMonitoring]
)
post_launch.order.add_edge(FeedbackGathering, IterationPlanning)
post_launch.order.add_edge(IterationPlanning, BrandMonitoring)

# QualityReview after batch production
quality_and_marketing = StrictPartialOrder(
    nodes=[QualityReview, pre_marketing]
)
quality_and_marketing.order.add_edge(QualityReview, pre_marketing)

# Compose main partial order:
# BotanicalSourcing --> ScentFormulation --> loop --> PackagingDesign --> BatchProduction --> QualityReview --> marketing
root = StrictPartialOrder(
    nodes=[pre_loop, loop_node, after_loop, quality_and_marketing, post_launch]
)
root.order.add_edge(pre_loop, loop_node)
root.order.add_edge(loop_node, after_loop)
root.order.add_edge(after_loop, quality_and_marketing)
root.order.add_edge(quality_and_marketing, post_launch)