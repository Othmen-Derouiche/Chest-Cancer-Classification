import mlflow
import tensorflow as tf
from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.model_evaluation_mlflow import Evaluation
from src.cnnClassifier import logger


# Patch the mlflow function
def patched_save_model(model, path, conda_env=None, code_paths=None, mlflow_model=None, custom_objects=None,
                       signature=None, input_example=None, pip_requirements=None, extra_pip_requirements=None,
                       saved_model_kwargs=None, keras_model_kwargs=None, metadata=None):
    from mlflow.models import Model
    from mlflow import pyfunc
    from mlflow.utils.environment import _mlflow_conda_env, _REQUIREMENTS_FILE_NAME
    
    if hasattr(tf.keras, '__version__'):
        keras_version = tf.keras.__version__
    else:
        keras_version = tf.__version__

    flavor_options = {
        "keras_version": keras_version,
        "save_format": "h5",
    }

    # rest of the original logic

# Apply the patch
mlflow.tensorflow.save_model = patched_save_model






STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        # evaluation.log_into_mlflow()




if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
            