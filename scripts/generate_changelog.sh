#!/usr/bin/env bash
set -euo pipefail

# Simple changelog generator: collects commits since last tag, or all commits if no tags.
REPO_DIR="$(pwd)"
cd "$REPO_DIR"

# Ensure full history is available
git fetch --tags --prune

# Determine range
if last_tag=$(git describe --tags --abbrev=0 2>/dev/null || true) && [ -n "$last_tag" ]; then
  range="$last_tag..HEAD"
else
  root=$(git rev-list --max-parents=0 HEAD)
  range="$root..HEAD"
fi

# Generate entries (skip merge commits)
commits=$(git log --no-merges --pretty=format:"- %s (%h)" $range)

if [ -z "$commits" ]; then
  echo "# Changelog\n\nNo changes detected." > CHANGELOG.md
  exit 0
fi

cat > CHANGELOG.md <<EOF
# Changelog

Changes since ${last_tag:-initial commit}:

$commits
EOF

# Print short preview
echo "Generated CHANGELOG.md with the following entries:"
echo "$commits"
