# Generated from: 56dd91c5-4fc5-4ec6-9a17-c9320950147a.json
# Description: This process encompasses the complex steps required to establish an urban vertical farm within a repurposed industrial building. It involves site analysis, environmental impact assessment, modular system design, customized nutrient solution formulation, automated climate control integration, and multi-tier crop scheduling. The process also includes community engagement for local sourcing, advanced pest control strategies without pesticides, renewable energy system installation, IoT sensor calibration, workforce training on agri-tech tools, and continuous yield optimization through data analytics. Each activity is critical to ensuring a sustainable, high-efficiency farm that maximizes urban space while minimizing environmental footprint, enabling year-round crop production in dense metropolitan areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
site          = Transition(label='Site Survey')
impact        = Transition(label='Impact Study')
design        = Transition(label='System Design')
nutrient      = Transition(label='Nutrient Mix')
climate       = Transition(label='Climate Setup')
schedule      = Transition(label='Crop Schedule')
community     = Transition(label='Community Meet')
pest          = Transition(label='Pest Control')
energy        = Transition(label='Energy Install')
sensor        = Transition(label='Sensor Setup')
training      = Transition(label='Tech Training')
monitor       = Transition(label='Data Monitor')
adjust        = Transition(label='Yield Adjust')
waste         = Transition(label='Waste Manage')
audit         = Transition(label='Quality Audit')

# Loop for continuous monitoring and yield adjustment
loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor, adjust])

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site, impact, design, nutrient, climate, schedule,
    community, pest, energy, sensor, training,
    loop, waste, audit
])

# Add control‐flow constraints
root.order.add_edge(site, impact)
root.order.add_edge(impact, design)
root.order.add_edge(impact, nutrient)
root.order.add_edge(impact, schedule)
root.order.add_edge(impact, community)
root.order.add_edge(impact, pest)

root.order.add_edge(design, climate)
root.order.add_edge(design, sensor)
root.order.add_edge(design, energy)

root.order.add_edge(design, training)
root.order.add_edge(climate, training)
root.order.add_edge(sensor, training)
root.order.add_edge(energy, training)

root.order.add_edge(training, loop)
root.order.add_edge(loop, waste)
root.order.add_edge(loop, audit)