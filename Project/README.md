## Workflows

### Loop Workflow

1. Update `config.yaml`
2. Update `params.yaml`
3. Update the entity
4. Update the configuration file in `src/config`
5. Update the components
6. Update the pipeline
7. Update `main.py`

### Final Step

8. Update `dvc.yaml` DVC for pipeline tracking 
- dvc init
- dvc repro
- dvc dag : dependencies graph 

launch mlflow remote server using DagsHub