# Deadpan Forecasts for Cities That Do Not Exist

[![make.fun](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![rank](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/khaliefk/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![reward](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/khaliefk/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)

Entry for the [make.fun bounty](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c): one absurd but believable weather line for an invented city, read deadpan like a TV meteorologist who has seen it all.

## What it does

`main.py` writes a single forecast line to `/output/entry.txt`:

> In Kesswick, expect a high of 21 degrees, light rain, and a 40% chance the clouds hand in their notice at noon and leave the sky to sort itself out.

Kesswick does not exist. The clouds, however, have given notice.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Stdlib only. No network, no randomness, no arguments. The same line comes out every run.
