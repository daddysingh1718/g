from duckduckgo_search import DDGS

def search_web(query: str) -> str:
    """
    Searches the web using DuckDuckGo and returns the top 5 results.

    Args:
        query: The search query.

    Returns:
        A formatted string of the search results, including title, snippet, and URL.
    """
    print(f"Tool: search_web, Query: {query}")
    try:
        # Using a context manager for the DDGS client
        with DDGS() as ddgs:
            # Fetching text search results
            results = list(ddgs.text(query, max_results=5))

        if not results:
            return "No results found for the query."

        # Format the results into a readable string for the LLM
        formatted_results = []
        for i, result in enumerate(results, 1):
            formatted_results.append(
                f"Result {i}:\n"
                f"  Title: {result.get('title', 'N/A')}\n"
                f"  Snippet: {result.get('body', 'N/A')}\n"
                f"  URL: {result.get('href', 'N/A')}\n"
            )

        return "\n".join(formatted_results)

    except Exception as e:
        return f"An error occurred during web search: {e}"
