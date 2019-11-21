import logging
from app import db
from .models import PlantImage


def save_images(
        user_id,
        image
):
    """
    Saves a Plant Image
    :param user_id:
    :param image:
    :return: Response of logging of transaction
    :rtype: dict
    """
    logging.info("Saving Plant Image to Database")

    try:
        plant_image = PlantImage(
            user_id=user_id,
            image=image
        )

        db.session.add(plant_image)
        db.session.commit()

        logging.info("Successfully Saved Plant Image")

    except Exception as ex:
        logging.error(f"Error Saving Plant Image with Error {ex}")
        db.session.rollback()
        raise Exception(f"Failed to Save Plant Image to Database")

