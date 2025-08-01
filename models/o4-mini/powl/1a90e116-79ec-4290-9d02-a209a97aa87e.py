# Generated from: 1a90e116-79ec-4290-9d02-a209a97aa87e.json
# Description: This process describes a complex cross-industry innovation cycle where a company integrates unconventional partnerships, iterative prototyping, and adaptive market testing to develop breakthrough products. Starting from ideation through biomimicry workshops, it moves into decentralized sourcing of unconventional materials, followed by rapid modular prototyping. The cycle includes parallel regulatory simulations, stakeholder co-creation sessions, and dynamic risk assessments. Post-launch, the process emphasizes continuous feedback loops via AI-driven sentiment analysis and adaptive supply chain recalibration to sustain competitive advantage in volatile markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
idea_harvest = Transition(label="Idea Harvest")
biomimicry_lab = Transition(label="Biomimicry Lab")
partner_vetting = Transition(label="Partner Vetting")
material_scout = Transition(label="Material Scout")
prototype_sprint = Transition(label="Prototype Sprint")

regulatory_scan = Transition(label="Regulatory Scan")
risk_mapping = Transition(label="Risk Mapping")
co_creation = Transition(label="Co-Creation")

market_pilot = Transition(label="Market Pilot")

feedback_loop = Transition(label="Feedback Loop")
sentiment_scan = Transition(label="Sentiment Scan")
data_fusion = Transition(label="Data Fusion")
trend_forecast = Transition(label="Trend Forecast")
supply_recalibrate = Transition(label="Supply Recalibrate")

scale_adjust = Transition(label="Scale Adjust")

# Parallel regulatory, risk and co-creation
parallel_assessments = StrictPartialOrder(
    nodes=[regulatory_scan, risk_mapping, co_creation]
)
# no edges => fully concurrent

# Feedback‐body for the loop: sentiment → data fusion → trend forecast → supply recalibrate
feedback_body = StrictPartialOrder(
    nodes=[sentiment_scan, data_fusion, trend_forecast, supply_recalibrate]
)
feedback_body.order.add_edge(sentiment_scan, data_fusion)
feedback_body.order.add_edge(data_fusion, trend_forecast)
feedback_body.order.add_edge(trend_forecast, supply_recalibrate)

# Loop: execute Feedback Loop activity, then either exit or do feedback_body then repeat
feedback_loop_cycle = OperatorPOWL(
    operator=Operator.LOOP,
    children=[feedback_loop, feedback_body]
)

# Build the top‐level partial order
root = StrictPartialOrder(
    nodes=[
        idea_harvest,
        biomimicry_lab,
        partner_vetting,
        material_scout,
        prototype_sprint,
        parallel_assessments,
        market_pilot,
        feedback_loop_cycle,
        scale_adjust
    ]
)

# Define the sequencing edges
root.order.add_edge(idea_harvest, biomimicry_lab)
root.order.add_edge(biomimicry_lab, partner_vetting)
root.order.add_edge(partner_vetting, material_scout)
root.order.add_edge(material_scout, prototype_sprint)

# Prototype Sprint must complete before parallel assessments
root.order.add_edge(prototype_sprint, parallel_assessments)

# All three assessments before market pilot
root.order.add_edge(parallel_assessments, market_pilot)

# Market pilot precedes the feedback loop
root.order.add_edge(market_pilot, feedback_loop_cycle)

# When the feedback loop finally exits, scale adjust happens
root.order.add_edge(feedback_loop_cycle, scale_adjust)