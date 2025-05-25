from langchain_core.tools import BaseTool
from typing import Optional, Type
from pydantic import BaseModel, Field

class WriteFileInput(BaseModel):
    filename: str = Field(..., description="The name of the file to write to")
    content: str = Field(..., description="The content to write to the file")

class WriteToFileTool(BaseTool):
    name = "write_to_file"
    description = "Write content to a file using filename and content input."
    args_schema: Type[BaseModel] = WriteFileInput

    def _run(self, filename: str, content: str, run_manager: Optional[object] = None) -> str:
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            return f"File '{filename}' written successfully."
        except Exception as e:
            return f"Error writing file: {e}"

    def _arun(self, *args, **kwargs):
        raise NotImplementedError("Async not supported.")

# Export an instance
write_to_file = WriteToFileTool()
