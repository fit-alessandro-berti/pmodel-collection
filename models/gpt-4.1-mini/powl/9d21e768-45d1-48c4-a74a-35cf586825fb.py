# Generated from: 9d21e768-45d1-48c4-a74a-35cf586825fb.json
# Description: This process involves establishing a sustainable urban rooftop farm that integrates advanced hydroponic systems, renewable energy sources, and community engagement initiatives. It begins with site analysis and structural assessments to ensure rooftop suitability, followed by design planning incorporating modular growth units and automated irrigation. The process continues with procurement of eco-friendly materials and installation of solar panels to power the farm's equipment. Concurrently, local community outreach programs are launched to recruit volunteers and educational partners. Once operational, continuous monitoring of plant health and system efficiency is performed using IoT sensors, while data is analyzed to optimize growth conditions. Harvesting is coordinated with local markets and donation centers to promote food equity. The process concludes with maintenance scheduling and seasonal adaptation planning to sustain year-round productivity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Site_Survey = Transition(label='Site Survey')
Structure_Check = Transition(label='Structure Check')
Design_Layout = Transition(label='Design Layout')
Hydroponic_Setup = Transition(label='Hydroponic Setup')
Solar_Install = Transition(label='Solar Install')
Material_Order = Transition(label='Material Order')
Community_Recruit = Transition(label='Community Recruit')
Volunteer_Train = Transition(label='Volunteer Train')
Irrigation_Config = Transition(label='Irrigation Config')
Sensor_Deploy = Transition(label='Sensor Deploy')
Data_Monitor = Transition(label='Data Monitor')
Health_Check = Transition(label='Health Check')
Harvest_Plan = Transition(label='Harvest Plan')
Market_Liaise = Transition(label='Market Liaise')
Maintenance_Plan = Transition(label='Maintenance Plan')
Season_Adjust = Transition(label='Season Adjust')
Donation_Arrange = Transition(label='Donation Arrange')

# Phase 1: Site analysis and structural assessments
phase1 = StrictPartialOrder(nodes=[Site_Survey, Structure_Check])
phase1.order.add_edge(Site_Survey, Structure_Check)

# Phase 2: Design planning incorporating modular growth units and automated irrigation
phase2 = StrictPartialOrder(nodes=[Design_Layout, Hydroponic_Setup, Irrigation_Config])
phase2.order.add_edge(Design_Layout, Hydroponic_Setup)
phase2.order.add_edge(Design_Layout, Irrigation_Config)

# Phase 3: Procurement of eco-friendly materials and installation of solar panels
procurement = StrictPartialOrder(nodes=[Material_Order, Solar_Install])
procurement.order.add_edge(Material_Order, Solar_Install)

# Phase 4: Concurrent local community outreach programs
community = StrictPartialOrder(nodes=[Community_Recruit, Volunteer_Train])
community.order.add_edge(Community_Recruit, Volunteer_Train)

# Phase 5: Setup irrigation and deploy sensors (sensor deployment after irrigation config)
setup_monitoring = StrictPartialOrder(nodes=[Irrigation_Config, Sensor_Deploy])
setup_monitoring.order.add_edge(Irrigation_Config, Sensor_Deploy)

# Phase 6: Continuous monitoring and data analysis in parallel
monitoring = StrictPartialOrder(nodes=[Data_Monitor, Health_Check])
# no edges, both concurrent

# Phase 7: Harvest coordination with local markets and donation centers (both concurrent)
harvest = StrictPartialOrder(nodes=[Harvest_Plan, Market_Liaise, Donation_Arrange])
harvest.order.add_edge(Harvest_Plan, Market_Liaise)
harvest.order.add_edge(Harvest_Plan, Donation_Arrange)

# Phase 8: Maintenance scheduling and seasonal adaptation planning
maintenance = StrictPartialOrder(nodes=[Maintenance_Plan, Season_Adjust])
# no edges, concurrent

# Compose phases in order
root = StrictPartialOrder(nodes=[phase1, phase2, procurement, community, setup_monitoring, monitoring, harvest, maintenance])

# Add edges to establish order between phases
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, procurement)
root.order.add_edge(phase2, community)
root.order.add_edge(procurement, setup_monitoring)
root.order.add_edge(community, setup_monitoring)
root.order.add_edge(setup_monitoring, monitoring)
root.order.add_edge(monitoring, harvest)
root.order.add_edge(harvest, maintenance)