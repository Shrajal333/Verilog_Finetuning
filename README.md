# LLM_Finetuning

### Verilog Parsing & AutoComplete Template Generation
Loops through all Verilog files in a specified directory, extracts useful code structures (e.g., modules, always blocks, if-else constructs), and converts them into autocomplete training templates.

### Model Fine-Tuning with Qwen2.5-Coder-1.5B
 - Uses state-of-the-art tools like:
 - AutoGPTQForCausalLM for quantized model support
 - AutoModelForCausalLM and AutoTokenizer from HuggingFace
 - LoRA (get_peft_model) for parameter-efficient fine-tuning
 - BitsAndBytesConfig for 4-bit training
 - SFTTrainer from HuggingFace Transformers for supervised fine-tuning
 - All powered by RunPod GPU infrastructure
