from fastmcp import FastMCP

mcp=FastMCP("add")


@mcp.tool
def add(a:int,b:int):
    """this tool is used to do the addition here"""
    return a+b


if __name__=="__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8080)
