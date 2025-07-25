# from langchain.callbacks.base import BaseCallbackHandler
# import json


# class GeminiTokenLogger(BaseCallbackHandler):
#     def __init__(self, log_file="gemini_token_log.jsonl"):
#         self.run_id_to_prompt = {}
#         self.log_file = log_file

#     def on_llm_start(self, serialized, prompts, **kwargs):
#         run_id = kwargs.get("run_id")
#         if run_id and prompts:
#             self.run_id_to_prompt[run_id] = prompts[0]

#     def on_llm_end(self, response, **kwargs):
#         run_id = kwargs.get("run_id")
#         self.run_id_to_prompt.pop(run_id, None)

#         try:
#             generation = response.generations[0][0]
#             message = generation.message
#             usage = vars(message).get("usage_metadata", {})
#             log_data = {
#                 "model": "gemini-2.0-flash",
#                 "input_tokens": usage.get("input_tokens", 0),
#                 "output_tokens": usage.get("output_tokens", 0),
#                 "total_tokens": usage.get("total_tokens", 0),
#             }

#             with open(self.log_file, "a", encoding="utf-8") as f:
#                 f.write(json.dumps(log_data) + "\n")
#         except Exception as e:
#             print("[❌ GeminiTokenLogger] Failed to log tokens:", e)


from langchain.callbacks.base import BaseCallbackHandler
import csv
import os


class GeminiTokenLogger(BaseCallbackHandler):
    def __init__(self, log_file="gemini_token_log.csv"):
        self.run_id_to_prompt = {}
        self.log_file = log_file

        # Write header if file doesn't exist
        if not os.path.exists(self.log_file):
            with open(self.log_file, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(
                    f,
                    fieldnames=[
                        "model",
                        "input_tokens",
                        "output_tokens",
                        "total_tokens",
                    ],
                )
                writer.writeheader()

    def on_llm_start(self, serialized, prompts, **kwargs):
        run_id = kwargs.get("run_id")
        if run_id and prompts:
            self.run_id_to_prompt[run_id] = prompts[0]

    def on_llm_end(self, response, **kwargs):
        run_id = kwargs.get("run_id")
        self.run_id_to_prompt.pop(run_id, None)

        try:
            generation = response.generations[0][0]
            message = generation.message
            usage = vars(message).get("usage_metadata", {})
            log_data = {
                "model": "gemini-2.0-flash",
                "input_tokens": usage.get("input_tokens", 0),
                "output_tokens": usage.get("output_tokens", 0),
                "total_tokens": usage.get("total_tokens", 0),
            }

            with open(self.log_file, mode="a", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(
                    f,
                    fieldnames=[
                        "model",
                        "input_tokens",
                        "output_tokens",
                        "total_tokens",
                    ],
                )
                writer.writerow(log_data)
        except Exception as e:
            print("[❌ GeminiTokenLogger] Failed to log tokens:", e)
