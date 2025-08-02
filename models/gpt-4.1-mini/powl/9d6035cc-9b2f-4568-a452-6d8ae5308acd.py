# Generated from: 9d6035cc-9b2f-4568-a452-6d8ae5308acd.json
# Description: This process involves leveraging a diverse, global community to generate, refine, and validate innovative product ideas. It starts with idea solicitation from contributors, followed by collaborative filtering, prototyping, and iterative feedback loops. The process integrates automated sentiment analysis and expert reviews to prioritize concepts. Selected ideas undergo rapid development cycles with continuous input from the crowd, culminating in pilot launches and scalability assessments. The approach balances creative freedom with structured evaluation to minimize risks and maximize market fit, creating a dynamic innovation pipeline fueled by collective intelligence.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Idea_Collection = Transition(label='Idea Collection')
Community_Voting = Transition(label='Community Voting')
Sentiment_Scan = Transition(label='Sentiment Scan')
Expert_Review = Transition(label='Expert Review')
Concept_Filtering = Transition(label='Concept Filtering')
Prototype_Build = Transition(label='Prototype Build')
Feedback_Loop = Transition(label='Feedback Loop')
Iterative_Design = Transition(label='Iterative Design')
Pilot_Launch = Transition(label='Pilot Launch')
Data_Analysis = Transition(label='Data Analysis')
Scalability_Test = Transition(label='Scalability Test')
Market_Survey = Transition(label='Market Survey')
Crowd_Incentives = Transition(label='Crowd Incentives')
Risk_Assessment = Transition(label='Risk Assessment')
Final_Selection = Transition(label='Final Selection')
Knowledge_Archive = Transition(label='Knowledge Archive')

# Loop for iterative feedback/design cycles: execute Feedback Loop, then choose to exit or repeat Iterative Design then Feedback Loop
feedback_loop_cycle = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Loop, Iterative_Design])

# Concept evaluation: Sentiment Scan XOR Expert Review (parallel filtering with choice)
concept_filtering_choice = OperatorPOWL(operator=Operator.XOR, children=[Sentiment_Scan, Expert_Review])

# Prioritization stage: Concept Filtering after voting and filtering
prioritization_po = StrictPartialOrder(
    nodes=[Community_Voting, concept_filtering_choice, Concept_Filtering]
)
prioritization_po.order.add_edge(Community_Voting, concept_filtering_choice)
prioritization_po.order.add_edge(concept_filtering_choice, Concept_Filtering)

# Development cycles after concept filtering: Prototype Build then the feedback loop cycle
development_po = StrictPartialOrder(
    nodes=[Prototype_Build, feedback_loop_cycle]
)
development_po.order.add_edge(Prototype_Build, feedback_loop_cycle)

# Pilot phase with pilot launch, market survey, data analysis, scalability test (some concurrency allowed)
pilot_phase_po = StrictPartialOrder(
    nodes=[Pilot_Launch, Market_Survey, Data_Analysis, Scalability_Test]
)
pilot_phase_po.order.add_edge(Pilot_Launch, Market_Survey)  # Market Survey after Pilot Launch
pilot_phase_po.order.add_edge(Pilot_Launch, Data_Analysis)  # Data Analysis after Pilot Launch
pilot_phase_po.order.add_edge(Market_Survey, Scalability_Test)  # Scalability Test after Market Survey
pilot_phase_po.order.add_edge(Data_Analysis, Scalability_Test)  # Scalability Test after Data Analysis

# Early stages: Idea Collection then Community Voting
early_stage_po = StrictPartialOrder(
    nodes=[Idea_Collection, Community_Voting]
)
early_stage_po.order.add_edge(Idea_Collection, Community_Voting)

# Risk and incentives assessment after pilot and scalability test
risk_and_incentives_po = StrictPartialOrder(
    nodes=[Crowd_Incentives, Risk_Assessment]
)

# Risk assessment must happen after Scalability_Test
risk_and_incentives_po.order.add_edge(Crowd_Incentives, Risk_Assessment)

# Final selection after risk assessment and concept filtering (both must be done)
final_selection_po = StrictPartialOrder(
    nodes=[Risk_Assessment, Concept_Filtering, Final_Selection]
)
final_selection_po.order.add_edge(Risk_Assessment, Final_Selection)
final_selection_po.order.add_edge(Concept_Filtering, Final_Selection)

# The full flow partial order combining all major stages using partial order (nodes are all submodels)
root = StrictPartialOrder(
    nodes=[
        early_stage_po,
        prioritization_po,
        development_po,
        pilot_phase_po,
        risk_and_incentives_po,
        final_selection_po,
        Knowledge_Archive
    ]
)

# Define partial order edges among these main phases/submodels

# Early -> Prioritization
root.order.add_edge(early_stage_po, prioritization_po)

# Prioritization -> Development
root.order.add_edge(prioritization_po, development_po)

# Development -> Pilot
root.order.add_edge(development_po, pilot_phase_po)

# Pilot -> Risk and Incentives (Crowd Incentives before Risk Assessment assumed internal)
root.order.add_edge(pilot_phase_po, risk_and_incentives_po)

# Risk and Incentives -> Final Selection
root.order.add_edge(risk_and_incentives_po, final_selection_po)

# Final Selection -> Knowledge Archive
root.order.add_edge(final_selection_po, Knowledge_Archive)