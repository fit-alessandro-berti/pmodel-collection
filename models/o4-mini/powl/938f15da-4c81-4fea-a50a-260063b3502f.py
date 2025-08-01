# Generated from: 938f15da-4c81-4fea-a50a-260063b3502f.json
# Description: This process manages the end-to-end syndication of digital content across multiple platforms, including social media, partner websites, and proprietary apps. It involves content adaptation for diverse formats, automated scheduling based on audience analytics, compliance checks for licensing and regional restrictions, real-time performance monitoring, and iterative optimization through machine learning insights. The workflow ensures consistent branding, maximizes reach, and balances organic and paid distribution strategies while maintaining content integrity and legal compliance in dynamic market environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
ingest = Transition(label='Content Ingest')
format_adapt = Transition(label='Format Adapt')
metadata = Transition(label='Metadata Tagging')
license_verify = Transition(label='License Verify')
compliance_check = Transition(label='Compliance Check')
audience_segment = Transition(label='Audience Segment')
schedule_publish = Transition(label='Schedule Publish')
platform_sync = Transition(label='Platform Sync')
quality_audit = Transition(label='Quality Audit')
performance_track = Transition(label='Performance Track')
engagement_analyze = Transition(label='Engagement Analyze')
budget_adjust = Transition(label='Budget Adjust')
campaign_optimize = Transition(label='Campaign Optimize')
partner_notify = Transition(label='Partner Notify')
report_generate = Transition(label='Report Generate')
feedback_integrate = Transition(label='Feedback Integrate')

# Build the iterative optimization loop body (B)
B = StrictPartialOrder(nodes=[
    engagement_analyze,
    budget_adjust,
    campaign_optimize,
    partner_notify,
    report_generate,
    feedback_integrate
])
B.order.add_edge(engagement_analyze, budget_adjust)
B.order.add_edge(budget_adjust, campaign_optimize)
B.order.add_edge(campaign_optimize, partner_notify)
B.order.add_edge(partner_notify, report_generate)
B.order.add_edge(report_generate, feedback_integrate)

# Loop: always execute performance tracking, then choose exit or execute B then track again
optimization_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[performance_track, B]
)

# Root partial order for the end‐to‐end syndication process
root = StrictPartialOrder(nodes=[
    ingest,
    format_adapt,
    metadata,
    license_verify,
    compliance_check,
    audience_segment,
    schedule_publish,
    platform_sync,
    quality_audit,
    optimization_loop
])
# Define the linear flow up to the optimization loop
root.order.add_edge(ingest, format_adapt)
root.order.add_edge(format_adapt, metadata)
root.order.add_edge(metadata, license_verify)
root.order.add_edge(license_verify, compliance_check)
root.order.add_edge(compliance_check, audience_segment)
root.order.add_edge(audience_segment, schedule_publish)
root.order.add_edge(schedule_publish, platform_sync)
root.order.add_edge(platform_sync, quality_audit)
root.order.add_edge(quality_audit, optimization_loop)