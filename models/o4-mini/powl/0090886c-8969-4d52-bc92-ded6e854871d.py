# Generated from: 0090886c-8969-4d52-bc92-ded6e854871d.json
# Description: This process involves establishing a vertical farming system within an urban environment, integrating advanced hydroponic and aeroponic technologies. It begins with site assessment and structural retrofitting, followed by environmental control installation, nutrient cycling design, and seed selection tailored to urban microclimates. The process includes IoT sensor deployment for real-time monitoring, automated irrigation calibration, pest management via integrated biological controls, and workforce training for operational maintenance. Finally, it covers yield forecasting using AI analytics and establishing supply chain logistics focused on rapid distribution to local markets, ensuring sustainability and minimal carbon footprint throughout the lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities
labels = [
    'Site Assessment', 'Structure Retrofit', 'Env Control', 'Nutrient Design',
    'Seed Selection', 'Sensor Deploy', 'Irrigation Setup', 'Pest Control',
    'Workforce Train', 'System Calibration', 'Growth Monitoring',
    'Data Analytics', 'Yield Forecast', 'Logistics Plan', 'Market Launch'
]
transitions = [Transition(label=l) for l in labels]

# Build a strictly sequential partial‐order workflow
root = StrictPartialOrder(nodes=transitions)
for prev, nxt in zip(transitions, transitions[1:]):
    root.order.add_edge(prev, nxt)