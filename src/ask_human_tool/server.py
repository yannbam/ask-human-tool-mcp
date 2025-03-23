#!/usr/bin/env python3

from typing import Any, Dict, List, Optional
import json
import datetime
from mcp.server.fastmcp import FastMCP

class AskHumanServer:
    def __init__(self, server_name="ask-human-tool"):
        # Initialize FastMCP server
        self.mcp = FastMCP(server_name)
        
        # Store the thoughts for logging purposes
        self.thoughts_log = []
        
        # Register tools
        self.register_tools()
    
    def register_tools(self):
        # Register the ask human tool
        @self.mcp.tool()
        async def ask_human_tool(query: str) -> str:
            """Use this tool to ask a human something. It will not return an answer directly, 
            but reconnect you with a human. You need to end your turn to get a reply. Use it when you feel stuck, to escape the tool use cycle—instead of trying a workaround that won't fix the real issue.

            Args:
                query: A query for the human.
            """
            
            # Return a confirmation
            return "You are now being reconnected with a human. Please end your turn."


            # # Log the thought with a timestamp
            # timestamp = datetime.datetime.now().isoformat()
            # self.thoughts_log.append({
            #     "timestamp": timestamp,
            #     "thought": thought
            # })


        # @self.mcp.tool()
        # async def think_tool_get_thoughts() -> str:
        #     """Retrieve all thoughts recorded in the current session.
            
        #     This tool helps review the thinking process that has occurred so far.
        #     """
        #     if not self.thoughts_log:
        #         return "No thoughts have been recorded yet."
            
        #     formatted_thoughts = []
        #     for i, entry in enumerate(self.thoughts_log, 1):
        #         formatted_thoughts.append(f"Thought #{i} ({entry['timestamp']}):\n{entry['thought']}\n")
            
        #     return "\n".join(formatted_thoughts)

        # @self.mcp.tool()
        # async def think_tool_clear_thoughts() -> str:
        #     """Clear all recorded thoughts from the current session.
            
        #     Use this to start fresh if the thinking process needs to be reset.
        #     """
        #     count = len(self.thoughts_log)
        #     self.thoughts_log = []
        #     return f"Cleared {count} recorded thoughts."

        # @self.mcp.tool()
        # async def think_tool_get_thought_stats() -> str:
        #     """Get statistics about the thoughts recorded in the current session."""
        #     if not self.thoughts_log:
        #         return "No thoughts have been recorded yet."
            
        #     total_thoughts = len(self.thoughts_log)
        #     avg_length = sum(len(entry["thought"]) for entry in self.thoughts_log) / total_thoughts if total_thoughts else 0
        #     longest_thought = max((len(entry["thought"]), i) for i, entry in enumerate(self.thoughts_log)) if self.thoughts_log else (0, -1)
            
        #     stats = {
        #         "total_thoughts": total_thoughts,
        #         "average_length": round(avg_length, 2),
        #         "longest_thought_index": longest_thought[1] + 1 if longest_thought[1] >= 0 else None,
        #         "longest_thought_length": longest_thought[0] if longest_thought[0] > 0 else None
        #     }
            
        #     return json.dumps(stats, indent=2)
    
    def run(self, transport='stdio'):
        """Run the server with the specified transport"""
        print(f"Starting Ask Human Tool MCP Server with {transport} transport...")
        self.mcp.run(transport=transport)


def main():
    server = AskHumanServer()
    server.run()


if __name__ == "__main__":
    main()