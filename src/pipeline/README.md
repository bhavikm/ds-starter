# AML Pipeline Example

Follow these steps:

```bash
az login --use-device-code --tenant <TENANT_ID>
```

Then select your correct subscription when prompted.

Also ensure you have the `az ml` extension is installed:

```bash
az ml --version
```

Next create compute cluster to run the pipeline in your AML workspace:

```bash
az ml compute create -f create-cpu-compute.yaml --workspace-name <YOUR_AML_WORKSPACE_NAME> --resource-group <YOUR_AML_RG>
```

Update `src/pipeline/components/inference/inference-conda-env.yaml` with the requirements you need to run `src/pipeline/components/inference/inference.py`. Then create inference step AML conda environment that is defined in the file `inference-aml-env.yaml`:

```bash
cd src/pipeline/components/inference
az ml environment create --file inference-aml-env.yaml --workspace-name <YOUR_AML_WORKSPACE_NAME> --resource-group <YOUR_AML_RG>
```

Update `src/pipeline/components/score/score-conda-env.yaml` with the requirements you need to run `src/pipeline/components/inference/score.py`. Then create score step AML conda environment that is defined in the file `score-aml-env.yaml`:

```bash
cd src/pipeline/components/score
az ml environment create --file score-aml-env.yaml --workspace-name <YOUR_AML_WORKSPACE_NAME> --resource-group <YOUR_AML_RG>
```

Once you have verified that the two custom environments are built succesfully in AML, you can launch the pipeline job.

Ensure you in the `src/pipeline` directory, then run:

```bash
az ml job create -f aml-components-pipeline.yaml --workspace-name <YOUR_AML_WORKSPACE_NAME> --resource-group <YOUR_AML_RG>
```
