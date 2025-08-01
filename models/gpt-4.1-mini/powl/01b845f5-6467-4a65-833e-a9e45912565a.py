# Generated from: 01b845f5-6467-4a65-833e-a9e45912565a.json
# Description: This process involves the bespoke design and manufacturing of high-frequency antennas tailored for specialized aerospace and defense applications. It starts with client requirement analysis, followed by electromagnetic simulation and material selection. The process continues with precision machining, micro-assembly, and multi-layer coating to optimize signal integrity and durability. Quality assurance is performed through advanced spectral testing and environmental stress screening. Final packaging includes custom shielding and documentation before dispatch to ensure performance under extreme conditions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Requirement_Analysis = Transition(label='Requirement Analysis')
Signal_Modeling = Transition(label='Signal Modeling')
Material_Selection = Transition(label='Material Selection')
Pattern_Etching = Transition(label='Pattern Etching')
Substrate_Cutting = Transition(label='Substrate Cutting')
Layer_Lamination = Transition(label='Layer Lamination')
Micro_Assembly = Transition(label='Micro Assembly')
Coating_Application = Transition(label='Coating Application')
Spectral_Testing = Transition(label='Spectral Testing')
Stress_Screening = Transition(label='Stress Screening')
Thermal_Cycling = Transition(label='Thermal Cycling')
Shielding_Setup = Transition(label='Shielding Setup')
Documentation = Transition(label='Documentation')
Final_Inspection = Transition(label='Final Inspection')
Custom_Packaging = Transition(label='Custom Packaging')

# Model the manufacturing sequence as partial orders to reflect concurrency and sequence

# Requirement Analysis --> Signal Modeling and Material Selection in parallel (no order between these two)
first_phase = StrictPartialOrder(nodes=[Requirement_Analysis, Signal_Modeling, Material_Selection])
first_phase.order.add_edge(Requirement_Analysis, Signal_Modeling)
first_phase.order.add_edge(Requirement_Analysis, Material_Selection)

# Pattern Etching, Substrate Cutting and Layer Lamination are sequential steps after Material Selection and Signal Modeling,
# assuming Signal Modeling and Material Selection must both complete before patterning starts.
patterning_phase = StrictPartialOrder(
    nodes=[Signal_Modeling, Material_Selection, Pattern_Etching, Substrate_Cutting, Layer_Lamination]
)
# Both Signal Modeling and Material Selection precede Pattern Etching
patterning_phase.order.add_edge(Signal_Modeling, Pattern_Etching)
patterning_phase.order.add_edge(Material_Selection, Pattern_Etching)
# Then Pattern Etching -> Substrate Cutting -> Layer Lamination sequentially
patterning_phase.order.add_edge(Pattern_Etching, Substrate_Cutting)
patterning_phase.order.add_edge(Substrate_Cutting, Layer_Lamination)

# Micro Assembly and Coating Application happen after Layer Lamination, possibly concurrent
micro_coating_phase = StrictPartialOrder(
    nodes=[Layer_Lamination, Micro_Assembly, Coating_Application]
)
micro_coating_phase.order.add_edge(Layer_Lamination, Micro_Assembly)
micro_coating_phase.order.add_edge(Layer_Lamination, Coating_Application)

# Quality Assurance: Spectral Testing, Stress Screening, Thermal Cycling are QA tests performed in parallel after Micro Assembly and Coating 
qa_phase = StrictPartialOrder(
    nodes=[Micro_Assembly, Coating_Application, Spectral_Testing, Stress_Screening, Thermal_Cycling]
)
qa_phase.order.add_edge(Micro_Assembly, Spectral_Testing)
qa_phase.order.add_edge(Micro_Assembly, Stress_Screening)
qa_phase.order.add_edge(Micro_Assembly, Thermal_Cycling)
qa_phase.order.add_edge(Coating_Application, Spectral_Testing)
qa_phase.order.add_edge(Coating_Application, Stress_Screening)
qa_phase.order.add_edge(Coating_Application, Thermal_Cycling)

# Final Packaging: Shielding Setup and Documentation happen in parallel before Final Inspection and Custom Packaging
packaging_phase = StrictPartialOrder(
    nodes=[Spectral_Testing, Stress_Screening, Thermal_Cycling, Shielding_Setup, Documentation, Final_Inspection, Custom_Packaging]
)
# All QA tests precede Shielding Setup and Documentation
for test in [Spectral_Testing, Stress_Screening, Thermal_Cycling]:
    packaging_phase.order.add_edge(test, Shielding_Setup)
    packaging_phase.order.add_edge(test, Documentation)
# Shielding Setup and Documentation precede Final Inspection, which precedes Custom Packaging
packaging_phase.order.add_edge(Shielding_Setup, Final_Inspection)
packaging_phase.order.add_edge(Documentation, Final_Inspection)
packaging_phase.order.add_edge(Final_Inspection, Custom_Packaging)

# Combine all phases into one partial order,
# connecting first_phase --> patterning_phase --> micro_coating_phase --> qa_phase --> packaging_phase
root = StrictPartialOrder(
    nodes=[
        Requirement_Analysis,
        Signal_Modeling,
        Material_Selection,
        Pattern_Etching,
        Substrate_Cutting,
        Layer_Lamination,
        Micro_Assembly,
        Coating_Application,
        Spectral_Testing,
        Stress_Screening,
        Thermal_Cycling,
        Shielding_Setup,
        Documentation,
        Final_Inspection,
        Custom_Packaging
    ]
)

# Add edges from first_phase
root.order.add_edge(Requirement_Analysis, Signal_Modeling)
root.order.add_edge(Requirement_Analysis, Material_Selection)

# Add edges from patterning_phase
root.order.add_edge(Signal_Modeling, Pattern_Etching)
root.order.add_edge(Material_Selection, Pattern_Etching)
root.order.add_edge(Pattern_Etching, Substrate_Cutting)
root.order.add_edge(Substrate_Cutting, Layer_Lamination)

# Add edges from micro_coating_phase
root.order.add_edge(Layer_Lamination, Micro_Assembly)
root.order.add_edge(Layer_Lamination, Coating_Application)

# Add edges from qa_phase
root.order.add_edge(Micro_Assembly, Spectral_Testing)
root.order.add_edge(Micro_Assembly, Stress_Screening)
root.order.add_edge(Micro_Assembly, Thermal_Cycling)
root.order.add_edge(Coating_Application, Spectral_Testing)
root.order.add_edge(Coating_Application, Stress_Screening)
root.order.add_edge(Coating_Application, Thermal_Cycling)

# Add edges from packaging_phase
for test in [Spectral_Testing, Stress_Screening, Thermal_Cycling]:
    root.order.add_edge(test, Shielding_Setup)
    root.order.add_edge(test, Documentation)

root.order.add_edge(Shielding_Setup, Final_Inspection)
root.order.add_edge(Documentation, Final_Inspection)
root.order.add_edge(Final_Inspection, Custom_Packaging)