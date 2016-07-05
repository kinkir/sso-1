from sqlalchemy import Column, String, BigInteger
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from db.meta import Base
from db.utils import guid


class MobileOAuth2Code(Base):
    __tablename__ = 'mobile_oauth_2_codes'

    id = Column(guid.GUID(), primary_key=True)
    code = Column(String(256), nullable=False, index=True, unique=True)
    expires_at = Column(BigInteger, nullable=False)
    created_at = Column(BigInteger, nullable=False)

    mobile_client_id = Column(guid.GUID(), ForeignKey('mobile_clients.id'), nullable=False)
    mobile_client = relationship('MobileClient', back_populates='mobile_oauth_2_codes')
