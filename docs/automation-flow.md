# Automation Flow

## Step-by-Step Execution

1. User enters search keyword
2. Browser opens Facebook people search
3. Script waits for results to load
4. Locates all "Add Friend" buttons using:
   - aria-label attributes
   - visible button text
5. Scrolls page to load additional results
6. Clicks each Add Friend button
7. Applies random delays between actions
8. Stops when no new results are loaded

---

## Anti-Detection Measures

- Random sleep intervals
- Real user profile
- No headless execution
- Natural scrolling behavior
