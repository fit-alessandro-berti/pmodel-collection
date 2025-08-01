# Generated from: 273f2630-b12c-4cff-bf39-1f83deb9d4c6.json
# Description: This process involves the detailed examination and verification of antique artifacts to determine authenticity, provenance, and value. It begins with initial visual inspection, followed by material analysis using advanced spectroscopy techniques. Experts then cross-reference historical records and provenance databases. Subsequently, microscopic wear pattern analysis is conducted to detect signs of age or forgery. Forensic imaging is employed to reveal hidden markings or restorations. The artifact undergoes carbon dating or thermoluminescence tests if applicable. A multidisciplinary panel reviews all findings to reach a consensus. Lastly, a comprehensive authenticity report is prepared, including recommendations for restoration or sale. The entire process ensures that collectors, museums, and sellers have accurate and reliable information about the artifact's legitimacy and history.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Initial_Inspect = Transition(label='Initial Inspect')

Material_Scan = Transition(label='Material Scan')

Historical_Check = Transition(label='Historical Check')
Database_Query = Transition(label='Database Query')
# The above two are parallel after Material Scan, both must complete

Wear_Analysis = Transition(label='Wear Analysis')
Microscope_View = Transition(label='Microscope View')
# The above two are parallel after Historical_Check and Database_Query complete

Forensic_Image = Transition(label='Forensic Image')

# Carbon Dating and Thermoluminescence tests are alternative - one or none can be done
Carbon_Dating = Transition(label='Carbon Dating')
Thermolum_Test = Transition(label='Thermolum Test')

# Expert Panel after all tests
Expert_Panel = Transition(label='Expert Panel')

# Final report preparation sequence: Report Draft -> Report Review -> (Restoration Advise || Sale Prep) -> Final Archive

Report_Draft = Transition(label='Report Draft')
Report_Review = Transition(label='Report Review')

Restoration_Advise = Transition(label='Restoration Advise')
Sale_Prep = Transition(label='Sale Prep')
# Restoration Advise and Sale Prep are parallel

Final_Archive = Transition(label='Final Archive')

# Build PO stepwise according to dependencies

# Step 1: After Initial Inspect -> Material Scan
step1 = StrictPartialOrder(nodes=[Initial_Inspect, Material_Scan])
step1.order.add_edge(Initial_Inspect, Material_Scan)

# Step 2: After Material Scan -> Historical Check and Database Query in parallel
step2 = StrictPartialOrder(nodes=[Historical_Check, Database_Query])
# no edges between Historical_Check and Database_Query means concurrent

# Link step1 to step2
po_12 = StrictPartialOrder(nodes=[step1, step2])
po_12.order.add_edge(step1, step2)

# Step 3: After Historical Check and Database Query complete -> Wear Analysis and Microscope View concurrently
step3 = StrictPartialOrder(nodes=[Wear_Analysis, Microscope_View])
# concurrent activities -> no order edges

# Link step2 to step3
po_23 = StrictPartialOrder(nodes=[po_12, step3])
po_23.order.add_edge(po_12, step3)

# Step 4: Forensic Image after Wear Analysis and Microscope View complete
step4 = Forensic_Image

po_34 = StrictPartialOrder(nodes=[po_23, step4])
po_34.order.add_edge(po_23, step4)

# Step 5: Carbon Dating or Thermolum Test choice after Forensic Image

# Choice operator XOR(C, T)
tests_choice = OperatorPOWL(operator=Operator.XOR, children=[Carbon_Dating, Thermolum_Test])

po_45 = StrictPartialOrder(nodes=[po_34, tests_choice])
po_45.order.add_edge(po_34, tests_choice)

# Step 6: Expert Panel after tests
po_56 = StrictPartialOrder(nodes=[po_45, Expert_Panel])
po_56.order.add_edge(po_45, Expert_Panel)

# Step 7: Report Draft after Expert Panel
po_67 = StrictPartialOrder(nodes=[po_56, Report_Draft])
po_67.order.add_edge(po_56, Report_Draft)

# Step 8: Report Review after Report Draft
po_78 = StrictPartialOrder(nodes=[po_67, Report_Review])
po_78.order.add_edge(po_67, Report_Review)

# Step 9: After Report Review, Restoration Advise and Sale Prep concurrently
step9 = StrictPartialOrder(nodes=[Restoration_Advise, Sale_Prep])
# no order edges -> concurrent

po_89 = StrictPartialOrder(nodes=[po_78, step9])
po_89.order.add_edge(po_78, step9)

# Step 10: Final Archive after both Restoration and Sale Prep complete
po_910 = StrictPartialOrder(nodes=[po_89, Final_Archive])
po_910.order.add_edge(po_89, Final_Archive)

# Define root as the full model
root = po_910