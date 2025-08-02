# Generated from: 2ab236de-c4e7-47ed-8484-49412bb1ded9.json
# Description: This process involves the detailed restoration of ancient artifacts discovered during archaeological digs. It requires initial assessment of artifact condition, cleaning using specialized chemical and mechanical methods, structural stabilization with reversible adhesives, pigment analysis through spectroscopy, digital reconstruction for visualization, and finally, controlled environment packaging to ensure long-term preservation. Each step demands meticulous documentation and quality checks to maintain historical integrity and scientific accuracy while enabling future research and exhibition possibilities.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Initial_Assessment = Transition(label='Initial Assessment')

# Cleaning subprocess: Chemical Wash and Mechanical Cleaning concurrent before Surface Cleaning
Chemical_Wash = Transition(label='Chemical Wash')
Mechanical_Cleaning = Transition(label='Mechanical Cleaning')
Surface_Cleaning = Transition(label='Surface Cleaning')
cleaning_PO = StrictPartialOrder(nodes=[Chemical_Wash, Mechanical_Cleaning, Surface_Cleaning])
cleaning_PO.order.add_edge(Chemical_Wash, Surface_Cleaning)
cleaning_PO.order.add_edge(Mechanical_Cleaning, Surface_Cleaning)

Damage_Mapping = Transition(label='Damage Mapping')

Pigment_Analysis = Transition(label='Pigment Analysis')
Material_Testing = Transition(label='Material Testing')

# Structural Repair subprocess: Adhesive Application after Structural Repair
Structural_Repair = Transition(label='Structural Repair')
Adhesive_Application = Transition(label='Adhesive Application')
structural_PO = StrictPartialOrder(nodes=[Structural_Repair, Adhesive_Application])
structural_PO.order.add_edge(Structural_Repair, Adhesive_Application)

Digital_Scan = Transition(label='Digital Scan')
Reconstruction_3D = Transition(label='3D Reconstruction')

Condition_Reporting = Transition(label='Condition Reporting')
Quality_Review = Transition(label='Quality Review')

Packaging_Prep = Transition(label='Packaging Prep')
Climate_Control = Transition(label='Climate Control')

Final_Documentation = Transition(label='Final Documentation')

# Combine Pigment Analysis and Material Testing as concurrent
analysis_PO = StrictPartialOrder(nodes=[Pigment_Analysis, Material_Testing])

# Combine Digital Scan and 3D Reconstruction in partial order: Digital Scan --> 3D Reconstruction
digital_PO = StrictPartialOrder(nodes=[Digital_Scan, Reconstruction_3D])
digital_PO.order.add_edge(Digital_Scan, Reconstruction_3D)

# Combine Packaging Prep and Climate Control in partial order: Packaging Prep --> Climate Control
packaging_PO = StrictPartialOrder(nodes=[Packaging_Prep, Climate_Control])
packaging_PO.order.add_edge(Packaging_Prep, Climate_Control)

# Define the overall process partial order:
# Initial Assessment --> Cleaning subprocess --> Damage Mapping --> analysis_PO --> structural_PO --> digital_PO --> Condition Reporting --> Quality Review --> packaging_PO --> Final Documentation

root = StrictPartialOrder(nodes=[
    Initial_Assessment,
    cleaning_PO,
    Damage_Mapping,
    analysis_PO,
    structural_PO,
    digital_PO,
    Condition_Reporting,
    Quality_Review,
    packaging_PO,
    Final_Documentation
])

root.order.add_edge(Initial_Assessment, cleaning_PO)
root.order.add_edge(cleaning_PO, Damage_Mapping)
root.order.add_edge(Damage_Mapping, analysis_PO)
root.order.add_edge(analysis_PO, structural_PO)
root.order.add_edge(structural_PO, digital_PO)
root.order.add_edge(digital_PO, Condition_Reporting)
root.order.add_edge(Condition_Reporting, Quality_Review)
root.order.add_edge(Quality_Review, packaging_PO)
root.order.add_edge(packaging_PO, Final_Documentation)