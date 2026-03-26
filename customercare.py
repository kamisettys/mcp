from mcp.server.fastmcp import FastMCP
mcp=FastMCP(name="swiggy_mcp", website_url="https://github.com/kamisettys/Generative-AI-phase1")


# tools
@mcp.tools()
def get_customer_summary(customer_id:str):
    pass

@mcp.tools()
def get_order_information(order_id:str):
    pass

@mcp.tools()
def get_restuarent_information(restaurant_id:str):
    pass



# resources
@mcp.resource("policy://refund")
def get_refund_policy():
    lines=[]
    with open('refundpolicy.md') as refund:
        lines = refund.readlines()
    return "\n".join(lines) 

@mcp.resource("complaint://{ctype}")
def get_complain_resolution(ctype)->str:
    lines=[]
    with open('latetimedeliverypolicy.md') as complain:
        lines = complain.readlines()
    return "\n".join(lines) 
