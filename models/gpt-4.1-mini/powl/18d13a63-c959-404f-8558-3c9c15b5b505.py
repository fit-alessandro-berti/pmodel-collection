# Generated from: 18d13a63-c959-404f-8558-3c9c15b5b505.json
# Description: This process involves the intricate creation of bespoke artisanal perfumes combining traditional craftsmanship with modern sensory analysis. Starting with raw material sourcing, the process includes botanical extraction, scent profiling, and iterative blending cycles guided by expert perfumers. Each batch undergoes stability testing and sensory panel reviews before final bottling and packaging. The process also integrates sustainable practices by recycling waste and optimizing ingredient usage, ensuring both quality and environmental responsibility throughout the development stages. Customer feedback loops further refine future formulations, making it a continuous innovation cycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Material_Sourcing = Transition(label='Material Sourcing')
Botanical_Extraction = Transition(label='Botanical Extraction')
Scent_Profiling = Transition(label='Scent Profiling')
Initial_Blending = Transition(label='Initial Blending')
Sensory_Analysis = Transition(label='Sensory Analysis')
Stability_Testing = Transition(label='Stability Testing')
Batch_Refinement = Transition(label='Batch Refinement')
Panel_Review = Transition(label='Panel Review')
Waste_Recycling = Transition(label='Waste Recycling')
Sustainability_Audit = Transition(label='Sustainability Audit')
Packaging_Design = Transition(label='Packaging Design')
Quality_Control = Transition(label='Quality Control')
Customer_Feedback = Transition(label='Customer Feedback')
Formula_Update = Transition(label='Formula Update')
Final_Bottling = Transition(label='Final Bottling')

# Define the iterative blending cycle loop: execute Initial_Blending then
# choose to exit or do (Batch_Refinement then the loop again)
blending_loop = OperatorPOWL(operator=Operator.LOOP, children=[Initial_Blending, Batch_Refinement])

# Customer feedback loop: execute Customer_Feedback then Formula_Update then loop
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Customer_Feedback, Formula_Update])

# Partial order for main core process flow before packaging
core_process = StrictPartialOrder(
    nodes=[
        Material_Sourcing,
        Botanical_Extraction,
        Scent_Profiling,
        blending_loop,
        Sensory_Analysis,
        Stability_Testing,
        Panel_Review,
        Waste_Recycling,
        Sustainability_Audit,
        Packaging_Design,
        Quality_Control,
        feedback_loop,
        Final_Bottling
    ]
)

# Add dependencies representing control flow
core_process.order.add_edge(Material_Sourcing, Botanical_Extraction)
core_process.order.add_edge(Botanical_Extraction, Scent_Profiling)
core_process.order.add_edge(Scent_Profiling, blending_loop)

blending_loop_idx = blending_loop
core_process.order.add_edge(blending_loop, Sensory_Analysis)
core_process.order.add_edge(Sensory_Analysis, Stability_Testing)
core_process.order.add_edge(Stability_Testing, Panel_Review)

# Waste Recycling and Sustainability Audit are sustainability practices integrated concurrently after Sensory Analysis
core_process.order.add_edge(Sensory_Analysis, Waste_Recycling)
core_process.order.add_edge(Sensory_Analysis, Sustainability_Audit)

# PackagingDesign and QualityControl follow PanelReview and sustainability practices
core_process.order.add_edge(Panel_Review, Packaging_Design)
core_process.order.add_edge(Waste_Recycling, Packaging_Design)
core_process.order.add_edge(Sustainability_Audit, Packaging_Design)

core_process.order.add_edge(Packaging_Design, Quality_Control)

# Customer feedback loop after Quality Control, then Final Bottling
core_process.order.add_edge(Quality_Control, feedback_loop)
core_process.order.add_edge(feedback_loop, Final_Bottling)

root = core_process