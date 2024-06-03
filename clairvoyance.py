import os

from aiocqhttp import MessageSegment

from hoshino.R import ResImg
from hoshino.modules.priconne.clairvoyance import sv, checkout_clairvoyance, clairvoyance_resource_dir, \
    clairvoyance_resource_obj


@sv.on_fullmatch('千里眼')
async def future_gacha(bot, ev):
    checkout_clairvoyance()
    filelist = os.listdir(clairvoyance_resource_obj)
    filelist = [filename for filename in filelist if filename.endswith((".png", ".jpg"))]
    filelist.sort()
    msg = [
        MessageSegment.text("千里眼数据来自：Columba-丘比@bilibili\n"),
        MessageSegment.text("https://www.bilibili.com/read/cv26851697/\n"),
    ]
    for file in filelist:
        msg.append(ResImg(os.path.join(clairvoyance_resource_dir, file)).cqcode)
    await bot.send(ev, msg, at_sender=True)
