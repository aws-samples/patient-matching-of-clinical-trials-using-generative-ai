# Patient Matching of Clinical Trials using Generative AI

This is a demo of how to leverage Generative AI to perform cohort identification by matching patients to clinical trials.

Clinical Trials Gen AI workshop.ipynb contains a jupyter notebook file which walksthrough step by step on how to use Amazon Bedrock and Large Language Models (LLM) to solve a real-world problem described in the User persona below.

### User persona

AnyCompany is a healthcare startup that provides insights based on patient history. They offer a solution that can be embedded into an EMR, so their customers include EMR vendors and healthcare providers. They offer their solution as a SaaS model and their infrastructure is cloud native and built leveraging serverless to provide elasticity and scalability. The Product team recently flagged the need for the company to offer Cohort Identification as a service and their first investment is to build a Clinical Trials matching feature. The business is attempting to evaluate if a clinical trial is suitable for a patient given a patient's longitudinal records.

As a data scientist recently hired by AnyCompany, you got pulled into a tiger team that has the goal of (i) validating if this project is feasible, (ii) building a working proof of concept.

If your assignment succeeds, this feature will be added to AnyCompany's next big release that is coming out soon.

The clock is ticking, so let's starting building!

## Prerequisites

The notebook requires mutiple resources to be enabled or created.

- Ensure [access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) to Anthropric models and Mistral Models.
- Ensure proper IAM permission to [invoke models](https://docs.aws.amazon.com/step-functions/latest/dg/bedrock-iam.html#bedrock-policy-invokemodel-full-access) and [subscribe](https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-subscription) to 3rd party models.
- Creation of [Amazon Healthlake](https://docs.aws.amazon.com/healthlake/latest/devguide/getting-started.html#setting-up-iam-amazon-healthlake) with Synthea data enabled and FHIR API permission enabled - (**Optional**)

### Environment

- Notebook Envinronment requires python version >= 3.10.0
- Compute resource similar to Sagemaker Studio's ml.t3.medium instance 2vCPU and 4Gib Memory
- Refer to requirements.txt for package requirements

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

## Citations

Jason Walonoski, Mark Kramer, Joseph Nichols, Andre Quina, Chris Moesel, Dylan Hall, Carlton Duffett, Kudakwashe Dube, Thomas Gallagher, Scott McLachlan, Synthea: An approach, method, and software mechanism for generating synthetic patients and the synthetic electronic health care record, Journal of the American Medical Informatics Association, Volume 25, Issue 3, March 2018, Pages 230–238, https://doi.org/10.1093/jamia/ocx079
