# Generated from: 4e179a9c-7651-4c71-bac9-0e002bad7aa7.json
# Description: This process orchestrates the integration of disparate industry insights to co-create breakthrough products. It begins by scouting emerging trends outside the core market, followed by cross-functional brainstorming sessions involving experts from unrelated sectors. Prototypes are then rapidly developed using unconventional materials, tested through immersive simulation environments, and evaluated via multi-stakeholder feedback loops. Risk assessments consider non-traditional variables, and iterative refinement cycles adapt the concept to diverse regulatory frameworks. The process culminates in a hybrid launch strategy, combining digital guerrilla marketing with selective physical showcases, ensuring maximum impact across varied customer segments and markets. Continuous post-launch analytics feed back into the innovation pipeline, fostering ongoing cross-pollination and sustained competitive advantage.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
tscout = Transition(label='Trend Scout')
expert_sync = Transition(label='Expert Sync')
idea_merge = Transition(label='Idea Merge')
material_select = Transition(label='Material Select')
prototype_build = Transition(label='Prototype Build')
simulate_test = Transition(label='Simulate Test')
stakeholder_poll = Transition(label='Stakeholder Poll')
risk_assess = Transition(label='Risk Assess')
iterate_design = Transition(label='Iterate Design')
regulation_map = Transition(label='Regulation Map')
hybrid_launch = Transition(label='Hybrid Launch')
market_segment = Transition(label='Market Segment')
guerrilla_ads = Transition(label='Guerrilla Ads')
showcase_plan = Transition(label='Showcase Plan')
feedback_loop = Transition(label='Feedback Loop')
data_analyze = Transition(label='Data Analyze')
pipeline_update = Transition(label='Pipeline Update')

# Loop for the refinement cycles (Iterate Design ↔ Regulation Map)
loop_refine = OperatorPOWL(
    operator=Operator.LOOP,
    children=[iterate_design, regulation_map]
)

# Parallel structure for the hybrid launch sub‐activities
parallel_launch_plan = StrictPartialOrder(
    nodes=[market_segment, guerrilla_ads, showcase_plan]
)
# no edges => fully concurrent

# Body of the post-launch analytics loop (Data Analyze → Pipeline Update)
analytics_body = StrictPartialOrder(
    nodes=[data_analyze, pipeline_update]
)
analytics_body.order.add_edge(data_analyze, pipeline_update)

# Loop for continuous post-launch analytics (Feedback Loop ↔ analytics_body)
loop_analytics = OperatorPOWL(
    operator=Operator.LOOP,
    children=[feedback_loop, analytics_body]
)

# Root model: the overall sequence and embedding of loops/parallelism
root = StrictPartialOrder(
    nodes=[
        tscout,
        expert_sync,
        idea_merge,
        material_select,
        prototype_build,
        simulate_test,
        stakeholder_poll,
        risk_assess,
        loop_refine,
        hybrid_launch,
        parallel_launch_plan,
        loop_analytics
    ]
)

# Define the partial order (the control‐flow dependencies)
root.order.add_edge(tscout, expert_sync)
root.order.add_edge(expert_sync, idea_merge)
root.order.add_edge(idea_merge, material_select)
root.order.add_edge(material_select, prototype_build)
root.order.add_edge(prototype_build, simulate_test)
root.order.add_edge(simulate_test, stakeholder_poll)
root.order.add_edge(stakeholder_poll, risk_assess)
root.order.add_edge(risk_assess, loop_refine)
root.order.add_edge(loop_refine, hybrid_launch)
root.order.add_edge(hybrid_launch, parallel_launch_plan)
root.order.add_edge(parallel_launch_plan, loop_analytics)