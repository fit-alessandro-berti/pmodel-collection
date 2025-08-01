# Generated from: 6d291212-6c4d-4a5a-ac78-b56d3538f529.json
# Description: This process details the intricate creation of artisanal perfumes, combining rare botanical extractions with traditional blending techniques. It begins with sourcing exotic raw materials from multiple continents, followed by delicate extraction methods like enfleurage and steam distillation. Next, master perfumers experiment with scent profiles in controlled environments, adjusting ratios to achieve a harmonious fragrance. Quality control includes olfactory testing and chemical analysis to ensure consistency and safety. The final phase involves aging the perfume in specialized containers, bottling, and bespoke packaging, while maintaining traceability and sustainability throughout the workflow.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Raw_Sourcing = Transition(label='Raw Sourcing')
Botanical_Sorting = Transition(label='Botanical Sorting')
Extraction_Prep = Transition(label='Extraction Prep')
Enfleurage_Process = Transition(label='Enfleurage Process')
Steam_Distill = Transition(label='Steam Distill')
Scent_Blending = Transition(label='Scent Blending')
Profile_Testing = Transition(label='Profile Testing')
Ratio_Adjust = Transition(label='Ratio Adjust')
Olfactory_Check = Transition(label='Olfactory Check')
Chemical_Scan = Transition(label='Chemical Scan')
Quality_Approval = Transition(label='Quality Approval')
Aging_Storage = Transition(label='Aging Storage')
Bottle_Filling = Transition(label='Bottle Filling')
Label_Printing = Transition(label='Label Printing')
Custom_Packaging = Transition(label='Custom Packaging')
Sustainability_Audit = Transition(label='Sustainability Audit')
Traceability_Log = Transition(label='Traceability Log')

# Extraction phase: Extraction Prep followed by choice between Enfleurage Process or Steam Distill
Extraction_Methods = OperatorPOWL(operator=Operator.XOR, children=[Enfleurage_Process, Steam_Distill])
Extraction_Phase = StrictPartialOrder(nodes=[Extraction_Prep, Extraction_Methods])
Extraction_Phase.order.add_edge(Extraction_Prep, Extraction_Methods)

# Scent blending phase: Scent Blending followed by Profile Testing then Ratio Adjust
Scent_Blending_Phase = StrictPartialOrder(nodes=[Scent_Blending, Profile_Testing, Ratio_Adjust])
Scent_Blending_Phase.order.add_edge(Scent_Blending, Profile_Testing)
Scent_Blending_Phase.order.add_edge(Profile_Testing, Ratio_Adjust)

# Quality control phase: Olfactory Check and Chemical Scan in parallel, both before Quality Approval
Quality_Checks = StrictPartialOrder(nodes=[Olfactory_Check, Chemical_Scan, Quality_Approval])
Quality_Checks.order.add_edge(Olfactory_Check, Quality_Approval)
Quality_Checks.order.add_edge(Chemical_Scan, Quality_Approval)

# Final phase: Aging Storage then Bottle Filling then Label Printing then Custom Packaging
Final_Phase = StrictPartialOrder(nodes=[Aging_Storage, Bottle_Filling, Label_Printing, Custom_Packaging])
Final_Phase.order.add_edge(Aging_Storage, Bottle_Filling)
Final_Phase.order.add_edge(Bottle_Filling, Label_Printing)
Final_Phase.order.add_edge(Label_Printing, Custom_Packaging)

# Sustainability and Traceability run concurrently with final phase and quality checks
# They have no ordering edges connected to Quality_Checks or Final_Phase => concurrent with them

# Compose the overall process partial order
root = StrictPartialOrder(
    nodes=[
        Raw_Sourcing, 
        Botanical_Sorting, 
        Extraction_Phase, 
        Scent_Blending_Phase, 
        Quality_Checks, 
        Final_Phase, 
        Sustainability_Audit, 
        Traceability_Log
    ]
)

# Set ordering edges to represent described flow
root.order.add_edge(Raw_Sourcing, Botanical_Sorting)
root.order.add_edge(Botanical_Sorting, Extraction_Phase)
root.order.add_edge(Extraction_Phase, Scent_Blending_Phase)
root.order.add_edge(Scent_Blending_Phase, Quality_Checks)
root.order.add_edge(Quality_Checks, Final_Phase)
# Sustainability Audit and Traceability Log run concurrently with Quality checks and final phase
# No edges needed for concurrency
