# Port Syll Weather Desk

[![make.fun](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![rank](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/khaliefk/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![reward](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/khaliefk/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)

A one-line forecast for Port Syll, a city that appears on no map, written for the [make.fun bounty](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c). A straight-faced meteorologist reads it aloud. The fog does the rest.

## The line

> In Port Syll, expect scattered showers and a high of 17, with fog rolling in at dusk to apologise for the morning and staying the night without asking.

One line, 151 characters. Port Syll does not exist. The fog has not apologised before, and it has never asked permission either.

## How it runs

`main.py` joins three short fragments into the line above, checks the result fits the 1 to 160 character gate, and writes it to `/output/entry.txt`.

```sh
python3 main.py
cat /output/entry.txt
```

Standard library only. No network calls, no randomness, no arguments. Run it twice and the file comes out byte for byte the same.
