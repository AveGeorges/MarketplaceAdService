from src.application.ports.uow import UnitOfWork
from src.application.ports.usecases import DeleteAdPort


class DeleteAd(DeleteAdPort):
    def __init__(self, uow: UnitOfWork) -> None:
        self._uow = uow

    async def execute(self, ad_id: int, user_id: int) -> None:
        raise NotImplementedError
