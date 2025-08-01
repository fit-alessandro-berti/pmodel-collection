# Generated from: a2d9cfc0-e73e-409a-8c70-ee7052817581.json
# Description: This process involves the systematic examination and verification of antique artifacts to determine authenticity and provenance. It integrates multidisciplinary assessments including material analysis, historical context evaluation, stylistic comparison, and provenance research. Experts collaborate to detect forgeries, restorations, or alterations while ensuring compliance with legal and ethical standards. The process culminates in certification, documentation, and recommendations for conservation or sale, tailored to the artifact’s unique characteristics and market demand.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Initial_Review = Transition(label='Initial Review')

# Multidisciplinary assessments in partial order with concurrency
Provenance_Check = Transition(label='Provenance Check')
Material_Sampling = Transition(label='Material Sampling')
Spectral_Scan = Transition(label='Spectral Scan')
Stylistic_Match = Transition(label='Stylistic Match')
Historical_Context = Transition(label='Historical Context')

# Expert collaboration partial order
Forgery_Detection = Transition(label='Forgery Detection')
Restoration_Check = Transition(label='Restoration Check')
Expert_Consultation = Transition(label='Expert Consultation')

# Legal and ethical screening partial order with concurrency
Legal_Assessment = Transition(label='Legal Assessment')
Ethics_Screening = Transition(label='Ethics Screening')

# Reporting and certification partial order
Condition_Report = Transition(label='Condition Report')
Certification_Prep = Transition(label='Certification Prep')
Documentation = Transition(label='Documentation')
Final_Approval = Transition(label='Final Approval')

# Final decision: either Conservation Plan or Market Analysis (exclusive choice)
Conservation_Plan = Transition(label='Conservation Plan')
Market_Analysis = Transition(label='Market Analysis')
Final_Choice = OperatorPOWL(operator=Operator.XOR, children=[Conservation_Plan, Market_Analysis])

# Construct multidisciplinary assessments partial order (all concurrent or partially ordered if needed)
multidisciplinary = StrictPartialOrder(
    nodes=[Provenance_Check, Material_Sampling, Spectral_Scan, Stylistic_Match, Historical_Context]
)
# no order edges - all concurrent here, could be done in any order

# Expert collaboration partial order:
# Let's assume Forgery_Detection and Restoration_Check precede Expert_Consultation
expert_collab = StrictPartialOrder(
    nodes=[Forgery_Detection, Restoration_Check, Expert_Consultation]
)
expert_collab.order.add_edge(Forgery_Detection, Expert_Consultation)
expert_collab.order.add_edge(Restoration_Check, Expert_Consultation)

# Legal and ethical screening concurrent
legal_ethics = StrictPartialOrder(
    nodes=[Legal_Assessment, Ethics_Screening]
)
# no order edges = concurrent

# Reporting and certification partial order (linear)
reporting = StrictPartialOrder(
    nodes=[Condition_Report, Certification_Prep, Documentation, Final_Approval]
)
reporting.order.add_edge(Condition_Report, Certification_Prep)
reporting.order.add_edge(Certification_Prep, Documentation)
reporting.order.add_edge(Documentation, Final_Approval)

# Now build the full partial order with all main blocks
# Ordering between:
# Initial Review -> multidisciplinary assessments
# multidisciplinary assessments -> expert collaboration
# expert collaboration -> legal & ethics screening
# legal & ethics screening -> reporting
# reporting -> final choice

root = StrictPartialOrder(
    nodes=[
        Initial_Review,
        multidisciplinary,
        expert_collab,
        legal_ethics,
        reporting,
        Final_Choice
    ]
)

# Add edges defining control flow dependencies
root.order.add_edge(Initial_Review, multidisciplinary)
root.order.add_edge(multidisciplinary, expert_collab)
root.order.add_edge(expert_collab, legal_ethics)
root.order.add_edge(legal_ethics, reporting)
root.order.add_edge(reporting, Final_Choice)