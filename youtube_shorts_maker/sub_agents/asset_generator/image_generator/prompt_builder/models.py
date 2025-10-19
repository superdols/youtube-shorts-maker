from pydantic import BaseModel, Field
from typing import List

class OptimizedPrompt(BaseModel):
    scene_id: int = Field(description="Scene ID from the original content plan")
    enhanced_prompt: str = Field(
        description="Detailed prompt with technical specs and text overlay instructions for vertical YouTube Shorts"
    )

class PromptBuilderInput(BaseModel):
    optimized_prompts: List[OptimizedPrompt]