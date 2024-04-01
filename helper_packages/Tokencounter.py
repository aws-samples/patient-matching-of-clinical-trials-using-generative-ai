"""Module providing a JSON Functionality"""
import json
import locale


class PrettyPrintModel():
    """Class representing a person"""

    def __init__(self, response, model_id):
        self.input_cost = None
        self.raw_input_cost = None
        self.latency = int(
            response['ResponseMetadata']['HTTPHeaders']['x-amzn-bedrock-invocation-latency'])
        self.output_cost = None
        self.raw_output_cost = None
        self.raw_content = json.loads(response.get('body').read())
        self.model = model_id
        self.input_tokens = self.raw_content['usage']['input_tokens']
        self.output_tokens = self.raw_content['usage']['output_tokens']
        self.content = "------".join((str(x['text'])
                                     for x in self.raw_content.get('content')))
        self.get_price()

    def get_price(self):
        """Class representing a person"""

        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        # Refer to https://aws.amazon.com/bedrock/pricing/ for most up to date pricing
        # Price provides as example
        price_map = {
            'anthropic.claude-3-sonnet-20240229-v1:0': {'input': 0.00300/1000, 'output': 0.01500/1000},
            'anthropic.claude-3-haiku-20240307-v1:0': {'input': 0.00025/1000, 'output': 0.00125/1000},
            'mistral.mixtral-8x7b-instruct-v0:1': {'input': 0.00045/1000, 'output': 0.0007/1000},
            'anthropic.claude-v2:1': {'input': 0.00800/1000, 'output': '0.02400'}
        }
        self.raw_input_cost = price_map[self.model]['input'] * \
            self.input_tokens * 1000
        self.raw_output_cost = price_map[self.model]['output'] * \
            self.output_tokens * 1000
        # Cost of token mulitplyied by 1000 similar record size patients
        self.input_cost = locale.currency(price_map[self.model]['input'] *
                                          self.input_tokens * 1000)
        self.output_cost = locale.currency(price_map[self.model]['output'] *
                                           self.output_tokens * 1000)

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self):
        return f"""
         InputTokens: {self.input_tokens} OutputToken: {self.output_tokens}\n \
        Cost for similar 1000 patient records: Input: {self.input_cost} Output: {self.output_cost}\n \
        Latency: {self.latency}ms\n \
        Response: \n{self.content}
"""
