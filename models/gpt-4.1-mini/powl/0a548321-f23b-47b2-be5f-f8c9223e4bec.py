# Generated from: 0a548321-f23b-47b2-be5f-f8c9223e4bec.json
# Description: This process involves the intricate steps required to restore historical artifacts within a museum setting. It begins with artifact assessment, followed by environmental analysis to determine optimal conservation conditions. The process includes cleaning with specialized tools, material stabilization, and structural repairs under controlled settings. Documentation and photographic records are maintained throughout to ensure traceability. Expert consultations help in selecting appropriate restoration chemicals. After restoration, artifacts undergo final quality checks and are prepared for display or storage, ensuring preservation while maintaining historical integrity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Artifact_Assess = Transition(label='Artifact Assess')
Env_Analysis = Transition(label='Env Analysis')
Clean_Tools = Transition(label='Clean Tools')
Material_Test = Transition(label='Material Test')
Stabilize_Form = Transition(label='Stabilize Form')
Structural_Repair = Transition(label='Structural Repair')
Chemical_Select = Transition(label='Chemical Select')
Expert_Consult = Transition(label='Expert Consult')
Photo_Record = Transition(label='Photo Record')
Condition_Monitor = Transition(label='Condition Monitor')
Documentation = Transition(label='Documentation')
Final_Inspect = Transition(label='Final Inspect')
Display_Prep = Transition(label='Display Prep')
Storage_Setup = Transition(label='Storage Setup')
Report_Archive = Transition(label='Report Archive')

# The process starts with Artifact Assess
# Then Env Analysis
# Cleaning with specialized tools, material stabilization, structural repairs under controlled settings happen
# Documentation and photographic records are maintained concurrently throughout the process -> model as concurrency alongside

# Expert consultations help selecting restoration chemicals, so Chemical_Select and Expert_Consult are sequential
# After restoration, final quality checks, then preparation for display or storage (choice)
# Finally, report archive

# The documentation and photo record should be concurrent with main process steps

# Construct the main restoration sequence first:
# Artifact Assess --> Env Analysis --> Clean Tools --> Material Test --> Stabilize Form --> Structural Repair

main_restoration = StrictPartialOrder(nodes=[Artifact_Assess, Env_Analysis, Clean_Tools, Material_Test, Stabilize_Form, Structural_Repair])
main_restoration.order.add_edge(Artifact_Assess, Env_Analysis)
main_restoration.order.add_edge(Env_Analysis, Clean_Tools)
main_restoration.order.add_edge(Clean_Tools, Material_Test)
main_restoration.order.add_edge(Material_Test, Stabilize_Form)
main_restoration.order.add_edge(Stabilize_Form, Structural_Repair)

# Documentation and Photo Record run concurrently, but they should overlap the main restoration steps,
# which we represent by putting them as concurrent nodes without order edges connecting to main_restoration nodes
# But since they are maintained throughout, we include them in the top-level PO alongside main_restoration.

# Expert Consult follows Chemical Select: Chemical_Select --> Expert_Consult
chem_expert = StrictPartialOrder(nodes=[Chemical_Select, Expert_Consult])
chem_expert.order.add_edge(Chemical_Select, Expert_Consult)

# Condition Monitor and Documentation and Photo Record are ongoing monitoring and records:
# "Documentation and photographic records are maintained throughout to ensure traceability."
# To model that, we add Documentation and Photo Record as nodes concurrent with main_restoration and chem_expert.

# Final Inspect after main restoration and expert consultation:
# So Final Inspect depends on Structural Repair and Expert Consult finishing.
final_inspect = Final_Inspect

# After Final Inspect, prepare for either Display Prep or Storage Setup (choice)
display_or_storage = OperatorPOWL(operator=Operator.XOR, children=[Display_Prep, Storage_Setup])

# Report Archive final after display or storage prep
# So order: final_inspect --> display_or_storage --> report_archive
# We need to combine these into a StrictPartialOrder for ordering

final_phase = StrictPartialOrder(nodes=[final_inspect, display_or_storage, Report_Archive])
final_phase.order.add_edge(final_inspect, display_or_storage)
final_phase.order.add_edge(display_or_storage, Report_Archive)

# Assemble all nodes at top level:
# - main_restoration (artifact to structural repair)
# - documentation, photo record, condition monitor (concurrent monitoring activities)
# - chem_expert (chemical select and expert consult)
# All must finish before final_phase can start

# So final_phase depends on main_restoration completion and chem_expert completion
# Monitoring activities run concurrently with main restoration and chem_expert, no strict order

root = StrictPartialOrder(nodes=[main_restoration, Documentation, Photo_Record, Condition_Monitor, chem_expert, final_phase])

# Add edges:
# main_restoration --> final_phase
root.order.add_edge(main_restoration, final_phase)

# chem_expert --> final_phase
root.order.add_edge(chem_expert, final_phase)