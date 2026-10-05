# CloudOps Platform -- Microservice Application & Container CI

Hardened Python Flask microservice used to demonstrate containerization, health probes, and automated CI/CD with GitHub Actions and GitHub Container Registry (GHCR).

Part of the **CloudOps Platform** project:
- **[terraform-platform](https://github.com/AhsanASid/terraform-platform)**: Modular AWS Infrastructure as Code (VPC, IAM, SSM, plan-only EKS)
- **[platform-manifests](https://github.com/AhsanASid/platform-manifests)**: Kubernetes desired state, Argo Rollouts, Observability, and Velero DR
- **[hello-api](https://github.com/AhsanASid/hello-api)**: Python microservice & automated GitHub Actions CI pipeline

## What's here
- `app.py`: API with `/` and `/healthz` (used by Kubernetes probes)
- `Dockerfile`: pinned base image, dependency layer cached separately, runs as a non-root user
- `.github/workflows/build.yml`: builds on every push and pull request; publishes to GHCR on pushes to `main`

## Pipeline
1. Push to `main` triggers GitHub Actions
2. The image is published as `ghcr.io/ahsanasid/hello-api:sha-<commit>`
3. Deployment manifests live in [platform-manifests](https://github.com/AhsanASid/platform-manifests)

## Security notes
- Registry login uses the short-lived `GITHUB_TOKEN` with `packages: write` only; no stored credentials
- Images are tagged by commit SHA, never `latest`, so every deployment is traceable to exact code
- Container runs as a non-root user

## Run locally
```bash
docker build -t hello-api:dev .
docker run --rm -p 8000:8000 hello-api:dev
```
