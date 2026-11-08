#!/usr/bin/env bash
# Export this repo's PRs and issues with gh, for scripts/metrics.py.
# Usage: scripts/export_github.sh [owner/repo]   -> data/github_export.json
set -euo pipefail
REPO="${1:-omorsi45/medilink-a3}"
cd "$(dirname "$0")/.."
mkdir -p data
gh pr list -R "$REPO" --state all --limit 30 \
  --json number,title,createdAt,mergedAt,closedAt,body,reviews,commits,labels > data/prs.json
gh issue list -R "$REPO" --state all --limit 200 \
  --json number,title,state,labels,createdAt,closedAt > data/issues.json
# CI check runs on each PR's first commit
echo "{" > data/first_commit_checks.json
first=1
for n in $(jq -r '.[].number' data/prs.json); do
  sha=$(jq -r ".[] | select(.number==$n) | .commits[0].oid" data/prs.json)
  count=$(gh api "repos/$REPO/commits/$sha/check-runs" --jq '.total_count')
  [ $first -eq 1 ] || echo "," >> data/first_commit_checks.json
  first=0
  echo "\"$n\": $count" >> data/first_commit_checks.json
done
echo "}" >> data/first_commit_checks.json
jq -n --slurpfile p data/prs.json --slurpfile i data/issues.json \
  --slurpfile c data/first_commit_checks.json \
  '{exported_at: (now | todate), prs: $p[0], issues: $i[0], first_commit_checks: $c[0]}' \
  > data/github_export.json
rm data/prs.json data/issues.json data/first_commit_checks.json
echo "wrote data/github_export.json"
