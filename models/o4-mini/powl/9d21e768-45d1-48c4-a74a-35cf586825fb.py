# Generated from: 9d21e768-45d1-48c4-a74a-35cf586825fb.json
# Description: This process involves establishing a sustainable urban rooftop farm that integrates advanced hydroponic systems, renewable energy sources, and community engagement initiatives. It begins with site analysis and structural assessments to ensure rooftop suitability, followed by design planning incorporating modular growth units and automated irrigation. The process continues with procurement of eco-friendly materials and installation of solar panels to power the farm's equipment. Concurrently, local community outreach programs are launched to recruit volunteers and educational partners. Once operational, continuous monitoring of plant health and system efficiency is performed using IoT sensors, while data is analyzed to optimize growth conditions. Harvesting is coordinated with local markets and donation centers to promote food equity. The process concludes with maintenance scheduling and seasonal adaptation planning to sustain year-round productivity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# define activities
SiteSurvey      = Transition(label='Site Survey')
StructureCheck  = Transition(label='Structure Check')
DesignLayout    = Transition(label='Design Layout')
HydroponicSetup = Transition(label='Hydroponic Setup')
IrrigationConfig= Transition(label='Irrigation Config')
MaterialOrder   = Transition(label='Material Order')
SolarInstall    = Transition(label='Solar Install')
CommunityRecruit= Transition(label='Community Recruit')
VolunteerTrain  = Transition(label='Volunteer Train')
SensorDeploy    = Transition(label='Sensor Deploy')
DataMonitor     = Transition(label='Data Monitor')
HealthCheck     = Transition(label='Health Check')
HarvestPlan     = Transition(label='Harvest Plan')
MarketLiaise    = Transition(label='Market Liaise')
DonationArrange = Transition(label='Donation Arrange')
MaintenancePlan = Transition(label='Maintenance Plan')
SeasonAdjust    = Transition(label='Season Adjust')

# build the partial order
root = StrictPartialOrder(nodes=[
    SiteSurvey, StructureCheck, DesignLayout,
    HydroponicSetup, IrrigationConfig,
    MaterialOrder, SolarInstall,
    CommunityRecruit, VolunteerTrain,
    SensorDeploy, DataMonitor, HealthCheck,
    HarvestPlan, MarketLiaise, DonationArrange,
    MaintenancePlan, SeasonAdjust
])

# site analysis & structure check
root.order.add_edge(SiteSurvey, StructureCheck)

# design planning & setup
root.order.add_edge(StructureCheck,    DesignLayout)
root.order.add_edge(DesignLayout,      HydroponicSetup)
root.order.add_edge(HydroponicSetup,   IrrigationConfig)

# after irrigation config, two branches run in parallel:
#   1) Material order -> solar install
#   2) Community recruit -> volunteer train
root.order.add_edge(IrrigationConfig, MaterialOrder)
root.order.add_edge(IrrigationConfig, CommunityRecruit)
root.order.add_edge(MaterialOrder,    SolarInstall)
root.order.add_edge(CommunityRecruit, VolunteerTrain)

# join branches before operation
root.order.add_edge(SolarInstall,   SensorDeploy)
root.order.add_edge(VolunteerTrain, SensorDeploy)

# monitoring & analysis
root.order.add_edge(SensorDeploy, DataMonitor)
root.order.add_edge(DataMonitor,  HealthCheck)

# harvesting coordination
root.order.add_edge(HealthCheck, HarvestPlan)
root.order.add_edge(HarvestPlan, MarketLiaise)
root.order.add_edge(HarvestPlan, DonationArrange)

# maintenance & seasonal adaptation
root.order.add_edge(MarketLiaise,    MaintenancePlan)
root.order.add_edge(DonationArrange, MaintenancePlan)
root.order.add_edge(MaintenancePlan, SeasonAdjust)