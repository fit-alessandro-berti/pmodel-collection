# Generated from: ec9aec90-0174-4e31-a649-c752527fd227.json
# Description: This process outlines the intricate workflow involved in restoring antique artifacts for museums or private collectors. It begins with artifact assessment and provenance verification to ensure authenticity. Following that, condition analysis identifies damage and material composition. Conservation planning is then developed, balancing preservation with restoration goals. Next, delicate cleaning and stabilization treatments are performed, often requiring custom tools. Missing parts are fabricated or sourced from archival materials. After structural repairs, surface treatments including patina preservation or color matching are applied. Documentation throughout ensures traceability. Final quality review and client approval precede careful packaging and transport arrangements to prevent damage during delivery. This atypical but realistic process demands expertise across multiple disciplines to return artifacts to display condition while respecting their historical integrity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Assess_Artifact = Transition(label='Assess Artifact')
Verify_Provenance = Transition(label='Verify Provenance')
Analyze_Condition = Transition(label='Analyze Condition')
Plan_Conservation = Transition(label='Plan Conservation')
Clean_Surface = Transition(label='Clean Surface')
Stabilize_Structure = Transition(label='Stabilize Structure')
Source_Materials = Transition(label='Source Materials')
Fabricate_Parts = Transition(label='Fabricate Parts')
Perform_Repairs = Transition(label='Perform Repairs')
Apply_Patina = Transition(label='Apply Patina')
Match_Colors = Transition(label='Match Colors')
Document_Process = Transition(label='Document Process')
Review_Quality = Transition(label='Review Quality')
Obtain_Approval = Transition(label='Obtain Approval')
Package_Securely = Transition(label='Package Securely')
Arrange_Transport = Transition(label='Arrange Transport')

# Create choice for sourcing or fabricating missing parts (Source Materials XOR Fabricate Parts)
source_or_fabricate = OperatorPOWL(operator=Operator.XOR, children=[Source_Materials, Fabricate_Parts])

# Create choice for surface treatments (Apply Patina XOR Match Colors)
surface_treatment = OperatorPOWL(operator=Operator.XOR, children=[Apply_Patina, Match_Colors])

# First partial order:
# Assess Artifact --> Verify Provenance --> Analyze Condition --> Plan Conservation
po1 = StrictPartialOrder(nodes=[Assess_Artifact, Verify_Provenance, Analyze_Condition, Plan_Conservation])
po1.order.add_edge(Assess_Artifact, Verify_Provenance)
po1.order.add_edge(Verify_Provenance, Analyze_Condition)
po1.order.add_edge(Analyze_Condition, Plan_Conservation)

# Second partial order:
# Plan Conservation --> Clean Surface --> Stabilize Structure
po2 = StrictPartialOrder(nodes=[Plan_Conservation, Clean_Surface, Stabilize_Structure])
po2.order.add_edge(Plan_Conservation, Clean_Surface)
po2.order.add_edge(Clean_Surface, Stabilize_Structure)

# Third partial order:
# Stabilize Structure --> (source_or_fabricate) --> Perform Repairs
po3 = StrictPartialOrder(nodes=[Stabilize_Structure, source_or_fabricate, Perform_Repairs])
po3.order.add_edge(Stabilize_Structure, source_or_fabricate)
po3.order.add_edge(source_or_fabricate, Perform_Repairs)

# Fourth partial order:
# Perform Repairs --> surface_treatment
po4 = StrictPartialOrder(nodes=[Perform_Repairs, surface_treatment])
po4.order.add_edge(Perform_Repairs, surface_treatment)

# Fifth partial order:
# surface_treatment --> Document Process
po5 = StrictPartialOrder(nodes=[surface_treatment, Document_Process])
po5.order.add_edge(surface_treatment, Document_Process)

# Sixth partial order:
# Document Process --> Review Quality --> Obtain Approval
po6 = StrictPartialOrder(nodes=[Document_Process, Review_Quality, Obtain_Approval])
po6.order.add_edge(Document_Process, Review_Quality)
po6.order.add_edge(Review_Quality, Obtain_Approval)

# Seventh partial order:
# Obtain Approval --> Package Securely --> Arrange Transport
po7 = StrictPartialOrder(nodes=[Obtain_Approval, Package_Securely, Arrange_Transport])
po7.order.add_edge(Obtain_Approval, Package_Securely)
po7.order.add_edge(Package_Securely, Arrange_Transport)

# Compose all partial orders into one single partial order to preserve order between them
# Here they are connected sequentially
root = StrictPartialOrder(
    nodes=[
        Assess_Artifact, Verify_Provenance, Analyze_Condition, Plan_Conservation,
        Clean_Surface, Stabilize_Structure, source_or_fabricate, Perform_Repairs,
        surface_treatment, Document_Process, Review_Quality, Obtain_Approval,
        Package_Securely, Arrange_Transport
    ]
)

# Add ordering edges by combining all dependencies defined
# po1
root.order.add_edge(Assess_Artifact, Verify_Provenance)
root.order.add_edge(Verify_Provenance, Analyze_Condition)
root.order.add_edge(Analyze_Condition, Plan_Conservation)
# po2
root.order.add_edge(Plan_Conservation, Clean_Surface)
root.order.add_edge(Clean_Surface, Stabilize_Structure)
# po3
root.order.add_edge(Stabilize_Structure, source_or_fabricate)
root.order.add_edge(source_or_fabricate, Perform_Repairs)
# po4
root.order.add_edge(Perform_Repairs, surface_treatment)
# po5
root.order.add_edge(surface_treatment, Document_Process)
# po6
root.order.add_edge(Document_Process, Review_Quality)
root.order.add_edge(Review_Quality, Obtain_Approval)
# po7
root.order.add_edge(Obtain_Approval, Package_Securely)
root.order.add_edge(Package_Securely, Arrange_Transport)