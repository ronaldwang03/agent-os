from agent_os.integrations.base import GovernancePolicy


def test_identical_policies_are_equal():
    p1 = GovernancePolicy(
        allowed_tools=["search", "read_file"],
        blocked_patterns=["password"],
        max_tool_calls=5,
    )
    p2 = GovernancePolicy(
        allowed_tools=["search", "read_file"],
        blocked_patterns=["password"],
        max_tool_calls=5,
    )

    assert p1 == p2


def test_policies_with_different_configuration_are_not_equal():
    p1 = GovernancePolicy(max_tokens=1024)
    p2 = GovernancePolicy(max_tokens=2048)

    assert p1 != p2


def test_policy_is_not_equal_to_non_policy_object():
    p = GovernancePolicy()

    assert p != "not-a-policy"


def test_policies_are_hashable_for_sets_and_dicts():
    p1 = GovernancePolicy(allowed_tools=["search"])
    p2 = GovernancePolicy(allowed_tools=["search"])
    p3 = GovernancePolicy(allowed_tools=["write"])

    policy_set = {p1, p2, p3}
    policy_dict = {p1: "alpha", p3: "beta"}

    assert len(policy_set) == 2
    assert policy_dict[p2] == "alpha"
