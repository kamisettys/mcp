from mcp.server.fastmcp import FastMCP

# creating a server
mcp=FastMCP("hello-mcp")

#define tools
@mcp.tool()
def add(a:int|float, b:int|float)-> int|float:
    """this method adds two numbers
    
    Args:
        a (int|float): first number
        b (int|float): second number
    Returns:
        int|float: the sum of a and b    
        
        
        """
    return a + b

if __name__ == "__main__":
    mcp.run(transport="stdio")