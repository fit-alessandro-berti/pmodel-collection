# Generated from: af23eed9-0a5b-46bd-9ff0-a6366aa95c30.json
# Description: This process is designed to authenticate and verify the provenance of rare historical artifacts prior to acquisition by a museum. It involves multidisciplinary evaluations including forensic material analysis, provenance research, expert consultations, and legal clearance. Initial steps include artifact intake and preliminary condition assessment, followed by spectroscopy and carbon dating tests to validate age. Concurrently, provenance documentation is gathered and cross-referenced with archival databases to detect forgeries or ownership disputes. Expert historians and conservators provide interpretive reports, while legal teams ensure compliance with cultural heritage laws. The process concludes with a comprehensive authentication report and decision on acquisition, ensuring the artifact’s legitimacy and ethical procurement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Artifact_Intake = Transition(label='Artifact Intake')
Condition_Check = Transition(label='Condition Check')

Material_Scan = Transition(label='Material Scan')
Age_Dating = Transition(label='Age Dating')

Provenance_Search = Transition(label='Provenance Search')
Archive_Review = Transition(label='Archive Review')
Forgery_Check = Transition(label='Forgery Check')

Expert_Consult = Transition(label='Expert Consult')
Historical_Report = Transition(label='Historical Report')
Conservator_Input = Transition(label='Conservator Input')

Legal_Review = Transition(label='Legal Review')
Compliance_Audit = Transition(label='Compliance Audit')

Risk_Assessment = Transition(label='Risk Assessment')
Final_Analysis = Transition(label='Final Analysis')

Report_Generation = Transition(label='Report Generation')
Acquisition_Vote = Transition(label='Acquisition Vote')

# 1. Initial sequence: Artifact Intake -> Condition Check
initial_seq = StrictPartialOrder(nodes=[Artifact_Intake, Condition_Check])
initial_seq.order.add_edge(Artifact_Intake, Condition_Check)

# 2. Material validation tests: Material Scan -> Age Dating
material_tests = StrictPartialOrder(nodes=[Material_Scan, Age_Dating])
material_tests.order.add_edge(Material_Scan, Age_Dating)

# 3. Provenance investigation concurrency: Provenance Search -> Archive Review -> Forgery Check
provenance_chain = StrictPartialOrder(nodes=[Provenance_Search, Archive_Review, Forgery_Check])
provenance_chain.order.add_edge(Provenance_Search, Archive_Review)
provenance_chain.order.add_edge(Archive_Review, Forgery_Check)

# 4. Expertise reports concurrency: Expert Consult, Historical Report, Conservator Input
expertise_reports = StrictPartialOrder(nodes=[Expert_Consult, Historical_Report, Conservator_Input])
# They are concurrent (no order edges)

# 5. Legal and compliance concurrency: Legal Review -> Compliance Audit
legal_compliance = StrictPartialOrder(nodes=[Legal_Review, Compliance_Audit])
legal_compliance.order.add_edge(Legal_Review, Compliance_Audit)

# 6. Risk Assessment and Final Analysis concurrency
risk_final_analysis = StrictPartialOrder(nodes=[Risk_Assessment, Final_Analysis])
# concurrent (no edges)

# Group all concurrency after initial checks
# According to description:
# After Condition Check, concurrently:
#   - material_tests
#   - provenance_chain
#   - expertise_reports
#   - legal_compliance
#   - risk_final_analysis

after_checks_concurrency = StrictPartialOrder(
    nodes=[material_tests, provenance_chain, expertise_reports, legal_compliance, risk_final_analysis]
)
# No order edges = fully concurrent

# 7. Report Generation after all above
# We add a final strict partial order:
# All concurrent groups --> Report Generation --> Acquisition Vote

# First, represent "all concurrency" --> Report Generation
final_report_order = StrictPartialOrder(
    nodes=[after_checks_concurrency, Report_Generation, Acquisition_Vote]
)
# all concurrency precedes Report Generation
final_report_order.order.add_edge(after_checks_concurrency, Report_Generation)
final_report_order.order.add_edge(Report_Generation, Acquisition_Vote)

# 8. Combine initial sequence with after_checks_concurrency with final report chain
# initial_seq --> after_checks_concurrency
# initial_seq.order.add_edge(Condition_Check, ... concurrency start)
root = StrictPartialOrder(
    nodes=[initial_seq, after_checks_concurrency, Report_Generation, Acquisition_Vote]
)
root.order.add_edge(initial_seq, after_checks_concurrency)
root.order.add_edge(after_checks_concurrency, Report_Generation)
root.order.add_edge(Report_Generation, Acquisition_Vote)