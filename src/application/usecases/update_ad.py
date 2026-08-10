from src.application.ports.uow import UnitOfWork
from src.application.ports.usecases import UpdateAdPort
from src.domain.entities import Ad


class UpdateAd(UpdateAdPort):
    def __init__(self, uow: UnitOfWork) -> None:
        self._uow = uow

    async def execute(
        self,
        ad_id: int,
        user_id: int,
        title: str | None,
        description: str | None,
        price: int | None,
        category: str | None,
        city: str | None,
    ) -> Ad:
        raise NotImplementedError
