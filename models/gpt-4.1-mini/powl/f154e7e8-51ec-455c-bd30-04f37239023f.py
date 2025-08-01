# Generated from: f154e7e8-51ec-455c-bd30-04f37239023f.json
# Description: This process outlines the comprehensive management of urban beekeeping operations, combining environmental monitoring, community engagement, hive maintenance, and honey production. It involves site selection based on urban flora assessments, regular hive health checks using digital sensors, pest control with organic methods, and coordination with local authorities for compliance. Additionally, the process includes educational workshops for residents, seasonal honey extraction, quality testing, packaging, and distribution through local markets, ensuring sustainable practices and community support while maximizing honey yield and bee welfare in a city environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Activities
Site_Survey = Transition(label='Site Survey')
Flora_Mapping = Transition(label='Flora Mapping')
Hive_Setup = Transition(label='Hive Setup')
Sensor_Install = Transition(label='Sensor Install')
Health_Check = Transition(label='Health Check')
Pest_Control = Transition(label='Pest Control')
Data_Logging = Transition(label='Data Logging')
Community_Meet = Transition(label='Community Meet')
Workshop_Plan = Transition(label='Workshop Plan')
Honey_Extract = Transition(label='Honey Extract')
Quality_Test = Transition(label='Quality Test')
Packaging = Transition(label='Packaging')
Market_Setup = Transition(label='Market Setup')
Sales_Report = Transition(label='Sales Report')
Regulation_Check = Transition(label='Regulation Check')
Waste_Manage = Transition(label='Waste Manage')
Seasonal_Review = Transition(label='Seasonal Review')

# Partial order for environmental monitoring and hive setup:
# Site Survey --> Flora Mapping --> Hive Setup --> Sensor Install
env_monitoring = StrictPartialOrder(nodes=[Site_Survey, Flora_Mapping, Hive_Setup, Sensor_Install])
env_monitoring.order.add_edge(Site_Survey, Flora_Mapping)
env_monitoring.order.add_edge(Flora_Mapping, Hive_Setup)
env_monitoring.order.add_edge(Hive_Setup, Sensor_Install)

# Partial order for hive maintenance activities:
# Health Check --> Pest Control --> Data Logging
hive_maintenance = StrictPartialOrder(nodes=[Health_Check, Pest_Control, Data_Logging])
hive_maintenance.order.add_edge(Health_Check, Pest_Control)
hive_maintenance.order.add_edge(Pest_Control, Data_Logging)

# Partial order for community engagement:
# Community Meet --> Workshop Plan
community_engagement = StrictPartialOrder(nodes=[Community_Meet, Workshop_Plan])
community_engagement.order.add_edge(Community_Meet, Workshop_Plan)

# Partial order for honey production:
# Honey Extract --> Quality Test --> Packaging
honey_production = StrictPartialOrder(nodes=[Honey_Extract, Quality_Test, Packaging])
honey_production.order.add_edge(Honey_Extract, Quality_Test)
honey_production.order.add_edge(Quality_Test, Packaging)

# Partial order for distribution:
# Market Setup --> Sales Report
distribution = StrictPartialOrder(nodes=[Market_Setup, Sales_Report])
distribution.order.add_edge(Market_Setup, Sales_Report)

# Partial order for compliance and waste:
# Regulation Check --> Waste Manage
compliance = StrictPartialOrder(nodes=[Regulation_Check, Waste_Manage])
compliance.order.add_edge(Regulation_Check, Waste_Manage)

# Seasonal Review is ongoing or after some major steps, so we leave it concurrent with others.

# Combine all subprocesses in a single partial order concurrently
# with additional edges for coordination where sensible:
root = StrictPartialOrder(
    nodes=[env_monitoring,
           hive_maintenance,
           community_engagement,
           honey_production,
           distribution,
           compliance,
           Seasonal_Review]
)

# Add edges from Sensor Install (end of env_monitoring) to Health Check and Regulation Check:
root.order.add_edge(env_monitoring, hive_maintenance)  # env_monitoring before hive_maintenance
root.order.add_edge(env_monitoring, compliance)       # env_monitoring before compliance

# Health check and pest control before community engagement to reflect some coordination:
root.order.add_edge(hive_maintenance, community_engagement)

# Packaging before distribution
root.order.add_edge(honey_production, distribution)

# Seasonal Review can follow Sales Report and Waste Manage
root.order.add_edge(distribution, Seasonal_Review)
root.order.add_edge(compliance, Seasonal_Review)