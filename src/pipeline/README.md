# AML Pipeline Example

Follow these steps:

```bash
az login --use-device-code --tenant <TENANT_ID>
```

Then select your correct subscription.

Create compute cluster:

```bash
az ml compute create -f create-cluster.yml
```

Create inference step AML conda environment:

```bash
cd src/pipeline/components/inference
az ml environment create --file inference-aml-env.yaml --workspace-name <YOUR_AML_WORKSPACE_NAME> --resource-group <YOUR_AML_RG>
```

Create score step AML conda environment:

```bash
cd src/pipeline/components/score
az ml environment create --file score-aml-env.yaml --workspace-name <YOUR_AML_WORKSPACE_NAME> --resource-group <YOUR_AML_RG>
```
