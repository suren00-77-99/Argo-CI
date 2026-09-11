# CI Repository — Python Frontend + Backend

This repository contains application source code and CI automation.

Flow:
1. Developer changes frontend/backend code.
2. CI runs lint + syntax validation.
3. Unit tests run.
4. Docker images are built.
5. Images are scanned.
6. Images are pushed to Amazon ECR.
7. CI updates the CD/GitOps repository with the new image tags.
8. Argo CD detects the Git change and deploys through Helm.

> Recommended production setup: use GitHub Actions OIDC to assume an AWS IAM role.
> Do not store AWS access keys in Git.
