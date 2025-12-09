# Table Reversal - Q&A and Exploration Notes

## Open Questions
1. How to handle markdown alignment when reversing?
   - Proposed: Adjust alignment markers based on new column order

2. Performance considerations for large tables?
   - Need benchmark comparisons
   - Consider generator-based approach for memory efficiency

## Potential Implementation Approaches
- Functional parsing pipeline
- Immutable data transformations
- Type-aware column reversal

## Input Format Considerations
- Markdown tables
  - | Delimiter
  - Alignment markers
- CSV tables
  - Comma-separated
  - Quoted fields
  - Potential escaping needs

## Safety Checklist
- ✓ No in-place mutations
- ✓ Input type validation
- ✓ Error handling
- ✓ Predictable output