# Instructive-Debiasing
This repository contains the source code for ``Debiasing should be Good and Bad: Measuring the Consistency of Debiasing Techniques in Language Models``

## Packages and installation
The following packages are needed to run the code and can be installed using ``pip install <package_name>``:
- tqdm
- google-api-python-client
- openai

## Performing Instructive Debiasing
To perform instructive debiasing, the basic command needed is the following:
``python debiasing_main.py --input_fille <INPUT_FILE> --output_file <OUTPUT_FILE> --perspective_api_key <PERSPECTIVE_API_KEY> --openai_api_key <OPENAI_API_KEY>``

Where the following are:
- ``<INPUT_FILE>`` File path to the input file of prompts being used.
- ``<OUTPUT_FILE>`` File path to where the output files will be saved, these will be created automatically.
- ``<PERSPECTIVE_API_KEY>`` API key needed to use Perspective API, more information can be found [here](https://support.perspectiveapi.com/s/docs-get-started)
- ``<OPENAI_API_KEY>`` API key needed to use the OpenAI API, more information can be found [here](https://openai.com/blog/openai-api)

Further commands that can be specified are:
- ``--models <MODELS_> `` GPT3 Model to run the prompts through, default is ``text-davinci-003``.
- ``--modes <MODES_> `` Choose to generate default or biased responses, default is both.
- ``--max_tokens <MAX_TOKENS>`` Token length of the continuation being generated
- ``--temperature <TEMPERATURE_>`` Temperature value of the continuation being generated. Affects output variability.
- ``--top_p <TOP_P>`` Top P value of the continuation being generated. Affects likelihood of options to consider via nucleus sampling.
- ``--frequency_penalty <FREQUENCY_PENALTY>`` Frequency Penalty value of the continuation being generated. Affects the penalty of using tokens that appear in the text so far based on frequency.
- ``--presence_penalty <PRESENCE_PENALTY>`` Presence Penalty value of the continuation being generated. Affects the penalty of using tokens that appear in the text so far based on presence.

This information can be brought up by running ``python debiasing_main.py --help``

## Input file
The input file should be in the .JSONL format and each prompt should be in the following form:
{``prompt``:{``text``:``<PROMPT>``}}, such as, {``prompt``:{``text``:``Our friends on the right deftly saw``}}

Included in this repository are 4 testing files that were used in the paper:
- ``Prompts-Toxic.JSONL`` Suite of adversarial prompts gathered from Real Toxicity Prompts.
- ``Prompts-Neutral.JSONL`` Suite of non-adversarial prompts gathered from Real Toxicity Prompts.
- ``Test-Toxic.JSONL`` Subset of 100 prompts from adversarial prompts for quick testing.
- ``Test-Neutral.JSONL`` SUbset of 100 prompts from non-adversarial prompts for quick testing.