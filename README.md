# hello-api

Small Flask service used to demonstrate a container CI/CD pipeline.

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
