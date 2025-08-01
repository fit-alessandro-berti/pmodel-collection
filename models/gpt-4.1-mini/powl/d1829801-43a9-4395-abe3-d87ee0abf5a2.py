# Generated from: d1829801-43a9-4395-abe3-d87ee0abf5a2.json
# Description: This process involves the detailed authentication of antique artifacts using a blend of scientific analysis, historical research, and expert validation. The process begins with initial artifact intake and visual inspection, followed by advanced material composition testing and radiocarbon dating. Parallelly, provenance research is conducted by examining archival records and previous ownership histories. Next, specialized experts assess stylistic and craftsmanship elements before the artifact undergoes condition assessment and restoration feasibility analysis. The process includes risk evaluation for potential forgery and legal compliance checks. Finally, findings are compiled into a comprehensive authentication report, and the artifact is cataloged into a secure database for future reference and insurance purposes.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Artifact_Intake = Transition(label='Artifact Intake')
Visual_Inspection = Transition(label='Visual Inspection')
Material_Testing = Transition(label='Material Testing')
Radiocarbon_Dating = Transition(label='Radiocarbon Dating')
Provenance_Check = Transition(label='Provenance Check')
Archive_Research = Transition(label='Archive Research')
Expert_Review = Transition(label='Expert Review')
Style_Analysis = Transition(label='Style Analysis')
Craftsmanship_Eval = Transition(label='Craftsmanship Eval')
Condition_Check = Transition(label='Condition Check')
Restoration_Plan = Transition(label='Restoration Plan')
Forgery_Risk = Transition(label='Forgery Risk')
Legal_Review = Transition(label='Legal Review')
Report_Drafting = Transition(label='Report Drafting')
Catalog_Entry = Transition(label='Catalog Entry')

# Step 1: Initial artifact intake and visual inspection in sequence
step1 = StrictPartialOrder(nodes=[Artifact_Intake, Visual_Inspection])
step1.order.add_edge(Artifact_Intake, Visual_Inspection)

# Step 2: Advanced material testing and radiocarbon dating in sequence
step2 = StrictPartialOrder(nodes=[Material_Testing, Radiocarbon_Dating])
step2.order.add_edge(Material_Testing, Radiocarbon_Dating)

# Step 3: Provenance research with archival records and ownership histories in parallel
step3 = StrictPartialOrder(nodes=[Provenance_Check, Archive_Research])

# Step 4: Experts assess stylistic and craftsmanship elements in parallel
step4 = StrictPartialOrder(nodes=[Expert_Review, Style_Analysis, Craftsmanship_Eval])

# Step 5: Condition assessment and restoration feasibility in sequence
step5 = StrictPartialOrder(nodes=[Condition_Check, Restoration_Plan])
step5.order.add_edge(Condition_Check, Restoration_Plan)

# Step 6: Risk evaluation and legal review in sequence
step6 = StrictPartialOrder(nodes=[Forgery_Risk, Legal_Review])
step6.order.add_edge(Forgery_Risk, Legal_Review)

# Step 7: Final report drafting and catalog entry in sequence
step7 = StrictPartialOrder(nodes=[Report_Drafting, Catalog_Entry])
step7.order.add_edge(Report_Drafting, Catalog_Entry)

# Combine step 2 and step 3 in parallel (material testing + radiocarbon dating) AND (provenance check + archive research)
step23 = StrictPartialOrder(nodes=[step2, step3])

# Combine step 4 and step 5 in sequence: first expert/style/craft, then condition/restoration
step45 = StrictPartialOrder(nodes=[step4, step5])
step45.order.add_edge(step4, step5)

# Combine all steps in the correct global order:
# step1 -> step23 (both step2 and step3 in parallel) -> step45 -> step6 -> step7

root = StrictPartialOrder(nodes=[step1, step23, step45, step6, step7])
root.order.add_edge(step1, step23)
root.order.add_edge(step23, step45)
root.order.add_edge(step45, step6)
root.order.add_edge(step6, step7)