# Generated from: bd1f3229-f70b-4526-8a31-dd5cd7f58652.json
# Description: This process outlines the complex supply chain for urban beekeeping, integrating sustainable sourcing, community engagement, and regulatory compliance. It begins with hive material procurement from eco-certified suppliers, followed by custom hive assembly tailored to city environments. Next, the process manages bee colony acquisition ensuring genetic diversity and disease resistance. Urban apiaries are then strategically located and registered with local authorities. Continuous monitoring includes environmental data collection and adaptive hive maintenance. Honey extraction involves precise timing and contamination prevention. The product undergoes natural filtration, quality testing, and innovative packaging with biodegradable materials. Finally, distribution leverages local markets, subscription services, and educational workshops to promote awareness and sustainability within urban settings.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Material_Sourcing = Transition(label='Material Sourcing')
Hive_Assembly = Transition(label='Hive Assembly')
Colony_Selection = Transition(label='Colony Selection')
Apiary_Setup = Transition(label='Apiary Setup')
Regulatory_Filing = Transition(label='Regulatory Filing')
Environmental_Scan = Transition(label='Environmental Scan')
Hive_Monitoring = Transition(label='Hive Monitoring')
Pest_Control = Transition(label='Pest Control')
Honey_Harvest = Transition(label='Honey Harvest')
Quality_Testing = Transition(label='Quality Testing')
Natural_Filtration = Transition(label='Natural Filtration')
Eco_Packaging = Transition(label='Eco Packaging')
Market_Distribution = Transition(label='Market Distribution')
Subscription_Setup = Transition(label='Subscription Setup')
Community_Outreach = Transition(label='Community Outreach')

# Monitoring loop: Environmental Scan, then loop of (Hive Monitoring + Pest Control)
monitoring_loop_body = StrictPartialOrder(nodes=[Hive_Monitoring, Pest_Control])
# concurrent Hive Monitoring and Pest Control (no order between them)
monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[Environmental_Scan, monitoring_loop_body])

# Packaging and testing partial order: Natural Filtration -> Quality Testing -> Eco Packaging
packaging_po = StrictPartialOrder(
    nodes=[Natural_Filtration, Quality_Testing, Eco_Packaging],
    )
packaging_po.order.add_edge(Natural_Filtration, Quality_Testing)
packaging_po.order.add_edge(Quality_Testing, Eco_Packaging)

# Distribution choice: XOR among Market Distribution, Subscription Setup, Community Outreach 
distribution_xor = OperatorPOWL(operator=Operator.XOR, children=[Market_Distribution, Subscription_Setup, Community_Outreach])

# Honey Extraction partial order including Honey Harvest -> packaging_po
honey_po = StrictPartialOrder(
    nodes=[Honey_Harvest, packaging_po]
)
honey_po.order.add_edge(Honey_Harvest, packaging_po)

# Setup partial order Apiary Setup -> Regulatory Filing
setup_po = StrictPartialOrder(nodes=[Apiary_Setup, Regulatory_Filing])
setup_po.order.add_edge(Apiary_Setup, Regulatory_Filing)

# Colony selection concurrent with setup
colony_setup_po = StrictPartialOrder(nodes=[Colony_Selection, setup_po])

# Assembly partial order: Material Sourcing -> Hive Assembly -> colony_setup_po
assembly_po = StrictPartialOrder(nodes=[Material_Sourcing, Hive_Assembly, colony_setup_po])
assembly_po.order.add_edge(Material_Sourcing, Hive_Assembly)
assembly_po.order.add_edge(Hive_Assembly, colony_setup_po)

# Then assembly_po -> monitoring_loop -> honey_po -> distribution_xor
root = StrictPartialOrder(
    nodes=[assembly_po, monitoring_loop, honey_po, distribution_xor]
)
root.order.add_edge(assembly_po, monitoring_loop)
root.order.add_edge(monitoring_loop, honey_po)
root.order.add_edge(honey_po, distribution_xor)