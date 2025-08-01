# Generated from: 011f8b89-babc-48e1-9fda-ae156710e002.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farming facility focused on sustainable food production within a limited city space. It includes site analysis, modular system design, environmental control calibration, nutrient cycling optimization, crop selection based on microclimate data, integration of IoT sensors for real-time monitoring, automation of irrigation and lighting, pest bio-control implementation, data-driven yield forecasting, staff training on hydroponic techniques, community engagement for local sourcing, regulatory compliance checks, energy consumption auditing, waste recycling protocols, and continuous process improvement through AI analytics to maximize output and minimize environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
labels = [
    'Site Survey', 'System Design', 'Env Control', 'Nutrient Mix', 'Crop Select',
    'Sensor Setup', 'Irrigation Auto', 'Lighting Adjust', 'Pest Control',
    'Yield Forecast', 'Staff Training', 'Community Meet', 'Compliance Check',
    'Energy Audit', 'Waste Recycle', 'Process Review'
]
transitions = {label: Transition(label=label) for label in labels}

# Define a silent transition for looping
skip = SilentTransition()

# Define a loop for continuous process review/improvement
proc_review = transitions['Process Review']
loop = OperatorPOWL(operator=Operator.LOOP, children=[proc_review, skip])

# Build the partial order: all activities except 'Process Review' in sequence, ending in the loop
sequence = [
    'Site Survey', 'System Design', 'Env Control', 'Nutrient Mix', 'Crop Select',
    'Sensor Setup', 'Irrigation Auto', 'Lighting Adjust', 'Pest Control',
    'Yield Forecast', 'Staff Training', 'Community Meet', 'Compliance Check',
    'Energy Audit', 'Waste Recycle'
]

# Root POWL model
root = StrictPartialOrder(nodes=[transitions[l] for l in sequence] + [loop])

# Add edges to enforce the sequence
for a, b in zip(sequence, sequence[1:]):
    root.order.add_edge(transitions[a], transitions[b])

# Connect the last activity to the loop of process review
root.order.add_edge(transitions['Waste Recycle'], loop)