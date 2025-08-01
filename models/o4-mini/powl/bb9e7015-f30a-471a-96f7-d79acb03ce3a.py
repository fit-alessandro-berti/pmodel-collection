# Generated from: bb9e7015-f30a-471a-96f7-d79acb03ce3a.json
# Description: This process involves the comprehensive management of urban beekeeping operations, integrating hive maintenance, environmental monitoring, community engagement, and honey production optimization. Activities include assessing local flora, installing smart sensors for hive health, coordinating with city authorities for permits, conducting pest control using eco-friendly methods, harvesting honey with quality checks, and organizing educational workshops for local residents. The process ensures sustainability by tracking seasonal changes, analyzing pollen diversity, and implementing adaptive hive designs to maximize yield while minimizing urban impact. Additionally, it incorporates data reporting and collaboration with research institutions to contribute to broader ecological studies.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities as POWL transitions
flora = Transition(label='Flora Survey')
permit_req = Transition(label='Permit Request')
hive_setup = Transition(label='Hive Setup')
sensor_install = Transition(label='Sensor Install')
health_check = Transition(label='Health Check')
pest_control = Transition(label='Pest Control')
honey_harvest = Transition(label='Honey Harvest')
quality_test = Transition(label='Quality Test')
data_upload = Transition(label='Data Upload')
report_compile = Transition(label='Report Compile')
workshop_plan = Transition(label='Workshop Plan')
community_meet = Transition(label='Community Meet')
research_link = Transition(label='Research Link')

# Define the seasonal adaptation loop:
# A = Seasonal Audit; B = concurrent Pollen Analyze & Design Update
seasonal_audit = Transition(label='Seasonal Audit')
pollen_analyze = Transition(label='Pollen Analyze')
design_update = Transition(label='Design Update')

# B: analyze pollen and update design can occur in parallel
seasonal_body = StrictPartialOrder(nodes=[pollen_analyze, design_update])
# Loop: do Seasonal Audit, then either exit or do (pollen+design) then audit again
seasonal_cycle = OperatorPOWL(operator=Operator.LOOP, children=[seasonal_audit, seasonal_body])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    flora,
    permit_req,
    hive_setup,
    sensor_install,
    health_check,
    pest_control,
    honey_harvest,
    quality_test,
    data_upload,
    report_compile,
    workshop_plan,
    community_meet,
    research_link,
    seasonal_cycle
])

# Define the control-flow dependencies
o = root.order
o.add_edge(flora, permit_req)
o.add_edge(permit_req, hive_setup)
o.add_edge(hive_setup, sensor_install)

# After installing sensors, start the seasonal adaptation loop concurrently
o.add_edge(sensor_install, seasonal_cycle)

# Main operational flow
o.add_edge(sensor_install, health_check)
o.add_edge(health_check, pest_control)
o.add_edge(pest_control, honey_harvest)
o.add_edge(honey_harvest, quality_test)

# Data reporting branch
o.add_edge(quality_test, data_upload)
o.add_edge(data_upload, report_compile)

# Community engagement branch (starts after report compilation)
o.add_edge(report_compile, workshop_plan)
o.add_edge(workshop_plan, community_meet)

# Research collaboration
o.add_edge(report_compile, research_link)