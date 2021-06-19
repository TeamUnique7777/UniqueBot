import random
from email import message
import asyncio
import discord

client = discord.Client()

@client.event
async  def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("자유경쟁전 대리 업계 최저가 ! 고랭 전문 / 주문제작 최단 시간 / 문의 폭풍 ! 문의: Unique#7777 / 디스코드: https://discord.gg/H4UvpQuPDU")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):

    if message.content == "!추첨 시작":

        randomNum = random.randrange(1, 100)
        if randomNum != 0:
            await message.channel.send("5초 뒤에 공개됩니다")
            await asyncio.sleep(0.5)
            await message.channel.send("5...")
            await asyncio.sleep(1)
            await message.channel.send("4...")
            await asyncio.sleep(1)
            await message.channel.send("3...")
            await asyncio.sleep(1)
            await message.channel.send("2...")
            await asyncio.sleep(1)
            await message.channel.send("1...!")
            await asyncio.sleep(1)
            await message.channel.send("이벤트 당첨 숫자는 %d 입니다!!" %randomNum)

    if message.content.startswith("!대리 가격표"):
        channel = message.content[8:26]
        embed = discord.Embed(title="Team Unique", description="배치 9승 보장 현재 역고 mmr or 전시즌 자경 mmr에서 +150점입니다.", color=0x62c1cc)

        embed.add_field(name="0-1500 (50점당) 2000원\n\n"
                             "1500-2000 (50점당) 3000원\n\n"
                             "2000-2500 (50점당) 4000원\n\n"
                             "2500-3000 (50점당) 5000원\n\n"
                             "3000-3250 (50점당) 7000원\n\n"
                             "3250-3500 (50점당) 8000원\n\n"
                             "3500-3750 (50점당) 10000원\n\n", value="자유경쟁전은 유니크팀", inline=True)

        embed.add_field(name="3750-4000 (50점당) 14000원\n\n"
                             "4000-4100 (50점당) 20000원\n\n"
                             "4100-4200 (50점당) 35000원\n\n"
                             "4200-4300 (50점당) 50000원\n\n"
                             "4300-4400 (50점당) 75000원\n\n"
                             "4400-4500 (50점당) 115000원\n\n"
                             "4500++ 상담 문의 부탁드리겠습니다.\n\n", value="역할고정은 사쿠라팀", inline=True)

        embed.set_footer(text="[주의사항]\n"
                              "* 문상 10% 수수료 추가\n"
                              "* 원챔 수수료 20% 추가\n"
                              "* 셧다운제 일시 사전에 미리 문의 부탁드립니다.\n"
                              "* 작업 도중 접속시, 목표 작업 점수에서 50점 차감\n"
                              "* 듀오 경쟁시 금액의 50% 추가됩니다 (듀오 이상이여도 가격 변동은 없습니다)\n"
                              "* 라이브 방송은 필수가 아닌 기사님의 선택입니다.")
        await client.get_channel(int(channel)).send(embed=embed)

    if message.content.startswith("!주문제작 가격표"):
        cchannel = message.content[10:28]
        embed = discord.Embed(title="Team Unique", description="계정 미배치 포함 / 게정 미배치 미포함", color=0x62c1cc)

        embed.add_field(name="(주문제작만)배치 9승보장 (30000원) / (15000원)\n\n"
                             "마스터 보장 (35000원) / (18000원)\n\n"
                             "그마 보장 (60000원) / (40000원)\n\n"
                             "4100 보장 (80000원) / (60000원)\n\n"
                             "4200 보장 (105000원) / (85000원)\n\n"
                             "4300 보장 (150000원) / (130000원)\n\n"
                             "4400 보장 부터는 상담 문의 부탁드리겠습니다.\n\n", value="자유경쟁전은 유니크팀", inline=True)

        embed.set_footer(text="[주의사항]\n"
                              "* 문상 10% 수수료 추가\n"
                              "* 원챔 수수료 30% 추가\n"
                              "* 셧다운제 일시 사전에 미리 문의 부탁드립니다.\n"
                              "* 작업 도중 접속시, 목표 작업 점수에서 50점 차감\n"
                              "* 듀오 경쟁시 금액의 50% 추가됩니다 (듀오 이상이여도 가격 변동은 없습니다)\n"
                              "* 라이브 방송은 필수가 아닌 기사님의 선택입니다.")
        await client.get_channel(int(cchannel)).send(embed=embed)



client.run("ODU1MTM0ODY4NDUwMzEyMTky.YMuEaA.z-ao0P-npeMfj-xkvGZM9lYch7E")