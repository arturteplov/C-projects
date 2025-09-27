# (STEP 5 • Adapters) Email interface
from abc import ABC, abstractmethod
from typing import Optional
class EmailAdapter(ABC):
    @abstractmethod
    def send(self, to_email: str, subject: str, body: str, attachment_path: Optional[str]  = None) -> None: ...
