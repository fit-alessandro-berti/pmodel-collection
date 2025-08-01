# Generated from: 938f15da-4c81-4fea-a50a-260063b3502f.json
# Description: This process manages the end-to-end syndication of digital content across multiple platforms, including social media, partner websites, and proprietary apps. It involves content adaptation for diverse formats, automated scheduling based on audience analytics, compliance checks for licensing and regional restrictions, real-time performance monitoring, and iterative optimization through machine learning insights. The workflow ensures consistent branding, maximizes reach, and balances organic and paid distribution strategies while maintaining content integrity and legal compliance in dynamic market environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities (Transitions)
Content_Ingest = Transition(label='Content Ingest')
Format_Adapt = Transition(label='Format Adapt')
Metadata_Tagging = Transition(label='Metadata Tagging')
License_Verify = Transition(label='License Verify')
Audience_Segment = Transition(label='Audience Segment')
Schedule_Publish = Transition(label='Schedule Publish')
Platform_Sync = Transition(label='Platform Sync')
Quality_Audit = Transition(label='Quality Audit')
Compliance_Check = Transition(label='Compliance Check')
Performance_Track = Transition(label='Performance Track')
Engagement_Analyze = Transition(label='Engagement Analyze')
Budget_Adjust = Transition(label='Budget Adjust')
Campaign_Optimize = Transition(label='Campaign Optimize')
Partner_Notify = Transition(label='Partner Notify')
Report_Generate = Transition(label='Report Generate')
Feedback_Integrate = Transition(label='Feedback Integrate')

# Step 1: Content preparation partial order:
# 'Content Ingest' -> ('Format Adapt' and 'Metadata Tagging' concurrent)
content_prep = StrictPartialOrder(nodes=[Content_Ingest, Format_Adapt, Metadata_Tagging])
content_prep.order.add_edge(Content_Ingest, Format_Adapt)
content_prep.order.add_edge(Content_Ingest, Metadata_Tagging)

# Step 2: Compliance & licensing partial order:
# 'License Verify' -> 'Compliance Check' -> 'Quality Audit' (linear order)
compliance_chain = StrictPartialOrder(
    nodes=[License_Verify, Compliance_Check, Quality_Audit]
)
compliance_chain.order.add_edge(License_Verify, Compliance_Check)
compliance_chain.order.add_edge(Compliance_Check, Quality_Audit)

# Step 3: Scheduling and publishing partial order:
# 'Audience Segment' -> 'Schedule Publish' -> 'Platform Sync' (linear)
schedule_publish = StrictPartialOrder(
    nodes=[Audience_Segment, Schedule_Publish, Platform_Sync]
)
schedule_publish.order.add_edge(Audience_Segment, Schedule_Publish)
schedule_publish.order.add_edge(Schedule_Publish, Platform_Sync)

# Step 4: Monitoring and analysis partial order:
# 'Performance Track' -> 'Engagement Analyze' (linear)
monitoring = StrictPartialOrder(
    nodes=[Performance_Track, Engagement_Analyze]
)
monitoring.order.add_edge(Performance_Track, Engagement_Analyze)

# Step 5: Optimization loop:
# Loop node: First do 'Budget Adjust'
# Then either exit or do ('Campaign Optimize' then loop again)
budget_adjust = Budget_Adjust
campaign_optimize = Campaign_Optimize
optimization_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[budget_adjust, campaign_optimize]
)

# Step 6: Notifications and reporting partial order:
# 'Partner Notify' and 'Report Generate' concurrent, both precede 'Feedback Integrate'
notify_report = StrictPartialOrder(
    nodes=[Partner_Notify, Report_Generate, Feedback_Integrate]
)
notify_report.order.add_edge(Partner_Notify, Feedback_Integrate)
notify_report.order.add_edge(Report_Generate, Feedback_Integrate)

# Step 7: Overall process assembly in partial order:
# Start with content prep
# Then compliance_chain
# Then scheduling
# Then monitoring
# Then optimization_loop (iteration for ML insights)
# Finally notify_report

root = StrictPartialOrder(
    nodes=[
        content_prep,
        compliance_chain,
        schedule_publish,
        monitoring,
        optimization_loop,
        notify_report
    ]
)

root.order.add_edge(content_prep, compliance_chain)
root.order.add_edge(compliance_chain, schedule_publish)
root.order.add_edge(schedule_publish, monitoring)
root.order.add_edge(monitoring, optimization_loop)
root.order.add_edge(optimization_loop, notify_report)