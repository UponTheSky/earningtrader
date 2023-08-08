from abc import ABC, abstractmethod


class ComponentBaseInterface(ABC):
    """
    The base interface for every pipeline component.
    """

    @abstractmethod
    def __repr__(self) -> str:
        """
        Prints detailed information about the component.
        """
        return f"Component '{self.__class__.__name__}'"

    @abstractmethod
    def _log(
        self, *, message: str, level: str
    ) -> None:  # TODO: change level => logging level
        """
        A "private" method for logging the information.

        The output stream is upto the inheriting subclasses.
        """
        ...
