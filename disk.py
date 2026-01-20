from typing import Any, Dict


class Disk:
    def __init__(self, path: str) -> None:
        self.path = path

    def save(self, data: Dict[str, Any]) -> None:
        """ Save data into disk. 

            Args:
                data: The data to be saved.
            
            Usage:
                >>> disk = _Disk("/path/to/file")
                >>> disk.save(data)
        """
        pass

    def load(self) -> Dict[str, Any]:
        """ Try to load data in supported format from `self.path`.
        
        Returns:
            Dict[str, Any]: The loaded data.
        
        Usage:
            >>> disk = _Disk("/path/to/file")
            >>> disk.load()
        """
        pass