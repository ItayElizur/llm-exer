## Activity 1: Basic Prompt Design
**Objective**: Create effective prompts for different types of code issues\
**Your Task**:
1. Design 3 different prompt templates:
   - One focused on bug detection
   - One focused on code style and readability
   - One focused on security issues
2. Test each prompt on the provided code samples
3. Compare the responses and effectiveness

**Deliverable**: Document your prompts and their results

## Activity 2: Role-Based vs Direct Prompting
**Objective**: Compare different prompting strategies\
**Your Task**:
1. Create two versions of the same review request:
    - Direct instruction approach
    - Role-based approach (e.g., "You are an expert Python developer...")
2. Test both on at least 3 code samples
3. Analyze differences in:
   - Response quality
   - Response length
   - Specific insights provided
   - False positives/negatives

**Deliverable**: Comparison report with examples

## Activity 3: Model Comparison
**Objective**: Evaluate different LLMs for code review\
**Your Task**:
1. Choose 2-3 different models (OpenAI, HuggingFace, local)
2. Use the same prompt on the same code samples
3. Compare results across models:
   - Accuracy of issue identification
   - Quality of explanations
   - Response time
   - Cost (if applicable)

**Deliverable**: Model evaluation matrix


## Evaluation Criteria
### For Prompt Effectiveness
- **Accuracy**: Does it correctly identify real issues?
- **Completeness**: Does it catch multiple types of problems?
- **Clarity**: Are the explanations clear and actionable?
- **Relevance**: Does it avoid false positives?

### For Code Analysis Quality
- **Bug Detection**: Logical errors, edge cases
- **Security Issues**: SQL injection, XSS, authentication flaws
- **Performance**: Inefficient algorithms, memory leaks
- **Style**: PEP 8 compliance, naming conventions
- **Maintainability**: Code structure, documentation

### Success Metrics
TODO: Define how you'll measure success
- Percentage of real bugs caught
- False positive rate
- Response time/efficiency
- User satisfaction with feedback quality