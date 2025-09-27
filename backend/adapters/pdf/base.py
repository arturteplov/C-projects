# (STEP 5 • Adapters) PDF interface
from abc import ABC, abstractmethod
class PdfAdapter(ABC):
    @abstractmethod
    def write_pdf(self, text: str, out_path: str) -> None: ...
