from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    """
    
The Handler interface declares a method for constructing a chain of handlers. He also declares a method for executing the request.    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside the base class
    handler.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = ha
# Returning a handler from here will allow us to bind handlers with a simple # way, like this:
 # monkey.set_next(squirrel).set_next(dog) return handler
@abstractmethod
def handle(self, request: Any) -> str:
if self._next_handler:
return self._next_handler.handle(request)
return None
"""
All Concrete Handlers either process the request or forward it
next handler in the chain.
"""


class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Banana":
            return f"Monkey: I'll eat the {request}"
        else:
            return super().handle(request)


from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    """
    
The Handler interface declares a method for constructing a chain of handlers. He also declares a method for executing the request.    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside the base class
    handler.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = ha
# Returning a handler from here will allow us to bind handlers with a simple # way, like this:
 # monkey.set_next(squirrel).set_next(dog) return handler
@abstractmethod
def handle(self, request: Any) -> str:
if self._next_handler:
return self._next_handler.handle(request)
return None
"""
All Concrete Handlers either process the request or forward it
next handler in the chain.
"""


class CatHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Fish":
            return f"Cat: I'll eat the {request}"
        else:
            return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "MeatBall":
            return f"dog: I'll eat the {request}"
        else:
            return super().handle(request)


class RabbitHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Carrot":
            return f"Rabbit: I'll eat the {request}"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    """
    
Typically, client code is designed to work with a single handler. In most cases, the client is not even aware that this handler is part of the chain.    """

    for food in ["MealBall", "Fish", "Cup of tea"]:
        print(f"\nClient: Who wants a {food}?")
        result = handler.handle(food)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {food} was left untouched.", end="")


if __name__ == "__main__":
    cat = CatHandler()
    dog = DogHandler()
    rabbit = RabbitHandler()

    cat.set_next(dog).set_next(rabbit)

# The client should be able to send a request to any handler, not
 # only the first one in the chain part of the chain.
    print("Chain: Cat > Dog > Rabbit")
    client_code(cat)
    print("\n")

    print("Subchain: Dog > Rabbit")
    client_code(dog)
