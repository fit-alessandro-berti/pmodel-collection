# Generated from: 25ac0908-826a-42a7-8f77-08d9a7a4c8af.json
# Description: This process involves the complex migration of a legacy enterprise resource planning (ERP) system to a modern cloud-based architecture. It includes detailed assessment of existing data structures, custom code review, incremental data extraction, transformation, and loading (ETL), parallel system testing, stakeholder training, and phased cutover. Due to the critical nature of the legacy system, thorough risk analysis and rollback planning are essential. The process also requires continuous monitoring post-migration to ensure data integrity and operational stability while minimizing downtime and business disruption across multiple departments and geographic locations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# define atomic activities
scope_review    = Transition(label='Scope Review')
data_audit      = Transition(label='Data Audit')
code_scan       = Transition(label='Code Scan')
risk_assess     = Transition(label='Risk Assess')
etl_design      = Transition(label='ETL Design')
extract_data    = Transition(label='Extract Data')
transform_data  = Transition(label='Transform Data')
load_data       = Transition(label='Load Data')
unit_testing    = Transition(label='Unit Testing')
integration_test= Transition(label='Integration Test')
user_training   = Transition(label='User Training')
parallel_run    = Transition(label='Parallel Run')
cutover_plan    = Transition(label='Cutover Plan')
final_migration = Transition(label='Final Migration')
post_audit      = Transition(label='Post Audit')
rollback_prep   = Transition(label='Rollback Prep')
system_monitor  = Transition(label='System Monitor')

# ETL loop body: Extract -> Transform -> Load
etl_body = StrictPartialOrder(nodes=[extract_data, transform_data, load_data])
etl_body.order.add_edge(extract_data, transform_data)
etl_body.order.add_edge(transform_data, load_data)

# loop the ETL body until exit
etl_loop = OperatorPOWL(operator=Operator.LOOP, children=[etl_body, etl_body])

# parallel group for training, parallel run and rollback preparation
parallel_group = StrictPartialOrder(nodes=[user_training, parallel_run, rollback_prep])
# no edges among them => concurrent execution

# assemble the overall partial order workflow
root = StrictPartialOrder(nodes=[
    scope_review,
    data_audit,
    code_scan,
    risk_assess,
    etl_design,
    etl_loop,
    unit_testing,
    integration_test,
    parallel_group,
    cutover_plan,
    final_migration,
    post_audit,
    system_monitor
])

# define the sequencing dependencies
root.order.add_edge(scope_review,      data_audit)
root.order.add_edge(data_audit,        code_scan)
root.order.add_edge(code_scan,         risk_assess)
root.order.add_edge(risk_assess,       etl_design)
root.order.add_edge(etl_design,        etl_loop)
root.order.add_edge(etl_loop,          unit_testing)
root.order.add_edge(unit_testing,      integration_test)
root.order.add_edge(integration_test,  parallel_group)
root.order.add_edge(parallel_group,    cutover_plan)
root.order.add_edge(cutover_plan,      final_migration)
root.order.add_edge(final_migration,   post_audit)
root.order.add_edge(post_audit,        system_monitor)