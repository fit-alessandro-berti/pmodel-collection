# Generated from: 15511caa-8f5b-4475-904d-5a4c16b1c703.json
# Description: This process involves orchestrating a product launch that integrates multisensory marketing techniques to engage customers on visual, auditory, olfactory, and tactile levels. The process begins with conceptualizing sensory themes, proceeds through iterative prototype testing with focus groups using VR and AR environments, and coordinates with supply chain teams to source unique materials for packaging that enhance touch and smell. Marketing campaigns are synchronized across digital, physical, and experiential channels, incorporating soundscapes and scent diffusers in retail locations. Post-launch, customer feedback is gathered via biometric sensors and sentiment analysis to refine future launches. This atypical approach ensures a deeply immersive brand experience, differentiating the product in competitive markets by leveraging sensory psychology and advanced technology integration.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Theme_Concept = Transition(label='Theme Concept')
Prototype_VR = Transition(label='Prototype VR')
Focus_Testing = Transition(label='Focus Testing')
Material_Sourcing = Transition(label='Material Sourcing')
Packaging_Design = Transition(label='Packaging Design')
Scent_Development = Transition(label='Scent Development')
Sound_Creation = Transition(label='Sound Creation')
Campaign_Sync = Transition(label='Campaign Sync')
Retail_Setup = Transition(label='Retail Setup')
Sensor_Install = Transition(label='Sensor Install')
Launch_Event = Transition(label='Launch Event')
Data_Capture = Transition(label='Data Capture')
Sentiment_Scan = Transition(label='Sentiment Scan')
Feedback_Review = Transition(label='Feedback Review')
Refinement_Plan = Transition(label='Refinement Plan')

# Loop for iterative prototype testing: Prototype VR -> Focus Testing -> (exit or repeat)
iterative_testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[Prototype_VR, Focus_Testing])

# Package sourcing and design including material and sensory development in partial order (concurrent where possible)
# Material Sourcing -> Packaging Design
# Packaging Design > (Scent Development and Sound Creation) concurrent
material_packaging_PO = StrictPartialOrder(nodes=[Material_Sourcing, Packaging_Design, Scent_Development, Sound_Creation])
material_packaging_PO.order.add_edge(Material_Sourcing, Packaging_Design)
material_packaging_PO.order.add_edge(Packaging_Design, Scent_Development)
material_packaging_PO.order.add_edge(Packaging_Design, Sound_Creation)

# Marketing campaigns synchronization and retail setup concurrent (Scent Development and Sound Creation ->
# Campaign Sync and Retail Setup)
marketing_PO = StrictPartialOrder(nodes=[material_packaging_PO, Campaign_Sync, Retail_Setup])
# The marketing_PO includes the nested material_packaging_PO as a node
marketing_PO.order.add_edge(material_packaging_PO, Campaign_Sync)
marketing_PO.order.add_edge(material_packaging_PO, Retail_Setup)

# Sensor installation before launch event
prelaunch_PO = StrictPartialOrder(nodes=[Sensor_Install, Launch_Event])
prelaunch_PO.order.add_edge(Sensor_Install, Launch_Event)

# Post-launch feedback gathering sequence
feedback_PO = StrictPartialOrder(nodes=[Data_Capture, Sentiment_Scan, Feedback_Review, Refinement_Plan])
feedback_PO.order.add_edge(Data_Capture, Sentiment_Scan)
feedback_PO.order.add_edge(Sentiment_Scan, Feedback_Review)
feedback_PO.order.add_edge(Feedback_Review, Refinement_Plan)

# Assemble main flow:
# Theme Concept -> iterative_testing_loop -> marketing_PO -> prelaunch_PO -> feedback_PO
root = StrictPartialOrder(
    nodes=[Theme_Concept, iterative_testing_loop, marketing_PO, prelaunch_PO, feedback_PO]
)
root.order.add_edge(Theme_Concept, iterative_testing_loop)
root.order.add_edge(iterative_testing_loop, marketing_PO)
root.order.add_edge(marketing_PO, prelaunch_PO)
root.order.add_edge(prelaunch_PO, feedback_PO)