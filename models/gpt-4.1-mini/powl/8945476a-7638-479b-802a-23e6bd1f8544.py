# Generated from: 8945476a-7638-479b-802a-23e6bd1f8544.json
# Description: This process manages the end-to-end handling of custom art commissions for a boutique studio specializing in mixed media pieces. It involves initial client consultation to understand artistic preferences, followed by concept sketching and iterative feedback cycles. Once approved, materials sourcing is conducted considering sustainability and cost. The creation phase includes layering of diverse media, drying periods, and quality checks. Post-production involves framing options, documentation of artwork provenance, and final client presentation. Payment scheduling aligns with milestone completions, and after-delivery support includes care instructions and potential restoration services. The workflow ensures personalized client engagement while maintaining artistic integrity and operational efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Client_Meet = Transition(label='Client Meet')
Preference_Survey = Transition(label='Preference Survey')
Concept_Sketch = Transition(label='Concept Sketch')
Feedback_Loop = Transition(label='Feedback Loop')
Material_Sourcing = Transition(label='Material Sourcing')
Cost_Analysis = Transition(label='Cost Analysis')
Layer_Application = Transition(label='Layer Application')
Drying_Period = Transition(label='Drying Period')
Quality_Check = Transition(label='Quality Check')
Frame_Selection = Transition(label='Frame Selection')
Provenance_Doc = Transition(label='Provenance Doc')
Final_Presentation = Transition(label='Final Presentation')
Payment_Setup = Transition(label='Payment Setup')
Delivery_Schedule = Transition(label='Delivery Schedule')
Aftercare_Support = Transition(label='Aftercare Support')
Restoration_Plan = Transition(label='Restoration Plan')

# Construct the iterative feedback cycle as a LOOP: concept sketch (A), feedback (B)
# * (Concept Sketch, Feedback Loop)
Feedback_Cycle = OperatorPOWL(operator=Operator.LOOP, children=[Concept_Sketch, Feedback_Loop])

# Material sourcing and cost analysis must be done sequentially after feedback cycle
Material_Phase_PO = StrictPartialOrder(nodes=[Material_Sourcing, Cost_Analysis])
Material_Phase_PO.order.add_edge(Material_Sourcing, Cost_Analysis)

# Creation phase: layering, drying, quality check sequential
Creation_PO = StrictPartialOrder(nodes=[Layer_Application, Drying_Period, Quality_Check])
Creation_PO.order.add_edge(Layer_Application, Drying_Period)
Creation_PO.order.add_edge(Drying_Period, Quality_Check)

# Post-production phase with three sequential activities
Postproduction_PO = StrictPartialOrder(nodes=[Frame_Selection, Provenance_Doc, Final_Presentation])
Postproduction_PO.order.add_edge(Frame_Selection, Provenance_Doc)
Postproduction_PO.order.add_edge(Provenance_Doc, Final_Presentation)

# Payment scheduling aligned with milestones (assumed after final presentation)
Payment_PO = StrictPartialOrder(nodes=[Payment_Setup, Delivery_Schedule])
Payment_PO.order.add_edge(Payment_Setup, Delivery_Schedule)

# After-delivery support includes care instructions and restoration plan, 
# assume these two activities are concurrent after delivery schedule
Aftercare_PO = StrictPartialOrder(nodes=[Aftercare_Support, Restoration_Plan])
# no ordering edges between Aftercare_Support and Restoration_Plan - concurrent

# Compose the front sequence: Client Meet -> Preference Survey -> Feedback_Cycle -> Material Phase -> Creation Phase -> Postproduction -> Payment -> Aftercare
root = StrictPartialOrder(nodes=[
    Client_Meet, Preference_Survey, Feedback_Cycle, Material_Phase_PO,
    Creation_PO, Postproduction_PO, Payment_PO, Aftercare_PO])

# Add ordering edges to capture the linear flow between phases
root.order.add_edge(Client_Meet, Preference_Survey)
root.order.add_edge(Preference_Survey, Feedback_Cycle)
root.order.add_edge(Feedback_Cycle, Material_Phase_PO)
root.order.add_edge(Material_Phase_PO, Creation_PO)
root.order.add_edge(Creation_PO, Postproduction_PO)
root.order.add_edge(Postproduction_PO, Payment_PO)
root.order.add_edge(Payment_PO, Aftercare_PO)