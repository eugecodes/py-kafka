#!/usr/bin/env bash

set -e

gitHubPullRequestMergedFlag=$(jq -r '.pull_request.merged' "$GITHUB_EVENT_PATH")

if [ "${gitHubPullRequestMergedFlag}" == "true" ]; then
{
  commit_sha=$(jq -r '.pull_request.merge_commit_sha' "$GITHUB_EVENT_PATH")
}
elif [ "${gitHubPullRequestMergedFlag}" == "false" ]; then
{
  commit_sha=$(jq -r '.pull_request.head.sha' "$GITHUB_EVENT_PATH")
}
fi
#. venv/bin/activate
bash <(curl -Ls https://coverage.codacy.com/get.sh) report -r coverage.xml --commit-uuid "${commit_sha}"
