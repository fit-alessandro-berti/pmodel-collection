# Generated from: 81441f5c-7e18-4939-834d-751c794fbc65.json
# Description: This process outlines the creation of a large-scale collaborative art installation involving multiple artists, engineers, and community stakeholders. It begins with concept ideation and stakeholder alignment, followed by material sourcing and prototype development. Parallel activities include regulatory compliance checks and community feedback sessions. After iterative design refinements, technical integration and structural testing are conducted to ensure safety and functionality. The installation phase involves coordinated logistics, on-site assembly, and real-time troubleshooting. Post-installation, the process includes interactive programming, public engagement events, and maintenance scheduling to sustain the artwork’s impact over time. Documentation and archival of the project complete the workflow, ensuring knowledge transfer and future reference.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Concept_Ideation = Transition(label='Concept Ideation')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Material_Sourcing = Transition(label='Material Sourcing')
Prototype_Build = Transition(label='Prototype Build')
Compliance_Check = Transition(label='Compliance Check')
Community_Review = Transition(label='Community Review')
Design_Refinement = Transition(label='Design Refinement')
Tech_Integration = Transition(label='Tech Integration')
Structural_Test = Transition(label='Structural Test')
Logistics_Plan = Transition(label='Logistics Plan')
Onsite_Setup = Transition(label='Onsite Setup')
Troubleshoot_Fix = Transition(label='Troubleshoot Fix')
Program_Install = Transition(label='Program Install')
Engagement_Event = Transition(label='Engagement Event')
Maintenance_Plan = Transition(label='Maintenance Plan')
Project_Archive = Transition(label='Project Archive')

# Sequential start: Concept Ideation --> Stakeholder Meet
start_po = StrictPartialOrder(nodes=[Concept_Ideation, Stakeholder_Meet])
start_po.order.add_edge(Concept_Ideation, Stakeholder_Meet)

# Next sequential: Material Sourcing --> Prototype Build
material_proto_po = StrictPartialOrder(nodes=[Material_Sourcing, Prototype_Build])
material_proto_po.order.add_edge(Material_Sourcing, Prototype_Build)

# Parallel activities: Compliance Check and Community Review (concurrent)
# so no order edges between them
parallel_checks = StrictPartialOrder(nodes=[Compliance_Check, Community_Review])

# After prototype build, parallel compliance and community review happen concurrently
# This means Prototype_Build -> Compliance_Check and Prototype_Build -> Community_Review
parallel_checks_big = StrictPartialOrder(nodes=[Prototype_Build, Compliance_Check, Community_Review])
parallel_checks_big.order.add_edge(Prototype_Build, Compliance_Check)
parallel_checks_big.order.add_edge(Prototype_Build, Community_Review)

# Then iterative design refinements (assume single Design_Refinement)
# Assume it starts after both Compliance_Check and Community_Review complete
design_refinement_po = StrictPartialOrder(nodes=[Compliance_Check, Community_Review, Design_Refinement])
design_refinement_po.order.add_edge(Compliance_Check, Design_Refinement)
design_refinement_po.order.add_edge(Community_Review, Design_Refinement)

# Technical integration and structural testing sequential
tech_struct_po = StrictPartialOrder(nodes=[Tech_Integration, Structural_Test])
tech_struct_po.order.add_edge(Tech_Integration, Structural_Test)

# Design refinement must be done before tech integration
design_tech_po = StrictPartialOrder(nodes=[Design_Refinement, Tech_Integration])
design_tech_po.order.add_edge(Design_Refinement, Tech_Integration)

# Combine design refinement + tech integration + structural testing sequence
design_tech_struct_po = StrictPartialOrder(
    nodes=[Design_Refinement, Tech_Integration, Structural_Test])
design_tech_struct_po.order.add_edge(Design_Refinement, Tech_Integration)
design_tech_struct_po.order.add_edge(Tech_Integration, Structural_Test)

# Installation phase: Logistics Plan --> Onsite Setup --> Troubleshoot Fix (sequence)
install_po = StrictPartialOrder(nodes=[Logistics_Plan, Onsite_Setup, Troubleshoot_Fix])
install_po.order.add_edge(Logistics_Plan, Onsite_Setup)
install_po.order.add_edge(Onsite_Setup, Troubleshoot_Fix)

# Program Install, Engagement Event, Maintenance Plan can be sequential after installation
post_install_po = StrictPartialOrder(
    nodes=[Program_Install, Engagement_Event, Maintenance_Plan])
post_install_po.order.add_edge(Program_Install, Engagement_Event)
post_install_po.order.add_edge(Engagement_Event, Maintenance_Plan)

# Finally after maintenance plan, Project Archive
archive_po = StrictPartialOrder(nodes=[Maintenance_Plan, Project_Archive])
archive_po.order.add_edge(Maintenance_Plan, Project_Archive)

