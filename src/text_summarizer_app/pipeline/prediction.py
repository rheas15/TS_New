import transformers 
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
from text_summarizer_app.logging import logger

class PredictionPipeline:
    def __init__(self, model_name="google/pegasus-cnn_dailymail"):
        self.model_name = model_name
        self.tokenizer = None
        self.model = None
        logger.info("TextSummarizer initialized with model: %s", model_name)

    def _load_model(self):
            self.tokenizer = PegasusTokenizer.from_pretrained(self.model_name)
            self.model = PegasusForConditionalGeneration.from_pretrained(self.model_name)
            logger.info("Model loaded successfully")
     
    def summarize_text(self, text, max_length=100, min_length=25):
        if self.model is None:
            self._load_model()
        inputs = self.tokenizer(text, truncation=True, padding="longest", return_tensors="pt")
        summary_ids = self.model.generate(inputs["input_ids"], max_length=max_length, min_length=min_length)
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True).replace("<n>", " ")
        logger.info("Text summarized successfully")
        return summary
