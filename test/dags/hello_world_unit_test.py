from airflow.models import DagBag

def test_no_import_errors():
    dag_bag = DagBag()
    dag = dag_bag.get_dag(dag_id='airflow_tutorial_v01')
    assert len(dag_bag.import_errors) == 0, "No Import Failures"
    assert dag is not None
test_no_import_errors()

def test_dag_structure():
    dag_bag = DagBag()
    dag = dag_bag.get_dag(dag_id='airflow_tutorial_v01')
    
    target_keys = {'print_hello', 'print_world'}
    assert dag.task_dict.keys() == target_keys