# Connect installation to post installation
install_post_po = StrictPartialOrder(
    nodes=[Logistics_Plan, Onsite_Setup, Troubleshoot_Fix, Program_Install, Engagement_Event, Maintenance_Plan])
install_post_po.order.add_edge(Logistics_Plan, Onsite_Setup)
install_post_po.order.add_edge(Onsite_Setup, Troubleshoot_Fix)
install_post_po.order.add_edge(Troubleshoot_Fix, Program_Install)
install_post_po.order.add_edge(Program_Install, Engagement_Event)
install_post_po.order.add_edge(Engagement_Event, Maintenance_Plan)

# Connect everything into a big partial order representing the workflow:

# Start phase to material sourcing
start_material_po = StrictPartialOrder(
    nodes=[Concept_Ideation, Stakeholder_Meet, Material_Sourcing])
start_material_po.order.add_edge(Concept_Ideation, Stakeholder_Meet)
start_material_po.order.add_edge(Stakeholder_Meet, Material_Sourcing)

# Combine material sourcing to prototype build
material_prototype_po = StrictPartialOrder(nodes=[Material_Sourcing, Prototype_Build])
material_prototype_po.order.add_edge(Material_Sourcing, Prototype_Build)

# After prototype build -> compliance and community review in parallel
proto_parallel_po = StrictPartialOrder(
    nodes=[Prototype_Build, Compliance_Check, Community_Review])
proto_parallel_po.order.add_edge(Prototype_Build, Compliance_Check)
proto_parallel_po.order.add_edge(Prototype_Build, Community_Review)

# Compliance and community review -> Design Refinement
review_refine_po = StrictPartialOrder(
    nodes=[Compliance_Check, Community_Review, Design_Refinement])
review_refine_po.order.add_edge(Compliance_Check, Design_Refinement)
review_refine_po.order.add_edge(Community_Review, Design_Refinement)

# Design Refinement -> Tech Integration -> Structural Test
refine_tech_struct_po = StrictPartialOrder(
    nodes=[Design_Refinement, Tech_Integration, Structural_Test])
refine_tech_struct_po.order.add_edge(Design_Refinement, Tech_Integration)
refine_tech_struct_po.order.add_edge(Tech_Integration, Structural_Test)

# Structural Test -> Logistics Plan phase
struct_logistics_po = StrictPartialOrder(
    nodes=[Structural_Test, Logistics_Plan])
struct_logistics_po.order.add_edge(Structural_Test, Logistics_Plan)

# Logistics Plan -> Onsite Setup -> Troubleshoot Fix -> Program Install -> Engagement Event -> Maintenance Plan -> Project Archive
install_full_po = StrictPartialOrder(
    nodes=[Logistics_Plan, Onsite_Setup, Troubleshoot_Fix, Program_Install, Engagement_Event, Maintenance_Plan, Project_Archive])
install_full_po.order.add_edge(Logistics_Plan, Onsite_Setup)
install_full_po.order.add_edge(Onsite_Setup, Troubleshoot_Fix)
install_full_po.order.add_edge(Troubleshoot_Fix, Program_Install)
install_full_po.order.add_edge(Program_Install, Engagement_Event)
install_full_po.order.add_edge(Engagement_Event, Maintenance_Plan)
install_full_po.order.add_edge(Maintenance_Plan, Project_Archive)

# Assemble all nodes in one StrictPartialOrder
root = StrictPartialOrder(nodes=[
    Concept_Ideation,
    Stakeholder_Meet,
    Material_Sourcing,
    Prototype_Build,
    Compliance_Check,
    Community_Review,
    Design_Refinement,
    Tech_Integration,
    Structural_Test,
    Logistics_Plan,
    Onsite_Setup,
    Troubleshoot_Fix,
    Program_Install,
    Engagement_Event,
    Maintenance_Plan,
    Project_Archive
])

# Add edges for the full flow
root.order.add_edge(Concept_Ideation, Stakeholder_Meet)
root.order.add_edge(Stakeholder_Meet, Material_Sourcing)
root.order.add_edge(Material_Sourcing, Prototype_Build)
root.order.add_edge(Prototype_Build, Compliance_Check)
root.order.add_edge(Prototype_Build, Community_Review)
root.order.add_edge(Compliance_Check, Design_Refinement)
root.order.add_edge(Community_Review, Design_Refinement)
root.order.add_edge(Design_Refinement, Tech_Integration)
root.order.add_edge(Tech_Integration, Structural_Test)
root.order.add_edge(Structural_Test, Logistics_Plan)
root.order.add_edge(Logistics_Plan, Onsite_Setup)
root.order.add_edge(Onsite_Setup, Troubleshoot_Fix)
root.order.add_edge(Troubleshoot_Fix, Program_Install)
root.order.add_edge(Program_Install, Engagement_Event)
root.order.add_edge(Engagement_Event, Maintenance_Plan)
root.order.add_edge(Maintenance_Plan, Project_Archive)