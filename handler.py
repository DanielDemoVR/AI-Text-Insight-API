import runpod

from transformers import pipeline



try:

    classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

except Exception as e:

    classifier = None



def handler(job):

    """



    """



    job_input = job.get('input', {})

    text = job_input.get('text', None)



    if not text:

        return {"error": "No text provided for analysis"}



    if classifier is None:

        return {"error": "Model failed to load"}





    result = classifier(text)





    return {

        "text": text,

        "analysis": result[0]

    }



runpod.serverless.start({"handler": handler})