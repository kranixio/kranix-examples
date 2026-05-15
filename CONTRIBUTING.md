# Contributing to kranix-examples

Thank you for your interest in contributing examples to the Kranix ecosystem!

## What Makes a Good Example?

A good example is:
- **Self-contained**: Can be run without external dependencies beyond what's documented
- **Documented**: Clear README with prerequisites, steps, and expected output
- **Tested**: Works against the latest Kranix release
- **Focused**: Demonstrates one specific concept or workflow
- **Maintainable**: Simple enough for others to understand and modify

## Example Structure

Every example should follow this structure:

```
example-name/
├── README.md          # What it does, prerequisites, steps, expected output
├── Makefile           # setup, run, verify, clean targets
├── manifests/         # KranixApp, KranixPolicy, and K8s YAMLs
├── scripts/           # Setup and teardown shell scripts
└── src/               # Application code (if applicable)
```

## Creating a New Example

### 1. Choose a Location

Pick the most appropriate category:
- `quickstart/` - First steps, minimal prerequisites
- `ai-agents/` - MCP + AI agent integrations
- `gitops/` - GitOps workflows with KranixApp CRDs
- `platform-engineering/` - IDP and platform patterns
- `observability/` - Monitoring and debugging
- `local-dev/` - Local development environments
- `reference-architectures/` - Full production-grade blueprints

### 2. Create the Directory

```bash
mkdir -p kranix-examples/category/your-example-name
cd kranix-examples/category/your-example-name
```

### 3. Write the README.md

Your README must include:

```markdown
# Example Name

Brief description of what this example demonstrates.

## What You'll Learn

- Concept 1
- Concept 2
- Concept 3

## Prerequisites

- Tool X (version Y or later)
- Tool Z
- A running kranix-api instance

## Setup

```bash
# Commands to set up the example
```

## Running the Example

```bash
# Commands to run the example
```

## Expected Output

Describe what you should see when the example runs successfully.

## Cleanup

```bash
# Commands to tear down the example
```

## Troubleshooting

Common issues and how to resolve them.
```

### 4. Create a Makefile

Include at minimum these targets:

```makefile
.PHONY: setup run verify clean

setup:
	# Install prerequisites, create cluster/namespace

run:
	# Deploy the example

verify:
	# Check expected state

clean:
	# Tear everything down
```

### 5. Add Manifests and Scripts

Place Kubernetes manifests in `manifests/` and shell scripts in `scripts/`.

## Testing Your Example

Before submitting:

1. **Test from scratch**: Start with a clean environment and follow your README
2. **Test cleanup**: Run `make clean` and verify everything is torn down
3. **Test on different platforms**: If possible, test on different OS/shell combinations
4. **Verify dependencies**: Document all required tools and their versions

## Submitting Your Example

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-example-name`
3. Add your example following the structure above
4. Test thoroughly
5. Commit with conventional commit format:
   - `feat: add example for X`
   - `docs: improve README for Y`
6. Push and open a Pull Request

## Review Process

We will:
- Test your example against the latest Kranix release
- Verify documentation is clear and complete
- Check that the example follows the structure guidelines
- Ensure the example is focused and demonstrates a specific concept

## Getting Help

If you need help creating an example:
- Open an issue with your question
- Join our community discussions
- Look at existing examples for reference

## License

By contributing, you agree that your contributions will be licensed under the Apache 2.0 License.
