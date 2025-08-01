# Generated from: 418fd8c0-d56e-4260-9475-14aeab6beb62.json
# Description: This process involves the intricate coordination and implementation of a dynamic art installation that reacts to environmental stimuli and audience interaction. It begins with concept validation and sensor calibration, progresses through modular component assembly and real-time data integration, and concludes with adaptive lighting and sound synchronization. The process requires multidisciplinary collaboration between artists, engineers, and software developers to ensure seamless interactivity and immersive experience. Continuous monitoring and iterative adjustments are essential to maintain responsiveness and artistic intent throughout exhibit duration.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Concept_Validate = Transition(label='Concept Validate')
Sensor_Calibrate = Transition(label='Sensor Calibrate')
Module_Assemble = Transition(label='Module Assemble')
Data_Integrate = Transition(label='Data Integrate')
Signal_Test = Transition(label='Signal Test')
Power_Configure = Transition(label='Power Configure')
Network_Setup = Transition(label='Network Setup')
Software_Deploy = Transition(label='Software Deploy')
Interaction_Map = Transition(label='Interaction Map')
Lighting_Sync = Transition(label='Lighting Sync')
Sound_Adjust = Transition(label='Sound Adjust')
Feedback_Collect = Transition(label='Feedback Collect')
System_Monitor = Transition(label='System Monitor')
Performance_Tune = Transition(label='Performance Tune')
Visitor_Track = Transition(label='Visitor Track')
Content_Update = Transition(label='Content Update')
Safety_Check = Transition(label='Safety Check')

# Initial sequential phase: Concept Validate --> Sensor Calibrate
initial_phase = StrictPartialOrder(nodes=[Concept_Validate, Sensor_Calibrate])
initial_phase.order.add_edge(Concept_Validate, Sensor_Calibrate)

# Assembly phase: Module Assemble --> Data Integrate --> Signal Test
assembly_phase = StrictPartialOrder(
    nodes=[Module_Assemble, Data_Integrate, Signal_Test]
)
assembly_phase.order.add_edge(Module_Assemble, Data_Integrate)
assembly_phase.order.add_edge(Data_Integrate, Signal_Test)

# Configuration phase parallel branches:
#  - Power Configure --> Network Setup
config_power_net = StrictPartialOrder(
    nodes=[Power_Configure, Network_Setup]
)
config_power_net.order.add_edge(Power_Configure, Network_Setup)

#  - Software Deploy
config_software = StrictPartialOrder(
    nodes=[Software_Deploy]
)

# Combine configuration branches as partial order (concurrent)
configuration_phase = StrictPartialOrder(
    nodes=[config_power_net, config_software]
)

# Link assembly phase to configuration_phase partial order (parallel)
assembly_to_config = StrictPartialOrder(
    nodes=[assembly_phase, configuration_phase]
)
# assembly_phase and configuration_phase run concurrently after assembly ends
# But configuration starts only after assembly, so assembly_phase --> configuration_phase
assembly_to_config.order.add_edge(assembly_phase, configuration_phase)

# Interaction phase partial order:
# Interaction Map --> (Lighting Sync || Sound Adjust)
interaction_phase = StrictPartialOrder(
    nodes=[Interaction_Map, Lighting_Sync, Sound_Adjust]
)
interaction_phase.order.add_edge(Interaction_Map, Lighting_Sync)
interaction_phase.order.add_edge(Interaction_Map, Sound_Adjust)
# Lighting Sync and Sound Adjust concurrent, no edges between

# Feedback and monitoring loop:
# Loop body: Feedback Collect
# Loop condition/continuation: System Monitor --> Performance Tune --> Visitor Track
feedback_loop_body = Feedback_Collect
feedback_loop_continue = StrictPartialOrder(
    nodes=[System_Monitor, Performance_Tune, Visitor_Track]
)
feedback_loop_continue.order.add_edge(System_Monitor, Performance_Tune)
feedback_loop_continue.order.add_edge(Performance_Tune, Visitor_Track)

feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_loop_body, feedback_loop_continue])

# Content update and safety check after feedback loop ends
post_feedback_phase = StrictPartialOrder(
    nodes=[Content_Update, Safety_Check]
)
# Safety Check depends on Content Update
post_feedback_phase.order.add_edge(Content_Update, Safety_Check)

# Construct full process partial order, combining phases in partial order, respecting flow:
# initial_phase --> assembly_phase --> configuration_phase --> interaction_phase --> feedback_loop --> post_feedback_phase

# We'll create a top-level partial order with all main phases as nodes:
root = StrictPartialOrder(
    nodes=[initial_phase,
           assembly_phase,
           configuration_phase,
           interaction_phase,
           feedback_loop,
           post_feedback_phase]
)

root.order.add_edge(initial_phase, assembly_phase)
root.order.add_edge(assembly_phase, configuration_phase)
root.order.add_edge(configuration_phase, interaction_phase)
root.order.add_edge(interaction_phase, feedback_loop)
root.order.add_edge(feedback_loop, post_feedback_phase)