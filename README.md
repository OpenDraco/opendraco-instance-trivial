# opendraco-instance-trivial

Synthetic SWE-bench instance for OpenDraco APR evaluation — **trivial** difficulty tier.

Contains a one-function Python module with a single deliberate bug: a
comparison-operator inversion (the literal `1` should be `0`). The fix
is a one-character edit; the failing test is obvious from the function
name and docstring.

This is the floor-of-difficulty baseline: any working topology should
solve it in a single Locator + Patcher pass.
