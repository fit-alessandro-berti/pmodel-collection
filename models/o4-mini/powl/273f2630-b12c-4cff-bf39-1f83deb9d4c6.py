# Generated from: 273f2630-b12c-4cff-bf39-1f83deb9d4c6.json
# Description: This process involves the detailed examination and verification of antique artifacts to determine authenticity, provenance, and value. It begins with initial visual inspection, followed by material analysis using advanced spectroscopy techniques. Experts then cross-reference historical records and provenance databases. Subsequently, microscopic wear pattern analysis is conducted to detect signs of age or forgery. Forensic imaging is employed to reveal hidden markings or restorations. The artifact undergoes carbon dating or thermoluminescence tests if applicable. A multidisciplinary panel reviews all findings to reach a consensus. Lastly, a comprehensive authenticity report is prepared, including recommendations for restoration or sale. The entire process ensures that collectors, museums, and sellers have accurate and reliable information about the artifact's legitimacy and history.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
init_inspect = Transition(label='Initial Inspect')
material_scan = Transition(label='Material Scan')
historical_check = Transition(label='Historical Check')
database_query = Transition(label='Database Query')
wear_analysis = Transition(label='Wear Analysis')
microscope_view = Transition(label='Microscope View')
forensic_image = Transition(label='Forensic Image')
carbon_dating = Transition(label='Carbon Dating')
thermolum_test = Transition(label='Thermolum Test')
expert_panel = Transition(label='Expert Panel')
report_draft = Transition(label='Report Draft')
report_review = Transition(label='Report Review')
restoration_advise = Transition(label='Restoration Advise')
sale_prep = Transition(label='Sale Prep')
final_archive = Transition(label='Final Archive')

# A silent transition to model "no dating" if tests are not applicable
skip = SilentTransition()

# Exclusive choice between Carbon Dating, Thermolum Test, or skipping
dating_choice = OperatorPOWL(operator=Operator.XOR, 
                             children=[carbon_dating, thermolum_test, skip])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    init_inspect,
    material_scan,
    historical_check,
    database_query,
    wear_analysis,
    microscope_view,
    forensic_image,
    dating_choice,
    expert_panel,
    report_draft,
    report_review,
    restoration_advise,
    sale_prep,
    final_archive
])

# Define the control‐flow dependencies
root.order.add_edge(init_inspect, material_scan)
# After material scan, do historical check and database query (can be concurrent)
root.order.add_edge(material_scan, historical_check)
root.order.add_edge(material_scan, database_query)
# Both historical_check and database_query must complete before wear_analysis
root.order.add_edge(historical_check, wear_analysis)
root.order.add_edge(database_query, wear_analysis)
# Wear analysis → Microscope view → Forensic image
root.order.add_edge(wear_analysis, microscope_view)
root.order.add_edge(microscope_view, forensic_image)
# Forensic image → Choice of dating or skip → Expert panel
root.order.add_edge(forensic_image, dating_choice)
root.order.add_edge(dating_choice, expert_panel)
# Expert panel → Report draft → Report review
root.order.add_edge(expert_panel, report_draft)
root.order.add_edge(report_draft, report_review)
# After review, restoration advice and sale prep can proceed in parallel
root.order.add_edge(report_review, restoration_advise)
root.order.add_edge(report_review, sale_prep)
# Both must complete before final archive
root.order.add_edge(restoration_advise, final_archive)
root.order.add_edge(sale_prep, final_archive)