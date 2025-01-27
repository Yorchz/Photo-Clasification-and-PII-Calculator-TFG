from src.handlers.models.ModelBlip2BHandler import ModelBlip2BHandler
from src.handlers.models.ModelBlipVqaHandler import ModelBlipVqaHandler
from src.handlers.models.ModelPnpVqaHandler import ModelPnpVqaHandler


class Mapper:

    _map = {
        "blip2_t5_pretrain_flant5xl": ModelBlip2BHandler,
        "blip2_opt_caption_coco_opt2.7b": ModelBlip2BHandler,
        "blip_vqa_vqav2": ModelBlipVqaHandler,
        "pnp_vqa_base": ModelPnpVqaHandler,
    }

    @staticmethod
    def get_class(key: str) -> type:
        return Mapper._map.get(key)
