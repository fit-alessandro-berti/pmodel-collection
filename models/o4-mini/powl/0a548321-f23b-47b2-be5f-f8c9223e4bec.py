# Generated from: 0a548321-f23b-47b2-be5f-f8c9223e4bec.json
# Description: This process involves the intricate steps required to restore historical artifacts within a museum setting. It begins with artifact assessment, followed by environmental analysis to determine optimal conservation conditions. The process includes cleaning with specialized tools, material stabilization, and structural repairs under controlled settings. Documentation and photographic records are maintained throughout to ensure traceability. Expert consultations help in selecting appropriate restoration chemicals. After restoration, artifacts undergo final quality checks and are prepared for display or storage, ensuring preservation while maintaining historical integrity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
artifact_assess   = Transition(label='Artifact Assess')
env_analysis     = Transition(label='Env Analysis')
expert_consult   = Transition(label='Expert Consult')
chemical_select  = Transition(label='Chemical Select')
clean_tools      = Transition(label='Clean Tools')
material_test    = Transition(label='Material Test')
stabilize_form   = Transition(label='Stabilize Form')
structural_repair= Transition(label='Structural Repair')
documentation    = Transition(label='Documentation')
photo_record     = Transition(label='Photo Record')
condition_monitor= Transition(label='Condition Monitor')
final_inspect    = Transition(label='Final Inspect')
report_archive   = Transition(label='Report Archive')
display_prep     = Transition(label='Display Prep')
storage_setup    = Transition(label='Storage Setup')

# XOR choice between displaying or storing after inspection
xor_disp_store = OperatorPOWL(
    operator=Operator.XOR,
    children=[display_prep, storage_setup]
)

# Build the partial‐order root
root = StrictPartialOrder(nodes=[
    artifact_assess,
    env_analysis,
    expert_consult,
    chemical_select,
    clean_tools,
    material_test,
    stabilize_form,
    structural_repair,
    documentation,
    photo_record,
    condition_monitor,
    final_inspect,
    xor_disp_store,
    report_archive
])

# Define the control‐flow dependencies
o = root.order
o.add_edge(artifact_assess,   env_analysis)
o.add_edge(env_analysis,      expert_consult)
o.add_edge(expert_consult,    chemical_select)
o.add_edge(chemical_select,   clean_tools)
o.add_edge(clean_tools,       material_test)
o.add_edge(material_test,     stabilize_form)
o.add_edge(stabilize_form,    structural_repair)
o.add_edge(structural_repair, final_inspect)
o.add_edge(final_inspect,     xor_disp_store)
o.add_edge(xor_disp_store,    report_archive)

# Documentation, photo and condition monitoring run concurrently from the start
# and all must finish before archiving the report
o.add_edge(artifact_assess,   documentation)
o.add_edge(artifact_assess,   photo_record)
o.add_edge(artifact_assess,   condition_monitor)
o.add_edge(documentation,     report_archive)
o.add_edge(photo_record,      report_archive)
o.add_edge(condition_monitor, report_archive)