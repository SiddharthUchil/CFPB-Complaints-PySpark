from finance_complaint.pipeline.training import TrainingPipeline
from finance_complaint.entity.config_entity import TrainingPipelineConfig
from finance_complaint.config.pipeline.training import FinanceConfig

if __name__=="__main__":
    training_pipeline = TrainingPipeline(FinanceConfig)
    training_pipeline.start()