"""import modules"""
import logging
import math

from sqlalchemy.orm import Session

from gd_nasa_api.infra.powerData import PowerData


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class PowerDataService:
    """contains all engine methods"""

    def sanitize_dict(self, data):
        """Remplace NaN, inf et -inf par None"""
        return {k: (None if isinstance(v, float) and (math.isnan(v) or math.isinf(v)) else v) for k, v in data.items()}

    def _get_power_data(self, db: Session, filter_by: str, value: str):
        output = db.query(PowerData).filter(
            getattr(PowerData, filter_by) == value).first()
        if output is None:
            logger.error("No data found for %s: %s", filter_by, value)
            return None
        logger.info("output is: %s", output.__dict__)
        excluded_keys = {'_sa_instance_state'}
        power_data_dict = {
            k: v for k, v in output.__dict__.items() if k not in excluded_keys}
        db_power = self.sanitize_dict(power_data_dict)
        return db_power

    def get_power_data_by_country(self, db: Session, country_name: str):
        return self._get_power_data(db, 'country', country_name)

    def get_power_data_by_city(self, db: Session, city_name: str):
        return self._get_power_data(db, 'city', city_name)
