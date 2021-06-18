import vk_api

vk = vk_api.VkApi(login='maman03032002@gmail.com', password='22ЫлнкшьЙЦУКЕНЩкшпшт22', app_id=6121396,
                  token='050502121ffc7f7b08b025f7395616fad04a3f637bb7ddf2d73445a1f8aa1904a0282dbe52d17f827742c')

vk.auth(token_only=True)
json = vk.method("audio.get", {"count": 1, "owner_id": 123456})
audio_with_url = vk.method("audio.getById", {"audios": "_".join(str(json['items'][0][i]) for i in ("owner_id", "id"))})
