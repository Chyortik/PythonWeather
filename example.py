import python_weather
import asyncio
import os


async def getweather():
  # единицы измерения температуры - METRIC --> Цельсий, IMPERIAL --> Фаренгейт
  async with python_weather.Client(format=python_weather.METRIC) as client:

    weather = await client.get("Moscow")
    print(weather.current.temperature)

    for forecast in weather.forecasts:
      print(forecast)

      for hourly in forecast.hourly:
        print(f' --> {hourly!r}')

if __name__ == "__main__":
  if os.name == "nt":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(getweather())
