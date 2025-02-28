# Agent Customization Guide

This guide explains how to customize agent behavior in OmnitrAIce using the web interface.

## Understanding Agent Types

OmnitrAIce includes several specialized agents:

1. **CEO Agent** - Responsible for high-level project vision and strategy
2. **Architect Agent** - Handles technical architecture and system design
3. **Developer Agent** - Focuses on implementation details and coding standards

Each agent can be customized to change how it approaches its role.

## The Customization Interface

The Agent Customization interface provides two ways to modify agent behavior:

### Template Editor

The Template Editor allows direct editing of the agent's prompt template. This is the most powerful way to change agent behavior, as it directly modifies the instructions given to the underlying DeepSeek LLM.

#### Example: Elon Musk-Style CEO

Here's an example template for making the CEO agent think like Elon Musk:

```
You are the CEO Agent embodying Elon Musk's revolutionary thinking style.
Current Project Context: {context}
Task: {task}

Channel Elon Musk's approach by:
1. First principles thinking - break down problems to their fundamental truths
2. Ambitious, moonshot goal-setting that others might consider impossible
3. Cross-disciplinary innovation - combine ideas from different fields
4. Rapid iteration and willingness to fail forward
5. Long-term vision while maintaining attention to critical details

When analyzing this project:
- Question every assumption and traditional approach
- Consider how to make the solution 10x better, not just 10% better
- Identify opportunities for vertical integration
- Focus on scalability and exponential impact
- Ask "How can we solve this in a way no one has attempted before?"

Consider how this solution could evolve over 5-10 years, not just immediate implementation.

Previous Decisions: {decisions}

Provide your analysis and decisions with bold, transformative thinking that challenges conventional wisdom while remaining grounded in technical and business reality.
```

### Parameter Editor

The Parameter Editor provides a more structured way to customize agents through four key parameters:

#### 1. Focus Areas

Define what the agent prioritizes. For example, for a Sustainability-Focused CEO:

```
Environmental impact assessment
Carbon footprint reduction
Circular economy implementation
Sustainable supply chain
Long-term resource management
```

#### 2. Strategy Level

Controls how strategic versus tactical the agent's thinking should be:
- **High**: Big-picture, long-term, abstract thinking
- **Medium**: Balanced strategic and tactical focus
- **Low**: Detailed, practical, implementation-focused

#### 3. Detail Level

Determines how detailed the agent's responses will be:
- **High**: Comprehensive, thorough analysis
- **Medium**: Balanced level of detail
- **Low**: Concise, high-level summaries

#### 4. Additional Considerations

Add specific instructions or considerations for the agent to keep in mind:

```
Consider data privacy regulations
Evaluate accessibility requirements
Assess international scalability
Factor in resource constraints
```

## Creating and Using Templates

### Saving Templates

After customizing an agent, click the "Save Template" button to store your changes. Templates are saved persistently and will be available in future sessions.

### Generating Templates from Parameters

When using the Parameter Editor, you can click "Generate Template from Parameters" to create a template based on your parameter settings. This is useful for:

1. Seeing how parameters translate to template language
2. Making further manual adjustments to the generated template
3. Creating a starting point for more detailed customization

## Best Practices

1. **Start with Parameters**: For simple adjustments, use the Parameter Editor first
2. **Refine with Templates**: For fine-grained control, generate a template from parameters and then refine it
3. **Test Incrementally**: Make small changes and test the results before making more significant changes
4. **Preserve Placeholders**: Always keep the placeholder variables like `{context}`, `{task}`, and `{decisions}` in your templates
5. **Be Specific**: The more specific your instructions, the more predictable the agent's behavior

## Examples

### Domain Expert CEO

To make the CEO agent behave like a healthcare industry expert:

**Focus Areas:**
```
Healthcare regulation compliance
Patient outcome optimization
Clinical workflow efficiency
Healthcare data security
Medical staff resource allocation
```

**Additional Considerations:**
```
Consider HIPAA compliance requirements
Evaluate patient privacy implications
Factor in medical ethics standards
```

### Tech-Focused Architect

To create a microservices-oriented Architect agent:

**Focus Areas:**
```
Microservice architecture principles
Service boundary definition
API design and standards
Scalability patterns
Communication protocols
```

**Strategy Level:** Medium
**Detail Level:** High

**Additional Considerations:**
```
Prioritize loose coupling
Consider eventual consistency
Evaluate containerization options
```

## Advanced Customization

For advanced users, it's possible to edit the template directly to include:

1. **Step-by-Step Instructions**: Guide the agent through a specific analytical process
2. **Persona Adoption**: Make the agent think like a specific person or role
3. **Specialized Terminology**: Include domain-specific language or frameworks
4. **Decision Criteria**: Define specific criteria for making decisions

Remember that the agent templates leverage the capabilities of the DeepSeek LLM, so well-structured, clear instructions will yield the best results.