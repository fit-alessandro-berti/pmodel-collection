# Generated from: 9ed97d72-319b-4337-bcc9-c01958d0e1e3.json
# Description: This complex process involves the detailed authentication of antique artifacts by combining scientific analysis, provenance research, and expert evaluation. Initially, artifacts undergo non-invasive imaging and material composition tests to detect forgeries or restorations. Concurrently, historical records and ownership chains are meticulously verified through archival research and interviews. The process also includes stylistic comparison with verified pieces and consultation with domain experts. Finally, all gathered data is synthesized into a comprehensive report that determines authenticity, estimated value, and historical significance, ensuring the artifact's credibility in the market and preservation archives.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# define all activities
visual_scan     = Transition(label='Visual Scan')
imaging_analysis = Transition(label='Imaging Analysis')
material_test   = Transition(label='Material Test')
forgery_detect  = Transition(label='Forgery Detect')

archive_search    = Transition(label='Archive Search')
interview_experts = Transition(label='Interview Experts')
provenance_check  = Transition(label='Provenance Check')
historical_cross  = Transition(label='Historical Cross')

stylistic_match = Transition(label='Stylistic Match')
expert_review   = Transition(label='Expert Review')

condition_report = Transition(label='Condition Report')
market_compare   = Transition(label='Market Compare')
value_estimation = Transition(label='Value Estimation')
db_update        = Transition(label='Database Update')
final_report     = Transition(label='Final Report')

# build the partial order
root = StrictPartialOrder(nodes=[
    # imaging & material branch
    visual_scan, imaging_analysis, material_test, forgery_detect,
    # provenance branch
    archive_search, interview_experts, provenance_check, historical_cross,
    # stylistic/expert branch
    stylistic_match, expert_review,
    # final synthesis branch
    condition_report, market_compare, value_estimation, db_update, final_report
])

# sequencing edges
# initial tests -> forgery detection
root.order.add_edge(visual_scan, forgery_detect)
root.order.add_edge(imaging_analysis, forgery_detect)
root.order.add_edge(material_test, forgery_detect)

# provenance research
root.order.add_edge(archive_search, provenance_check)
root.order.add_edge(interview_experts, provenance_check)
root.order.add_edge(provenance_check, historical_cross)

# stylistic comparison -> expert review
root.order.add_edge(stylistic_match, expert_review)

# join branches into condition report
root.order.add_edge(forgery_detect, condition_report)
root.order.add_edge(historical_cross, condition_report)
root.order.add_edge(expert_review, condition_report)

# final synthesis workflow
root.order.add_edge(condition_report, market_compare)
root.order.add_edge(market_compare, value_estimation)
root.order.add_edge(value_estimation, db_update)
root.order.add_edge(db_update, final_report)