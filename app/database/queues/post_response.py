from sqlalchemy import select

from app.database.models.bids import Response
from app.database.models.sync_session import sync_session


def post_response(bid_id: int, performer_telegram_id: int) -> bool | None:
    with sync_session() as session:
        with session.begin():
            try:
                response = session.scalar(select(Response).where(Response.bid_id == bid_id,
                                                                 Response.performer_telegram_id == performer_telegram_id))

                if response:
                    return False
                else:
                    response = Response(bid_id = bid_id,
                                        performer_telegram_id = performer_telegram_id)
                    session.add(response)

                    return True
            except Exception as e:
                print(f'Error creating response: {e}')
                return None