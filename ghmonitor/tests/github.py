import json

GITHUB_GET_REPOS_RESPONSE = """
{
  "id": 724712,
  "node_id": "MDEwOlJlcG9zaXRvcnk3MjQ3MTI=",
  "name": "rust",
  "full_name": "rust-lang/rust",
  "private": false,
  "owner": {
    "login": "rust-lang",
    "id": 5430905,
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0MzA5MDU=",
    "avatar_url": "https://avatars1.githubusercontent.com/u/5430905?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/rust-lang",
    "html_url": "https://github.com/rust-lang",
    "followers_url": "https://api.github.com/users/rust-lang/followers",
    "following_url": "https://api.github.com/users/rust-lang/following{/other_user}",
    "gists_url": "https://api.github.com/users/rust-lang/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/rust-lang/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/rust-lang/subscriptions",
    "organizations_url": "https://api.github.com/users/rust-lang/orgs",
    "repos_url": "https://api.github.com/users/rust-lang/repos",
    "events_url": "https://api.github.com/users/rust-lang/events{/privacy}",
    "received_events_url": "https://api.github.com/users/rust-lang/received_events",
    "type": "Organization",
    "site_admin": false
  },
  "html_url": "https://github.com/rust-lang/rust",
  "description": "Empowering everyone to build reliable and efficient software.",
  "fork": false,
  "url": "https://api.github.com/repos/rust-lang/rust",
  "forks_url": "https://api.github.com/repos/rust-lang/rust/forks",
  "keys_url": "https://api.github.com/repos/rust-lang/rust/keys{/key_id}",
  "collaborators_url": "https://api.github.com/repos/rust-lang/rust/collaborators{/collaborator}",
  "teams_url": "https://api.github.com/repos/rust-lang/rust/teams",
  "hooks_url": "https://api.github.com/repos/rust-lang/rust/hooks",
  "issue_events_url": "https://api.github.com/repos/rust-lang/rust/issues/events{/number}",
  "events_url": "https://api.github.com/repos/rust-lang/rust/events",
  "assignees_url": "https://api.github.com/repos/rust-lang/rust/assignees{/user}",
  "branches_url": "https://api.github.com/repos/rust-lang/rust/branches{/branch}",
  "tags_url": "https://api.github.com/repos/rust-lang/rust/tags",
  "blobs_url": "https://api.github.com/repos/rust-lang/rust/git/blobs{/sha}",
  "git_tags_url": "https://api.github.com/repos/rust-lang/rust/git/tags{/sha}",
  "git_refs_url": "https://api.github.com/repos/rust-lang/rust/git/refs{/sha}",
  "trees_url": "https://api.github.com/repos/rust-lang/rust/git/trees{/sha}",
  "statuses_url": "https://api.github.com/repos/rust-lang/rust/statuses/{sha}",
  "languages_url": "https://api.github.com/repos/rust-lang/rust/languages",
  "stargazers_url": "https://api.github.com/repos/rust-lang/rust/stargazers",
  "contributors_url": "https://api.github.com/repos/rust-lang/rust/contributors",
  "subscribers_url": "https://api.github.com/repos/rust-lang/rust/subscribers",
  "subscription_url": "https://api.github.com/repos/rust-lang/rust/subscription",
  "commits_url": "https://api.github.com/repos/rust-lang/rust/commits{/sha}",
  "git_commits_url": "https://api.github.com/repos/rust-lang/rust/git/commits{/sha}",
  "comments_url": "https://api.github.com/repos/rust-lang/rust/comments{/number}",
  "issue_comment_url": "https://api.github.com/repos/rust-lang/rust/issues/comments{/number}",
  "contents_url": "https://api.github.com/repos/rust-lang/rust/contents/{+path}",
  "compare_url": "https://api.github.com/repos/rust-lang/rust/compare/{base}...{head}",
  "merges_url": "https://api.github.com/repos/rust-lang/rust/merges",
  "archive_url": "https://api.github.com/repos/rust-lang/rust/{archive_format}{/ref}",
  "downloads_url": "https://api.github.com/repos/rust-lang/rust/downloads",
  "issues_url": "https://api.github.com/repos/rust-lang/rust/issues{/number}",
  "pulls_url": "https://api.github.com/repos/rust-lang/rust/pulls{/number}",
  "milestones_url": "https://api.github.com/repos/rust-lang/rust/milestones{/number}",
  "notifications_url": "https://api.github.com/repos/rust-lang/rust/notifications{?since,all,participating}",
  "labels_url": "https://api.github.com/repos/rust-lang/rust/labels{/name}",
  "releases_url": "https://api.github.com/repos/rust-lang/rust/releases{/id}",
  "deployments_url": "https://api.github.com/repos/rust-lang/rust/deployments",
  "created_at": "2010-06-16T20:39:03Z",
  "updated_at": "2019-01-03T11:01:45Z",
  "pushed_at": "2019-01-03T10:37:37Z",
  "git_url": "git://github.com/rust-lang/rust.git",
  "ssh_url": "git@github.com:rust-lang/rust.git",
  "clone_url": "https://github.com/rust-lang/rust.git",
  "svn_url": "https://github.com/rust-lang/rust",
  "homepage": "https://www.rust-lang.org",
  "size": 412185,
  "stargazers_count": 32869,
  "watchers_count": 32869,
  "language": "Rust",
  "has_issues": true,
  "has_projects": true,
  "has_downloads": true,
  "has_wiki": false,
  "has_pages": false,
  "forks_count": 5435,
  "mirror_url": null,
  "archived": false,
  "open_issues_count": 4768,
  "license": {
    "key": "other",
    "name": "Other",
    "spdx_id": "NOASSERTION",
    "url": null,
    "node_id": "MDc6TGljZW5zZTA="
  },
  "forks": 5435,
  "open_issues": 4768,
  "watchers": 32869,
  "default_branch": "master",
  "permissions": {
    "admin": false,
    "push": false,
    "pull": true
  },
  "organization": {
    "login": "rust-lang",
    "id": 5430905,
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjU0MzA5MDU=",
    "avatar_url": "https://avatars1.githubusercontent.com/u/5430905?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/rust-lang",
    "html_url": "https://github.com/rust-lang",
    "followers_url": "https://api.github.com/users/rust-lang/followers",
    "following_url": "https://api.github.com/users/rust-lang/following{/other_user}",
    "gists_url": "https://api.github.com/users/rust-lang/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/rust-lang/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/rust-lang/subscriptions",
    "organizations_url": "https://api.github.com/users/rust-lang/orgs",
    "repos_url": "https://api.github.com/users/rust-lang/repos",
    "events_url": "https://api.github.com/users/rust-lang/events{/privacy}",
    "received_events_url": "https://api.github.com/users/rust-lang/received_events",
    "type": "Organization",
    "site_admin": false
  },
  "network_count": 5435,
  "subscribers_count": 1369
}
"""


def mock_github_request(url):
    if url.startswith('https://api.github.com/'):
        if '/repos/' in url and '/rust-lang/rust' in url:
            return 200, json.loads(GITHUB_GET_REPOS_RESPONSE)
        elif '/issues/' in url:
            pass
        elif '/pulls/' in url:
            pass
        else:
            return None
    else:
        return None
